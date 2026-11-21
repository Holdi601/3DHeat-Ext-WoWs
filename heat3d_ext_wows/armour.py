"""
A ship's armour model from its `.geometry` file (the one named like the ship, beside the `_Bow`, `_MidFront`,
`_MidBack` and `_Stern` sections).

The geometry file starts with six counts (vertex blocks, index blocks, vertex mappings, index mappings, collision
models, armour models) and six 64-bit offsets to those tables. An armour model's record is 32 bytes; its data
follows it: a 32-bit word, the model's box (six floats), the number of pieces, then each piece: its key (32 bits:
layer << 16 | material), its box, its vertex count and the vertices (position as three floats and four bytes),
three to a triangle. The key is what `armor` in the ship's hull parameters gives a thickness in millimetres for.
"""

from __future__ import annotations

import struct

import numpy as np

_VERTEX = np.dtype([("p", "<f4", 3), ("n", "u1", 4)])


def armour_pieces(data: bytes) -> list[tuple[int, np.ndarray]]:
    """Every armour piece as (key, triangles n x 3 x 3), in model units (x across, y up, z along)."""
    counts = struct.unpack_from("<6I", data, 0)
    offsets = struct.unpack_from("<6Q", data, 24)
    if counts[5] == 0 or offsets[5] == 0:
        return []
    out: list[tuple[int, np.ndarray]] = []
    o = offsets[5]
    for _ in range(counts[5]):
        p = o + 32 + 4 + 24
        (n_pieces,) = struct.unpack_from("<I", data, p)
        p += 4
        for _ in range(n_pieces):
            key = struct.unpack_from("<I", data, p)[0]
            (count,) = struct.unpack_from("<I", data, p + 28)
            p += 32
            v = np.frombuffer(data, _VERTEX, count, p)["p"].astype(np.float64)
            p += count * _VERTEX.itemsize
            out.append((key, v[: count - count % 3].reshape(-1, 3, 3)))
        o = p
    return out


def to_figure(tri: np.ndarray, scale: float) -> np.ndarray:
    """Model units (x to starboard, y up, z towards the bow; left-handed) -> the figure frame (x forward, y up, z right), metres."""
    return np.stack([tri[..., 2], tri[..., 1], tri[..., 0]], axis=-1) * scale
