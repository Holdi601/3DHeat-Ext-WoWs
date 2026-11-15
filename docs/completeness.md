---
title: Completeness
nav_order: 8
---

# Completeness

Nothing in a replay is thrown away. What the converter reads goes into the
table and the match document; every other item is kept whole in the sidecar
`<match>.messages.parquet`; and the match document's
`selfCheck.completeness` counts what became of each kind of item. This is
the rule all 3DHeat converters share:
[Converters keep everything](https://holdi601.github.io/3DHeat/converters.html).

![The self-check of a synthetic replay: every item seen, read, kept or lost](assets/img/completeness.svg)

## The count

For each kind of item, `selfCheck.completeness.types` gives:

| Count | Means |
|---|---|
| `seen` | how many the replay holds |
| `decoded` | read whole |
| `partial` | read in part, and kept whole in the sidecar |
| `raw` | only kept whole in the sidecar, not read |
| `lost` | lost: always `0` |

The kinds are the replay's own: `block <n>` (the JSON blocks), the
container's own bytes, `packet <type>`, and for calls on entities
`method <entity type>.<number>` and `property <entity type>.<number>`.
`selfCheck.entities.roles` says which entity type is the recording player's
avatar and which the ships. A kind nobody knew of shows up with its count.

## The sidecar

| Column | What |
|---|---|
| `time` | the replay's clock, as in the table |
| `type`, `name` | the kind of item; what the converter calls it, where it reads it |
| `entity` | the ship or avatar it belongs to, as the table's `entity` |
| `decoded` | what was read of it, as JSON |
| `payload`, `text` | its bytes, whole; the JSON blocks, whole |
| `entityType`, `packet`, `method` | the numbers |

Rows are sorted by packet, method, entity and time. Which entity is which
player: the match document's `entities` and `players`.

## What is read, and how it was checked

- **The results** (15.x, `results`): their battle id is the stream's, and
  every player in them is in the header's roster.
- **The ids block** (15.x, `blockIds`): the account and the battle, read as
  text so no digit is lost.
- **Pitch and roll** of every position: the roll goes with the rate of turn,
  as a ship heels in a turn; the pitch is almost always 0.
- **Entities** (`entities`): when each came into the client's view and left.
  No ship has a position between leaving and coming back.
- **The version in the stream** (`streamVersion`): the same as the header's.

Everything else read (sinkings, damage, health, shells, torpedoes, where
shells ended, chat, pickled calls, the players' records, positions) is
`partial`: in the table or the match document, and kept whole in the
sidecar.

**Kept but not read** (`raw`), the biggest kinds: position updates not in
the table (after a ship sank, entities without a player), the frequent
properties and methods without a reader, the properties of entity creations,
and every other packet without a reader.

## Not available

- What the server never sent the recording client: other players' aim,
  camera and inputs, enemies while unspotted. A replay is what one client
  was told.
- The names of entity types, methods, properties and the statistics' keys:
  they are in the game's definition files, not in the replay. The numbers
  are kept.
- Ship names for the ship numbers (use `--ship-names`), and anything else
  that needs the game's own files.
- Results of clients before 15.x: not in their replays.

---

Part of [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
