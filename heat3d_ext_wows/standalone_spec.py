"""
The standalone app's description of this tool (app/spec.py): the World of
Warships install (Steam on any system, the launcher's Games folders, or the
folder you choose), its `replays` folder, and the conversions as tasks:
replays into matches, the ship catalogue and the local model pack from the
install. A replay reader has no maps. `python -m heat3d_ext_wows.standalone_spec`
runs the app from a checkout; the release executables run the same.
"""

from __future__ import annotations

from pathlib import Path

from . import __version__
from .app import paths
from .app.spec import GameSpec, Input, Replays, Spec, Task, game_folders


def _find(given: str | None) -> Path | None:
    from .gamefiles import find_install

    try:
        return find_install(given)
    except (FileNotFoundError, OSError):
        return None


def _build(game: Path) -> str | None:
    from .gamefiles import builds

    found = builds(game)
    return found[0].name if found else None


def _game() -> Path | None:
    return game_folders(SPEC).get("wows")


def _replays(levels: Path) -> str:
    game = _game()
    return str(game / "replays") if game and (game / "replays").is_dir() else ""


def _with_game(argv: list[str]) -> list[str]:
    game = _game()
    return argv + (["--game", str(game)] if game else [])

def _replay_info(path: Path) -> dict:
    """`info <replay> --json`: the header only (replay_info.py)."""
    from .replay_info import info

    return info(path)


SPEC = Spec(
    id="heat3d-wows",
    name="3DHeat WoWs",
    repo="Holdi601/3DHeat-Ext-WoWs",
    version=__version__,
    tools={"heat3d-wows-replay": "heat3d_ext_wows.cli:main"},
    default_tool="heat3d-wows-replay",
    description="World of Warships replays into matches for the 3DHeat viewer",
    module="heat3d_ext_wows.standalone_spec",
    games=[GameSpec(key="wows", label="World of Warships", find=_find, subdir="wows", build=_build,
                    platforms=("windows-x64", "linux-x64", "macos-arm64"))],
    tasks=[
        Task("replays", "Convert replays",
             [Input("src", "Folder with .wowsreplay replays", "folder", default=_replays),
              Input("out", "Where the matches go", "folder",
                    default=lambda levels: str(paths.data_dir() / "matches" / "wows"))],
             lambda v, levels: ["heat3d-wows-replay", v["src"], "-o", v["out"]],
             help="each battle becomes a table and match document the viewer opens"),
        Task("catalog", "Ship catalogue from the install",
             [Input("out", "Catalogue file", "text", default=lambda levels: str(levels / "wows" / "catalog.json"))],
             lambda v, levels: _with_game(["heat3d-wows-replay", "catalog", "-o", v["out"]]),
             help="every ship, shell and torpedo with names and numbers, from your install"),
        Task("models", "Ship models from the install",
             [Input("out", "Model pack folder", "folder",
                    default=lambda levels: str(levels / "model-packs" / "wows"))],
             lambda v, levels: _with_game(["heat3d-wows-replay", "models", "-o", v["out"]]),
             help="each ship's armour model as a local model pack; it stays on your machine"),
    ],
    min_free_gb=2.0,
    replays=Replays("wows", (".wowsreplay",), lambda r, out: ["heat3d-wows-replay", str(r), "-o", str(out)], info=_replay_info),
    notice="Not affiliated with or endorsed by Wargaming.",
)

if __name__ == "__main__":
    from . import update
    from .app.entry import main

    raise SystemExit(main(SPEC, apply_source=update.apply))
