"""
What a World of Warships replay says about its battle, without converting it.

Reads only the JSON blocks at the head of the file (see `bigworld`): the map,
the battle type, the client version, the local time the recording began and
the roster. The enciphered packet stream after them is never deciphered, so
what only the stream holds - the battle's length, who won (newer clients keep
the results in the stream, see `kept.results`) - is None here.

Everything is what the file holds; what it does not say is None or [].
"""

from __future__ import annotations

import struct
from datetime import datetime
from pathlib import Path
from typing import Any

from . import bigworld as bw
from .replay import ship_class

#: The roster's `relation`: 0 the recording player, 1 an ally, 2 an enemy - as the converter's `team` column has it.
TEAMS = {0: "ally", 1: "ally", 2: "enemy"}


def _head(path: Path) -> list[Any]:
    """The JSON blocks, read without the stream: the counts first, then each block's length and bytes."""
    with path.open("rb") as fh:
        start = fh.read(8)
        if len(start) < 8 or struct.unpack("<I", start[:4])[0] != bw.MAGIC:
            raise ValueError("not a World of Warships replay")
        (count,) = struct.unpack("<I", start[4:])
        if not 0 < count < 16:
            raise ValueError(f"not a World of Warships replay ({count} blocks)")
        buf = bytearray(start)
        for _ in range(count):
            size = fh.read(4)
            if len(size) < 4:
                raise ValueError("not a World of Warships replay (cut off in its header)")
            body = fh.read(struct.unpack("<I", size)[0])
            buf += size + body
    blocks, _ = bw.read_blocks(bytes(buf))
    return blocks


def _date(text: Any) -> str | None:
    """`dateTime`, `dd.mm.yyyy HH:MM:SS` in the recording computer's local time (no zone): naive ISO 8601."""
    try:
        return datetime.strptime(str(text), "%d.%m.%Y %H:%M:%S").isoformat()
    except ValueError:
        return None


def info(path: Path, ship_names: dict[str, str] | None = None) -> dict:
    """
    The battle's map, mode, start, players, teams and client version, from the header. `ship_names` maps a roster
    `shipId` to a name, as the converter's `--ship-names`; the recording player's own ship is named by the header.
    """
    path = Path(path)
    try:
        blocks = _head(path)
    except OSError as e:
        raise ValueError(f"not a readable World of Warships replay: {e}") from None
    head = blocks[0] if blocks and isinstance(blocks[0], dict) else {}
    if not head or not ("mapName" in head or "vehicles" in head):
        raise ValueError("not a World of Warships replay (no battle in its header)")
    ship_names = ship_names or {}
    me = str(head.get("playerName") or "")
    players = []
    for v in head.get("vehicles") or []:
        if not isinstance(v, dict):
            continue
        name = str(v.get("name") or "")
        own = bool(me) and name == me
        ship_id = str(v.get("shipId") or "")
        ship = str(head.get("playerVehicle") or ship_id) if own else ship_names.get(ship_id, ship_id)
        row: dict[str, Any] = {"name": name, "team": TEAMS.get(v.get("relation")), "ship": ship or None,
                               "ship_id": ship_id or None, "type": ship_class(ship) if ship else None, "own": own}
        if v.get("id") is not None:
            row["account_id"] = v["id"]
        players.append(row)
    teams = [{"id": t} for t in ("ally", "enemy") if any(p["team"] == t for p in players)]
    limit = head.get("duration")
    return {
        "map": str(head["mapName"]) if head.get("mapName") else None,
        "map_title": str(head["mapDisplayName"]) if head.get("mapDisplayName") else None,
        "mode": str(head["gameType"]) if head.get("gameType") else None,
        "scenario": str(head["scenario"]) if head.get("scenario") else None,
        "date": _date(head.get("dateTime")) if head.get("dateTime") else None,
        "duration_s": None,  # the header has the time limit only (`time_limit_s`); the length is in the stream
        "time_limit_s": float(limit) if isinstance(limit, (int, float)) and not isinstance(limit, bool) else None,
        "players": players,
        "teams": teams,
        "outcome": None,
        "game_version": str(head.get("clientVersionFromExe") or "").replace(",", ".") or None,
        "recording_player": me or None,
    }
