---
title: Installing
nav_order: 3
---

# Installing

New to the command line? Read [Before you start](before-you-start.md) first.
Needs Python 3.10 or later; numpy and pyarrow are installed with it.

## The standalone program (no Python needed)

Each [release](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases/latest) has a ready-to-run program for Windows, Linux (also Steam Deck) and macOS
(`heat3d-wows-<version>-windows-x64.zip`, `...-linux-x64.tar.gz`, `...-macos-arm64.tar.gz`), with a
`SHA256SUMS` file to check the download. Unpack it anywhere and start `heat3d-wows` (on macOS the
first start may need *Open* from the right-click menu, as the program is not notarised).

Started without arguments it opens a window that:

- finds your World of Warships install (Steam on any system, the launcher's `Games` folders,
  `~/Games` and Wine/Lutris prefixes on Linux), or lets you choose its folder;
- says what is missing (the game, free disk space);
- converts the battles in its `replays` folder, or any folder you pick, into tables and match
  documents (by default into the 3DHeat data folder's `matches/wows`);
- writes the ship catalogue and the local ship model pack from your install (they stay on your machine);
- checks for updates and asks before installing one, unless you tick *Update automatically*.

The same program runs every command below: `heat3d-wows heat3d-wows-replay --help`. For scripts:
`heat3d-wows --check --json` says what is found and missing, and `heat3d-wows status --json` what is found
(a replay reader has no maps; `extract` has nothing to do). The 3DHeat app's Extractors panel installs,
updates and starts it for you.

The window walks through four steps (find the game, choose, work, done) in the 3DHeat look, dark or light. On Windows the program opens only its window, with no console window; in a terminal it prints as usual, and `heat3d-wows-cli.cmd` in the same folder makes the terminal wait for it and pass on its exit code.

Replays from the command line: `heat3d-wows convert <replay>... -o <folder> [--progress-json]` converts them (one JSON line per replay with `--progress-json`), and `heat3d-wows info <replay> --json` prints what a replay says about its match (map, mode, date, length, players, teams, result, game version), read from its header without converting it. The 3DHeat Library uses both.

## Step by step

1. Get the code: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   or download a zip from [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   and unpack it.
2. Open a terminal in that folder and type `pip install -e .`. This puts the
   `heat3d-wows-replay` command on your path.
3. Check it: `heat3d-wows-replay --version`. You should see
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` lists the options:

![heat3d-wows-replay --help](assets/img/help.svg)

Without installing, `python -m heat3d_ext_wows ...` in the tool's folder does
the same.

The 3DHeat Watcher runs this command on new replays when it is installed,
and works without it.

## Updates

Every start first checks the project's GitHub releases (at most one request
every few hours; it never stops a conversion, online or not). When a newer
release is out, the command asks before installing it: a `git clone` is
updated with `git pull --ff-only` (refused while you have local changes), a
downloaded copy from the release's archive. `HEAT3D_NO_UPDATE=1` switches the
check and the update off.

---

Part of [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
