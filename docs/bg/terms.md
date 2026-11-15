---
title: Условия и лиценз
nav_order: 9
lang: "bg"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Условия и лиценз {#terms-and-licence}

## Условията на Wargaming {#wargamings-terms}

Прочетено на 2026-11-07, Wargaming EULA версия 14 (в сила от 10 април 2024 г., посочено като актуално); неговата точка 12.3 сочи към правила за модификации на World of Warships, чиято страница не се показа извън браузър и не е прочетена:

- 5.3 (b): освен ако не е разрешено писмено, не трябва да "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): забранено е "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Какво прави този преобразувател: чете файл, който играта е записала, след битката,
извън играта. Той не променя нищо в играта, не говори с никой сървър и
не показва нищо по време на битка. Той декодира потока с ключа на играта, което 5.3 (b) и 12.1 (p) може
да се четат като покриващи. Използването му е решение на потребителя; затова е отделен пакет.

## Лиценз и източници {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Нужни са numpy (BSD-3-Clause) и pyarrow
(Apache-2.0). Написано за този проект: шифърът Blowfish тук е собствен,
с таблиците му, изчислени от цифрите на числото пи, както ги определя шифърът.
Фактите за формата са общоизвестни сред инструментите за повторения; бележката за мащаба на единиците е от landaire/wows-toolkit (MIT). Никакъв код не е взет от друг
проект.

`bigworld.py` и `table.py` са същите файлове като в преобразувателя за World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); променяйте и двата заедно.

---

Част от [3DHeat](https://github.com/Holdi601/3DHeat) ([документация](https://holdi601.github.io/3DHeat/)). Източник: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
