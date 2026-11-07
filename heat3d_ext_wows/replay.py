"""
A World of Warships replay (.wowsreplay) as rows: every ship's position over
time, and every ship sunk where it happened.

What the file holds (see `bigworld` for the container):

- The first JSON block: the map (`mapName`, e.g. `spaces/54_Faroe`), the
  client version, the recording player (`playerName`, `playerVehicle`, e.g.
  `PASB018-Iowa-1944`) and the roster - `vehicles`, a list of `name`, `id`
  (the player's account), `shipId` (the ship's number in the game's own
  parameters, not its name) and `relation` (0 the recording player, 1 an ally,
  2 an enemy). There are no results; newer clients add two blocks that are not
  read.
- The packet stream. The ships' positions are engine position updates, as in
  World of Tanks, with the heading, in the game's world units (x east, y up -
  sea level 0 - z north). A world unit is not a metre: a battleship at speed
  covers about 2.4 of them a second, and a map spans about 1,200. Placed
  against hull geometry a unit is 15 m; the game's own range figures put it at
  30 m (landaire/wows-toolkit, `wows-core/src/units.rs`, MIT, which leaves
  the two unreconciled). The table keeps world units, scale 1, so it lands on
  a level exported in the game's own units; the recording client gets them for the ships it can see (its own
  team, enemies while spotted or near), several times a second while they
  move, less while they do not. Its own ship is in a packet of its own (the
  client writes it rather than receives it), about seven times a second.

Which entity in the stream is which player is not in the JSON. The server
sends it once, at the start, as a pickled list of player records (Python 2
pickle, a list of (key number, value) pairs per player). The key numbers
change with patches, so this reader finds the keys by what their values are:
the one whose values are the roster's names, and the one whose values are
entities with position updates. Unpickling is done with a loader that builds
nothing but plain data - every class the pickle names becomes an empty
placeholder - so a crafted replay cannot run code through it.

Ships sunk come from the server's call announcing a death to the client,
(victim, killer, cause), found by its shape: twelve bytes of arguments, the
first two entity ids of ships, each victim once. Its time is exact; its place
is where the victim was last seen, when that was within five seconds. The
cause is the game's own number, not named here.

Damage, health, shells, torpedoes, where shells ended, the chat and the
pickled calls to the recording player are read by `stream`, also by shape.
"""

from __future__ import annotations

import io
import math
import pickle
import struct
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np

from . import bigworld as bw
from . import stream as st

#: The key World of Warships enciphers its replays' packet streams with, as the
#: community tools that read them have published.
KEY = bytes.fromhex("29B7C909383F8488FA98EC4E131979FB")

HINTS = {
    "version": 1,
    "kind": "wows-replay",
    "game": "World of Warships",
    # BigWorld's world: x east, y up, z north - left-handed, so Z is flipped to keep the map unmirrored.
    "axes": {"up": "y", "flipX": False, "flipY": False, "flipZ": True, "scale": 1},
    # A middling cruiser, about 180 m: 12 world units at 15 m each (see the module docstring).
    "entity": {"size": 12},
    "columns": {
        "x": "x",
        "y": "y",
        "z": "z",
        "time": "time",
        "timeUnit": "seconds",
        "personId": "player",
        "teamId": "team",
        "sessionId": "match",
        "lookMode": "vector",
        "dirX": "dirX",
        "dirY": "dirY",
        "dirZ": "dirZ",
        "extra": ["event", "vehicle", "type", "own", "battleTime", "other", "reason", "map", "value", "health",
                  "text", "shot", "params"],
    },
}

COLUMNS = {
    "match": "s", "map": "s", "time": "d", "battleTime": "f", "event": "s",
    "player": "s", "team": "s", "vehicle": "s", "type": "s", "own": "i",
    "x": "f", "y": "f", "z": "f", "dirX": "f", "dirY": "f", "dirZ": "f",
    "other": "s", "reason": "s", "entity": "l",
    "value": "f", "health": "f", "text": "s", "shot": "l", "params": "l",
}  # fmt: skip

#: The class letter in a ship's index name (`PASB018`: P, nation A, S, class B).
CLASSES = {"A": "aircraft carrier", "B": "battleship", "C": "cruiser", "D": "destroyer", "S": "submarine"}

FRESH_SECONDS = 5.0


@dataclass
class Match:
    name: str
    map: str
    rows: dict[str, list] = field(default_factory=lambda: {c: [] for c in COLUMNS})
    summary: dict[str, Any] = field(default_factory=dict)

    def add(self, **row: Any) -> None:
        for c in COLUMNS:
            self.rows[c].append(row.get(c))


# ---------------------------------------------------------------- the pickles


class _Placeholder:
    """What every class a pickle names becomes: it keeps its arguments and does nothing."""

    def __init__(self, *args: Any, **kw: Any) -> None:
        self.args = args

    def __setstate__(self, state: Any) -> None:
        self.state = state


class _PlainUnpickler(pickle.Unpickler):
    def find_class(self, module: str, name: str) -> Any:  # noqa: ARG002 - nothing is ever looked up
        return _Placeholder


def unpickle(buf: bytes) -> Any:
    """A pickle from a replay, as plain data only. Raises on anything that is not a pickle."""
    return _PlainUnpickler(io.BytesIO(buf), encoding="latin1").load()


def _records(obj: Any) -> list[list[tuple[int, Any]]] | None:
    """A list of player records: each a list of (key number, value)."""
    if not isinstance(obj, list) or not obj:
        return None
    for rec in obj:
        if not isinstance(rec, list) or not rec:
            return None
        for kv in rec:
            if not (isinstance(kv, tuple) and len(kv) == 2 and isinstance(kv[0], int)):
                return None
    return obj


def player_records(calls: list[bw.Call]) -> list[tuple[list[list[tuple[int, Any]]], bw.Call]]:
    """Every pickled list of player records in the calls, each with the call it came in."""
    found: list[tuple[list[list[tuple[int, Any]]], bw.Call]] = []
    for c in calls:
        if len(c.args) < 32 or b"\x80\x02" not in c.args:
            continue
        at = 0
        while True:
            at = c.args.find(b"\x80\x02", at)
            if at < 0:
                break
            try:
                recs = _records(unpickle(c.args[at:]))
            except Exception:  # noqa: BLE001 - most hits are not pickles
                recs = None
            at += 2
            if recs:
                found.append((recs, c))
    return found


def _key_for(records: list[list[tuple[int, Any]]], values: set) -> int | None:
    """The key number whose values are most often in `values`."""
    counts: dict[int, int] = {}
    for rec in records:
        for k, v in rec:
            if isinstance(v, (int, str)) and not isinstance(v, bool) and v in values:
                counts[k] = counts.get(k, 0) + 1
    return max(counts, key=lambda k: counts[k]) if counts else None


# ------------------------------------------------------------------ the match


def ship_class(index_name: str) -> str:
    """`PASB018-Iowa-1944` -> "battleship"; "ship" when the name does not say."""
    head = index_name.split("-")[0]
    return CLASSES.get(head[3:4], "ship") if len(head) >= 4 and head[0] == "P" and head[2] == "S" else "ship"


def read(buf: bytes, name: str = "replay", ship_names: dict[str, str] | None = None) -> Match:
    """
    A replay's bytes as a match. `name` is used when no match id is found;
    `ship_names` maps a roster `shipId` to a name, where the caller has one.
    """
    rep = bw.read_replay(buf, KEY)
    head = rep.header
    if not head:
        raise ValueError("the replay has no readable header")
    roster = [v for v in head.get("vehicles") or [] if isinstance(v, dict)]
    me = str(head.get("playerName") or "")
    map_id = str(head.get("mapName") or "unknown")
    ship_names = ship_names or {}

    idx = bw.index(rep.stream)
    pos_kind = bw.find_position_type(rep.stream, idx)
    all_tracks = bw.tracks(rep.stream, pos_kind, idx) if pos_kind is not None else {}
    calls = bw.calls(rep.stream, bw.call_types(rep.stream, idx), idx)

    # Which entity is which player: from the pickled records.
    names = {str(v.get("name")) for v in roster if v.get("name")}
    by_entity: dict[int, dict[str, Any]] = {}
    states_call = None
    for recs, call in player_records(calls):
        name_key = _key_for(recs, names)
        entity_key = _key_for(recs, set(all_tracks))
        if name_key is None or entity_key is None:
            continue  # not the roster: a later partial update, say
        states_call = states_call or call
        for rec in recs:
            d = dict(rec)
            n, e = d.get(name_key), d.get(entity_key)
            if isinstance(n, str) and isinstance(e, int) and not isinstance(e, bool):
                by_entity[e] = {"name": n, "record": {str(k): bw.plain(x) for k, x in rec}}
    by_name = {str(v.get("name")): v for v in roster}
    avatar = states_call.entity if states_call else None
    match_id = name
    if states_call and len(states_call.args) >= 8:
        (arena,) = struct.unpack_from("<q", states_call.args, 0)
        if arena > 0:
            match_id = str(arena)
    m = Match(name=match_id, map=map_id)

    def who(entity: int) -> dict[str, Any]:
        n = by_entity.get(entity, {}).get("name")
        v = by_name.get(n or "", {})
        own = bool(me) and n == me
        ship = str(v.get("shipId") or "")
        vehicle = str(head.get("playerVehicle") or ship) if own else ship_names.get(ship, ship)
        return {
            "player": n or f"entity {entity}",
            "team": {0: "ally", 1: "ally", 2: "enemy"}.get(v.get("relation"), ""),
            "vehicle": vehicle,
            "type": ship_class(vehicle),
            "own": 1 if own else 0,
            "entity": entity,
        }

    tracks = {e: t for e, t in all_tracks.items() if e in by_entity}
    own_entity = next((e for e, d in by_entity.items() if d["name"] == me), None)
    own_kind = None
    if own_entity is not None and own_entity not in tracks:
        own_kind, own = bw.own_track(rep.stream, own_entity, idx)
        if own is not None:
            tracks[own_entity] = own
    # Ships lie perfectly still in the countdown and gather way slowly, and a world unit is 15 m or more:
    # the first twentieth of a unit is the start.
    start = bw.battle_start(tracks, threshold=0.05)

    # Ships sunk: the call (victim, killer, cause) on the player's avatar, found by its shape.
    deaths: dict[int, tuple[float, int, int]] = {}
    death_method = None
    ships = set(by_entity)
    candidates: dict[tuple[int, int], list[bw.Call]] = {}
    for c in calls:
        if c.entity == avatar and len(c.args) == 12:
            candidates.setdefault((c.type, c.method), []).append(c)
    best: list[tuple[float, int, int]] = []
    best_victims: list[int] = []
    for method, cs in candidates.items():
        rows = [struct.unpack("<III", c.args) for c in cs]
        victims = [r[0] for r in rows]
        if (
            all(v in ships for v in victims)
            and len(set(victims)) == len(victims)
            and all(k in ships or k == 0 for _, k, _ in rows)
            and all(r < 256 for _, _, r in rows)
            and len(rows) > len(best)
        ):
            best = [(c.time, k, r) for c, (_, k, r) in zip(cs, rows)]
            best_victims = victims
            death_method = list(method)
    for victim, (t, k, r) in zip(best_victims, best):
        deaths[victim] = (t, k, r)

    for e, t in sorted(tracks.items()):
        w = who(e)
        end = deaths[e][0] if e in deaths else math.inf
        keep = t.time <= end
        for tt, x, y, z, yaw in zip(t.time[keep], t.x[keep], t.y[keep], t.z[keep], t.yaw[keep]):
            m.add(match=match_id, map=map_id, time=float(tt), battleTime=_bt(tt, start), event="position",
                  x=x, y=y, z=z, dirX=math.sin(yaw), dirY=0.0, dirZ=math.cos(yaw), **w)

    # Everything else in the stream: damage, health, shells, torpedoes, where shells ended, chat, pickles.
    dec = st.decode(rep.stream, idx, set(by_entity), avatar)

    def where(e: int | None, t: float) -> tuple[float, float, float] | None:
        i = _fresh(tracks.get(e), t) if e is not None else None
        if i is None:
            return None
        tr = tracks[e]
        return float(tr.x[i]), float(tr.y[i]), float(tr.z[i])

    def label(e: int | None) -> str | None:
        return who(e)["player"] if e is not None and e in by_entity else None

    def add(event: str, t: float, e: int | None, pos: tuple[float, float, float] | None, **kw: Any) -> None:
        if pos is None:
            return
        w = who(e) if e is not None and e in by_entity else {"player": "", "team": "", "vehicle": "", "type": "",
                                                              "own": 0}
        m.add(match=match_id, map=map_id, time=t, battleTime=_bt(t, start), event=event, x=pos[0], y=pos[1],
              z=pos[2], **{**w, **kw})

    def health_at(e: int, t: float) -> float | None:
        if e not in dec.health:
            return None
        ht, hv = dec.health[e]
        i = int(np.searchsorted(ht, t + 0.2, side="right")) - 1
        return float(hv[i]) if i >= 0 else None

    for t, victim, attacker, dmg in dec.damage:
        about = dict(value=dmg, health=health_at(victim, t))
        add("hurt", t, victim, where(victim, t), other=label(attacker), **about)
        if attacker != victim:
            add("damage", t, attacker, where(attacker, t), other=label(victim), **about)
    for sv in dec.salvoes:
        for pos, d in sv.items:
            speed = math.sqrt(sum(x * x for x in d))
            dirs = dict(dirX=d[0] / speed, dirY=d[1] / speed, dirZ=d[2] / speed) if speed > 0 else {}
            add("shot" if sv.kind == "shell" else "torpedo", sv.time, sv.owner, pos, value=speed, shot=sv.salvo,
                params=sv.params, **dirs)
    for e in dec.ended:
        for p in e.points:
            add("impact", e.time, e.owner, p, reason=str(e.hit_type))
    account = {v.get("id"): str(v.get("name")) for v in roster}
    entity_of_name = {d["name"]: e for e, d in by_entity.items()}
    chat = []
    # The sender is a ship, an account, or (older clients) another of the ids in the player's record.
    in_record = {}
    for e, d in by_entity.items():
        for v in d["record"].values():
            if isinstance(v, int) and not isinstance(v, bool) and v > 1000:
                in_record.setdefault(v, e)
    for t, sender, channel, line, extra in dec.chat:
        e = sender if sender in by_entity else entity_of_name.get(account.get(sender, "")) or in_record.get(sender)
        chat.append({"time": round(t, 2), "sender": label(e) or account.get(sender) or sender, "channel": channel,
                     "text": line, "extra": extra or None})
        add("chat", t, e, where(e, t), text=line, reason=channel)

    kills = []
    for victim, (t, killer, cause) in sorted(deaths.items(), key=lambda kv: kv[1][0]):
        vw = who(victim)
        kw = who(killer) if killer in ships else None
        kill: dict[str, Any] = {"time": round(t, 2), "victim": vw["player"], "killer": kw["player"] if kw else None,
                                "reason": cause}
        i = _fresh(tracks.get(victim), t)
        if i is not None:
            vt = tracks[victim]
            kill.update(x=float(vt.x[i]), y=float(vt.y[i]), z=float(vt.z[i]))
            m.add(match=match_id, map=map_id, time=t, battleTime=_bt(t, start), event="death",
                  x=vt.x[i], y=vt.y[i], z=vt.z[i], other=kill["killer"], reason=str(cause), **vw)
        k = _fresh(tracks.get(killer), t) if kw and killer != victim else None
        if k is not None:
            kt = tracks[killer]
            m.add(match=match_id, map=map_id, time=t, battleTime=_bt(t, start), event="kill",
                  x=kt.x[k], y=kt.y[k], z=kt.z[k], other=vw["player"], reason=str(cause), **kw)
        kills.append(kill)

    players = []
    entity_of = {d["name"]: e for e, d in by_entity.items()}
    for v in sorted(roster, key=lambda v: (v.get("relation", 9) == 2, str(v.get("name")))):
        e = entity_of.get(str(v.get("name")))
        w = who(e) if e is not None else {}
        t = tracks.get(e) if e is not None else None
        players.append({
            "name": v.get("name"),
            "team": {0: "ally", 1: "ally", 2: "enemy"}.get(v.get("relation"), ""),
            "relation": v.get("relation"),
            "shipId": v.get("shipId"),
            "vehicle": w.get("vehicle") or str(v.get("shipId") or ""),
            "entity": e,
            "own": bool(me) and v.get("name") == me,
            "samples": int(len(t.time)) if t is not None else 0,
            "kills": sum(1 for _, k, _ in deaths.values() if k == e) if e is not None and deaths else None,
            "survived": (e not in deaths) if e is not None and death_method is not None else None,
            # What the recording client saw: its own team throughout, enemies while in range.
            "seen": None if e is None else {
                "damageDealt": round(sum(x for _, _, a, x in dec.damage if a == e), 1),
                "damageReceived": round(sum(x for _, vv, _, x in dec.damage if vv == e), 1),
                "shells": sum(len(sv.items) for sv in dec.salvoes if sv.owner == e and sv.kind == "shell"),
                "torpedoes": sum(len(sv.items) for sv in dec.salvoes if sv.owner == e and sv.kind == "torpedo"),
                "lastHealth": float(dec.health[e][1][-1]) if e in dec.health else None,
            },
            "header": v,
            "record": by_entity.get(e, {}).get("record") if e is not None else None,
        })  # fmt: skip
    m.summary = {
        "format": "heat3d-wows-match",
        "version": 2,
        "game": "World of Warships",
        "match": match_id,
        "map": map_id,
        "mapName": head.get("mapDisplayName"),
        "clientVersion": str(head.get("clientVersionFromExe") or "").replace(",", "."),
        "recorded": head.get("dateTime"),
        "player": me or None,
        "vehicle": head.get("playerVehicle"),
        "gameType": head.get("gameType"),
        "scenario": head.get("scenario"),
        "duration": head.get("duration"),
        "truncated": rep.truncated,
        "battleStart": round(start, 2) if start is not None else None,
        "recordingSeconds": round(float(idx["time"].max()), 2) if len(idx) else 0.0,
        "positionPacket": pos_kind,
        "ownPositionPacket": own_kind,
        "deathMethod": death_method,
        "hz": bw.rate({e: t for e, t in tracks.items() if e != own_entity}),
        "ownHz": bw.rate({own_entity: tracks[own_entity]}) if own_entity in tracks else None,
        "positions": int(sum(1 for e in m.rows["event"] if e == "position")),
        "units": "World of Warships world units (15 m by hull geometry, 30 m by the game's ranges); "
        "x east, y up (sea level 0), z north",
        "players": players,
        "kills": kills,
        "events": dict(sorted(Counter(e for e in m.rows["event"] if e != "position").items())),
        "decoded": dec.found,
        "chat": chat,
        "damageStats": [{"weapon": k[0], "kind": k[1], "count": v[0], "amount": v[1]}
                        for k, v in sorted((st.damage_stats(dec) or {}).items())],
        "avatarPickles": [{"time": round(t, 2), "method": mm, "value": bw.plain(v)} for t, mm, v in dec.pickles],
        # The header as the file has it, but for the roster (in each player's line), and the blocks after it.
        "header": {k: v for k, v in head.items() if k != "vehicles"},
        "moreBlocks": [bw.plain(b) for b in rep.blocks[1:]],
    }
    return m


def _fresh(track: bw.Track | None, t: float | None) -> int | None:
    """The sample of `track` that says where it was at `t`: the last one by then, if it is recent."""
    if track is None or t is None:
        return None
    i = track.at(t + 0.5)
    return i if i is not None and t - track.time[i] <= FRESH_SECONDS else None


def _bt(t: float, start: float | None) -> float | None:
    return float(t) - start if start is not None else None


def read_file(path: str | Path, ship_names: dict[str, str] | None = None) -> Match:
    p = Path(path)
    return read(p.read_bytes(), name=p.stem, ship_names=ship_names)
