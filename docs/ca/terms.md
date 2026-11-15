---
title: Condicions i llicència
nav_order: 9
lang: "ca"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Condicions i llicència {#terms-and-licence}

## Les condicions de Wargaming {#wargamings-terms}

Llegides el 2026-11-07, EULA de Wargaming versió 14 (en vigor des del 10 d'abril de 2024, indicada com a vigent);
la seva secció 12.3 remet a una política de mods de World of Warships, la pàgina de la qual no es va mostrar fora
d'un navegador i no es va llegir:

- 5.3 (b): tret que s'autoritzi per escrit, no pots «... decompile, disassemble, reverse engineer or otherwise make
  unauthorized use of the Content» (descompilar, desmuntar, fer enginyeria inversa o fer d'una altra manera un ús no
  autoritzat del Contingut).
- 12.1 (k): es prohibeix «Creating, using, making available, or distributing any unauthorized software or tools,
  including hacks, cheats, exploits, scripts, bots, trainers, automation programs, or other software that interacts
  with a Product in any way and for any purpose, including intercepts, emulates, or redirects any communication
  between such software and Wargaming» (crear, usar, posar a disposició o distribuir qualsevol programari o eina no
  autoritzats, incloent-hi hacks, trampes, exploits, scripts, bots, entrenadors, programes d'automatització o
  qualsevol altre programari que interactuï d'alguna manera amb un Producte i per a qualsevol finalitat, incloent-hi
  els que interceptin, emulin o redirigeixin qualsevol comunicació entre aquest programari i Wargaming).
- 12.1 (l): «... any software designed to modify a Product and change the user experience ("mods") unless expressly
  permitted by Wargaming» (qualsevol programari dissenyat per modificar un Producte i canviar l'experiència de
  l'usuari («mods») tret que Wargaming ho permeti expressament).
- 12.1 (p): «Circumventing or bypassing enforcement and security measures implemented by Wargaming» (eludir o saltar-se
  les mesures de compliment i de seguretat que aplica Wargaming).

El que fa aquest convertidor: llegeix un fitxer que ha escrit el joc, després de la batalla, fora del joc. No canvia
res al joc, no parla amb cap servidor, i no mostra res durant una batalla. Sí que desxifra el flux amb la clau del
joc, cosa que 5.3 (b) i 12.1 (p) es poden llegir com a coberta. Fer-lo servir és decisió de l'usuari; per això és un
paquet a part.

## Llicència i fonts {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Necessita numpy (BSD-3-Clause) i
pyarrow (Apache-2.0). Escrit per a aquest projecte: el xifrat Blowfish d'aquí és propi, amb les seves taules calculades
a partir dels dígits de pi tal com les defineix el xifrat. Els fets del format són coneguts entre les eines de
repeticions; la nota de l'escala d'unitats ve de landaire/wows-toolkit (MIT). No s'ha pres cap codi de cap altre
projecte.

`bigworld.py` i `table.py` són els mateixos fitxers que al convertidor de World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); canvia'ls tots dos alhora.

---

Part de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentació](https://holdi601.github.io/3DHeat/)). Font: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
