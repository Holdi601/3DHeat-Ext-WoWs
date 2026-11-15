---
title: "Villkor och licens"
nav_order: 9
lang: "sv"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Villkor och licens {#terms-and-licence}

## Wargamings villkor {#wargamings-terms}

Lästa 2026-11-07, Wargaming EULA version 14 (gäller från 10 april 2024, listad som
gällande); dess avsnitt 12.3 hänvisar till en modpolicy för World of Warships, vars
sida inte visades utanför en webbläsare och inte lästes:

- 5.3 (b): om inte skriftligt godkänt får du inte "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): förbjudet är "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Vad den här konverteraren gör: den läser en fil som spelet skrev, efter striden,
utanför spelet. Den ändrar inget i spelet, pratar med ingen server, och visar inget
under en strid. Den avkodar strömmen med spelets nyckel, vilket 5.3 (b) och 12.1 (p)
kan läsas som att de täcker. Att använda den är användarens beslut; därför är den ett
eget paket.

## Licens och källor {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Kräver numpy (BSD-3-Clause) och pyarrow
(Apache-2.0). Skriven för det här projektet: Blowfish-chiffret här är eget, med sina tabeller
uträknade ur siffrorna i pi, så som chiffret definierar dem. Fakta om formatet är allmänt kända bland
repriverktyg; noten om enhetens skala kommer från landaire/wows-toolkit (MIT). Ingen kod togs från
något annat projekt.

`bigworld.py` och `table.py` är samma filer som i World of Tanks-konverteraren
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); ändra båda tillsammans.

---

Del av [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentation](https://holdi601.github.io/3DHeat/)). Källa: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
