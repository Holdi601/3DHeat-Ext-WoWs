---
title: "Podmienky a licencia"
nav_order: 9
lang: sk
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Podmienky a licencia {#terms-and-licence}

## Podmienky Wargamingu {#wargamings-terms}

Prečítané 2026-11-07, EULA Wargamingu verzia 14 (platná od 10. apríla 2024, uvedená ako aktuálna); jej časť 12.3 odkazuje na pravidlá modov pre World of Warships, ktorých stránka sa mimo prehliadača nezobrazila a nebola prečítaná:

- 5.3 (b): pokiaľ to nepovolíte písomne, nesmiete: "... decompile, disassemble, reverse engineer or otherwise make unauthorized use of the Content".
- 12.1 (k): zakázané je: "Creating, using, making available, or distributing any unauthorized software or tools, including hacks, cheats, exploits, scripts, bots, trainers, automation programs, or other software that interacts with a Product in any way and for any purpose, including intercepts, emulates, or redirects any communication between such software and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures implemented by Wargaming".

Čo tento konvertor robí: číta súbor, ktorý hra zapísala, po bitke, mimo hry. Nič v hre nemení, so serverom nekomunikuje a nič nezobrazuje počas bitky. Tok dešifruje kľúčom hry, čo sa dá podľa 5.3 (b) a 12.1 (p) vykladať tak, že to pokrývajú. Použitie je rozhodnutie používateľa; preto je to samostatný balík.

## Licencia a zdroje {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Potrebuje numpy (BSD-3-Clause) a pyarrow
(Apache-2.0). Napísané pre tento projekt: šifra Blowfish tu je vlastná, jej tabuľky sú vypočítané z číslic čísla pi, ako to šifra definuje.
Fakty o formáte sú medzi autormi replay nástrojov všeobecne známe; poznámka k mierke jednotiek pochádza z landaire/wows-toolkit (MIT).
Žiadny kód sa neprebral z iného projektu.

`bigworld.py` a `table.py` sú tie isté súbory ako v konvertore pre World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); meňte ich oba naraz.

---

Súčasť [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentácia](https://holdi601.github.io/3DHeat/)). Zdroj: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
