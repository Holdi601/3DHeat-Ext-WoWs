import struct

import numpy as np

from heat3d_ext_wows import armour, gamefiles, shippack


def _geometry(key: int, tris: np.ndarray) -> bytes:
    """A geometry file with no render data and one armour model of one piece."""
    head = struct.pack("<6I", 0, 0, 0, 0, 0, 1) + struct.pack("<6Q", 0, 0, 0, 0, 0, 72)
    verts = b"".join(struct.pack("<3f4B", *p, 127, 0, 127, 0) for p in tris.reshape(-1, 3))
    piece = struct.pack("<I6fI", key, 0, 0, 0, 1, 1, 1, len(tris) * 3) + verts
    model = struct.pack("<4Q", 0, 0, 0, 0) + struct.pack("<I6f", 1, 0, 0, 0, 1, 1, 1) + struct.pack("<I", 1) + piece
    return head + model


def test_armour_pieces_and_frame():
    tris = np.array([[[0, 0, 0], [1, 0, 0], [0, 1, 2]]], float)
    (key, got), = armour.armour_pieces(_geometry(65573, tris))
    assert key == 65573 and np.allclose(got, tris)
    # z (towards the bow) is forward, x (starboard) is right.
    assert np.allclose(armour.to_figure(got, 15)[0, 2], [30, 15, 0])


def test_catalog_ships_and_shells():
    gp = {
        "PJSB010_Nagato_1944": {"typeinfo": {"type": "Ship", "species": "Battleship", "nation": "Japan"},
                                "index": "PJSB010", "id": 42, "level": 7, "group": "upgradeable",
                                "A_Hull": {"model": "x.model", "size": (225.0, 34.6, 39.0), "health": 49000.0}},
        "PJPA005_AP": {"typeinfo": {"type": "Projectile", "species": "Artillery", "nation": "Japan"},
                       "index": "PJPA005", "ammoType": "AP", "bulletDiametr": 0.41, "alphaDamage": 12500.0},
    }
    c = shippack.build_catalog(gp, {"IDS_PJSB010": "Nagato"})
    ship, shell = c["items"]
    assert (ship["name"], ship["class"], ship["numbers"]["tier"], ship["numbers"]["length"]) == ("Nagato", "battleship", 7, 225.0)
    assert ship["aliases"] == ["PJSB010", "PJSB010-Nagato-1944", "42"]
    assert (shell["kind"], shell["group"], shell["numbers"]["calibre"]) == ("weapon", "AP", 410)


def test_messages(tmp_path):
    build = tmp_path / "bin" / "1"
    (build / "idx").mkdir(parents=True)
    texts = build / "res" / "texts" / "en" / "LC_MESSAGES"
    texts.mkdir(parents=True)
    k, v = b"IDS_PJSB010", "Nagato \u00e9".encode()
    ko, vo = 28, 36
    data = struct.pack("<7I", 0x950412DE, 0, 1, ko, vo, 0, 0) + struct.pack("<2I", len(k), 44) \
        + struct.pack("<2I", len(v), 44 + len(k)) + k + v
    (texts / "global.mo").write_bytes(data)

    class Pk:
        pass

    pk = Pk()
    pk.build = build
    assert gamefiles.messages(pk) == {"IDS_PJSB010": "Nagato \u00e9"}
