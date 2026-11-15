---
title: "Podmínky a licence"
nav_order: 9
lang: "cs"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Podmínky a licence {#terms-and-licence}

## Podmínky Wargamingu {#wargamings-terms}

Přečteno 2026-11-07, EULA Wargamingu verze 14 (účinná od 10. dubna 2024, uvedená jako platná); její oddíl 12.3
odkazuje na zásady modů pro World of Warships, jejichž stránka se mimo prohlížeč nezobrazila a nebyla přečtena:

- 5.3 (b): pokud to nepovolíte písemně, nesmíte "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): zakázáno je "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Co tento převodník dělá: čte soubor, který hra zapsala po bitvě, mimo hru. Nic ve hře nemění, s žádným serverem
nemluví a během bitvy nic neukazuje. Proud dešifruje klíčem hry, o kterém lze podle 5.3 (b) a 12.1 (p) číst, že je
pokrytý. Použití je rozhodnutí uživatele; proto je to samostatný balíček.

## Licence a zdroje {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Potřebuje numpy (BSD-3-Clause) a pyarrow
(Apache-2.0). Napsáno pro tento projekt: šifra Blowfish zde je vlastní,
s tabulkami spočítanými z číslic pí, jak ji šifra definuje.
Fakta o formátu jsou mezi nástroji pro čtení replayů běžně známá; poznámka o měřítku jednotek pochází od
landaire/wows-toolkit (MIT). Žádný kód nebyl převzat z jiného projektu.

`bigworld.py` a `table.py` jsou stejné soubory jako v převodníku pro World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); měňte je vždy společně.

---

Součást [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentace](https://holdi601.github.io/3DHeat/)). Zdroj: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
