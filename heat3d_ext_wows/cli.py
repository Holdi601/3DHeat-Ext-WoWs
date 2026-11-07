"""
heat3d-wows-replay <replays or folders> -o <out>

Each World of Warships replay into `<out>/<map>/<match>.parquet` and
`<match>.match.json`. A match already written is skipped unless `--force`.
Exit status: 0 when every replay was converted (or skipped), 1 when any
failed, 2 when no replay was found.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import __version__
from .replay import COLUMNS, HINTS, read_file
from .table import paths, write

SUFFIX = ".wowsreplay"


def find(inputs: list[str]) -> list[Path]:
    out: list[Path] = []
    for i in inputs:
        p = Path(i)
        if p.is_dir():
            out += sorted(q for q in p.rglob(f"*{SUFFIX}") if q.is_file())
        elif p.is_file():
            out.append(p)
    return out


def main(argv: list[str] | None = None) -> int:
    # A newer release is offered, and installed only if the user says yes (notified only when nobody can be asked).
    try:
        import heat3d_update

        heat3d_update.startup("heat3d_ext_wows")
    except Exception:  # an update check never stops a conversion
        pass
    ap = argparse.ArgumentParser(prog="heat3d-wows-replay", description="World of Warships replays into 3DHeat tables")
    ap.add_argument("replays", nargs="+", help=f"{SUFFIX} files, or folders searched for them")
    ap.add_argument("-o", "--out", required=True, help="folder to write into (a folder per map inside)")
    ap.add_argument("--force", action="store_true", help="convert again what is already written")
    ap.add_argument("--ship-names", metavar="JSON", help="a JSON object of shipId -> ship name; replays carry only "
                    "the number for every ship but the recording player's")
    ap.add_argument("--version", action="version", version=__version__)
    args = ap.parse_args(argv)
    files = find(args.replays)
    if not files:
        print(f"no {SUFFIX} files in {', '.join(args.replays)}", file=sys.stderr)
        return 2
    names = json.loads(Path(args.ship_names).read_text(encoding="utf-8")) if args.ship_names else None
    failed = 0
    for f in files:
        try:
            m = read_file(f, ship_names={str(k): str(v) for k, v in (names or {}).items()})
            data, _doc = paths(args.out, m.map, m.name)
            if data.exists() and not args.force:
                print(f"{f.name}: already written, {data}")
                continue
            data, _doc = write(args.out, m.map, m.name, m.rows, COLUMNS, HINTS, m.summary)
            s = m.summary
            print(f"{f.name}: {s['positions']} positions of {len(s['players'])} ships at {s['hz']} Hz (own {s['ownHz']} Hz), "
                  f"{len(s['kills'])} sunk, {s['map']} ({s['clientVersion']}) -> {data}")
        except Exception as e:  # noqa: BLE001 - one bad replay does not stop the next
            failed += 1
            print(f"{f.name}: not converted: {e}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
