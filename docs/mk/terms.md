---
title: "Услови и лиценца"
nav_order: 9
lang: mk
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Услови и лиценца {#terms-and-licence}

## Условите на Wargaming {#wargamings-terms}

Прочитано на 2026-11-07, Wargaming EULA верзија 14 (во сила од 10 April 2024, наведена како актуелна); нејзиниот дел 12.3 упатува на политика за модови на World of Warships, чија страница не се прикажа надвор од прелистувач и не беше прочитана:

- 5.3 (b): освен ако не е овластено писмено, не смеете да „... decompile, disassemble, reverse engineer or otherwise make unauthorized use of the Content“.
- 12.1 (k): забрането е „Creating, using, making available, or distributing any unauthorized software or tools, including hacks, cheats, exploits, scripts, bots, trainers, automation programs, or other software that interacts with a Product in any way and for any purpose, including intercepts, emulates, or redirects any communication between such software and Wargaming.“
- 12.1 (l): „... any software designed to modify a Product and change the user experience ("mods") unless expressly permitted by Wargaming“.
- 12.1 (p): „Circumventing or bypassing enforcement and security measures implemented by Wargaming“.

Што прави овој конвертор: чита датотека што ја напишала играта, по битката, надвор од играта. Не менува ништо во играта, не разговара со ниту еден сервер и не прикажува ништо за време на битка. Го дешифрира текот со клучот на играта, што 5.3 (b) и 12.1 (p) може да се прочитаат дека го опфаќаат. Користењето е одлука на корисникот; затоа е одделен пакет.

## Лиценца и извори {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Бара numpy (BSD-3-Clause) и pyarrow (Apache-2.0). Напишано за овој проект: шифрата Blowfish тука е сопствена, со табели пресметани од цифрите на пи како што ги дефинира шифрата. Фактите за форматот се општо знаење меѓу алатките за снимки; белешката за размерот на единиците е од landaire/wows-toolkit (MIT). Ниту еден код не е земен од кој и да е друг проект.

`bigworld.py` и `table.py` се истите датотеки како во конверторот за World of Tanks ([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); менувајте ги заедно.

---

Дел од [3DHeat](https://github.com/Holdi601/3DHeat) ([документација](https://holdi601.github.io/3DHeat/)). Извор: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
