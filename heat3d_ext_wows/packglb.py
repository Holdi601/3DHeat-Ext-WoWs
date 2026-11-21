"""
Writes a local model pack in the layout the 3DHeat viewer reads (`model-pack.json` beside one `.glb` per unit).

A unit's `.glb` has a root node `unit` (extras: unit, kind, domain, anchor, box, pivots) with children `lod0`,
`lod1`, `lod2` (full, coarse, far), each holding one mesh node per part: `hull`, `gear` (running gear, drawn in the
track colour), `turret` (extras {joint: 'yaw', pivot}) and `gun` (extras {joint: 'pitch', pivot, parent}). An
optional child `dm` holds hit-relevant parts (`dm:<name>`, not drawn). Positions are float32 metres in the figure
frame (x forward, y up, z right) about the unit's own origin; indices u16 where they fit, else u32. `asset.extras`
holds {source, version, game, gameBuild, unit, scale}.

The pack is written for the machine it is made on and stays there.
"""

from __future__ import annotations

import hashlib
import json
import struct
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

PARTS = ("hull", "gear", "turret", "gun")


def weld(v: np.ndarray, f: np.ndarray, tol: float = 1e-4) -> tuple[np.ndarray, np.ndarray]:
    """Vertices at the same place made one (split by texture seams in the source), degenerate triangles dropped."""
    if not len(v):
        return v, f
    key = np.round(v / tol).astype(np.int64)
    _, first, inverse = np.unique(key, axis=0, return_index=True, return_inverse=True)
    inverse = inverse.reshape(-1)
    v2 = v[first]
    f2 = inverse[f]
    keep = (f2[:, 0] != f2[:, 1]) & (f2[:, 1] != f2[:, 2]) & (f2[:, 0] != f2[:, 2])
    return v2, f2[keep]


def simplify(v: np.ndarray, f: np.ndarray, budget: int) -> tuple[np.ndarray, np.ndarray]:
    """A mesh at no more than `budget` triangles (quadric decimation), unused vertices dropped."""
    if len(f) > budget and budget > 0:
        import fast_simplification

        v, f = fast_simplification.simplify(v.astype(np.float64), f.astype(np.int64),
                                            target_reduction=1 - budget / len(f), agg=5)
    used = np.unique(f)
    remap = np.full(len(v), -1, np.int64)
    remap[used] = np.arange(len(used))
    return np.asarray(v[used], np.float32), remap[f].astype(np.int64)


@dataclass
class Lod:
    parts: dict[str, tuple[np.ndarray, np.ndarray]]
    tris: int = 0
    simplified: bool = False
    source: int = 0


@dataclass
class Built:
    lods: list[Lod]
    pivots: dict[str, list[float]] = field(default_factory=dict)
    dm: list = field(default_factory=list)


def build_lods(parts: dict[str, tuple[np.ndarray, np.ndarray]], budgets: tuple[int, int, int]) -> Built:
    """Three levels of detail of welded parts, each part's share of a level's budget by its share of triangles."""
    parts = {k: weld(np.asarray(v, np.float64), np.asarray(f, np.int64)) for k, (v, f) in parts.items() if len(f)}
    total = sum(len(f) for _, f in parts.values()) or 1
    lods = []
    for budget in budgets:
        lp = {}
        for name, (v, f) in parts.items():
            share = max(12, int(budget * len(f) / total))
            lp[name] = simplify(v, f, share)
        tris = sum(len(f) for _, f in lp.values())
        lods.append(Lod(lp, tris, tris < total))
    return Built(lods)


class _Bin:
    def __init__(self):
        self.chunks: list[bytes] = []
        self.size = 0
        self.views: list[dict] = []
        self.accessors: list[dict] = []

    def add(self, data: bytes, target: int) -> int:
        pad = (-self.size) % 4
        if pad:
            self.chunks.append(b"\0" * pad)
            self.size += pad
        self.views.append({"buffer": 0, "byteOffset": self.size, "byteLength": len(data), "target": target})
        self.chunks.append(data)
        self.size += len(data)
        return len(self.views) - 1

    def mesh(self, v: np.ndarray, f: np.ndarray) -> dict:
        v = np.ascontiguousarray(v, np.float32)
        pv = self.add(v.tobytes(), 34962)
        self.accessors.append({"bufferView": pv, "componentType": 5126, "count": len(v), "type": "VEC3",
                               "min": v.min(0).tolist(), "max": v.max(0).tolist()})
        pa = len(self.accessors) - 1
        idx = np.ascontiguousarray(f.reshape(-1), np.uint16 if len(v) < 65536 else np.uint32)
        iv = self.add(idx.tobytes(), 34963)
        self.accessors.append({"bufferView": iv, "componentType": 5123 if idx.dtype == np.uint16 else 5125,
                               "count": len(idx), "type": "SCALAR"})
        return {"primitives": [{"attributes": {"POSITION": pa}, "indices": len(self.accessors) - 1, "mode": 4}]}


def write_unit_glb(path: Path, built: Built, meta: dict, asset_extras: dict) -> int:
    b = _Bin()
    meshes: list[dict] = []
    nodes: list[dict] = [{"name": "unit", "children": [], "extras": meta}]

    def add_node(name: str, parent: int, v=None, f=None, extras=None) -> int:
        n: dict = {"name": name}
        if v is not None and len(f):
            meshes.append(b.mesh(v, f))
            n["mesh"] = len(meshes) - 1
        if extras:
            n["extras"] = extras
        nodes.append(n)
        i = len(nodes) - 1
        nodes[parent].setdefault("children", []).append(i)
        return i

    for k, lod in enumerate(built.lods):
        li = add_node(f"lod{k}", 0, extras={"sourceLod": lod.source, "simplified": lod.simplified, "triangles": lod.tris})
        for part in PARTS:
            if part not in lod.parts:
                continue
            v, f = lod.parts[part]
            ex = None
            if part == "turret" and "turret" in built.pivots:
                ex = {"joint": "yaw", "pivot": built.pivots["turret"]}
            elif part == "gun" and "gun" in built.pivots:
                ex = {"joint": "pitch", "pivot": built.pivots["gun"], "parent": "turret" if "turret" in built.pivots else None}
            add_node(part, li, v, f, ex)
    if built.dm:
        di = add_node("dm", 0)
        for name, v, f, extras in built.dm:
            add_node(f"dm:{name}", di, v, f, extras)
    gltf = {
        "asset": {"version": "2.0", "generator": asset_extras.get("source", ""), "extras": asset_extras},
        "scene": 0, "scenes": [{"nodes": [0]}], "nodes": nodes, "meshes": meshes,
        "buffers": [{"byteLength": b.size}], "bufferViews": b.views, "accessors": b.accessors,
    }
    js = json.dumps(gltf, separators=(",", ":")).encode()
    js += b" " * ((-len(js)) % 4)
    binb = b"".join(b.chunks)
    binb += b"\0" * ((-len(binb)) % 4)
    total = 12 + 8 + len(js) + 8 + len(binb)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".glb.part")
    with tmp.open("wb") as fh:
        fh.write(struct.pack("<III", 0x46546C67, 2, total))
        fh.write(struct.pack("<II", len(js), 0x4E4F534A) + js)
        fh.write(struct.pack("<II", len(binb), 0x004E4942) + binb)
    tmp.replace(path)
    return total


def unit_entry(uid: str, built: Built, *, kind: str, domain: str, anchor: str = "ground", name: str = "",
               aliases: list[str] | None = None, type_word: str = "", source_key: str = "", **more) -> dict:
    """The unit's line in `model-pack.json`."""
    pts = np.concatenate([v for v, _ in built.lods[0].parts.values()]) if built.lods[0].parts else np.zeros((1, 3))
    lo, hi = pts.min(0), pts.max(0)
    return {
        "file": f"{uid}.glb", "name": name, "aliases": aliases or [], "kind": kind, "domain": domain, "type": type_word,
        "anchor": anchor, "box": [*map(float, lo), *map(float, hi)],
        "length": round(float(hi[0] - lo[0]), 3), "width": round(float(hi[2] - lo[2]), 3),
        "height": round(float(hi[1] - lo[1]), 3), "parts": [p for p in PARTS if p in built.lods[0].parts],
        "pivots": built.pivots, "tris": [lod.tris for lod in built.lods],
        "key": hashlib.sha1(source_key.encode()).hexdigest()[:16], **more,
    }


def write_index(folder: Path, game: str, game_build: str, source: str, units: dict[str, dict]) -> Path:
    out = folder / "model-pack.json"
    for e in units.values():
        e.setdefault("gameBuild", game_build)
        e.setdefault("source", source)
    doc = {"format": "3dheat-model-pack", "version": 1, "game": game, "gameBuild": game_build, "source": source,
           "units": dict(sorted(units.items()))}
    tmp = out.with_suffix(".json.part")
    tmp.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    tmp.replace(out)
    return out
