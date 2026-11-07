# World of Warships replays

World of Warships replays (`.wowsreplay`) into heatmap tables and match
summaries for the 3DHeat viewer - or anything that reads Parquet and JSON.
Every ship's position over time, and every ship sunk where it happened.

This converter is kept outside the 3DHeat Watcher on purpose: the replays are
enciphered, and Wargaming's terms (below) are broad. If the converter ever has
to go, nothing else goes with it. The Watcher runs it as a command when it is
installed, and works without it.

```bash
pip install -e .                                   # installs the heat3d-wows-replay command
heat3d-wows-replay <replays or folders> -o out     # or: python -m heat3d_ext_wows ...
heat3d-wows-replay ... --ship-names names.json     # optional: {"<shipId>": "<name>", ...}
```

Per replay, into a folder per map (`out/54_Faroe/...`):

- `<match>.parquet` - every ship's position while the recording client saw it,
  and each sinking twice: where the ship sank, and where its killer was.
- `<match>.match.json` - the map, the client version, who recorded it, every
  player's line (ally or enemy, ship, kills, whether they survived) and every
  sinking with its time, place and cause.

`<match>` is the battle's own id, or the file's name when none is found. A
match already written is skipped unless `--force`. Exit status 0 when every
replay was converted, 1 when any failed (the rest are still converted), 2 when
none was found.

Replays are where the game saves them when replay recording is on
(`isReplayEnabled` in the game's `preferences.xml`, or the game's own setting
where it has one): `<World of Warships>/replays/`.

## The table

| Column | What |
|---|---|
| `match`, `map` | the battle's id; the map (`spaces/54_Faroe`) |
| `time` | seconds since the recording began (the countdown is in it) |
| `battleTime` | seconds since the battle began; negative during the countdown |
| `event` | `position`, `death` (where the ship sank), `kill` (where its killer was) |
| `player`, `team`, `own` | the player's name; `ally` or `enemy` of the recording player; `1` on the recording player's rows |
| `vehicle`, `type` | the recording player's ship by name (`PASB018-Iowa-1944`), the others by the game's ship number (`4253956080`) unless `--ship-names` names them; `battleship`, `cruiser`, `destroyer`, `aircraft carrier`, `submarine` where the name says, else `ship` |
| `x`, `y`, `z` | the game's world units: x east, y up (sea level 0), z north |
| `dirX`, `dirY`, `dirZ` | where the bow points, a unit vector in the same frame (`dirY` 0: heading only) |
| `other`, `reason` | for a sinking the killer, for a kill the victim; the game's cause number (not named) |
| `entity` | the ship's id in the replay |

**Units.** A world unit is not a metre. A battleship at speed covers about 2.4
of them a second, and a map is about 1,200 across. Placed against the ships'
hull geometry, a unit is 15 m; the game's own range figures make it 30 m
(landaire/wows-toolkit, `crates/wows-core/src/units.rs`, MIT, which leaves the
two unreconciled). The table keeps world units at scale 1, as every 3DHeat
source keeps its game's own units, so a level exported in the same units lines
up. The footer's `heat3d` hints: Y up, Z flipped (so the map is not mirrored),
a ship 12 units long, `player` as the person, `team` as the group, `match` as
the session.

## What it reads, and how

A replay is a header of JSON blocks and the game's packet stream (format notes
in [`heat3d_ext_wows/bigworld.py`](heat3d_ext_wows/bigworld.py)):

- The first block, in the clear: the map, the client version, the recording
  player and ship, and the roster - each player's name, ally or enemy, and
  ship number. Newer clients add two more blocks, which are not read. There
  are no results.
- The packet stream, zlib-compressed and Blowfish-enciphered with a key the
  game carries, which the community tools that read these files have
  published. Deciphered, it holds:
  - the engine's position updates of every ship the client could see (its
    own team throughout, enemies while spotted or near), several times a
    second while they move and less often while they do not;
  - the recording player's own ship in a packet of its own, about seven times
    a second;
  - once, at the start, the players' records as a pickled Python list. These
    say which entity in the stream is which player. Their keys are numbered,
    and the numbers change with patches, so the reader finds the keys by
    their values: the key holding the roster's names, and the key holding
    entities that have position updates;
  - the server's call telling the client a ship has sunk: victim, killer,
    cause. It is found by its shape (twelve bytes; the first two are ship
    entities; each victim appears once), not by its number.

Packet and method numbers that differ between the versions checked (the own
ship's packet is 43 or 44, the sinking call 76 or 83) are all found this way,
so a renumbering patch does not empty the table.

**The pickle is untrusted data.** A replay is a file from anywhere, and a
pickle can name code to run. It is loaded with an unpickler that hands every
class or function the pickle names an inert placeholder, so it builds plain
data and nothing else. A test feeds it a pickle that calls `os.system`.

**Sinkings** have the call's exact time. Their place is where the victim was
last seen, when that was within five seconds. **The battle's start** is the
first moment any ship moves at all (ships lie still in the countdown).

**Not read:** shells, torpedoes, aircraft and their squadrons, damage, fires,
floods, spotting, capture points, ribbons, chat, results. The ship number is
not turned into a name: the names are in the game's own parameter files, not
in the replay.

## Verified

On public replays, at 2026-11-07:

| Client | Map | Ships | Positions | Others' rate | Own ship | Sunk (placed) |
|---|---|---|---|---|---|---|
| 0.9.6 (July 2020) | Shoreside | 24 of 24 | 41,036 | 5.7 Hz | 7.0 Hz | 20 (19) |
| 0.10.11 | naval_mission | 14 of 14 | 47,212 | 6.8 Hz | 7.0 Hz | 9 (9) |
| 15.9 (2026) | Seychelles | 24 of 24 | 20,345 | 6.0 Hz | 7.0 Hz | 14 (13) |
| 15.10 (November 2026) | Faroe | 12 of 12 | 19,419 | 7.0 Hz | 7.0 Hz | 10 (10) |

Rates are the median gap between one ship's updates; a ship lying still is
updated less often. Checks: every ship's entity was matched to a roster name
on all four; headings agree with the direction of travel to 0.01-0.07 rad;
after its sinking call, every one of the 53 victims moves no more than 0.1
units (a ship under way covers about 2 a second). The battle's start came out
at 30.6-31.9 s on three of the replays; on the 0.9.6 one at 12.5 s, possibly a
recording that began late in the countdown (not checked). The tests build
replays to the same layout, so no real replay is kept in this repository.

**Not checked:** clients before 0.9.6, the Lesta client (Mir Korabley),
operations and scenarios beyond the one above, clan and ranked battles, and
which ship number is which ship.

## Wargaming's terms

Read on 2026-11-07, Wargaming EULA version 14 (effective 10 April 2024, listed
as current); its section 12.3 points to a World of Warships mod policy, whose
page did not render outside a browser and was not read:

- 5.3 (b): unless authorised in writing, you must not "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): prohibited is "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

What this converter does: it reads a file the game wrote, after the battle,
outside the game. It changes nothing in the game, talks to no server, and
shows nothing during a battle. It does decipher the stream with the game's
key, which 5.3 (b) and 12.1 (p) can be read to cover. Using it is the user's
decision; that is why it is a separate package.

## Licence and sources

MIT ([`LICENSE`](LICENSE)). Needs numpy (BSD-3-Clause) and pyarrow
(Apache-2.0). Written for this project: the Blowfish cipher here is its own,
with its tables computed from the digits of pi as the cipher defines them.
Facts about the format are common knowledge among replay tools; the unit scale
note is from landaire/wows-toolkit (MIT). No code was taken from any project,
and none from Monstrofil/replays_unpack, which has no licence.

`bigworld.py` and `table.py` are the same files as in the World of Tanks
converter (`../wot-replay`); change both together.
