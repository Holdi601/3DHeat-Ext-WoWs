---
title: Pogoji in licenca
nav_order: 9
lang: "sl"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Pogoji in licenca {#terms-and-licence}

## Pogoji Wargaminga {#wargamings-terms}

Prebrano 2026-11-07, Wargaming EULA različica 14 (velja od 10. aprila 2024, navedena kot trenutna); njen
oddelek 12.3 kaže na pravilnik o modifikacijah World of Warships, katerega stran se zunaj brskalnika ni
prikazala in ni bila prebrana:

- 5.3 (b): razen če je dovoljeno pisno, ne smete "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): prepovedano je "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Kaj ta pretvornik počne: prebere datoteko, ki jo je igra zapisala, po bitki, zunaj igre. Ničesar ne spremeni v
igri, z nobenim strežnikom se ne pogovarja in med bitko ničesar ne prikaže. Dekodira pa tok z igrinim ključem,
kar je mogoče razumeti kot zajeto v 5.3 (b) in 12.1 (p). Uporaba je odločitev uporabnika; zato je to ločen
paket.

## Licenca in viri {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Potrebuje numpy (BSD-3-Clause) in
pyarrow (Apache-2.0). Napisano za ta projekt: šifra Blowfish tukaj je njena lastna, z njenimi tabelami,
izračunanimi iz številk števila pi, kot jih šifra določa. Dejstva o formatu so med orodji za branje posnetkov
splošno znana; opomba o merilu enot prihaja iz landaire/wows-toolkit (MIT). Nobena koda ni bila vzeta iz
kateregakoli drugega projekta.

`bigworld.py` in `table.py` sta iste datoteki kot v pretvorniku World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); spremenite ju obe hkrati.

---

Del [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Vir: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
