"""
heat3d-wows-replay <replays or folders> -o <out>
heat3d-wows-replay catalog [-o catalog.json] [--game <folder>]
heat3d-wows-replay models [-o <folder>] [--game <folder>] [--only <name> ...]

Each World of Warships replay into `<out>/<map>/<match>.parquet`,
`<match>.match.json` and the sidecar `<match>.messages.parquet` (everything
the two do not hold whole; see docs/converters.md of 3DHeat). A match already written is skipped unless `--force`.
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
from .sidecar import WHAT
from .table import paths, write, write_sidecar

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


def _levels(*parts: str) -> Path:
    """Under HEAT3D_LEVELS when it is set, else the current folder."""
    import os

    home = os.environ.get("HEAT3D_LEVELS")
    return Path(home, *parts) if home else Path(parts[-1])


def _install_verb(argv: list[str]) -> int:
    """`catalog` and `models`: the ship catalogue and the local model pack, from the installed game."""
    from . import gamefiles, shippack

    verb = argv[0]
    ap = argparse.ArgumentParser(prog=f"heat3d-wows-replay {verb}", description=(
        "every ship, shell and torpedo with names and numbers (catalog.json)" if verb == "catalog" else
        "each ship's armour model as a local model pack for the viewer (model-pack.json + one .glb each)"))
    ap.add_argument("-o", "--out", help="where to write (default under $HEAT3D_LEVELS, else the current folder)")
    ap.add_argument("--game", help="the World of Warships folder (default: found in the Steam libraries and X:/Games)")
    if verb == "models":
        ap.add_argument("--only", nargs="+", help="just the ships whose parameter name contains these")
    args = ap.parse_args(argv[1:])
    try:
        game = gamefiles.find_install(args.game)
    except FileNotFoundError as e:
        print(f"heat3d-wows-replay: {e}", file=sys.stderr)
        return 2
    source = f"heat3d-wows-replay {__version__}"
    if verb == "catalog":
        out = Path(args.out) if args.out else _levels("wows", "catalog.json")
        c = shippack.write_catalog(game, out, source=source)
        ships = sum(1 for i in c["items"] if i["kind"] == "vehicle")
        print(f"{out}: {ships} ships, {len(c['items']) - ships} shells, torpedoes and bombs (build {c['gameBuild']})")
        return 0
    out = Path(args.out) if args.out else _levels("model-packs", "wows")
    out.mkdir(parents=True, exist_ok=True)
    r = shippack.write_pack(game, out, source=source, only=args.only, say=lambda t: print(t, file=sys.stderr))
    size = sum(f.stat().st_size for f in out.glob("*.glb"))
    print(f"{out}: {len(r['units'])} ships, {size / 1e6:.0f} MB; {len(r['missing'])} without an armour model in this install")
    return 0 if r["units"] else 1


def _catalog_names() -> dict[str, str] | None:
    """shipId -> name from the ship catalogue (`catalog`), when one is under HEAT3D_LEVELS."""
    path = _levels("wows", "catalog.json")
    if not path.is_file():
        return None
    try:
        items = json.loads(path.read_text(encoding="utf-8")).get("items", [])
    except (OSError, ValueError):
        return None
    return {i["aliases"][-1]: i["id"].replace("_", "-") for i in items
            if i.get("kind") == "vehicle" and i.get("aliases") and i["aliases"][-1]}


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv and argv[0] in ("catalog", "models"):
        return _install_verb(argv)
    # A newer release is offered, and installed only if the user says yes (notified only when nobody can be asked).
    try:
        from . import update

        update.startup("heat3d_ext_wows")
    except Exception:  # an update check never stops a conversion
        pass
    ap = argparse.ArgumentParser(prog="heat3d-wows-replay", description="World of Warships replays into 3DHeat tables")
    ap.add_argument("replays", nargs="+", help=f"{SUFFIX} files, or folders searched for them")
    ap.add_argument("-o", "--out", required=True, help="folder to write into (a folder per map inside)")
    ap.add_argument("--force", action="store_true", help="convert again what is already written")
    ap.add_argument("--ship-names", metavar="JSON", help="a JSON object of shipId -> ship name; replays carry only "
                    "the number for every ship but the recording player's (default: the ship catalogue, `catalog`, "
                    "when it is under HEAT3D_LEVELS)")
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = ap.parse_args(argv)
    files = find(args.replays)
    if not files:
        print(f"no {SUFFIX} files in {', '.join(args.replays)}", file=sys.stderr)
        return 2
    names = json.loads(Path(args.ship_names).read_text(encoding="utf-8")) if args.ship_names else _catalog_names()
    failed = 0
    for f in files:
        try:
            m = read_file(f, ship_names={str(k): str(v) for k, v in (names or {}).items()})
            data, _doc = paths(args.out, m.map, m.name)
            if data.exists() and not args.force:
                print(f"{f.name}: already written, {data}")
                continue
            data, _doc = write(args.out, m.map, m.name, m.rows, COLUMNS, HINTS, m.summary)
            if m.messages is not None:
                write_sidecar(args.out, m.map, m.name, WHAT, m.messages)
            s = m.summary
            print(f"{f.name}: {s['positions']} positions of {len(s['players'])} ships at {s['hz']} Hz (own {s['ownHz']} Hz), "
                  f"{len(s['kills'])} sunk, {s['map']} ({s['clientVersion']}) -> {data}")
        except Exception as e:  # noqa: BLE001 - one bad replay does not stop the next
            failed += 1
            print(f"{f.name}: not converted: {e}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
