"""
The World of Warships reader on replays built here, to the layout real ones
have: no real replay is kept in the repository.
"""

from __future__ import annotations

import json
import math
import pickle
import struct

import pyarrow.parquet as pq
import pytest

from heat3d_ext_wows import bigworld as bw
from heat3d_ext_wows.cli import main
from heat3d_ext_wows.replay import KEY, read, ship_class, unpickle

AVATAR, OWN, ALLY, ENEMY = 500, 501, 502, 503
ARENA = 2630531823886288

HEADER = {
    "mapName": "spaces/99_Test",
    "mapDisplayName": "99_Test",
    "clientVersionFromExe": "15,10,0,13533378",
    "playerName": "me",
    "playerVehicle": "PASB018-Iowa-1944",
    "dateTime": "07.11.2026 12:00:00",
    "gameType": "RandomBattle",
    "duration": 1200,
    "vehicles": [
        {"shipId": 4001, "relation": 0, "id": 9001, "name": "me"},
        {"shipId": 4002, "relation": 1, "id": 9002, "name": "friend"},
        {"shipId": 4003, "relation": 2, "id": 9003, "name": "foe"},
    ],
}


class _Camouflage:
    """Stands for a game class a real record names; the reader must not need it."""

    def __init__(self, scheme: int) -> None:
        self.scheme = scheme


def records(name_key: int = 26, entity_key: int = 35) -> bytes:
    def rec(account: int, name: str, entity: int, ship: int) -> list:
        return [(0, account), (3, _Camouflage(1)), (12, account), (name_key, name), (entity_key, entity),
                (36, ship), (38, 1)]

    data = [rec(1, "me", OWN, 4001), rec(2, "friend", ALLY, 4002), rec(3, "foe", ENEMY, 4003)]
    return pickle.dumps(data, protocol=2)


def states_call(method: int = 154, **kw) -> bytes:
    # The arena id, a team build byte, a blob, then the player records.
    args = struct.pack("<qB", ARENA, 0) + b"\x05\x80\x02]q\x00." + records(**kw) + b"\x00" * 16
    return struct.pack("<III", AVATAR, method, len(args)) + args


def position(entity: int, x: float, z: float, yaw: float) -> bytes:
    return bw.POSITION.pack(entity, 1, x, 0.0, z, 0, 0, 0, yaw, 0, 0, 0)


def own(x: float, z: float, yaw: float) -> bytes:
    return bw.PLAYER_POSITION.pack(OWN, 0, x, 0.0, z, yaw, 0, 0)


def stream(death_method: int = 83, own_type: int = 44, **kw) -> bytes:
    out = bytearray(bw.packet(8, 0.0, states_call(**kw)))
    for i in range(301):
        t = i / 7
        go = max(0.0, t - 30.0)
        out += bw.packet(10, t, position(ALLY, -100.0, 2.0 * go, 0.0))
        if t <= 40.0:
            out += bw.packet(10, t, position(ENEMY, 300.0 - go, 300.0, -math.pi / 2))
        out += bw.packet(own_type, t, own(2.4 * go, -200.0, math.pi / 2))
        # The avatar riding the ship: not a position of its own.
        out += bw.packet(own_type, t, bw.PLAYER_POSITION.pack(AVATAR, OWN, 1, 0, 1, 0, 0, 0))
        out += bw.packet(7, t, struct.pack("<III", ALLY, 4, 1) + b"\x01")
        if i == 280:
            out += bw.packet(8, t, struct.pack("<III", AVATAR, death_method, 12) + struct.pack("<III", ENEMY, OWN, 17))
    return bytes(out)


def replay(**kw) -> bytes:
    return bw.encipher([HEADER], stream(**kw), KEY)


def test_blowfish_matches_the_published_test_vector():
    assert bw.Blowfish(bytes(8)).encrypt_block(bytes(8)).hex() == "4ef997456198dd78"


def test_a_pickle_cannot_run_code(tmp_path):
    # A pickle that would call os.system to leave a file behind, as a crafted replay could.
    marker = tmp_path / "ran"
    command = f'echo x > "{marker.as_posix()}"'.encode()
    for module in (b"os", b"nt", b"posix", b"subprocess"):
        payload = b"c" + module + b"\nsystem\n(S'" + command + b"'\ntR."
        assert type(unpickle(payload)).__name__ == "_Placeholder"
    assert not marker.exists()


def test_ship_class_from_the_index_name():
    assert ship_class("PASB018-Iowa-1944") == "battleship"
    assert ship_class("PJSD012-Shimakaze") == "destroyer"
    assert ship_class("4001") == "ship"


def test_every_ship_is_named_and_tracked():
    m = read(replay())
    s = m.summary
    assert s["match"] == str(ARENA) and s["map"] == "spaces/99_Test" and s["clientVersion"] == "15.10.0.13533378"
    players = {p["name"]: p for p in s["players"]}
    assert players["me"]["entity"] == OWN and players["foe"]["entity"] == ENEMY
    assert players["me"]["samples"] == 301 and s["ownPositionPacket"] == 44
    assert s["hz"] == pytest.approx(7.0, rel=0.01) and s["ownHz"] == pytest.approx(7.0, rel=0.01)
    i = m.rows["player"].index("me")
    assert m.rows["own"][i] == 1 and m.rows["vehicle"][i] == "PASB018-Iowa-1944" and m.rows["type"][i] == "battleship"
    j = m.rows["player"].index("foe")
    assert m.rows["team"][j] == "enemy" and m.rows["vehicle"][j] == "4003" and m.rows["type"][j] == "ship"
    assert m.rows["team"][m.rows["player"].index("friend")] == "ally"
    assert AVATAR not in m.rows["entity"]


def test_ship_names_can_be_given():
    m = read(replay(), ship_names={"4003": "PGSC108-Hipper"})
    assert m.rows["vehicle"][m.rows["player"].index("foe")] == "PGSC108-Hipper"


def test_battle_start_and_heading():
    m = read(replay())
    assert m.summary["battleStart"] == pytest.approx(30.0, abs=0.5)
    i = m.rows["player"].index("me")
    assert m.rows["dirX"][i] == pytest.approx(1.0, abs=1e-6)


def test_a_ship_sunk_is_placed_and_its_killer_named():
    m = read(replay())
    (kill,) = m.summary["kills"]
    assert kill["victim"] == "foe" and kill["killer"] == "me" and kill["reason"] == 17
    # The foe was last seen at 40 s, the sinking at 40 s: placed there.
    assert kill["time"] == pytest.approx(40.0, abs=0.01) and kill["x"] == pytest.approx(290.0, abs=0.5)
    d, k = m.rows["event"].index("death"), m.rows["event"].index("kill")
    assert m.rows["player"][d] == "foe" and m.rows["player"][k] == "me"
    assert {p["name"]: p["survived"] for p in m.summary["players"]} == {"me": True, "friend": True, "foe": False}


def test_patch_renumbering_is_followed():
    m = read(replay(death_method=91, own_type=43, name_key=24, entity_key=32))
    assert m.summary["deathMethod"] == [8, 91] and m.summary["ownPositionPacket"] == 43
    assert len(m.summary["kills"]) == 1 and {p["entity"] for p in m.summary["players"]} == {OWN, ALLY, ENEMY}


def test_the_command_writes_the_table_and_summary(tmp_path):
    (tmp_path / "a.wowsreplay").write_bytes(replay())
    out = tmp_path / "out"
    assert main([str(tmp_path), "-o", str(out)]) == 0
    t = pq.read_table(out / "99_Test" / f"{ARENA}.parquet")
    hints = json.loads(t.schema.metadata[b"heat3d"])
    assert hints["kind"] == "wows-replay" and hints["entity"]["size"] == 12
    doc = json.loads((out / "99_Test" / f"{ARENA}.match.json").read_text(encoding="utf-8"))
    assert doc["format"] == "heat3d-wows-match" and doc["player"] == "me"


def test_ship_names_file(tmp_path):
    (tmp_path / "a.wowsreplay").write_bytes(replay())
    names = tmp_path / "names.json"
    names.write_text(json.dumps({"4003": "PGSC108-Hipper"}), encoding="utf-8")
    assert main([str(tmp_path / "a.wowsreplay"), "-o", str(tmp_path / "out"), "--ship-names", str(names)]) == 0
    t = pq.read_table(tmp_path / "out" / "99_Test" / f"{ARENA}.parquet")
    assert "PGSC108-Hipper" in t.column("vehicle").to_pylist()
