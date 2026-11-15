---
title: Noteikumi un licence
nav_order: 9
lang: lv
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Noteikumi un licence {#terms-and-licence}

## Wargaming noteikumi {#wargamings-terms}

Lasīts 2026-11-07, Wargaming EULA versija 14 (spēkā no 2024. gada 10. aprīļa, uzskaitīta kā pašreizējā); tās 12.3 punkts atsaucas uz World of Warships modifikāciju politiku, kuras lappuse ārpus pārlūka neatvērās un netika lasīta:

- 5.3 (b): ja nav rakstiski atļauts, tu nedrīksti "... decompile, disassemble, reverse engineer or otherwise make unauthorized use of the Content".
- 12.1 (k): aizliegts ir "Creating, using, making available, or distributing any unauthorized software or tools, including hacks, cheats, exploits, scripts, bots, trainers, automation programs, or other software that interacts with a Product in any way and for any purpose, including intercepts, emulates, or redirects any communication between such software and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures implemented by Wargaming".

Ko dara šis konvertētājs: tas nolasa failu, ko spēle uzrakstīja pēc kaujas, ārpus spēles. Tas nemaina neko spēlē, nesazinās ar serveri un nerāda neko kaujas laikā. Tas tomēr atšifrē straumi ar spēles atslēgu, ko 5.3 (b) un 12.1 (p) var lasīt kā aptverošu. Tā izmantošana ir lietotāja lēmums; tāpēc tas ir atsevišķs pakotne.

## Licence un avoti {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Nepieciešams numpy (BSD-3-Clause) un pyarrow (Apache-2.0). Rakstīts šim projektam: šeit esošais Blowfish šifrs ir pats savs, ar tabulām, kas aprēķinātas no skaitļa pi cipariem, kā to nosaka šifrs. Fakti par formātu ir kopīga zināšana starp atkārtojumu rīkiem; vienības mēroga piezīme ir no landaire/wows-toolkit (MIT). Nekāds kods nav ņemts no kāda cita projekta.

`bigworld.py` un `table.py` ir tie paši faili, kas World of Tanks konvertētājā ([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); maini abus kopā.

---

Daļa no [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentācija](https://holdi601.github.io/3DHeat/)). Avots: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
