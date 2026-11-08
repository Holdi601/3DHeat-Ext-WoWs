"""
Everything of a replay the table and the match document do not hold whole,
kept whole beside them, and the count of what became of each kind of item:
the rule all 3DHeat converters follow,
https://github.com/Holdi601/3DHeat/blob/main/docs/converters.md.

Every item of a replay file is one of:

- a JSON block at the head of the file (`block 0`, `block 1`, ...);
- the container's own bytes: the two sizes after the blocks (`container
  sizes`), enciphered bytes after the last whole 8-byte block (`cipher
  tail`), bytes after the end of the compressed stream (`deflate tail`),
  bytes after the last whole packet (`stream tail`);
- a packet of the stream: `packet <type>`, or, for an entity call,
  `method <entity type>.<method>` and `property <entity type>.<property>`
  (the numbers are the game's own: entity types from the packets that create
  entities, methods and properties as the call names them).

The converter marks the items it read: `decoded` (whole in the table or the
match document) or `partial` (read in part; what was read goes into the row
as JSON). Every item not marked decoded becomes one row of the sidecar
`<match>.messages.parquet`, whole and unchanged. The self-check counts
`seen` from the stream's own packet index (and the file's blocks), `decoded`
from the marks, `partial` and `raw` from the rows actually in the sidecar;
`lost` is what is left, 0 unless an item went missing.

This file is the same in the World of Tanks and the World of Warships
converters; change both together.
"""

from __future__ import annotations

import json
import re
import struct
from collections import Counter
from typing import Any

import numpy as np

from . import bigworld as bw

RULE = "https://github.com/Holdi601/3DHeat/blob/main/docs/converters.md"

#: The sidecar's word in `<match>.<what>.parquet`.
WHAT = "messages"

#: The packet types that are entity calls: a property set, a method called.
ENTITY_CALLS = {7: "property", 8: "method"}

#: The packets that create an entity: entity id uint32, then its type uint16 (the player's own avatar, any other).
CREATES = (0, 5)


def entity_types(stream: bytes, idx: np.ndarray) -> dict[int, int]:
    """Every created entity's type number, from the packets that create entities."""
    out: dict[int, int] = {}
    for r in idx[np.isin(idx["type"], CREATES) & (idx["size"] >= 6)]:
        eid, kind = struct.unpack_from("<IH", stream, int(r["at"]))
        out.setdefault(eid, kind)
    return out


def entity_packets(stream: bytes, idx: np.ndarray, known: set[int]) -> set[int]:
    """
    The packet types (other than entity calls) whose payload begins with an
    entity id: those where the first four bytes are a known entity in 99% of
    the packets. Their rows get the entity, so a row can be joined to a track.
    """
    out = set()
    for kind in np.unique(idx["type"]):
        if int(kind) in ENTITY_CALLS:
            continue
        rows = idx[(idx["type"] == kind) & (idx["size"] >= 4)]
        if not len(rows) or len(rows) < 0.99 * int((idx["type"] == kind).sum()):
            continue
        ok = sum(struct.unpack_from("<I", stream, int(r["at"]))[0] in known for r in rows)
        if ok >= 0.99 * len(rows):
            out.add(int(kind))
    return out


def jsonable(value: Any) -> Any:
    """A decoded value as JSON: bytes as hex, tuples as lists, numbers that are not finite as None."""
    if isinstance(value, (bytes, bytearray)):
        return bytes(value).hex()
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [jsonable(v) for v in value]
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (float, np.floating)):
        return float(value) if np.isfinite(value) else None
    return value


class Ledger:
    """
    The marks a converter makes on a replay's items, and from them the
    sidecar and the self-check. Packets are marked by their payload's offset
    in the stream (`bigworld.Call.at`, `bigworld.Track.offset`, `idx["at"]`).
    """

    def __init__(self, rep: bw.Replay, idx: np.ndarray) -> None:
        self.rep, self.idx = rep, idx
        #: packet offset -> (whole, name, decoded JSON)
        self.marks: dict[int, tuple[bool, str, str]] = {}
        #: block number -> (whole, name, decoded JSON)
        self.blocks: dict[int, tuple[bool, str, str]] = {}
        #: Names of item types, where known (`packet 10` -> "position", `method 6.2` -> "health").
        self.names: dict[str, str] = {}
        self.types = entity_types(rep.stream, idx)
        self.with_entity = entity_packets(rep.stream, idx, set(self.types))

    def decoded(self, at: int, name: str = "") -> None:
        """A packet read whole into the table or the match document."""
        self.marks[at] = (True, name, "")

    def partial(self, at: int, value: Any = None, name: str = "") -> None:
        """A packet read in part: kept whole, with what was read (`value`, as JSON) beside it."""
        text = json.dumps(jsonable(value), ensure_ascii=False, separators=(",", ":")) if value is not None else ""
        if at not in self.marks or not self.marks[at][0]:
            self.marks[at] = (False, name, text)

    def block(self, i: int, whole: bool, name: str = "") -> None:
        self.blocks[i] = (whole, name, "")

    def item_type(self, kind: int, payload: bytes) -> tuple[str, int | None, int | None]:
        """A packet's item type, its entity and its method or property number."""
        if kind in ENTITY_CALLS and len(payload) >= 12:
            entity, method, n = struct.unpack_from("<III", payload)
            if n == len(payload) - 12:
                et = self.types.get(entity)
                return f"{ENTITY_CALLS[kind]} {'?' if et is None else et}.{method}", entity, method
        entity = struct.unpack_from("<I", payload)[0] if kind in self.with_entity and len(payload) >= 4 else None
        return f"packet {kind}", entity, None

    def build(self, sidecar: str) -> tuple[Any, dict[str, Any]]:
        """The sidecar as an Arrow table, and the `completeness` block (naming the sidecar file `sidecar`)."""
        import pyarrow as pa
        import pyarrow.compute as pc

        rep, stream = self.rep, self.rep.stream
        cols: dict[str, list] = {k: [] for k in ("time", "type", "name", "entity", "decoded", "payload", "text",
                                                 "entityType", "packet", "method")}
        seen: Counter = Counter()
        decoded: Counter = Counter()
        partial: Counter = Counter()
        named: dict[str, str] = dict(self.names)  # an item type's name: given, else that of its first marked item

        def row(t, typ, name, entity, dec, payload, text, packet=None, method=None) -> None:
            cols["time"].append(t)
            cols["type"].append(typ)
            cols["name"].append(name or self.names.get(typ, ""))
            cols["entity"].append(entity)
            cols["decoded"].append(dec)
            cols["payload"].append(payload)
            cols["text"].append(text)
            cols["entityType"].append(self.types.get(entity) if entity is not None else None)
            cols["packet"].append(packet)
            cols["method"].append(method)

        for i, raw in enumerate(rep.raw_blocks):
            typ = f"block {i}"
            seen[typ] += 1
            whole, name, dec = self.blocks.get(i, (False, "", ""))
            if name:
                named.setdefault(typ, name)
            if whole:
                decoded[typ] += 1
                continue
            try:
                text, payload = raw.decode("utf-8"), None
            except UnicodeDecodeError:
                text, payload = None, raw
            row(None, typ, name, None, dec, payload, text)
            partial[typ] += i in self.blocks
        end = int(self.idx["at"][-1] + self.idx["size"][-1]) if len(self.idx) else 0
        for typ, raw in (("container sizes", rep.sizes), ("cipher tail", rep.leftover), ("deflate tail", rep.unused),
                         ("stream tail", stream[end:])):
            if raw:
                seen[typ] += 1
                row(None, typ, "", None, "", bytes(raw), None)
        ats, sizes, kinds, times = (self.idx[k].tolist() for k in ("at", "size", "type", "time"))
        for at, size, kind, t in zip(ats, sizes, kinds, times):
            payload = stream[at : at + size]
            typ, entity, method = self.item_type(kind, payload)
            seen[typ] += 1
            whole, name, dec = self.marks.get(at, (False, "", ""))
            if name:
                named.setdefault(typ, name)
            if whole:
                decoded[typ] += 1
                continue
            row(t, typ, name, entity, dec, payload, None, kind, method)
            partial[typ] += at in self.marks
        table = pa.table({
            "time": pa.array(cols["time"], pa.float64()),
            "type": pa.array(cols["type"], pa.string()).dictionary_encode(),
            "name": pa.array(cols["name"], pa.string()).dictionary_encode(),
            "entity": pa.array(cols["entity"], pa.int64()),
            "decoded": pa.array(cols["decoded"], pa.string()),
            "payload": pa.array(cols["payload"], pa.binary()),
            "text": pa.array(cols["text"], pa.string()),
            "entityType": pa.array(cols["entityType"], pa.int32()),
            "packet": pa.array(cols["packet"], pa.int64()),
            "method": pa.array(cols["method"], pa.int64()),
        })
        # By kind, then entity, then time: like items side by side compress best (a third smaller than in stream
        # order); the blocks and the container's bytes (no packet) first.
        table = table.take(pc.sort_indices(table, [("packet", "ascending"), ("method", "ascending"),
                                                   ("entity", "ascending"), ("time", "ascending")],
                                           null_placement="at_start"))
        # The rows actually in the sidecar, counted from it, not from the marks.
        kept = Counter()
        if table.num_rows:
            for v in pc.value_counts(table["type"].combine_chunks().dictionary_decode()).to_pylist():
                kept[v["values"]] = v["counts"]
        types = {}
        for typ in sorted(seen, key=_order):
            p = min(partial[typ], kept[typ])
            types[typ] = {"seen": seen[typ], "decoded": decoded[typ], "partial": p, "raw": kept[typ] - p,
                          "lost": seen[typ] - decoded[typ] - kept[typ]}
            if named.get(typ):
                types[typ]["name"] = named[typ]
        return table, {
            "rule": RULE,
            "sidecars": [sidecar],
            "types": types,
            "seen": sum(seen.values()),
            "decoded": sum(decoded.values()),
            "partial": sum(t["partial"] for t in types.values()),
            "raw": sum(t["raw"] for t in types.values()),
            "lost": sum(t["lost"] for t in types.values()),
        }


def version(led: Ledger) -> str | None:
    """
    The client's version as the stream says it, once, near the start: a
    packet of its own, a length and the version's digits and dots (or
    commas). Read whole (into the summary's `streamVersion`); checked against
    the header's.
    """
    stream, idx = led.rep.stream, led.idx
    for kind in np.unique(idx["type"]):
        rows = idx[idx["type"] == kind]
        if len(rows) != 1 or not 8 <= int(rows[0]["size"]) <= 40:
            continue
        at, size = int(rows[0]["at"]), int(rows[0]["size"])
        p = stream[at : at + size]
        if struct.unpack_from("<I", p)[0] == size - 4 and re.fullmatch(rb"[0-9][0-9., ]*", p[4:]):
            led.names[f"packet {int(kind)}"] = "version"
            led.decoded(at, "version")
            return p[4:].decode("ascii")
    return None


#: The packet that says an entity left the client's view: its id, uint32, nothing else.
LEAVE = 4


def entities(led: Ledger, position: int | None, roles: dict[int, str]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """
    Every entity the stream creates: its type number and role (`roles`, by
    type), when it was created (each time it came into the client's view) and
    when it left. The creating packets are read in part (the id and the
    type; the properties after them are kept whole); the leaving packets
    whole (they hold the id alone). Marks both in `led`.

    The check: no position update of an entity (packet `position`) between
    its leaving and its next creation - `positionsWhileGone` is 0 when the
    leaving packet is what it is taken for.
    """
    stream, idx = led.rep.stream, led.idx
    out: dict[int, dict[str, Any]] = {}
    for r in idx[np.isin(idx["type"], CREATES + (LEAVE,))]:
        at, size, kind, t = int(r["at"]), int(r["size"]), int(r["type"]), float(r["time"])
        if kind == LEAVE:
            if size != 4:
                continue
            (eid,) = struct.unpack_from("<I", stream, at)
            if eid not in out:
                continue
            out[eid]["left"].append(t)
            led.decoded(at, "entity leaves")
            continue
        if size < 6:
            continue
        eid, et = struct.unpack_from("<IH", stream, at)
        e = out.setdefault(eid, {"entity": eid, "type": et, "role": roles.get(et, ""), "created": [], "left": []})
        e["created"].append(t)
        led.partial(at, {"entity": eid, "entityType": et}, "player created" if kind == 0 else "entity created")
    gone = 0
    if position is not None:
        spans = {e: list(zip(d["left"], d["created"][1:] + [np.inf])) for e, d in out.items() if d["left"]}
        for r in idx[(idx["type"] == position) & (idx["size"] >= 4)]:
            (eid,) = struct.unpack_from("<I", stream, int(r["at"]))
            t = float(r["time"])
            gone += any(a < t < b for a, b in spans.get(eid, ()))
    check = {"entities": len(out), "leaves": sum(len(d["left"]) for d in out.values()), "positionsWhileGone": gone}
    return sorted(out.values(), key=lambda d: (d["created"][0], d["entity"])), check


def _order(typ: str) -> tuple:
    """Blocks, the container, packets by number, then calls by entity type and number."""
    head, _, rest = typ.partition(" ")
    rank = {"block": 0, "container": 1, "cipher": 1, "deflate": 1, "stream": 1, "packet": 2, "property": 3,
            "method": 4}.get(head, 5)
    nums = tuple(int(x) if x.isdigit() else -1 for x in rest.replace(".", " ").split())
    return rank, nums, typ
