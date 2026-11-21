---
title: Terms and licence
nav_order: 9
---

# Terms and licence

## What it reads

The converter reads replay files that the game wrote on your own computer,
after the battle and outside the game. It changes nothing in the game, talks
to no server and shows nothing during a battle. Nothing from the game is
shipped or redistributed with it: no game assets, no game code, no DLLs. What
it writes stays on your computer.

`catalog` and `models` read the files of the copy of the game you installed,
read-only: the package index, the parameter table, the English names and the
ships' armour models. The catalogue and the model pack they write are for your
machine, not to be passed on.

3DHeat is not affiliated with or endorsed by Wargaming. World of Warships and
related names and trademarks belong to their owners.

Rights holders: open an issue at
<https://github.com/Holdi601/3DHeat-Ext-WoWs/issues> - we respond quickly and
remove anything on request.

## Licence and sources

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Needs numpy (BSD-3-Clause) and pyarrow
(Apache-2.0). Written for this project: the Blowfish cipher here is its own,
with its tables computed from the digits of pi as the cipher defines them.
Facts about the format are common knowledge among replay tools; the unit scale
note is from landaire/wows-toolkit (MIT). No code was taken from any other
project.

`bigworld.py` and `table.py` are the same files as in the World of Tanks
converter ([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); change both together.

---

Part of [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
