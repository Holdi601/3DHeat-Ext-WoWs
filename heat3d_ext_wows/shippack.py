"""
World of Warships' catalogue and local model pack, from your own install.

`catalog`: every ship (name, class, nation, tier, group, size, speed, health) and every shell, torpedo and bomb
(calibre, kind, damage, speed, penetration numbers) of the parameter table, with the game's English names, in the
viewer's catalogue format (`3dheat-catalog`, version 1).

`models`: each ship's armour model (the hull, deck, belts, bulkheads, barbettes and superstructure plates the game
uses to resolve hits), scaled to metres, as one `.glb` per ship plus `model-pack.json`. The drawn hull (`hull`) is
the armour shell simplified to three levels of detail; under `dm` each plate group keeps its thickness in mm
(`extras.mm`, from the stock hull's `armor` table), so hits can be coloured by plate. Turrets are not placed yet
(their positions are in the ship's visual, which is not read). The pack is for this machine only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

import numpy as np

from . import armour, gamefiles, packglb

GAME = "wows"
#: The game's models are at this fraction of the real size; checked against each hull's stated length.
MODEL_SCALE = 15.0
BUDGETS = (14000, 4000, 1000)
SPECIES = {"Battleship": "battleship", "Cruiser": "cruiser", "Destroyer": "destroyer", "AirCarrier": "carrier",
           "Submarine": "submarine", "Auxiliary": "auxiliary"}
PROJECTILE_NUMBERS = {"bulletDiametr": "calibre", "alphaDamage": "damage", "bulletSpeed": "speed",
                      "bulletMass": "mass", "bulletKrupp": "krupp", "alphaPiercingHE": "hePenetration",
                      "bulletDetonatorThreshold": "fuseThreshold", "bulletRicochetAt": "ricochetAt",
                      "bulletAlwaysRicochetAt": "alwaysRicochetAt", "maxDist": "range"}


def _ships(gp: dict) -> dict[str, dict]:
    return {k: v for k, v in gp.items() if isinstance(v, dict) and (v.get("typeinfo") or {}).get("type") == "Ship"}


def _hulls(ship: dict) -> list[dict]:
    """The ship's hull modules, stock first (`A_Hull`, `B_Hull`, ...)."""
    return [ship[k] for k in sorted(ship) if k.endswith("_Hull") and isinstance(ship[k], dict) and ship[k].get("model")]


def _name(texts: dict[str, str], index: str, fallback: str) -> str:
    return texts.get(f"IDS_{index}") or fallback


def build_catalog(gp: dict, texts: dict[str, str], *, game_build: str = "", source: str = "") -> dict:
    items = []
    for key, s in _ships(gp).items():
        info = s["typeinfo"]
        index = s.get("index", "")
        name = _name(texts, index, key.split("_", 1)[-1].replace("_", " "))
        hull = (_hulls(s) or [{}])[0]
        size = hull.get("size") or ()
        numbers = {k: v for k, v in (("tier", s.get("level")), ("health", hull.get("health")),
                                     ("maxSpeed", hull.get("maxSpeed")), ("length", size[0] if size else None),
                                     ("beam", size[1] if len(size) > 1 else None), ("draft", hull.get("draft")),
                                     ("tonnage", hull.get("tonnage"))) if isinstance(v, (int, float))}
        items.append({
            "id": key, "key": name, "kind": "vehicle", "name": name,
            "longName": texts.get(f"IDS_{index}_FULL", name),
            "class": SPECIES.get(info.get("species"), str(info.get("species", "")).lower()),
            "group": s.get("group", ""), "nation": info.get("nation", ""),
            "aliases": [index, key.replace("_", "-"), str(s.get("id", ""))],
            "model": f"model-packs/{GAME}/{key.lower()}.glb", "numbers": numbers,
        })
    for key, p in gp.items():
        if not isinstance(p, dict) or (p.get("typeinfo") or {}).get("type") != "Projectile":
            continue
        index = p.get("index", "")
        numbers = {n: p[k] for k, n in PROJECTILE_NUMBERS.items() if isinstance(p.get(k), (int, float)) and p.get(k)}
        if "calibre" in numbers:
            numbers["calibre"] = round(numbers["calibre"] * 1000)  # mm
        items.append({
            "id": key, "key": _name(texts, index, key), "kind": "weapon", "name": _name(texts, index, key),
            "class": str(p["typeinfo"].get("species", "")).lower(), "group": p.get("ammoType", ""),
            "nation": p["typeinfo"].get("nation", ""), "aliases": [index], "model": "", "numbers": numbers,
        })
    return {"format": "3dheat-catalog", "version": 1, "game": GAME, "gameBuild": game_build, "source": source,
            "items": items}


def ship_model(pk: gamefiles.Packages, ship: dict) -> tuple[packglb.Built, dict] | None:
    """A ship's armour as a pack model (hull + `dm` plates by thickness) and its facts, or None without one."""
    hulls = _hulls(ship)
    if not hulls:
        return None
    hull = hulls[0]
    geo = hull["model"].rsplit(".", 1)[0] + ".geometry"
    if geo not in pk.files:
        return None
    pieces = armour.armour_pieces(pk.read(geo))
    if not pieces:
        return None
    allt = np.concatenate([t for _, t in pieces])
    extent = float(allt[..., 2].max() - allt[..., 2].min())
    stated = (hull.get("size") or (0,))[0]
    scale = MODEL_SCALE
    if stated and extent and abs(stated / extent - MODEL_SCALE) / MODEL_SCALE < 0.15:
        scale = stated / extent
    tri = armour.to_figure(allt, scale)
    v = tri.reshape(-1, 3)
    f = np.arange(len(v)).reshape(-1, 3)
    built = packglb.build_lods({"hull": (v, f)}, BUDGETS)
    table = hull.get("armor") or {}
    by_mm: dict[float, list[np.ndarray]] = {}
    for key, t in pieces:
        by_mm.setdefault(float(table.get(key, 0.0)), []).append(t)
    for mm in sorted(by_mm):
        t = armour.to_figure(np.concatenate(by_mm[mm]), scale)
        dv, df = packglb.weld(t.reshape(-1, 3), np.arange(t.shape[0] * 3).reshape(-1, 3))
        built.dm.append((f"armour_{mm:g}mm", dv.astype(np.float32), df,
                         {"part": "armour", "group": "armour", "class": "plate", "mm": mm}))
    return built, {"scale": round(scale, 4), "plates": len(pieces), "geometry": geo}


def write_pack(game: Path, out_dir: Path, *, source: str, only: list[str] | None = None,
               say: Callable[[str], None] = print) -> dict:
    pk = gamefiles.Packages(game)
    gp = gamefiles.game_params(pk)
    texts = gamefiles.messages(pk)
    ships = _ships(gp)
    if only:
        ships = {k: v for k, v in ships.items() if any(o.lower() in k.lower() for o in only)}
    say(f"{len(ships)} ships in build {pk.build.name}")
    units, missing = {}, []
    for key, s in sorted(ships.items()):
        got = ship_model(pk, s)
        if got is None:
            missing.append(key)
            continue
        built, facts = got
        uid = key.lower()
        index = s.get("index", "")
        name = _name(texts, index, key.split("_", 1)[-1].replace("_", " "))
        species = SPECIES.get(s["typeinfo"].get("species"), "ship")
        asset = {"source": source, "version": 1, "game": GAME, "gameBuild": pk.build.name, "unit": uid, "scale": 1}
        meta = {"unit": uid, "kind": "ship", "domain": "sea", "anchor": "ground", "pivots": {}}
        packglb.write_unit_glb(out_dir / f"{uid}.glb", built, meta, asset)
        units[uid] = packglb.unit_entry(
            uid, built, kind="ship", domain="sea", name=name, aliases=[index.lower(), key.replace("_", "-").lower(),
                                                                       str(s.get("id", ""))],
            type_word=species, source_key=f"{facts['geometry']}|{pk.build.name}", nation=s["typeinfo"].get("nation", ""),
            tier=s.get("level"), dm=len(built.dm), **facts)
    if units:
        packglb.write_index(out_dir, GAME, pk.build.name, source, units)
    return {"units": units, "missing": missing, "build": pk.build.name}


def write_catalog(game: Path, out: Path, *, source: str) -> dict:
    pk = gamefiles.Packages(game)
    catalog = build_catalog(gamefiles.game_params(pk), gamefiles.messages(pk), game_build=pk.build.name, source=source)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(catalog, indent=1, ensure_ascii=False), encoding="utf-8")
    return catalog
