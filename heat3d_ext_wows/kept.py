"""
What of a World of Warships replay is read, and what is kept whole: the
marks on every item for `sidecar.Ledger`, so that the sidecar
`<match>.messages.parquet` holds everything the table and the match document
do not, and the match document says how much of each kind there was.

Items read in part (`partial`) carry what was read as JSON in the sidecar's
`decoded`; the layouts are the ones `stream` and `replay` find (see there):

| Item | `decoded` |
|---|---|
| position, own ship's position (in the table) | none: x, y, z, yaw, pitch, roll are the table's row |
| damage (ship method) | hits: [attacker, damage] each |
| health (ship property) | health |
| shells, torpedoes (avatar methods) | salvoes: params, owner, salvo, items ([start, direction] each) |
| where shells ended (avatar method) | ended: owner, hitType, points |
| chat (avatar method) | sender, channel, line, extra |
| pickled calls (avatar methods) | value (the pickle as JSON) |
| sinking (avatar method) | victim, killer, cause |
| players' records (avatar method) | arenaUniqueID, records (their number; the records are in the summary) |
| entity created (packets 0, 5) | entity, entityType |
"""

from __future__ import annotations

import json
import struct
from typing import Any

import numpy as np

from . import bigworld as bw
from . import sidecar as sc
from . import stream as st


def _group(calls: list[bw.Call], kind: int, method: int, entities: set[int]) -> list[bw.Call]:
    return [c for c in calls if c.type == kind and c.method == method and c.entity in entities]


def _safe(read):
    """`read`, with anything it cannot read as None rather than an error: what is not read stays raw, whole."""
    def inner(a: bytes):
        try:
            return read(a)
        except Exception:  # noqa: BLE001
            return None

    return inner


def ledger(rep: bw.Replay, idx: np.ndarray, calls: list[bw.Call], dec: st.Decoded, ships: set[int],
           avatar: int | None, position: int | None, in_table: set[int], death: list[int] | None,
           records: bw.Call | None) -> tuple[sc.Ledger, list[dict[str, Any]], dict[str, Any]]:
    """
    The marks for a replay read by `replay.read`: `ships` the ships'
    entities, `avatar` the recording player's, `position` the position packet
    type, `in_table` the offsets of the position packets that are rows of the
    table, `death` the sinking call's packet type and method, `records` the
    call with the players' records. Returns the ledger, the entities (for the
    match document) and their check.
    """
    led = sc.Ledger(rep, idx)
    roles: dict[int, str] = {}
    if avatar is not None and avatar in led.types:
        roles[led.types[avatar]] = "avatar"
    vt = [led.types[e] for e in ships if e in led.types]
    if vt:
        roles[max(set(vt), key=vt.count)] = "ship"
    ents, check = sc.entities(led, position, roles)
    check["roles"] = {str(k): v for k, v in sorted(roles.items())}
    if position is not None:
        led.names[f"packet {position}"] = "position"
    for at in in_table:
        led.partial(int(at), None, "position")
    found = dec.found
    me = {avatar} if avatar is not None else set()

    def mark(cs: list[bw.Call], name: str, read) -> None:
        for c in cs:
            led.partial(c.at, _safe(read)(c.args), name)

    if "damage" in found:
        mark(_group(calls, st.METHOD, found["damage"], ships), "damage",
             lambda a: {"hits": [struct.unpack_from("<if", a, 1 + 8 * i) for i in range(a[0])]})
    if "health" in found:
        mark(_group(calls, st.PROPERTY, found["health"], ships), "health",
             lambda a: {"health": struct.unpack("<f", a)[0]})
    for kind, head in (("shell", 12), ("torpedo", 16)):
        if kind in found:
            f = found[kind]
            mark(_group(calls, st.METHOD, f["method"], me), "shells" if kind == "shell" else "torpedoes",
                 lambda a, head=head, size=f["size"]: {"salvoes": [
                     {"params": p, "owner": o, "salvo": s, "items": items}
                     for p, o, s, items in st._salvoes(a, head, size, ships) or []]})
    if "ended" in found:
        f = found["ended"]
        mark(_group(calls, st.METHOD, f["method"], me), "shells ended",
             lambda a: {"ended": [{"owner": e.owner, "hitType": e.hit_type, "points": e.points}
                                  for e in st._parse_ended(a, f["size"], ships, f["flagged"]) or []]})
    if "chat" in found:
        def chat(a: bytes) -> dict[str, Any]:
            channel, at = bw.bw_string(a, 4)
            line, at = bw.bw_string(a, at)
            extra, at = bw.bw_string(a, at)
            return {"sender": struct.unpack_from("<i", a)[0], "channel": channel.decode("utf-8", "replace"),
                    "line": line.decode("utf-8", "replace"), "extra": extra.decode("utf-8", "replace")}

        mark(_group(calls, st.METHOD, found["chat"], me), "chat", chat)
    for m in found.get("pickles", []):
        mark(_group(calls, st.METHOD, m, me), "pickle", lambda a: {"value": bw.plain(bw.unpickle(bw.bw_string(a, 0)[0]))})
    if death:
        mark([c for c in _group(calls, death[0], death[1], me) if len(c.args) == 12], "sinking",
             lambda a: dict(zip(("victim", "killer", "cause"), struct.unpack("<III", a))))
    if records is not None:
        led.partial(records.at, {"arenaUniqueID": struct.unpack_from("<q", records.args)[0]}, "players' records")
    return led, ents, check


def results(led: sc.Ledger) -> Any:
    """
    The battle's results, as newer clients (15.x) keep them in the stream: a
    packet of its own near the end, a length and a JSON object with the
    battle's `arenaUniqueID`, found by that shape. Read whole into the
    summary's `results`; None when the replay has none (older clients, or a
    recording that stopped early).
    """
    stream, idx = led.rep.stream, led.idx
    for r in idx[idx["size"] > 64]:
        at, size = int(r["at"]), int(r["size"])
        if stream[at + 4 : at + 5] != b"{" or struct.unpack_from("<I", stream, at)[0] != size - 4:
            continue
        try:
            value = json.loads(stream[at + 4 : at + size].decode("utf-8"))
        except ValueError:
            continue
        if isinstance(value, dict) and "arenaUniqueID" in value:
            led.names[f"packet {int(r['type'])}"] = "results"
            led.decoded(at, "results")
            return value
    return None


def block_ids(text: str) -> dict[str, int] | None:
    """
    The last block of newer clients' replays (15.x): two numbers joined by a
    dot, `<account>.<arenaUniqueID>` - the recording player's account and the
    battle. Read as text (as a JSON number it loses the battle's digits).
    """
    head, dot, tail = text.strip().partition(".")
    return {"account": int(head), "arenaUniqueID": int(tail)} if dot and head.isdigit() and tail.isdigit() else None
