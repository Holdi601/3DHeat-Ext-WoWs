---
title: Vilkår og licens
nav_order: 9
lang: da
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Vilkår og licens {#terms-and-licence}

## Wargamings vilkår {#wargamings-terms}

Læst 2026-11-07, Wargaming EULA version 14 (i kraft fra 10. april 2024, angivet som gældende); dens afsnit 12.3
henviser til en modpolitik for World of Warships, hvis side ikke kunne vises uden for en browser og ikke blev læst:

- 5.3 (b): medmindre det er godkendt skriftligt, må du ikke "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): forbudt er "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Hvad denne konverter gør: den læser en fil, spillet skrev, efter kampen, uden for spillet. Den ændrer
intet i spillet, taler med ingen server og viser intet under en kamp. Den dekrypterer strømmen med spillets
nøgle, hvilket 5.3 (b) og 12.1 (p) kan læses som dækkende. At bruge den er brugerens beslutning; derfor er
den en separat pakke.

## Licens og kilder {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Kræver numpy (BSD-3-Clause) og pyarrow
(Apache-2.0). Skrevet til dette projekt: Blowfish-chifferet her er sit eget, med tabellerne udregnet ud fra cifrene i pi,
som chifferet definerer dem. Fakta om formatet er almindeligt kendt blandt replay-værktøjer; noten om enhedsskalaen
stammer fra landaire/wows-toolkit (MIT). Ingen kode er taget fra noget andet projekt.

`bigworld.py` og `table.py` er de samme filer som i World of Tanks-konverteren
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); ændr begge sammen.

---

Del af [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentation](https://holdi601.github.io/3DHeat/)). Kilde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
