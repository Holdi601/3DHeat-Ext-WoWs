---
title: Termeni și licență
nav_order: 9
lang: "ro"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Termeni și licență {#terms-and-licence}

## Termenii Wargaming {#wargamings-terms}

Citit pe 2026-11-07, EULA Wargaming versiunea 14 (în vigoare de la 10 aprilie 2024, listat
ca fiind cel curent); secțiunea sa 12.3 trimite la o politică de modificări pentru World of Warships, a cărei
pagină nu s-a afișat în afara unui browser și nu a fost citită:

- 5.3 (b): dacă nu sunteți autorizat în scris, nu trebuie să „... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content” (să decompilezi, să dezasamblezi, să faci inginerie inversă sau să folosiți altfel neautorizat Conținutul).
- 12.1 (k): este interzis „Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming.” (Crearea, folosirea, punerea la dispoziție sau distribuirea oricărui software sau instrument neautorizat, inclusiv hack-uri, trișe, exploatări, scripturi, boți, trainere, programe de automatizare sau alt software care interacționează în vreun fel cu un Produs, în orice scop, inclusiv cel care interceptează, emulează sau redirecționează orice comunicare între acel software și Wargaming.)
- 12.1 (l): „... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming” (orice software proiectat să modifice un Produs și să schimbe experiența utilizatorului („modificări”), dacă Wargaming nu le permite explicit).
- 12.1 (p): „Circumventing or bypassing enforcement and security measures
  implemented by Wargaming” (Ocolirea sau evitarea măsurilor de aplicare și de securitate implementate de Wargaming).

Ce face acest convertor: citește un fișier scris de joc, după bătălie, în afara jocului. Nu schimbă
nimic în joc, nu vorbește cu niciun server și nu arată nimic în timpul unei bătălii. Descifrează totuși
fluxul cu cheia jocului, ceea ce 5.3 (b) și 12.1 (p) pot fi citite ca fiind acoperite. Folosirea lui este
decizia utilizatorului; de aceea este un pachet separat.

## Licență și surse {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Are nevoie de numpy (BSD-3-Clause) și pyarrow
(Apache-2.0). Scris pentru acest proiect: cifrul Blowfish de aici este propriul său,
cu tabelele sale calculate din cifrele lui pi, așa cum le definește cifrul.
Faptele despre format sunt cunoscute în comun de instrumentele pentru replay; nota despre scara unităților
este din landaire/wows-toolkit (MIT). Niciun cod nu a fost luat de la alt proiect.

`bigworld.py` și `table.py` sunt aceleași fișiere ca în convertorul pentru World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); schimbați-le pe amândouă împreună.

---

Parte din [3DHeat](https://github.com/Holdi601/3DHeat) ([documentație](https://holdi601.github.io/3DHeat/)). Sursă: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
