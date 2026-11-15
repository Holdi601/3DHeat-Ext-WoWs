---
title: Ehdot ja lisenssi
nav_order: 9
lang: "fi"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Ehdot ja lisenssi {#terms-and-licence}

## Wargamingin ehdot {#wargamings-terms}

Luettu 2026-11-07, Wargamingin EULA versio 14 (voimassa 10. huhtikuuta 2024 alkaen, luettelo nykyisenä).
Sen kohta 12.3 viittaa World of Warshipsin mod-käytäntöön, jonka sivu ei latautunut selaimen ulkopuolella,
eikä sitä luettu:

- 5.3 (b): ilman kirjallista lupaa et saa "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): kiellettyä on "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Mitä tämä muunnin tekee: se lukee pelin kirjoittaman tiedoston taistelun jälkeen, pelin ulkopuolella.
Se ei muuta mitään pelissä, ei puhu palvelimelle eikä näytä mitään taistelun aikana. Se kyllä purkaa
virran pelin avaimella, ja 5.3 (b) ja 12.1 (p) voidaan lukea kattavan sen. Käyttö on käyttäjän päätös;
siksi se on erillinen paketti.

## Lisenssi ja lähteet {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Tarvitsee numpyn
(BSD-3-Clause) ja pyarrow'n (Apache-2.0). Kirjoitettu tätä projektia varten: tämän Blowfish-salaus on
oma toteutus, jonka taulukot on laskettu piin numeroista, niin kuin salaus ne määrittelee. Tiedot
formaatista ovat replay-työkalujen yhteistä tietoa; yksikköskaalan huomautus on landaire/wows-toolkitista
(MIT). Mitään koodia ei ole otettu muista projekteista.

`bigworld.py` ja `table.py` ovat samat tiedostot kuin World of Tanks -muuntimessa
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); muuta molempia yhdessä.

---

Osa [3DHeatiä](https://github.com/Holdi601/3DHeat) ([dokumentaatio](https://holdi601.github.io/3DHeat/)). Lähde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
