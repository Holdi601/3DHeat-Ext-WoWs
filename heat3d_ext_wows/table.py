"""
What a match is written as, the same contract as 3DHeat CS2's: a Parquet
table with the viewer's reading instructions in its footer (key `heat3d`), and
a JSON summary beside it, in a folder per map:

    <out>/<map>/<match>.parquet
    <out>/<map>/<match>.match.json

This file is the same in the World of Tanks and the World of Warships
converters; change both together.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import numpy as np
import pyarrow as pa
import pyarrow.parquet as pq

#: Column kinds: d float64, f float32, i int8, l int64, s text (dictionary-encoded).
_TYPES = {"d": pa.float64(), "f": pa.float32(), "i": pa.int8(), "l": pa.int64()}


def slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "-", str(text)).strip("-")[:80] or "match"


def table(rows: dict[str, list], kinds: dict[str, str], hints: dict[str, Any]) -> pa.Table:
    arrays, fields = [], []
    for name, kind in kinds.items():
        values = rows.get(name, [])
        if kind == "s":
            arr = pa.array(["" if v is None else str(v) for v in values], type=pa.string()).dictionary_encode()
            fields.append(pa.field(name, pa.dictionary(pa.int32(), pa.string())))
        else:
            num = np.array([np.nan if v is None else float(v) for v in values], dtype=np.float64)
            mask = ~np.isfinite(num)
            if kind in ("i", "l"):
                ints = np.where(mask, 0, num).astype(np.int64)
                arr = pa.array(ints, type=_TYPES[kind], mask=mask)
            else:
                arr = pa.array(num.astype(np.float32 if kind == "f" else np.float64), type=_TYPES[kind], mask=mask)
            fields.append(pa.field(name, _TYPES[kind]))
        arrays.append(arr)
    schema = pa.schema(fields, metadata={"heat3d": json.dumps(hints)})
    return pa.Table.from_arrays(arrays, schema=schema)


def paths(out: str | Path, map_id: str, match: str) -> tuple[Path, Path]:
    folder = Path(out) / slug(map_id.split("/")[-1])
    return folder / f"{slug(match)}.parquet", folder / f"{slug(match)}.match.json"


def write(out: str | Path, map_id: str, match: str, rows: dict[str, list], kinds: dict[str, str],
          hints: dict[str, Any], summary: dict[str, Any]) -> tuple[Path, Path]:
    data, doc = paths(out, map_id, match)
    data.parent.mkdir(parents=True, exist_ok=True)
    pq.write_table(table(rows, kinds, hints), data, compression="snappy", row_group_size=256_000)
    doc.write_text(json.dumps(summary, indent=1, ensure_ascii=False), encoding="utf-8")
    return data, doc
