# Changelog

## Unreleased

- `catalog`: every ship, shell, torpedo and bomb of the installed game with
  names and numbers (`catalog.json`, format `3dheat-catalog`).
- `models`: each ship's armour model as a local model pack for the viewer:
  the hull at three levels of detail and the plates by thickness.
- Replays name every ship from the catalogue when it is there and no
  `--ship-names` is given.

## 0.1.0

- `--version` prints the command's name with the version
  (`heat3d-wows-replay 0.1.0`), as the other 3DHeat converters do.
- Documentation: a page for beginners, a key table for the match document,
  generated reference pages, no real map names or replay figures.

- Every ship's position, heading, pitch and roll while the client saw it;
  every sinking where it happened.
- Hits and health, every shell and torpedo fired, where shells ended (on a
  ship: the point in its own frame), chat, the recording player's damage
  statistics, the results of 15.x clients.
- Ship names from a JSON file (`--ship-names`).
- Nothing lost: the sidecar keeps every item not read whole, and the
  self-check counts each kind.
- Installs with one pip line from the release zip, no Git needed; a pip install knows its version and updates itself with pip when a newer release is out.
- README: a quick start for new users.

## Docs

Where each feature is documented:

| Feature | Page |
|---|---|
| installing, updates | [Installing](docs/installing.md), [Before you start](docs/before-you-start.md) |
| converting, options (`--ship-names`), messages, exit status | [Converting replays](docs/converting.md), [Command reference](docs/cli-reference.md) |
| positions, heading, pitch, roll, units | [The table](docs/table.md) |
| sinkings, hits, shells, torpedoes, impacts | [The table](docs/table.md) (events) |
| players, chat, damage statistics, results | [The match document](docs/match-document.md) |
| every column and its type | [Column list](docs/columns.md) |
| the format, and how the reading was checked | [How it reads a replay](docs/how-it-reads.md) |
| sidecar, self-check | [Completeness](docs/completeness.md) |
| what it reads, licence | [Terms and licence](docs/terms.md) |
| releasing | [Maintaining](docs/maintaining.md) |
