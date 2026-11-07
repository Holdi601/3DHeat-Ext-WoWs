"""
The replay container World of Tanks and World of Warships share, and the
packet stream inside it.

Both games run on Wargaming's BigWorld engine, and both save a replay as:

    uint32   0x11343212, the magic
    uint32   how many JSON blocks follow (1: the battle as it began; 2 or 3:
             the results the server sent at the end, too)
    per block: uint32 length, that many bytes of UTF-8 JSON
    8 bytes  two uint32 sizes (not needed: the stream says its own length)
    the rest the game's packet stream, zlib-compressed, then enciphered with
             Blowfish in 8-byte blocks, each block XORed with the plain text
             of the one before it

The first JSON block is in the clear and has the map, the recording player,
the client version and the roster. The stream holds what the client was told
during the battle, packet by packet:

    uint32   payload length
    uint32   packet type
    float32  seconds since the recording began
    payload

The two games use the same engine packets for the same things - the one this
module looks for is the position update, which carries an entity id, a
position in metres (x east, y up, z north) and its heading - but they number
other packets differently, and both renumber them now and then with a patch.
Each game's decoder therefore finds the packet types it needs by their shape,
not by a fixed number; see `find_position_type`.

The Blowfish key of each game is the one the game itself uses, published
since 2013 by the community tools that read these files. Blowfish's own
tables are the hexadecimal digits of pi (Schneier, 1993); they are computed
here rather than typed in.
"""

from __future__ import annotations

import json
import struct
import zlib
from dataclasses import dataclass
from functools import lru_cache
from typing import Any

import numpy as np

MAGIC = 0x11343212


# --------------------------------------------------------------------- Blowfish


@lru_cache(maxsize=1)
def _pi_words() -> tuple[int, ...]:
    """The first 1042 32-bit words of pi's fraction in hexadecimal: Blowfish's P-array and S-boxes."""
    words = 18 + 4 * 256
    bits = words * 32 + 64  # guard bits

    def arctan_inv(x: int) -> int:
        # arctan(1/x) * 2^bits by its series
        total = term = (1 << bits) // x
        x2, n, sign = x * x, 1, -1
        while term:
            term //= x2
            n += 2
            total += sign * (term // n)
            sign = -sign
        return total

    pi = 16 * arctan_inv(5) - 4 * arctan_inv(239)  # Machin
    frac = (pi - (3 << bits)) >> 64  # the fraction, words * 32 bits of it
    return tuple((frac >> (32 * (words - 1 - i))) & 0xFFFFFFFF for i in range(words))


class Blowfish:
    """
    Blowfish (Schneier, 1993), deciphering many blocks at once with numpy.

    Big-endian blocks, as the cipher is defined: the test vector key 0, block 0
    gives 4E F9 97 45 61 98 DD 78.
    """

    def __init__(self, key: bytes) -> None:
        if not 4 <= len(key) <= 56:
            raise ValueError("a Blowfish key is 4 to 56 bytes")
        pi = _pi_words()
        p = list(pi[:18])
        s = [list(pi[18 + 256 * i : 18 + 256 * (i + 1)]) for i in range(4)]
        k = (key * (72 // len(key) + 1))[:72]
        for i in range(18):
            p[i] ^= int.from_bytes(k[4 * i : 4 * i + 4], "big")
        self._p, self._s = p, s
        left = right = 0
        for i in range(0, 18, 2):
            left, right = self._encrypt_one(left, right)
            p[i], p[i + 1] = left, right
        for box in s:
            for i in range(0, 256, 2):
                left, right = self._encrypt_one(left, right)
                box[i], box[i + 1] = left, right
        self.P = np.array(p, dtype=np.uint32)
        self.S = np.array(s, dtype=np.uint32)

    def _f(self, x: int) -> int:
        s = self._s
        h = (s[0][x >> 24] + s[1][(x >> 16) & 0xFF]) & 0xFFFFFFFF
        return ((h ^ s[2][(x >> 8) & 0xFF]) + s[3][x & 0xFF]) & 0xFFFFFFFF

    def _encrypt_one(self, left: int, right: int) -> tuple[int, int]:
        p = self._p
        for i in range(16):
            left ^= p[i]
            right ^= self._f(left)
            left, right = right, left
        left, right = right, left
        return left ^ p[17], right ^ p[16]

    def encrypt_block(self, block: bytes) -> bytes:
        left, right = struct.unpack(">II", block)
        return struct.pack(">II", *self._encrypt_one(left, right))

    def decrypt(self, data: bytes) -> np.ndarray:
        """ECB-decipher `data` (a multiple of 8 bytes); returns the plain blocks as bytes in a uint8 array."""
        words = np.frombuffer(data, dtype=">u4").astype(np.uint32)
        left, right = words[0::2].copy(), words[1::2].copy()
        P, S = self.P, self.S
        for i in range(17, 1, -1):
            left ^= P[i]
            f = (S[0][left >> 24] + S[1][(left >> 16) & 0xFF]) ^ S[2][(left >> 8) & 0xFF]
            right ^= f + S[3][left & 0xFF]
            left, right = right, left
        left, right = right, left
        right ^= P[1]
        left ^= P[0]
        out = np.empty(len(words), dtype=">u4")
        out[0::2], out[1::2] = left, right
        return out.view(np.uint8)


# -------------------------------------------------------------------- container


@dataclass
class Replay:
    """A replay file taken apart: its JSON blocks and its packet stream."""

    blocks: list[Any]
    stream: bytes
    #: True when the stream ended before its end (a recording cut off by a crash).
    truncated: bool = False

    @property
    def header(self) -> dict[str, Any]:
        return self.blocks[0] if self.blocks and isinstance(self.blocks[0], dict) else {}


def read_blocks(buf: bytes) -> tuple[list[Any], int]:
    """The JSON blocks at the head of a replay, and where they end."""
    if len(buf) < 12:
        raise ValueError("too short for a replay")
    magic, count = struct.unpack_from("<II", buf, 0)
    if magic != MAGIC:
        raise ValueError("not a World of Tanks or World of Warships replay")
    if not 0 < count < 16:
        raise ValueError(f"a replay with {count} blocks")
    at = 8
    blocks: list[Any] = []
    for _ in range(count):
        (n,) = struct.unpack_from("<I", buf, at)
        at += 4
        if at + n > len(buf):
            raise ValueError("a block runs past the end of the file")
        raw = buf[at : at + n]
        at += n
        try:
            blocks.append(json.loads(raw.decode("utf-8", errors="replace")))
        except ValueError:
            blocks.append(None)  # a block that is not JSON is kept as a gap, not a failure
    return blocks, at


def read_replay(buf: bytes, key: bytes) -> Replay:
    """A whole replay: the blocks, and the stream deciphered and inflated."""
    blocks, at = read_blocks(buf)
    body = buf[at + 8 :]
    body = body[: len(body) - len(body) % 8]
    if not body:
        return Replay(blocks, b"")
    plain = Blowfish(key).decrypt(body)
    # Each block was XORed with the plain text before it: undo it with a running XOR.
    chained = np.bitwise_xor.accumulate(plain.view(np.uint64)).view(np.uint8).tobytes()
    z = zlib.decompressobj()
    try:
        stream = z.decompress(chained)
    except zlib.error as e:
        raise ValueError(f"the packet stream does not inflate ({e}); not a replay this reader knows") from e
    return Replay(blocks, stream, truncated=not z.eof)


# ---------------------------------------------------------------------- packets


def index(stream: bytes) -> np.ndarray:
    """Every packet's offset, length, type and time, as a structured array - for finding packets by shape."""
    rows = []
    at, end = 0, len(stream)
    while at + 12 <= end:
        size, kind, clock = struct.unpack_from("<IIf", stream, at)
        if at + 12 + size > end:
            break
        rows.append((at + 12, size, kind, clock))
        at += 12 + size
    return np.array(rows, dtype=[("at", "<i8"), ("size", "<u4"), ("type", "<u4"), ("time", "<f4")])


#: The engine's position update: entity, space, position (3 floats), its error (3), yaw, pitch, roll, a flag.
POSITION = struct.Struct("<II3f3f3fB")


@dataclass
class Track:
    """One entity's positions over time, sorted by time."""

    time: np.ndarray
    x: np.ndarray
    y: np.ndarray
    z: np.ndarray
    #: Heading in radians, 0 facing +z (north), growing towards +x (east).
    yaw: np.ndarray

    def at(self, t: float) -> int | None:
        """The index of the last sample at or before `t`, or None before the first."""
        i = int(np.searchsorted(self.time, t, side="right")) - 1
        return i if i >= 0 else None


def _plausible(x: float, y: float, z: float) -> bool:
    return (
        bool(np.isfinite(x) and np.isfinite(y) and np.isfinite(z))
        and abs(x) < 20000
        and abs(z) < 20000
        and -2000 < y < 5000
    )


def find_position_type(stream: bytes, idx: np.ndarray | None = None) -> int | None:
    """
    The packet type that carries position updates, found by its shape: 45
    bytes of payload, plausible coordinates (metres, within 20 km of the
    origin), and the most of them. Both games have used 0x0A for it in every
    version read so far; finding it by shape keeps a renumbering patch from
    silently emptying the table.
    """
    idx = index(stream) if idx is None else idx
    best, best_count = None, 0
    for kind in np.unique(idx["type"][idx["size"] == POSITION.size]):
        rows = idx[(idx["type"] == kind) & (idx["size"] == POSITION.size)]
        if len(rows) < 20:
            continue
        sample = rows[:: max(1, len(rows) // 200)]
        ok = sum(_plausible(*POSITION.unpack_from(stream, int(r["at"]))[2:5]) for r in sample)
        if ok >= 0.95 * len(sample) and len(rows) > best_count:
            best, best_count = int(kind), len(rows)
    return best


def _track(rows: list[tuple[float, float, float, float, float]]) -> Track:
    a = np.array(rows, dtype=np.float64).reshape(-1, 5)
    a = a[np.argsort(a[:, 0], kind="stable")]
    return Track(a[:, 0], a[:, 1], a[:, 2], a[:, 3], a[:, 4])


def tracks(stream: bytes, kind: int, idx: np.ndarray | None = None) -> dict[int, Track]:
    """
    Every entity's position updates from packets of type `kind`. An all-zero
    position (an entity not placed in the world) is skipped.
    """
    idx = index(stream) if idx is None else idx
    rows: dict[int, list] = {}
    for r in idx[(idx["type"] == kind) & (idx["size"] == POSITION.size)]:
        v = POSITION.unpack_from(stream, int(r["at"]))
        x, y, z = v[2:5]
        if not _plausible(x, y, z) or (x == 0 and y == 0 and z == 0):
            continue
        rows.setdefault(v[0], []).append((float(r["time"]), x, y, z, v[8]))
    return {e: _track(r) for e, r in rows.items()}


#: The recording player's own position, which the client writes itself rather than receives: two entity
#: ids (the one moved, and the one it is attached to, or 0), the position, and yaw, pitch, roll.
PLAYER_POSITION = struct.Struct("<II3f3f")


def own_track(stream: bytes, entity: int, idx: np.ndarray | None = None) -> tuple[int | None, Track | None]:
    """
    The positions the client recorded for its own `entity`: from the 32-byte
    packet type in which `entity` moves on its own (second id 0) most often.
    Returns the packet type found, and the track.
    """
    idx = index(stream) if idx is None else idx
    best: tuple[int | None, list] = (None, [])
    for kind in np.unique(idx["type"][idx["size"] == PLAYER_POSITION.size]):
        rows = []
        for r in idx[(idx["type"] == kind) & (idx["size"] == PLAYER_POSITION.size)]:
            v = PLAYER_POSITION.unpack_from(stream, int(r["at"]))
            if v[0] == entity and v[1] == 0 and _plausible(*v[2:5]) and v[2:5] != (0.0, 0.0, 0.0):
                rows.append((float(r["time"]), v[2], v[3], v[4], v[5]))
        if len(rows) > len(best[1]):
            best = (int(kind), rows)
    return (best[0], _track(best[1])) if best[1] else (None, None)


@dataclass
class Call:
    """
    A method called on an entity, or a property set on one (the two look the
    same): its packet type, the entity, which method or property (a number
    patches change), and its arguments or value.
    """

    type: int
    time: float
    entity: int
    method: int
    args: bytes


def call_types(stream: bytes, idx: np.ndarray | None = None) -> list[int]:
    """
    The packet types shaped like entity calls - entity id, method or property
    id, the length of the arguments, then exactly that many bytes - most
    packets first. Method calls (8) and property updates (7) in every version
    read so far.
    """
    idx = index(stream) if idx is None else idx
    found = []
    for kind in np.unique(idx["type"]):
        rows = idx[(idx["type"] == kind) & (idx["size"] >= 12)]
        if not len(rows):
            continue
        sample = rows[:: max(1, len(rows) // 300)]
        ok = sum(struct.unpack_from("<I", stream, int(r["at"]) + 8)[0] == int(r["size"]) - 12 for r in sample)
        if ok >= 0.98 * len(sample):
            found.append((len(rows), int(kind)))
    return [k for _, k in sorted(found, reverse=True)]


def calls(stream: bytes, kinds: list[int], idx: np.ndarray | None = None) -> list[Call]:
    """Every call in packets of the types `kinds`, in stream order."""
    idx = index(stream) if idx is None else idx
    out = []
    for r in idx[np.isin(idx["type"], kinds)]:
        at, size = int(r["at"]), int(r["size"])
        if size < 12:
            continue
        entity, method, n = struct.unpack_from("<III", stream, at)
        if n != size - 12:
            continue
        out.append(Call(int(r["type"]), float(r["time"]), entity, method, stream[at + 12 : at + size]))
    return out


def battle_start(tracks: dict[int, Track], threshold: float = 1.0) -> float | None:
    """
    When the battle began, on the replay's clock: the first moment any of
    `tracks` is more than `threshold` metres from where it was first seen.
    Nothing moves during the countdown, in either game.
    """
    first = []
    for t in tracks.values():
        if len(t.time) < 2:
            continue
        d = np.hypot(t.x - t.x[0], t.z - t.z[0])
        moved = np.nonzero(d > threshold)[0]
        if len(moved):
            first.append(float(t.time[moved[0]]))
    return min(first) if first else None


def rate(tracks: dict[int, Track]) -> float | None:
    """The typical sampling rate in Hz: the median gap between one entity's samples, over all of them."""
    parts = [np.diff(t.time) for t in tracks.values() if len(t.time) > 2]
    gaps = np.concatenate(parts) if parts else np.array([])
    gaps = gaps[gaps > 0]
    return round(float(1.0 / np.median(gaps)), 2) if len(gaps) else None


# --------------------------------------------------------------- building files


def encipher(blocks: list[Any], stream: bytes, key: bytes) -> bytes:
    """
    A replay file from blocks and a packet stream - the reverse of
    `read_replay`, for building test files. One block at a time, so meant for
    small streams.
    """
    out = bytearray(struct.pack("<II", MAGIC, len(blocks)))
    for b in blocks:
        raw = json.dumps(b).encode("utf-8")
        out += struct.pack("<I", len(raw)) + raw
    packed = zlib.compress(stream)
    packed += bytes(-len(packed) % 8)
    out += struct.pack("<II", len(stream), len(packed))
    bf = Blowfish(key)
    prev = 0
    for i in range(0, len(packed), 8):
        (word,) = struct.unpack_from("<Q", packed, i)
        out += bf.encrypt_block(struct.pack("<Q", word ^ prev))
        prev = word
    return bytes(out)


def packet(kind: int, time: float, payload: bytes) -> bytes:
    """One packet of a stream, for building test files."""
    return struct.pack("<IIf", len(payload), kind, time) + payload
