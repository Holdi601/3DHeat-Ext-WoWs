---
title: Warunki i licencja
nav_order: 9
lang: "pl"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Warunki i licencja {#terms-and-licence}

## Warunki Wargaming {#wargamings-terms}

Przeczytane 2026-11-07, EULA Wargaming w wersji 14 (obowiązuje od 10 kwietnia 2024, wymieniona
jako aktualna); jej punkt 12.3 odsyła do zasad dotyczących modów World of Warships, których
strona nie wyświetliła się poza przeglądarką i nie została przeczytana:

- 5.3 (b): bez pisemnej zgody nie wolno "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): zabronione jest "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Co robi ten konwerter: czyta plik, który gra zapisała, po bitwie, poza grą. Nic nie zmienia w grze, nie rozmawia z żadnym serwerem i
niczego nie pokazuje podczas bitwy. Odszyfrowuje strumień kluczem gry, co punkty 5.3 (b) i 12.1 (p) mogą
obejmować. Korzystanie z niego to decyzja użytkownika; dlatego jest to osobny pakiet.

## Licencja i źródła {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Wymaga numpy (BSD-3-Clause) i pyarrow
(Apache-2.0). Napisane na potrzeby tego projektu: użyty tu szyfr Blowfish jest własny,
z tablicami wyliczonymi z cyfr liczby pi, tak jak definiuje to szyfr.
Fakty o formacie są powszechnie znane wśród narzędzi do replayów; uwaga o skali jednostek pochodzi od
landaire/wows-toolkit (MIT). Żaden kod nie został wzięty z innego projektu.

`bigworld.py` i `table.py` to te same pliki co w konwerterze World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); zmieniaj oba razem.

---

Część [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacja](https://holdi601.github.io/3DHeat/)). Źródło: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
