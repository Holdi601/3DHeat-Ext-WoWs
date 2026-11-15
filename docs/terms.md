---
title: Terms and licence
nav_order: 9
---

# Terms and licence

## Wargaming's terms

Read on 2026-11-07, Wargaming EULA version 14 (effective 10 April 2024, listed
as current); its section 12.3 points to a World of Warships mod policy, whose
page did not render outside a browser and was not read:

- 5.3 (b): unless authorised in writing, you must not "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): prohibited is "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

What this converter does: it reads a file the game wrote, after the battle,
outside the game. It changes nothing in the game, talks to no server, and
shows nothing during a battle. It does decipher the stream with the game's
key, which 5.3 (b) and 12.1 (p) can be read to cover. Using it is the user's
decision; that is why it is a separate package.

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
