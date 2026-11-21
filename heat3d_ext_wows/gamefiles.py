"""
World of Warships' own files, read from your install: the package index, the packed files, the game's parameter
table and the English names. Read-only; nothing in the install is changed.

- `bin/<build>/idx/*.idx` (magic `ISFP`): a tree of names (nodes: name length, name offset, id, parent id; 32
  bytes each), then a record per file (node id, package id, offset, compression type and flags, packed size,
  CRC-32, size; 48 bytes), then the packages (name length, name offset, id). Offsets count from byte 16.
- `res_packages/*.pkg`: the files one after another, raw deflate where the flags say so.
- `content/GameParams.data`: zlib over the bytes reversed, then a pickled table of every ship, gun, shell and
  module. Read here with an unpickler that builds plain dicts, so no code from the file is run.
- `bin/<build>/res/texts/en/LC_MESSAGES/global.mo`: gettext's message catalogue (`IDS_<index>` = a ship's name).
"""

from __future__ import annotations

import io
import pickle
import struct
import zlib
from dataclasses import dataclass
from pathlib import Path

FOLDER_NAMES = ("World_of_Warships", "World of Warships", "World_of_Warships_EU", "World_of_Warships_NA",
                "World_of_Warships_ASIA")


@dataclass
class PackedFile:
    package: str
    offset: int
    flags: int
    packed: int
    size: int


def _candidates() -> list[Path]:
    """Where installs usually are: every Steam library (Windows, Linux incl. flatpak and Steam Deck, macOS),
    the Wargaming launcher's `<drive>:/Games` on Windows, and `~/Games` (also inside Wine/Lutris prefixes)."""
    import sys

    from .app import paths

    out = [d for name in FOLDER_NAMES for d in paths.steam_game_dirs(name)]
    if sys.platform == "win32":
        out += [Path(f"{drive}:/Games") / name for drive in "CDEFGH" for name in FOLDER_NAMES]
    else:
        games = Path.home() / "Games"
        out += [games / name for name in FOLDER_NAMES]
        try:
            prefixes = [p for p in games.iterdir() if (p / "drive_c").is_dir()] if games.is_dir() else []
        except OSError:
            prefixes = []
        out += [p / "drive_c" / "Games" / name for p in prefixes for name in FOLDER_NAMES]
    return out


def builds(game: Path) -> list[Path]:
    """The install's build folders that hold a package index, newest first."""
    b = game / "bin"
    found = [p for p in b.iterdir() if p.is_dir() and p.name.isdigit() and (p / "idx").is_dir()] if b.is_dir() else []
    return sorted(found, key=lambda p: int(p.name), reverse=True)


def find_install(given: str | None = None) -> Path:
    """The game's folder (the one holding `bin` and `res_packages`): `given`, else the usual places (`_candidates`)."""
    if given:
        g = Path(given)
        if builds(g):
            return g
        raise FileNotFoundError(f"{given} is not a World of Warships folder (no bin/<build>/idx under it)")
    candidates = _candidates()
    for c in candidates:
        if c.is_dir() and builds(c):
            return c
    raise FileNotFoundError("World of Warships not found (Steam libraries, the launcher's Games folders); "
                            "name its folder with --game")


class Packages:
    """Every file the install's package index lists, by path."""

    def __init__(self, game: Path):
        self.game = game
        self.build = builds(game)[0]
        self.files: dict[str, PackedFile] = {}
        for idx in sorted((self.build / "idx").glob("*.idx")):
            self._read_idx(idx)

    def _read_idx(self, path: Path) -> None:
        b = path.read_bytes()
        if b[:4] != b"ISFP":
            return
        nodes, files, packages = struct.unpack_from("<3I", b, 16)
        header, data, footer = struct.unpack_from("<3Q", b, 32)
        names: dict[int, tuple[str, int]] = {}
        o = 16 + header
        for _ in range(nodes):
            length, at, nid, parent = struct.unpack_from("<4Q", b, o)
            names[nid] = (b[o + at:o + at + length].split(b"\0")[0].decode("utf-8", "replace"), parent)
            o += 32
        vols: dict[int, str] = {}
        o = 16 + footer
        for _ in range(packages):
            length, at, vid = struct.unpack_from("<3Q", b, o)
            vols[vid] = b[o + at:o + at + length].split(b"\0")[0].decode()
            o += 24
        cache: dict[int, str] = {}

        def full(nid: int) -> str:
            if nid in cache:
                return cache[nid]
            name, parent = names.get(nid, ("", 0))
            out = f"{full(parent)}/{name}" if parent in names else name
            cache[nid] = out
            return out

        o = 16 + data
        for _ in range(files):
            nid, vid, offset, _kind, flags, packed, _crc, size = struct.unpack_from("<QQQIIIIQ", b, o)
            self.files[full(nid)] = PackedFile(vols.get(vid, ""), offset, flags, packed, size)
            o += 48

    def read(self, path: str) -> bytes:
        f = self.files[path]
        with (self.game / "res_packages" / f.package).open("rb") as fh:
            fh.seek(f.offset)
            raw = fh.read(f.packed)
        return zlib.decompress(raw, -15) if f.flags else raw


class _Obj(dict):
    def __setstate__(self, state):
        self.update(state if isinstance(state, dict) else {"_state": state})


class _Unpickler(pickle.Unpickler):
    """Only plain containers: every class in the file becomes a dict, `copy_reg` rebuilds it empty."""

    def find_class(self, module, name):
        if module in ("copy_reg", "copyreg") and name == "_reconstructor":
            return lambda cls, base, state: cls()
        if module in ("__builtin__", "builtins") and name in ("set", "frozenset", "list", "dict", "tuple", "object"):
            import builtins

            return getattr(builtins, name)
        return _Obj


def game_params(pk: Packages) -> dict:
    """The parameter table: every entry by its name (`PJSB010_Nagato_1944`, ...)."""
    data = pk.read("content/GameParams.data")
    table = _Unpickler(io.BytesIO(zlib.decompress(data[::-1])), encoding="latin1").load()
    return table.get("", table) if isinstance(table, dict) else table[0]


def messages(pk: Packages, lang: str = "en") -> dict[str, str]:
    """The game's English texts (a gettext .mo file), id -> text."""
    path = pk.build / "res" / "texts" / lang / "LC_MESSAGES" / "global.mo"
    if not path.is_file():
        return {}
    b = path.read_bytes()
    magic = struct.unpack_from("<I", b)[0]
    e = "<" if magic == 0x950412DE else ">"
    _, n, ko, vo = struct.unpack_from(e + "4I", b, 4)
    out = {}
    for i in range(n):
        kl, ka = struct.unpack_from(e + "2I", b, ko + 8 * i)
        vl, va = struct.unpack_from(e + "2I", b, vo + 8 * i)
        out[b[ka:ka + kl].decode("utf-8", "replace")] = b[va:va + vl].decode("utf-8", "replace")
    return out
