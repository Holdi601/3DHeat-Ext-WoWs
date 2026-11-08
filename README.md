# World of Warships replays

World of Warships replays (`.wowsreplay`) into heatmap tables and match
summaries for the 3DHeat viewer - or anything that reads Parquet and JSON.
Every ship's position over time; every ship sunk, every hit and its damage,
every shell and torpedo fired and where shells ended, where it happened; ship
health, chat, and the recording player's own damage statistics.

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
  and the events below, each where it happened.
- `<match>.match.json` - the map, the client version, who recorded it, every
  player's line (ally or enemy, ship, kills, whether they survived, what the
  client saw of them, their whole player record), every sinking with its
  time, place and cause, the chat, and everything else the file holds.
- `<match>.messages.parquet` - the sidecar: every item of the replay the two
  files above do not hold whole, kept whole (see [Completeness](#completeness)).

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
| `event` | what the row is (below) |
| `player`, `team`, `own` | the player's name; `ally` or `enemy` of the recording player; `1` on the recording player's rows |
| `vehicle`, `type` | the recording player's ship by name (`PASB018-Iowa-1944`), the others by the game's ship number (`4253956080`) unless `--ship-names` names them; `battleship`, `cruiser`, `destroyer`, `aircraft carrier`, `submarine` where the name says, else `ship` |
| `x`, `y`, `z` | the game's world units: x east, y up (sea level 0), z north |
| `dirX`, `dirY`, `dirZ` | where the bow points, a unit vector in the same frame (`dirY` 0: heading only); on a shell or torpedo the way it went |
| `other`, `reason` | the other ship of an event (killer, victim, attacker); the game's cause number for a sinking (not named), the hit type for an impact, the channel for chat |
| `value`, `health` | the event's number (damage, a shell's or torpedo's speed in world units a second); the ship's health after a hit |
| `text` | a chat line |
| `shot`, `params` | a salvo's id; the shell's or torpedo's type, as the game's parameter number |
| `entity` | the ship's id in the replay |
| `pitch`, `roll` | on a position, the ship's pitch and roll (radians) as the game sends them: a ship heels in a turn |

| `event` | On the row of | What |
|---|---|---|
| `position` | every ship | while the client saw it |
| `death`, `kill` | the victim, the killer | each sinking twice: where the ship sank, and where its killer was |
| `hurt`, `damage` | the victim, the attacker | a hit: `value` the damage, `health` what is left |
| `shot` | the shooter | one row per shell, at the gun, in the direction it flew |
| `torpedo` | the shooter | one row per torpedo, where it was launched, in the direction it ran |
| `impact` | the shooter | where a shell ended (hit, miss into the water, ...); `reason` the hit type number; on a ship (any type but 0 water, 8, 32, 64 land, within 6 units of a ship) `other`/`otherVehicle`/`otherType` the ship and `hitLocalX/Y/Z` the point in its frame (m at 15 m a unit: x forward, y up from the sea, z right) |
| `chat` | the sender | `text` the line, `reason` the channel (`battle_team`, `battle_common`) |

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
  ship number. Newer clients (15.x) add two more blocks: an empty one, and
  the recording player's account and the battle's id as text, read into
  `blockIds`. The results are not in the JSON; 15.x keeps them in the stream.
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
    entities; each victim appears once), not by its number;
  - each ship's damage: an array of (attacker, damage) per hit, on the ship
    hit; and its health, a property set a moment before;
  - every salvo of shells and of torpedoes the client was told of: the shell
    type, the shooter, the salvo, and each shell's or torpedo's start and
    velocity;
  - where shells ended: the shooter, a hit type, and the place of each (on
    15.x clients with more about the shell where it struck, which is skipped);
  - the chat: sender, channel, line;
  - pickled calls to the recording player: its damage statistics, updates of
    the players' records, the battle's state;
  - on 15.x clients, the battle's results at the end: a packet of its own, a
    JSON object with the battle's id, read whole into the summary's
    `results` (the game's own lists, unnamed: `commonList`,
    `privateDataList`, `playersPublicInfo` per account, ...).

Packet and method numbers that differ between the versions checked (the own
ship's packet is 43 or 44, the sinking call 76 or 83, the shells 101, 102,
126 or 127) are all found by shape - see
[`heat3d_ext_wows/stream.py`](heat3d_ext_wows/stream.py) - so a renumbering
patch does not empty the table. The numbers found are in the summary's
`decoded`.

**The pickle is untrusted data.** A replay is a file from anywhere, and a
pickle can name code to run. It is loaded with an unpickler that hands every
class or function the pickle names an inert placeholder, so it builds plain
data and nothing else. A test feeds it a pickle that calls `os.system`.

**Sinkings** have the call's exact time. Their place is where the victim was
last seen, when that was within five seconds. **The battle's start** is the
first moment any ship moves at all (ships lie still in the countdown).

**The summary** has, besides the match's lines: each player's `seen`
(damage dealt and received, shells, torpedoes, last health the client saw),
`header` (the roster's entry) and `record` (the player record from the
stream, by key number); `chat`; `damageStats` (the recording player's own,
as the game keeps them: per weapon and kind, a count and an amount - kind 0
is damage dealt); `avatarPickles` (every pickled call to the recording
player, decoded, by method number); `header` (the first block, all of it but
the roster: game mode, weather, map border, team sizes...); `moreBlocks`;
`results` (15.x); `blockIds`; `entities` (every entity the stream creates:
its type number and role, when it came into the client's view and when it
left); `streamVersion` (the version as the stream says it); and `selfCheck`
(the completeness count, and the checks of the entities, the results, the
ids and the version).

**What the client was told** is complete for its own team and partial for
enemies: their shots, hits and health are there while in range.

**Not read:**

- Aircraft and their squadrons (the calls that carry them were not taken
  apart), the minimap's vision updates (packed), spotting, ribbons, fires and
  floods as events of their own (their damage is in the hits), consumables,
  capture points and team scores (properties of entities without a
  definition, not told apart by shape), the rest of a ship's properties
  (aim, rudder, speed setting...).
- The player records' and damage statistics' key numbers as names: the game
  numbers them, and the numbers change; they are kept as numbers.
- A shell's extra data where it struck (15.x) and the bytes after a shell's
  or torpedo's start and velocity.
- Results of clients before 15.x: their replays carry none.
- The ship number as a name: the names are in the game's own parameter
  files, not in the replay.

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
recording that began late in the countdown (not checked).

Checks on the rest, in the order of the table above:

- **Health:** each ship sunk within the client's view has a last health of 0
  (17 of 20, 9 of 9, 12 of 14, 10 of 10 sunk ships; the others sank out of
  view). A hit's damage equals a fall of the health in the second before it
  for 64%, 67%, 54% and 52% of hits; the rest fall together with repairs or
  with other hits.
- **Damage against the game's own statistics:** on the 15.10 replay the
  recording player's damage read (91,461) is within 0.1% of the statistics'
  damage dealt (91,544). On the others the statistics are 12-79% higher
  (95,310 read against 170,884; 225,064 against 252,506; 84,295 against
  124,353) - the client is not sent every hit of its own ship, or the
  statistics count more than hits; not resolved.
- **Shells:** a shell starts a median 2.5-4.5 units from its ship's last
  known position (the guns are along a ship 12 or more units long).
- **Where shells ended:** 2,973 of 2,992, 1,576 of 1,576, 980 of 1,176 and
  1,645 of 1,648 end within a minute after their ship fired a shell or
  torpedo the client saw (the rest: shells of ships out of sight).

The tests build replays to the same layout, so no real replay is kept in this
repository.

**Not checked:** clients before 0.9.6, the Lesta client (Mir Korabley),
operations and scenarios beyond the one above, clan and ranked battles, and
which ship number is which ship.

## Completeness

The converter follows the rule all 3DHeat converters share,
[Converters keep everything](https://github.com/Holdi601/3DHeat/blob/main/docs/converters.md):
what it reads goes into the table and the summary; every other item of the
replay is kept whole in the sidecar `<match>.messages.parquet`; and the
summary's `selfCheck.completeness` counts, for each kind of item, how many the
replay holds (`seen`), how many were read whole (`decoded`), read in part and
kept whole (`partial`), only kept (`raw`), and lost (`lost`, 0).

The kinds are the replay's own: `block 0`, `block 1`, `block 2` (the JSON
blocks, kept as text), `container sizes` and `deflate tail` (the container's
own bytes), `packet <type>`, and for entity calls
`method <entity type>.<number>` and `property <entity type>.<number>`. Entity
types are the numbers the creating packets give; the summary's
`selfCheck.entities.roles` says which is the recording player's avatar and
which the ships (1 and 2 on every replay read). They are counted as the
converter meets them in the stream, so a kind nobody knew of shows up with
its count.

The sidecar's columns: `time` (the replay's clock, as the table's), `type`,
`name` (what the converter calls it, where it reads it), `entity` (the ship
or avatar it belongs to, as the table's `entity`), `decoded` (what was read
of it, JSON), `payload` (its bytes, whole: a packet's payload as the stream
has it), `text` (the JSON blocks, whole), `entityType`, `packet` and `method`
(the numbers). Rows are sorted by packet, method, entity and time. Everything
a later reader needs is in it, or in the summary's `entities` and `players`
(which entity is which player).

**Read** (new in this pass, each checked against something independent):

- **The results** (15.x, summary `results`): their `arenaUniqueID` is the
  battle's id read from the stream, and every player of their
  `playersPublicInfo` is in the header's roster (24 of 24 on 15.9, 12 of 12
  on 15.10).
- **The ids block** (15.x, `blockIds`): the account is the results'
  `accountDBID`, the battle the stream's, on both. Read as text: as JSON it is
  a number, and `moreBlocks` has it with the battle's last digits lost.
- **Pitch and roll** of every position (`pitch`, `roll`). Roll goes with the
  rate of turn, as a ship heels in a turn (correlation 0.66, 0.64, 0.47, 0.63
  on 0.9.6, 0.10.11, 15.9, 15.10). Pitch is 0 for all but 17, 42, 268 and 0
  of the updates; where it is not (15.9), it is minus the slope of the ship's
  path (correlation -0.97).
- **Entities** (summary `entities`): the creating packets (0 and 5) give the
  entity and its type, the rest of them is kept; the leaving packet (4: the
  entity alone) is read whole. Check: no ship has a position update between
  leaving and coming back (0 on all four; 46, 19, 50 and 24 entities, 142,
  49, 58 and 39 leaves).
- **The version in the stream** (packet 22, `streamVersion`): the same as the
  header's on all four.

Everything read before this pass (sinkings, damage, health, shells,
torpedoes, where shells ended, chat, the pickled calls, the players' records)
is `partial`: read into the table and the summary as above, and kept whole in
the sidecar with what was read in `decoded`. So are the positions: the table
has place, heading, pitch and roll, the sidecar the whole update.

**Kept raw** (in the sidecar, not read), the biggest kinds:

- `packet 10`, the position updates not in the table (after a ship sank,
  entities without a player), and in every update three numbers BigWorld
  calls the position's error (here integers such as 32002 and 64004, not
  floats; not known) and a flag byte; the own ship's packet (43 or 44) where
  it carries the avatar riding the ship.
- `packet 24` (52 bytes, a rotation of length 1 at byte 28) and `packet 36`
  (0.9, 0.10) or `37` (15.x) (56 or 60 bytes, beginning with a rotation of
  length 1), as many of each, 8-10 a second: likely the camera. Not read:
  their forward does not follow the recording player's shells (which leave
  the gun upwards, in an arc), so nothing checked it. `packet 29` and `14`
  (4 and 8 bytes): not known.
- An entity, a byte, a length and that many bytes (`packet 34` in 0.9 and
  0.10, `35` in 15.x, 1,000 to 6,500 a battle, the entity always one the
  stream created): likely a change inside a property; not read.
- The ships' frequent small properties (`property 2.20`, `2.17` in 0.9.6;
  `2.26`, `2.21` in 0.10.11; `2.25`, `2.20` in 15.x) and the avatar's frequent
  methods (`method 1.70`, `1.113` in 0.9.6; `1.56`, `1.57` in 15.10; `1.146`
  in 15.9): not known. Aircraft, consumables, capture points, ribbons,
  spotting and the minimap are among the kinds not read.
- The entity creations' properties, and every other method, property and
  packet without a reader.

Per replay (the four of [Verified](#verified)):

| Replay | Seen | Decoded | Partial | Raw | Lost | Sidecar | Replay |
|---|---|---|---|---|---|---|---|
| Shoreside 0.9.6 | 199,872 | 143 | 48,845 | 150,884 | 0 | 2.51 MB | 2.97 MB |
| naval_mission 0.10.11 | 138,343 | 50 | 52,235 | 86,058 | 0 | 1.58 MB | 2.04 MB |
| Seychelles 15.9 | 129,579 | 60 | 24,544 | 104,975 | 0 | 1.53 MB | 1.95 MB |
| Faroe 15.10 | 108,407 | 41 | 24,410 | 83,956 | 0 | 1.41 MB | 1.68 MB |

**Not available:**

- What the server never sent the recording client: other players' aim,
  camera and inputs, enemies while unspotted. A replay is what one client
  was told.
- The names of entity types, methods, properties and the records' and
  statistics' keys: they are in the game's definition files, not in the
  replay. The numbers are kept; the converter names what it finds by content.
- Ship names for the ship numbers, and anything else that needs the game's
  own parameter files.
- Results of clients before 15.x: not in their replays.

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
