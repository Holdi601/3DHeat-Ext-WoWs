"""The standalone spec on a synthetic install (tiny fake files, no game data)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from heat3d_ext_wows import standalone_spec
from heat3d_ext_wows.app import entry, paths, update
from heat3d_ext_wows.app import spec as app_spec


@pytest.fixture(autouse=True)
def _isolated(tmp_path, monkeypatch):
    monkeypatch.setenv("LOCALAPPDATA", str(tmp_path / "appdata"))
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path / "appdata"))
    monkeypatch.setenv("HEAT3D_LEVELS", str(tmp_path / "levels"))
    monkeypatch.setenv("HEAT3D_NO_UPDATE", "1")
    update.AUTO_THIS_RUN = False


def install(root: Path) -> Path:
    game = root / "steamapps" / "common" / "World of Warships"
    (game / "bin" / "8000" / "idx").mkdir(parents=True)
    (game / "bin" / "9000" / "idx").mkdir(parents=True)
    (game / "replays").mkdir()
    (game / "replays" / "20260101_000000_ship_map.wowsreplay").write_bytes(b"x")
    return game


def test_find_in_steam_and_given(tmp_path, monkeypatch):
    steam = tmp_path / "Steam"
    game = install(steam)
    monkeypatch.setattr(paths, "steam_roots", lambda: [steam])
    g = standalone_spec.SPEC.games[0]
    assert g.find(None) == game
    assert g.find(str(game)) == game
    assert g.find(str(tmp_path / "nothing")) is None
    assert g.build(game) == "9000"


def test_tasks(tmp_path, monkeypatch):
    game = install(tmp_path / "elsewhere")
    app_spec.save_settings("heat3d-wows", {"games": {"wows": str(game)}})
    levels = tmp_path / "levels"
    replays, catalog, models = standalone_spec.SPEC.tasks
    src, out = replays.inputs
    assert src.default(levels) == str(game / "replays")
    assert out.default(levels) == str(paths.data_dir() / "matches" / "wows")
    assert replays.argv({"src": "r", "out": "o"}, levels) == ["heat3d-wows-replay", "r", "-o", "o"]
    assert catalog.argv({"out": "c.json"}, levels) == ["heat3d-wows-replay", "catalog", "-o", "c.json", "--game", str(game)]
    assert models.argv({"out": "m"}, levels)[:4] == ["heat3d-wows-replay", "models", "-o", "m"]
    for t in standalone_spec.SPEC.tasks:
        assert t.argv({i.key: "x" for i in t.inputs}, levels)[0] in standalone_spec.SPEC.tools


def test_no_maps_nothing_to_extract(tmp_path, capsys):
    game = install(tmp_path / "elsewhere")
    app_spec.save_settings("heat3d-wows", {"games": {"wows": str(game)}})
    assert entry.main(standalone_spec.SPEC, ["status", "--json"]) == 0
    g = json.loads(capsys.readouterr().out)["games"][0]
    assert g["found"] and g["build"] == "9000" and g["maps"] == []
    assert entry.main(standalone_spec.SPEC, ["extract", "--new", "--progress-json"]) == 0
    assert json.loads(capsys.readouterr().out.splitlines()[-1]) == {"event": "done", "ok": 0, "failed": 0}
