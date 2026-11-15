---
title: "Feltételek és licenc"
nav_order: 9
lang: "hu"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Feltételek és licenc {#terms-and-licence}

## A Wargaming feltételei {#wargamings-terms}

2026-11-07-én olvasva, a Wargaming EULA 14-es verziója (hatályos 2024. április 10-től, mint jelenlegi);
a 12.3 pontja egy World of Warships modszabályzatra hivatkozik, amelynek oldala böngészőn kívül nem
jelent meg, ezért nem olvastuk el:

- 5.3 (b): hacsak írásban nincs engedélyezve, nem szabad "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): tilos "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Amit ez a konverter csinál: a játék által, a csata után, a játékon kívül írt fájlt olvas.
A játékban semmit nem változtat, egyetlen szerverrel sem beszél, és csata közben semmit nem mutat.
A folyamot a játék kulcsával fejti vissza, amit az 5.3 (b) és a 12.1 (p) pont lefedhet. Hogy
használod-e, a felhasználó döntése; ezért külön csomag.

## Licenc és források {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). A numpy
(BSD-3-Clause) és a pyarrow (Apache-2.0) csomagokat használja. Ez a projekthez készült: az itteni
Blowfish-titkosítás saját, a táblázatait pedig a pi jegyeiből számoljuk, ahogy a titkosítás
előírja. A formátum tényei közismertek a visszajátszó-eszközök között; az egységmérték megjegyzése
a landaire/wows-toolkit (MIT) projektből való. Kódot más projektből nem vettünk át.

A `bigworld.py` és a `table.py` ugyanazok a fájlok, mint a World of Tanks konverterében
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); mindkettőt egyszerre módosítsd.

---

A [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentáció](https://holdi601.github.io/3DHeat/)) része. Forrás: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
