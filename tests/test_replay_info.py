"""The header-only battle summary on replays built here: no real replay, no real names."""

from __future__ import annotations

import pytest

from heat3d_ext_wows import bigworld as bw
from heat3d_ext_wows.replay import KEY
from heat3d_ext_wows.replay_info import info

HEADER = {
    "mapName": "spaces/99_testmap",
    "mapDisplayName": "99_testmap",
    "clientVersionFromExe": "15,10,0,13533378",
    "playerName": "tester_a",
    "playerVehicle": "PASB018-Testship",
    "dateTime": "07.11.2026 12:34:56",
    "gameType": "RandomBattle",
    "scenario": "Domination",
    "duration": 1200,
    "vehicles": [
        {"shipId": 4001, "relation": 0, "id": 9001, "name": "tester_a"},
        {"shipId": 4002, "relation": 1, "id": 9002, "name": "tester_b"},
        {"shipId": 4003, "relation": 2, "id": 9003, "name": "tester_c"},
    ],
}


def _replay(tmp_path, blocks=None):
    f = tmp_path / "test.wowsreplay"
    stream = bw.packet(0, 0.0, b"") + bw.packet(1, 1.0, b"\x00" * 8)
    f.write_bytes(bw.encipher(blocks or [HEADER], stream, KEY))
    return f


def test_the_header(tmp_path):
    d = info(_replay(tmp_path), ship_names={"4003": "PJSD000-Testfoe"})
    assert d["map"] == "spaces/99_testmap" and d["map_title"] == "99_testmap"
    assert d["mode"] == "RandomBattle" and d["scenario"] == "Domination"
    assert d["date"] == "2026-11-07T12:34:56"
    assert d["duration_s"] is None and d["time_limit_s"] == 1200.0
    assert d["game_version"] == "15.10.0.13533378"
    assert d["teams"] == [{"id": "ally"}, {"id": "enemy"}]
    assert d["outcome"] is None
    me, friend, foe = d["players"]
    assert me == {"name": "tester_a", "team": "ally", "ship": "PASB018-Testship", "ship_id": "4001",
                  "type": "battleship", "own": True, "account_id": 9001}
    assert friend["team"] == "ally" and friend["ship"] == "4002" and not friend["own"]
    assert foe["team"] == "enemy" and foe["ship"] == "PJSD000-Testfoe" and foe["type"] == "destroyer"


def test_newer_clients_extra_blocks_are_fine(tmp_path):
    d = info(_replay(tmp_path, [HEADER, {}, "9001.2630531823886288"]))
    assert d["map"] == "spaces/99_testmap" and len(d["players"]) == 3


def test_not_a_replay(tmp_path):
    f = tmp_path / "junk.wowsreplay"
    f.write_bytes(b"not a replay" * 200)
    with pytest.raises(ValueError):
        info(f)
    with pytest.raises(ValueError):
        info(_replay(tmp_path, [{"something": "else"}]))
