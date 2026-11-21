---
title: Command reference
nav_order: 90
---

# Command reference

This page is generated from the code by `tools/gen_docs_reference.py`; do not edit it by hand.
The other pages explain each command step by step.

## `heat3d-wows-replay`

```text
usage: heat3d-wows-replay [-h] -o OUT [--force] [--ship-names JSON] [--version]
                          replays [replays ...]

World of Warships replays into 3DHeat tables

positional arguments:
  replays            .wowsreplay files, or folders searched for them

options:
  -h, --help         show this help message and exit
  -o, --out OUT      folder to write into (a folder per map inside)
  --force            convert again what is already written
  --ship-names JSON  a JSON object of shipId -> ship name; replays carry only the
                     number for every ship but the recording player's (default: the
                     ship catalogue, `catalog`, when it is under HEAT3D_LEVELS)
  --version          show program's version number and exit
```
