---
title: Installing
nav_order: 2
---

# Installing

Needs Python 3.10 or later; numpy and pyarrow are installed with it.

## Step by step

1. Get the code: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git` (or download a release zip from
   [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases) and unpack it).
2. Install it into your Python: in that folder, `pip install -e .`. This
   puts the `heat3d-wows-replay` command on your path.
3. Check it: `heat3d-wows-replay --version` prints the version (the `VERSION` file), and
   `heat3d-wows-replay --help` the options:

![heat3d-wows-replay --help](assets/img/help.svg)

Without installing, `python -m heat3d_ext_wows ...` in the repository folder does the
same.

The 3DHeat Watcher runs this command on new replays when it is installed, and
works without it.

## Updates

Every start first checks the project's GitHub releases (one request at most
every few hours, cached; it never stops a conversion, offline or not). When a
newer release is out, the command asks before installing it: a `git clone` is
updated with `git pull --ff-only` (refused while you have local changes), a
downloaded copy from the release's source archive. `HEAT3D_NO_UPDATE=1`
switches the check and the update off. Code: `heat3d_update`
(`startup("heat3d_ext_wows")`).

---

Part of [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
