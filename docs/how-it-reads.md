---
title: How it reads a replay
nav_order: 6
---

# How it reads a replay

A replay is a header of JSON blocks and the game's packet stream (format notes
in [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

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
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - so a renumbering
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

---

Part of [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
