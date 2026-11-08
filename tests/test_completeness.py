"""
The rule every 3DHeat converter follows (docs/converters.md of 3DHeat): all
the replay holds is decoded, or kept whole in the sidecar
`<match>.messages.parquet`, and the match document counts what became of
each kind of item - nothing lost. On replays built here, to the 15.x layout:
three blocks (the header, an empty one, the account and battle ids as text)
and the results in the stream.
"""

from __future__ import annotations

import json
import math
import struct

import pyarrow.parquet as pq

from heat3d_ext_wows import bigworld as bw
from heat3d_ext_wows.cli import main
from heat3d_ext_wows.replay import KEY, read
from test_stream import DAMAGE, call
from test_stream import stream as full_stream
from test_wows import ALLY, ARENA, AVATAR, ENEMY, HEADER, OWN

UNKNOWN_PACKET, UNKNOWN_METHOD = 77, 99
AVATAR_TYPE, SHIP = 1, 2
ACCOUNT = 9001
RESULTS = {"arenaUniqueID": ARENA, "accountDBID": ACCOUNT, "playersPublicInfo": {"9001": [9001, "me"],
                                                                                 "9003": [9003, "foe"]}}


def stream() -> bytes:
    out = bytearray()
    out += bw.packet(0, 0.0, struct.pack("<IH", AVATAR, AVATAR_TYPE) + b"\x00base")
    for e in (OWN, ALLY, ENEMY):
        out += bw.packet(5, 0.0, struct.pack("<IH", e, SHIP) + b"\x00" * 30)
    out += bw.packet(22, 0.0, struct.pack("<I", 9) + b"15,10,0,0")
    out += full_stream()
    out += bw.packet(UNKNOWN_PACKET, 40.0, b"\x00 not read yet \xff")
    out += call(8, 40.0, ALLY, UNKNOWN_METHOD, b"\x01\x02\x03")
    # A ship heeling in a turn, the enemy leaving the client's view, and the results at the end.
    out += bw.packet(10, 43.0, bw.POSITION.pack(ALLY, 0, -100.0, 0.0, 30.0, 0, 0, 0, 0.3, 0.0, -0.04, 1))
    out += bw.packet(4, 43.0, struct.pack("<I", ENEMY))
    raw = json.dumps(RESULTS).encode()
    out += bw.packet(34, 44.0, struct.pack("<I", len(raw)) + raw)
    return bytes(out)


def replay() -> bytes:
    """Three blocks as 15.x writes them; the stream after them as `bigworld.encipher` builds it."""
    whole = bw.encipher([HEADER], stream(), KEY)
    _, at = bw.read_blocks(whole)
    head = json.dumps(HEADER).encode()
    ids = f"{ACCOUNT}.{ARENA}".encode()
    blocks = struct.pack("<I", len(head)) + head + struct.pack("<I", 0) + struct.pack("<I", len(ids)) + ids
    return struct.pack("<II", bw.MAGIC, 3) + blocks + whole[at:]


def completeness(m):
    return m.summary["selfCheck"]["completeness"]


def test_nothing_is_lost():
    m = read(replay())
    c = completeness(m)
    assert c["lost"] == 0 and all(t["lost"] == 0 for t in c["types"].values())
    assert c["sidecars"] == [f"{ARENA}.messages.parquet"]
    rep = bw.read_replay(replay(), KEY)
    packets = len(bw.index(rep.stream))
    assert c["seen"] == packets + 3 + sum(1 for b in (rep.sizes, rep.leftover, rep.unused) if b)
    assert c["seen"] == c["decoded"] + c["partial"] + c["raw"]
    assert m.messages.num_rows == c["seen"] - c["decoded"]


def test_what_nobody_reads_yet_is_kept_whole():
    m = read(replay())
    rows = m.messages.to_pylist()
    (unknown,) = [r for r in rows if r["type"] == f"packet {UNKNOWN_PACKET}"]
    assert unknown["payload"] == b"\x00 not read yet \xff"
    (method,) = [r for r in rows if r["type"] == f"method {SHIP}.{UNKNOWN_METHOD}"]
    assert method["entity"] == ALLY and method["payload"].endswith(b"\x01\x02\x03")
    # The empty block and the ids block, whole: as JSON the ids block is a number that loses digits.
    blocks = {r["type"]: r["text"] for r in rows if r["type"].startswith("block")}
    assert blocks["block 1"] == "" and blocks["block 2"] == f"{ACCOUNT}.{ARENA}"


def test_what_is_read_in_part_carries_what_was_read():
    m = read(replay())
    rows = m.messages.to_pylist()
    damage = [json.loads(r["decoded"]) for r in rows if r["type"] == f"method {SHIP}.{DAMAGE}"]
    assert damage and damage[0] == {"hits": [[OWN, 3000.0]]}
    types = completeness(m)["types"]
    assert types[f"method {SHIP}.{DAMAGE}"]["name"] == "damage" and types[f"method {SHIP}.{DAMAGE}"]["raw"] == 0


def test_the_results_the_ids_and_the_version():
    m = read(replay())
    assert m.summary["results"] == RESULTS and m.summary["blockIds"] == {"account": ACCOUNT, "arenaUniqueID": ARENA}
    check = m.summary["selfCheck"]
    assert check["results"] == {"arenaUniqueID": True, "playersInRoster": 2, "players": 2}
    assert check["blockIds"] == {"arenaUniqueID": True, "account": True} and check["streamVersionAgrees"] is True
    types = completeness(m)["types"]
    assert types["packet 34"]["decoded"] == 1 and types["packet 22"]["decoded"] == 1


def test_entities_come_and_go():
    m = read(replay())
    ents = {e["entity"]: e for e in m.summary["entities"]}
    assert ents[AVATAR]["role"] == "avatar" and ents[ENEMY]["role"] == "ship" and ents[ENEMY]["left"] == [43.0]
    assert m.summary["selfCheck"]["entities"]["positionsWhileGone"] == 0


def test_roll_is_in_the_table():
    m = read(replay())
    i = max(k for k, (e, p) in enumerate(zip(m.rows["event"], m.rows["player"])) if e == "position" and p == "friend")
    assert m.rows["pitch"][i] == 0.0 and math.isclose(m.rows["roll"][i], -0.04, rel_tol=1e-6)


def test_the_command_writes_the_sidecar(tmp_path):
    (tmp_path / "a.wowsreplay").write_bytes(replay())
    out = tmp_path / "out"
    assert main([str(tmp_path), "-o", str(out)]) == 0
    side = pq.read_table(out / "99_Test" / f"{ARENA}.messages.parquet")
    doc = json.loads((out / "99_Test" / f"{ARENA}.match.json").read_text(encoding="utf-8"))
    assert doc["selfCheck"]["completeness"]["lost"] == 0
    assert side.num_rows == doc["selfCheck"]["completeness"]["seen"] - doc["selfCheck"]["completeness"]["decoded"]
