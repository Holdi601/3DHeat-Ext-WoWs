---
title: The match document
nav_order: 6
---

# The match document

`<match>.match.json` holds everything the replay says that is not a row of
the table. The viewer's Match tab reads it. (The code calls it the summary.)

![The start of a synthetic match document, and its keys](assets/img/match-document.svg)

## The battle

| Key | What |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; the battle's id; the map as the game names it (`spaces/<map>`) and its display name |
| `clientVersion`, `streamVersion` | the game version from the header, and as the packet stream says it |
| `recorded` | when the replay was recorded, as the game writes it |
| `player`, `vehicle` | the recording player and their ship |
| `gameType`, `scenario` | the battle's type (`RandomBattle`, ...) and scenario, from the header |
| `duration` | the battle's time limit in seconds, from the header |
| `truncated` | the recording stopped early |
| `battleStart`, `recordingSeconds` | the battle's start (the first moment any ship moves) and the recording's length, in seconds |
| `positionPacket`, `ownPositionPacket` | the packet numbers the positions came in: other ships', the recording player's |
| `deathMethod` | the method number the sinkings were found in |
| `hz`, `ownHz`, `positions` | samples a second of other ships and of the own ship; position rows |
| `units` | world units (15 m by the hulls, 30 m by the game's ranges); x east, y up, z north |
| `events` | the number of table rows of each event |
| `decoded` | the method and packet numbers found for each kind of message |

## Players and events

| Key | What |
|---|---|
| `players` | one entry a ship: name, `ally` or `enemy`, ship number and name, entity, samples, kills, survived; `seen` (damage dealt and received, shells, torpedoes and last health the client saw); `header` (the roster's entry) and `record` (the player's record from the stream, by key number) |
| `kills` | every sinking: time, victim, killer, cause number, place |
| `chat` | every chat line, with channel and sender |
| `damageStats` | the recording player's own statistics as the game keeps them: per weapon and kind, a count and an amount (kind 0 is damage dealt) |
| `avatarPickles` | every pickled call to the recording player, decoded, by method number |

## Header, results and checks

| Key | What |
|---|---|
| `header` | the first JSON block, all of it but the roster: game mode, weather, map border, team sizes and more |
| `moreBlocks` | the JSON blocks after the first, as they are |
| `blockIds` | 15.x: the recording player's account and the battle's id, read as text |
| `results` | 15.x: the results, which these clients keep in the stream |
| `entities` | every entity the stream creates: its type number and role, when it came into the client's view and when it left |
| `selfCheck` | the completeness count ([Completeness](completeness.md)) and the checks of the entities, the results, the ids and the version |

---

Part of [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
