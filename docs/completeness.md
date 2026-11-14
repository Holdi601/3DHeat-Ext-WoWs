---
title: Completeness
nav_order: 7
---

# Completeness

![The self-check of a synthetic replay: every item seen, read, kept or lost](assets/img/completeness.svg)

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

Per replay (the four of [Verified](how-it-reads.md#verified)):

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

---

Part of [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
