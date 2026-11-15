---
title: "Uvjeti i licenca"
nav_order: 9
lang: "bs"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Uvjeti i licenca {#terms-and-licence}

## Wargamingovi uvjeti {#wargamings-terms}

Pročitano 2026-11-07, Wargaming EULA verzija 14 (na snazi od 10. aprila 2024., navedena
kao aktualna); njen odjeljak 12.3 upućuje na pravila o modovima za World of Warships, čija
se stranica nije prikazala izvan preglednika i nije pročitana:

- 5.3 (b): osim ako nije pismeno odobreno, ne smijete "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): zabranjeno je "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Šta ovaj konverter radi: čita datoteku koju je igra napisala, poslije bitke,
izvan igre. Ne mijenja ništa u igri, ne razgovara ni s jednim serverom i
ne prikazuje ništa tokom bitke. Dešifrira tok ključem igre,
što se može čitati kao obuhvaćeno tačkama 5.3 (b) i 12.1 (p). Korištenje je odluka
korisnika; zato je to poseban paket.

## Licenca i izvori {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Potrebni su numpy (BSD-3-Clause) i pyarrow
(Apache-2.0). Napisano za ovaj projekat: Blowfish šifra ovdje je vlastita,
s tabelama izračunatim iz cifara broja pi kako ih šifra definira.
Činjenice o formatu su opće znanje među alatima za replayeve; bilješka o mjerilu
jedinica je iz landaire/wows-toolkit (MIT). Nikakav kod nije preuzet iz bilo kojeg drugog
projekta.

`bigworld.py` i `table.py` su iste datoteke kao u World of Tanks
konverteru ([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); mijenjajte oba zajedno.

---

Dio [3DHeata](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Izvor: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
