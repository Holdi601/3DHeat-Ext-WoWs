---
title: How it reads a replay
nav_order: 7
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
    JSON object with the battle's id, read whole into the match document's
    `results` (the game's own lists, unnamed: `commonList`,
    `privateDataList`, `playersPublicInfo` per account, ...).

Packet and method numbers that differ between the versions checked (the own
ship's packet is 43 or 44, the sinking call 76 or 83, the shells 101, 102,
126 or 127) are all found by shape - see
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - so a renumbering
patch does not empty the table. The numbers found are in the match document's
`decoded`.

**The pickle is untrusted data.** A replay is a file from anywhere, and a
pickle can name code to run. It is loaded with an unpickler that hands every
class or function the pickle names an inert placeholder, so it builds plain
data and nothing else. A test feeds it a pickle that calls `os.system`.

**Sinkings** have the call's exact time. Their place is where the victim was
last seen, when that was within five seconds. **The battle's start** is the
first moment any ship moves at all (ships lie still in the countdown).

Everything that is not a table row is in [the match document](match-document.md).

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

## How the reading was checked

The reading was checked on public replays of clients from 0.9 to 15.x, each
value against something the replay gives a second time:

- **Positions:** every ship's entity matched a roster name; headings agree
  with the direction of travel to within 0.1 rad; after its sinking, a ship
  moves less than 0.1 units. A ship lying still is updated less often.
- **Health:** each ship sunk within the client's view ends with health 0.
  About half of all hits match a fall of health in the second before; the
  rest fall together with repairs or other hits.
- **Damage against the game's own statistics:** on the newest client the
  recording player's damage read is within 0.1% of the statistics. On older
  clients the statistics are higher: the client is not sent every hit, or
  the statistics count more than hits (not resolved).
- **Shells:** a shell starts a few units from its ship's last known position
  (the guns are spread along the hull); nearly every shell's end follows,
  within a minute, a shot the client saw.

The tests build replays to the same layout, so no real replay is kept in
this repository.

**Not checked:** clients before 0.9.6, the Lesta client (Mir Korabley),
operations and scenarios beyond one, clan and ranked battles, and
which ship number is which ship.

---

Part of [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
