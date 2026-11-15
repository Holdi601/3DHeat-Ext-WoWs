---
title: Installing
nav_order: 3
---

# Installing

New to the command line? Read [Before you start](before-you-start.md) first.
Needs Python 3.10 or later; numpy and pyarrow are installed with it.

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
