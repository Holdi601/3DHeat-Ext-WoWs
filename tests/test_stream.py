"""
Damage, health, shells, torpedoes, where shells ended, chat and pickled
statistics, on a replay built here. The method numbers are made up: the reader
must find them by shape.
"""

from __future__ import annotations

import math
import pickle
import struct

import pytest

from heat3d_ext_wows import bigworld as bw
from heat3d_ext_wows import stream as st
from heat3d_ext_wows.replay import KEY, read
from test_wows import ALLY, AVATAR, ENEMY, HEADER, OWN, own, position, states_call

DAMAGE, HEALTH, SHELLS, TORPS, ENDED, CHAT, STATS = 61, 33, 120, 121, 125, 140, 160


def call(kind: int, t: float, entity: int, method: int, args: bytes) -> bytes:
    return bw.packet(kind, t, struct.pack("<III", entity, method, len(args)) + args)


def bw_str(b: bytes) -> bytes:
    return bytes([len(b)]) + b


def stream() -> bytes:
    out = bytearray(bw.packet(8, 0.0, states_call()))
    health = 50000.0
    for i in range(301):
        t = round(i / 7, 3)
        go = max(0.0, t - 30.0)
        me_x = 2.4 * go
        out += bw.packet(10, t, position(ALLY, -100.0, 2.0 * go, 0.0))
        out += bw.packet(10, t, position(ENEMY, 300.0 - go, 300.0, -math.pi / 2))
        out += bw.packet(44, t, own(me_x, -200.0, math.pi / 2))
        if i in (220, 230, 240):
            # A salvo of two shells from my guns towards the enemy, and where they ended.
            shell = struct.pack("<3f3f", me_x, 0.0, -200.0, 0.0, 5.0, 40.0) + bytes(24)
            out += call(8, t, AVATAR, SHELLS, b"\x01" + struct.pack("<III", 77, OWN, i) + b"\x02" + shell + shell)
            ended = struct.pack("<3fHB", 300.0 - go, 1.0, 300.0, i, 0)
            out += call(8, t + 0.5, AVATAR, ENDED, b"\x01" + struct.pack("<I", OWN) + bytes([99, 1]) + ended)
            health -= 3000.0
            out += call(7, t + 0.2, ENEMY, HEALTH, struct.pack("<f", health))
            out += call(8, t + 0.6, ENEMY, DAMAGE, b"\x01" + struct.pack("<if", OWN, 3000.0))
            out += call(8, t + 0.7, AVATAR, STATS, bw_str(pickle.dumps({(1, 0): [i - 219, 3000.0 * (i - 219) / 10]},
                                                                     protocol=2)))
        if i in (250, 255, 260):
            torp = struct.pack("<3f3f", 300.0, -0.14, 300.0, -1.0, 0.0, 0.0) + bytes(5)
            out += call(8, t, AVATAR, TORPS, b"\x01" + struct.pack("<IIII", 88, ENEMY, 1, 5) + b"\x01" + torp)
        if i == 100:
            out += call(8, t, AVATAR, CHAT, struct.pack("<i", 9002) + bw_str(b"battle_team") + bw_str(b"go B")
                        + bw_str(b""))
    return bytes(out)


def replay() -> bytes:
    return bw.encipher([HEADER], stream(), KEY)


def rows(m, event):
    return [{c: v[i] for c, v in m.rows.items()} for i, e in enumerate(m.rows["event"]) if e == event]


def test_the_calls_are_found_by_their_shape():
    rep = bw.read_replay(replay(), KEY)
    dec = st.decode(rep.stream, bw.index(rep.stream), {OWN, ALLY, ENEMY}, AVATAR)
    assert dec.found["damage"] == DAMAGE and dec.found["health"] == HEALTH
    assert dec.found["shell"] == {"method": SHELLS, "size": 48} and dec.found["torpedo"] == {"method": TORPS, "size": 29}
    assert dec.found["ended"]["method"] == ENDED and dec.found["chat"] == CHAT and STATS in dec.found["pickles"]


def test_damage_is_hurt_and_damage_rows_with_health():
    m = read(replay())
    hurt = rows(m, "hurt")
    assert [r["value"] for r in hurt] == [3000.0] * 3 and all(r["player"] == "foe" and r["other"] == "me" for r in hurt)
    assert [r["health"] for r in hurt] == [47000.0, 44000.0, 41000.0]
    assert all(r["player"] == "me" for r in rows(m, "damage"))
    me = [p for p in m.summary["players"] if p["name"] == "me"][0]
    assert me["seen"]["damageDealt"] == 9000.0 and me["seen"]["shells"] == 6


def test_shells_torpedoes_and_where_they_ended():
    m = read(replay())
    shots = rows(m, "shot")
    assert len(shots) == 6 and all(r["player"] == "me" and r["params"] == 77 for r in shots)
    assert shots[0]["dirZ"] == pytest.approx(40 / math.hypot(5, 40)) and shots[0]["value"] == pytest.approx(math.hypot(5, 40))
    torps = rows(m, "torpedo")
    assert len(torps) == 3 and all(r["player"] == "foe" and r["dirX"] == pytest.approx(-1.0) for r in torps)
    impacts = rows(m, "impact")
    assert len(impacts) == 3 and all(r["player"] == "me" and r["reason"] == "99" for r in impacts)


def test_chat_and_the_damage_statistics():
    m = read(replay())
    (chat,) = rows(m, "chat")
    assert chat["player"] == "friend" and chat["text"] == "go B" and chat["reason"] == "battle_team"
    assert m.summary["damageStats"] == [{"weapon": 1, "kind": 0, "count": 21, "amount": 6300.0}]
