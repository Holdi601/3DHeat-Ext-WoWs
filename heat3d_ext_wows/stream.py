"""
Everything in a World of Warships packet stream besides positions and
sinkings, found by shape rather than by number.

The engine numbers an entity's methods and properties by their place in the
game's definition files, which change with patches (0.9.6 and 15.10 number the
same calls 40 apart). Each kind is found by what its arguments look like, and
the numbers found go into the match summary (`decoded`). What is read:

- **Damage to a ship** (a ship method): an array (count uint8) of (attacker's
  entity id int32, damage float32) - each hit the ship took, by whom.
- **Health** (a ship property, float32): found as the one that changes when
  damage comes in.
- **Shells** (an avatar method): an array of salvoes - shell type id, the
  shooter's entity id, salvo id uint32 each, then an array of shells of a
  fixed size beginning with the gun's position and the shell's direction
  (three float32 each).
- **Torpedoes** (an avatar method): the same, with one more uint32 (the skin)
  before the array, each torpedo its position and direction first.
- **Where shells ended** (an avatar method): an array of (shooter's entity
  id, hit type uint8, an array of records beginning with the place).
- **Chat** (an avatar method): the sender's id int32, then three strings: the
  channel (`battle_team`, `battle_common`, ...), the line, and an extra.
- **Pickles** (avatar methods whose argument is a Python pickle): the
  recording player's damage statistics, player updates, the battle's state -
  kept as they are, read by a reader that runs nothing.
"""

from __future__ import annotations

import struct
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Any

import numpy as np

from . import bigworld as bw

PROPERTY, METHOD = 7, 8


@dataclass
class Salvo:
    time: float
    kind: str  # "shell" or "torpedo"
    params: int
    owner: int
    salvo: int
    #: Each shell or torpedo: its start and direction (the direction's length is the speed, in world units).
    items: list[tuple[tuple[float, float, float], tuple[float, float, float]]]


@dataclass
class Ended:
    time: float
    owner: int
    hit_type: int
    points: list[tuple[float, float, float]]


@dataclass
class Decoded:
    damage: list[tuple[float, int, int, float]] = field(default_factory=list)  # time, victim, attacker, damage
    health: dict[int, tuple[np.ndarray, np.ndarray]] = field(default_factory=dict)  # ship -> times, values
    salvoes: list[Salvo] = field(default_factory=list)
    ended: list[Ended] = field(default_factory=list)
    chat: list[tuple[float, int, str, str, str]] = field(default_factory=list)  # time, sender, channel, line, extra
    pickles: list[tuple[float, int, Any]] = field(default_factory=list)  # time, method, value
    found: dict[str, Any] = field(default_factory=dict)


def _groups(calls: list[bw.Call]) -> dict[tuple[int, int], list[bw.Call]]:
    out: dict[tuple[int, int], list[bw.Call]] = defaultdict(list)
    for c in calls:
        out[(c.type, c.method)].append(c)
    return out


def _damage(groups: dict, ships: set[int], dec: Decoded) -> None:
    best, best_n = None, 0
    for (kind, m), cs in groups.items():
        if kind != METHOD or len(cs) < 2:
            continue
        if not all(len(c.args) >= 9 and len(c.args) == 1 + 8 * c.args[0] for c in cs):
            continue
        ok = total = 0
        for c in cs:
            for i in range(c.args[0]):
                who, dmg = struct.unpack_from("<if", c.args, 1 + 8 * i)
                total += 1
                ok += who in ships and np.isfinite(dmg) and 0 <= dmg < 1e6
        if ok >= 0.9 * total and len(cs) > best_n:
            best, best_n = m, len(cs)
    if best is None:
        return
    dec.found["damage"] = best
    for c in groups[(METHOD, best)]:
        for i in range(c.args[0]):
            who, dmg = struct.unpack_from("<if", c.args, 1 + 8 * i)
            dec.damage.append((c.time, c.entity, who, float(dmg)))


def _health(groups: dict, dec: Decoded) -> None:
    """
    The ships' float property that falls by what a damage call says: the
    server sends the new value a moment (up to a second) before the call, so
    each call is matched with a fall of the same size in the second before it.
    (Over a whole battle the two do not add up: repairs raise the health.)
    """
    calls: dict[tuple[float, int], float] = defaultdict(float)
    for t, victim, _, dmg in dec.damage:
        calls[(t, victim)] += dmg
    if not calls:
        return
    best, best_score = None, 0.0
    for (kind, m), cs in groups.items():
        if kind != PROPERTY or not all(len(c.args) == 4 for c in cs) or len(cs) < 3:
            continue
        falls: dict[int, list[tuple[float, float]]] = defaultdict(list)
        last: dict[int, float] = {}
        for c in cs:
            (v,) = struct.unpack("<f", c.args)
            if c.entity in last:
                falls[c.entity].append((c.time, last[c.entity] - v))
            last[c.entity] = v
        agree = 0
        for (t, victim), dmg in calls.items():
            agree += any(t - 1.0 <= ft <= t + 0.2 and abs(fall - dmg) <= max(1.0, 0.01 * dmg)
                         for ft, fall in falls.get(victim, ()))
        score = agree / len(calls)
        if score > best_score:
            best, best_score = m, score
    dec.found["healthAgreement"] = round(best_score, 3)
    if best is None or best_score < 0.3:
        return
    dec.found["health"] = best
    per: dict[int, list[tuple[float, float]]] = defaultdict(list)
    for c in groups[(PROPERTY, best)]:
        per[c.entity].append((c.time, struct.unpack("<f", c.args)[0]))
    dec.health = {e: (np.array([t for t, _ in v]), np.array([x for _, x in v])) for e, v in per.items()}


def _salvoes(buf: bytes, head: int, size: int, ships: set[int]) -> list[tuple[int, int, int, list]] | None:
    """`buf` as an array of salvoes with a header of `head` bytes and items of `size`; None if it is not."""
    try:
        n, at, out = buf[0], 1, []
        for _ in range(n):
            params, owner, salvo = struct.unpack_from("<III", buf, at)
            at += head
            k = buf[at]
            at += 1
            items = []
            for _ in range(k):
                pos, d = bw.vec3(buf, at), struct.unpack_from("<3f", buf, at + 12)
                if pos is None or not all(np.isfinite(d)):
                    return None
                items.append((pos, tuple(float(x) for x in d)))
                at += size
            if owner not in ships:
                return None
            out.append((params, owner, salvo, items))
        return out if at == len(buf) and n else None
    except (struct.error, IndexError):
        return None


def _shots(groups: dict, ships: set[int], dec: Decoded) -> None:
    found: dict[str, tuple[int, int]] = {}
    for kind_name, head in (("shell", 12), ("torpedo", 16)):
        best = None
        for (kind, m), cs in groups.items():
            if kind != METHOD or len(cs) < 3 or any(m == f[0] for f in found.values()):
                continue
            sample = cs[:: max(1, len(cs) // 50)]
            for size in range(26, 64):
                if sum(_salvoes(c.args, head, size, ships) is not None for c in sample) >= 0.9 * len(sample):
                    if best is None or len(cs) > len(groups[(METHOD, best[0])]):
                        best = (m, size)
                    break
        if best is not None:
            found[kind_name] = best
    for kind_name, (m, size) in found.items():
        head = 12 if kind_name == "shell" else 16
        dec.found[kind_name] = {"method": m, "size": size}
        for c in groups[(METHOD, m)]:
            for params, owner, salvo, items in _salvoes(c.args, head, size, ships) or []:
                dec.salvoes.append(Salvo(c.time, kind_name, params, owner, salvo, items))
    dec.salvoes.sort(key=lambda s: s.time)


#: Newer clients (15.x) end a shell's record with a flag; when it is 1, 29 more bytes follow (the shell's
#: state where it struck: a place, a velocity, a byte, a float).
FLAGGED_EXTRA = 29


def _parse_ended(buf: bytes, size: int, ships: set[int], flagged: bool = False) -> list[Ended] | None:
    try:
        n, at, out = buf[0], 1, []
        for _ in range(n):
            (owner,) = struct.unpack_from("<I", buf, at)
            hit, k = buf[at + 4], buf[at + 5]
            at += 6
            pts = []
            for _ in range(k):
                p = bw.vec3(buf, at)
                if p is None:
                    return None
                pts.append(p)
                at += size
                if flagged:
                    if buf[at - 1] not in (0, 1):
                        return None
                    at += FLAGGED_EXTRA if buf[at - 1] else 0
            if owner not in ships or not k:
                return None
            out.append(Ended(0.0, owner, hit, pts))
        return out if at == len(buf) and n else None
    except (struct.error, IndexError):
        return None


def _ended(groups: dict, ships: set[int], dec: Decoded) -> None:
    best = None
    taken = {f["method"] for f in (dec.found.get("shell"), dec.found.get("torpedo")) if f}
    for (kind, m), cs in groups.items():
        if kind != METHOD or len(cs) < 3 or m in taken:
            continue
        sample = cs[:: max(1, len(cs) // 50)]
        for size, flagged in [(15, True)] + [(n, False) for n in range(12, 32)]:
            if sum(_parse_ended(c.args, size, ships, flagged) is not None for c in sample) >= 0.9 * len(sample):
                if best is None or len(cs) > len(groups[(METHOD, best[0])]):
                    best = (m, size, flagged)
                break
    if best is None:
        return
    m, size, flagged = best
    dec.found["ended"] = {"method": m, "size": size, "flagged": flagged}
    for c in groups[(METHOD, m)]:
        for e in _parse_ended(c.args, size, ships, flagged) or []:
            e.time = c.time
            dec.ended.append(e)


def _chat(groups: dict, dec: Decoded) -> None:
    for (kind, m), cs in groups.items():
        if kind != METHOD:
            continue
        out = []
        for c in cs:
            try:
                (sender,) = struct.unpack_from("<i", c.args)
                channel, at = bw.bw_string(c.args, 4)
                line, at = bw.bw_string(c.args, at)
                extra, at = bw.bw_string(c.args, at)
            except (ValueError, struct.error):
                break
            if at != len(c.args) or not channel.startswith(b"battle_"):
                break
            out.append((c.time, sender, channel.decode("utf-8", "replace"), line.decode("utf-8", "replace"),
                        extra.decode("utf-8", "replace")))
        else:
            if out:
                dec.chat = out
                dec.found["chat"] = m
                return


def _pickles(groups: dict, dec: Decoded) -> None:
    """Every avatar call whose arguments are one pickle (with its length first): kept as data."""
    methods = []
    for (kind, m), cs in groups.items():
        if kind != METHOD:
            continue
        got = []
        for c in cs:
            try:
                raw, end = bw.bw_string(c.args, 0)
                if end != len(c.args) or raw[:1] not in (b"\x80", b"\x78"):
                    break
                got.append((c.time, m, bw.unpickle(raw)))
            except Exception:  # noqa: BLE001 - not a pickle: not this method
                break
        else:
            if got:
                dec.pickles += got
                methods.append(m)
    dec.pickles.sort(key=lambda p: p[0])
    if methods:
        dec.found["pickles"] = sorted(methods)


def decode(stream: bytes, idx: np.ndarray, ships: set[int], avatar: int | None) -> Decoded:
    dec = Decoded()
    calls = bw.calls(stream, [k for k in bw.call_types(stream, idx) if k in (PROPERTY, METHOD)], idx)
    on_ships = _groups([c for c in calls if c.entity in ships])
    on_avatar = _groups([c for c in calls if c.entity == avatar]) if avatar is not None else {}
    _damage(on_ships, ships, dec)
    _health(on_ships, dec)
    _shots(on_avatar, ships, dec)
    _ended(on_avatar, ships, dec)
    _chat(on_avatar, dec)
    _pickles(on_avatar, dec)
    return dec


def damage_stats(dec: Decoded) -> dict[tuple[int, int], list] | None:
    """
    The recording player's own damage statistics as the game keeps them:
    {(weapon, kind): [count, amount]}, each call bringing the entries that
    changed - merged here, the last value of each. Kind 0 is damage dealt
    (the sum checks against the damage read); the others (spotting,
    potential damage, ...) are kept unnamed.
    """
    merged: dict[tuple[int, int], list] = {}
    for _, _, v in dec.pickles:
        if isinstance(v, dict) and v and all(
            isinstance(k, tuple) and len(k) == 2 and isinstance(x, list) and len(x) == 2 for k, x in v.items()
        ):
            merged.update(v)
    return merged or None


def counts(dec: Decoded) -> dict[str, int]:
    return dict(Counter(s.kind for s in dec.salvoes))
