# 3DHeat World of Warships replays

**What is it?** World of Warships can save every battle you play as a
replay file. This tool turns those files into a table and a match document
(the battle's summary) that the [3DHeat viewer](https://holdi601.github.io/3DHeat/)
shows in 3D: where every ship sailed, fired and was hit.

**Why would I use it?** To watch a battle again from above, every ship at
once; to see heatmaps of where you and others sail, fight and sink over
hundreds of battles; to see where shells and torpedoes came from and where
they ended; or to read a replay with your own scripts (pandas, DuckDB),
since the output is plain Parquet and JSON.

**Example:** `example.wowsreplay` in, `out/<map>/<match>.parquet` (the
table) and `<match>.match.json` (the match document) out.

![From a replay to the 3DHeat viewer](docs/assets/img/pipeline.svg)

**Documentation, step by step with pictures:
<https://holdi601.github.io/3DHeat-Ext-WoWs/>** (Documentation in your
language: choose it at the top of any page there.)

Part of [3DHeat](https://github.com/Holdi601/3DHeat), the realtime 3D
telemetry and replay viewer ([documentation](https://holdi601.github.io/3DHeat/)).

Each game reader is its own small project with its own licence file, releases
and issue tracker, so it can be installed, updated, maintained - or withdrawn
on a rights holder's request - on its own, without affecting the viewer or the
other tools.

## The standalone program

No Python needed: download the file for your system (Windows, Linux (also Steam Deck) and macOS) from the
[latest release](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases/latest), check it against `SHA256SUMS`, unpack it and start `heat3d-wows`. Its window
finds your install, converts the battles in its `replays` folder (or any folder you pick),
writes the ship catalogue and model pack from your install, and asks before it updates itself. `heat3d-wows --help` lists its commands (`heat3d-wows heat3d-wows-replay ...` runs every command below).
The 3DHeat app's Extractors panel can install and update it for you. See
[the install page](https://holdi601.github.io/3DHeat-Ext-WoWs/installing.html).

The window walks through four steps (find the game, choose, work, done) in the 3DHeat look, dark or light. On Windows the program opens only its window, with no console window; in a terminal it prints as usual, and `heat3d-wows-cli.cmd` in the same folder makes the terminal wait for it and pass on its exit code.

Replays from the command line: `heat3d-wows convert <replay>... -o <folder> [--progress-json]` converts them (one JSON line per replay with `--progress-json`), and `heat3d-wows info <replay> --json` prints what a replay says about its match (map, mode, date, length, players, teams, result, game version), read from its header without converting it. The 3DHeat Library uses both.

## Quick start for new users (Python)

You need: Windows, [Python](https://www.python.org/downloads/) 3.10 or later
("Add python.exe to PATH" ticked in its installer), and World of Warships with
replay recording switched on (`isReplayEnabled` in the game's
`preferences.xml`, or the game's own setting where it has one; the game then
saves each battle in the `replays` folder of its install). No Git is needed.

1. Install the tool (one line, in PowerShell or a command prompt):

   ```bash
   python -m pip install https://github.com/Holdi601/3DHeat-Ext-WoWs/archive/refs/tags/v0.1.0.zip
   ```

2. Convert the replays (the folder of your install, or single `.wowsreplay`
   files; run it again later and only the new ones are converted):

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   ```

   Replays name only your own ship; `--ship-names names.json` (a JSON file
   `{"<shipId>": "<name>", ...}`) names the others.
3. The output is a folder per map in `out`: per battle `<match>.parquet`
   (the table), `<match>.match.json` (the match document) and
   `<match>.messages.parquet`. It prints one line per replay, ending in
   `-> out/<map>/<match>.parquet`.
4. Open it in the [3DHeat viewer](https://github.com/Holdi601/3DHeat#quick-start):
   download the viewer (**Code -> Download ZIP**, unpack) and double-click
   `start.bat`; it offers to install [Node.js](https://nodejs.org/) when it is
   missing and opens Chrome or Edge at `http://127.0.0.1:5273`. There,
   **Source -> Files...** and pick the `<match>.parquet` files (or drop them
   on the Source panel) for the Heatmap tab; for the battle itself, the
   **Match** tab's **Load match files...** and the `<match>.match.json`.

When a new release is out, the tool says so when it starts and offers to
update itself (`python -m heat3d_ext_wows.update` does the same).

## Install from a checkout

New to the command line? Read
[Before you start](https://holdi601.github.io/3DHeat-Ext-WoWs/before-you-start.html)
first. Needs Python 3.10 or later.

```bash
git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git
cd 3DHeat-Ext-WoWs
pip install -e .                  # installs the heat3d-wows-replay command
heat3d-wows-replay --version      # you should see: heat3d-wows-replay 0.1.0
```

`python -m heat3d_ext_wows ...` does the same as `heat3d-wows-replay ...`.

## Use

Switch replay recording on (`isReplayEnabled` in the game's
`preferences.xml`, or the game's own setting where it has one). The game
then saves replays in the `replays` folder of your World of Warships install.

```bash
heat3d-wows-replay "<World of Warships>/replays" -o out
heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
heat3d-wows-replay a.wowsreplay -o out --ship-names names.json
```

You should see one line per replay:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz (own 6.99 Hz), 0 sunk, spaces/99_testmap (15.10.0.13533378) -> out/99_testmap/2630531823886288.parquet
```

| Option | Default | Does |
|---|---|---|
| `replays` (one or more) | - | `.wowsreplay` files, or folders searched for them (subfolders too) |
| `-o`, `--out` | required | the folder to write into; a folder per map inside |
| `--force` | off | convert again what is already written (else it is skipped) |
| `--ship-names JSON` | - | a JSON file `{"<shipId>": "<name>", ...}`: replays name only the recording player's ship, the others by number |
| `--version` | - | print `heat3d-wows-replay <version>` and stop |
| `-h`, `--help` | - | print the options and stop |

Exit status: `0` every replay converted (or skipped), `1` any failed (the
rest are still converted), `2` no replay file found. Every start first looks
for a newer release and asks before installing it; `HEAT3D_NO_UPDATE=1`
switches that off. All options, as the program prints them:
[Command reference](https://holdi601.github.io/3DHeat-Ext-WoWs/cli-reference.html).

## Catalogue and model pack

With the game installed, `heat3d-wows-replay catalog` writes every ship, shell
and torpedo with names and numbers, and `heat3d-wows-replay models` writes each
ship's armour model (hull and plates by thickness) for the viewer; both stay on
your machine. See [Catalogue and models](docs/catalog-models.md).

## Output

Loose files only (this converter writes no `.3dheat`; the viewer can pack
them into one, see [One file a match](https://holdi601.github.io/3DHeat/container.html)).
Per replay, into `out/<map>/` (the map's name without its `spaces/`):

| File | What | In the viewer |
|---|---|---|
| `<match>.parquet` | the table: every ship's position while the client saw it, and every event where it happened | Heatmap tab |
| `<match>.match.json` | the match document: map, client version, players, sinkings, chat, everything else | Match tab |
| `<match>.messages.parquet` | the sidecar: every item of the replay the two above do not hold whole | - |

`<match>` is the battle's id, or the file's name when none is found.

The table's columns (31), in short:

| Columns | What |
|---|---|
| `match`, `map`, `time`, `battleTime`, `event` | which battle, when (seconds), what the row is |
| `player`, `team`, `own`, `vehicle`, `type`, `entity` | who: name, `ally` or `enemy`, `1` on the recording player's rows, the ship and its class |
| `x`, `y`, `z` | where, in the game's world units (not metres): x east, y up, z north |
| `dirX`, `dirY`, `dirZ`, `pitch`, `roll` | which way the bow points |
| `other`, `reason`, `value`, `health`, `text`, `shot`, `params` | the event: the other ship, why, how much, health left, chat text, salvo id, shell type |
| `otherVehicle`, `otherType`, `hitLocalX/Y/Z` | where a shell ended on a ship, in metres in the ship's own frame |

Events: `position`, `death`, `kill`, `hurt`, `damage`, `shot`, `torpedo`,
`impact`, `chat`. Every column with its unit:
[The table](https://holdi601.github.io/3DHeat-Ext-WoWs/table.html); every key
of the match document:
[The match document](https://holdi601.github.io/3DHeat-Ext-WoWs/match-document.html);
how the viewer reads columns and roles:
[Column mapping](https://holdi601.github.io/3DHeat/column-mapping.html).

## Good to know

- A replay is what one game client was told: your team all the time,
  enemies only while spotted or near.
- What the converter reads, and that nothing from the game is shipped with
  it: [Terms and licence](https://holdi601.github.io/3DHeat-Ext-WoWs/terms.html).
- How a replay is read and how it was checked:
  [How it reads a replay](https://holdi601.github.io/3DHeat-Ext-WoWs/how-it-reads.html)
  and [Completeness](https://holdi601.github.io/3DHeat-Ext-WoWs/completeness.html).

## The 3DHeat tools

| Tool | What it does | Source | Documentation |
|---|---|---|---|
| 3DHeat viewer | shows the data in 3D: heatmaps, replays, race analysis | [3DHeat](https://github.com/Holdi601/3DHeat) | [site](https://holdi601.github.io/3DHeat/) |
| GameFiles | courses and levels out of the files games ship | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [site](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | lap telemetry, and levels rebuilt from gameplay video | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [site](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | an Unreal Editor plugin that exports a level | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [site](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | Counter-Strike 2 demos and maps | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [site](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | records what games publish while you play | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [site](https://holdi601.github.io/3DHeat-Watcher/) |
| War Thunder replays | `.wrpl` replays and War Thunder levels | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [site](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| World of Tanks replays | `.wotreplay` replays | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [site](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| World of Warships replays | `.wowsreplay` replays | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [site](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Squad demos | Squad server demos | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [site](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| DCS maps | DCS World maps as 3D levels | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [site](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| IL-2 maps | IL-2 Great Battles maps as 3D levels | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [site](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Dota 2 map | the Dota 2 map from your own install as a 3D level | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [site](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Dota 2 replays | Dota 2 replays | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [site](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Riot replays | League of Legends and VALORANT replays (what they carry unencrypted) | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [site](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Forza maps | Forza courses, races and cars from your own install | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [site](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Battlefield maps | Battlefield levels (Frostbite) as 3D levels | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [site](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| BeamNG maps | BeamNG.drive courses | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [site](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| AC Rally maps | Assetto Corsa Rally stages as courses | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [site](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Reforger maps | Arma Reforger worlds (Enfusion) as 3D levels | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [site](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| R6 replays | Rainbow Six Siege match replays | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [site](https://holdi601.github.io/3DHeat-Ext-R6/) |

## Licence

MIT ([`LICENSE`](LICENSE)). Needs numpy (BSD-3-Clause) and pyarrow
(Apache-2.0). All code is written for this project; no code was taken from
other replay tools. Tests: `pip install -e .[test]` then `pytest` (the tests
build replays in code; no real replay is kept here). For maintainers:
[Maintaining](https://holdi601.github.io/3DHeat-Ext-WoWs/maintaining.html).

3DHeat is not affiliated with or endorsed by Wargaming. World of Warships and
related names and trademarks belong to their owners. Rights holders: open an
issue at <https://github.com/Holdi601/3DHeat-Ext-WoWs/issues> - we respond quickly
and remove anything on request.
