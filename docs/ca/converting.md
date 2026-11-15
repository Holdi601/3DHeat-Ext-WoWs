---
title: Conversió de repeticions
nav_order: 4
lang: ca
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Conversió de repeticions {#converting-replays}

## Pas a pas {#step-by-step}

1. **Activa l'enregistrament**: `isReplayEnabled` al `preferences.xml` del joc, o l'opció pròpia del joc quan
   en té una. A partir d'aleshores el joc desa cada batalla a la carpeta `replays` de la teva instal·lació de
   World of Warships, per exemple `C:\Games\World_of_Warships_EU\replays`.
2. **Obre un terminal** en una carpeta on puguin anar els resultats ([Abans de començar](before-you-start.md)).
3. **Executa el convertidor** sobre fitxers de repetició, o sobre carpetes que els contenen:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` es crea a la carpeta on és el teu terminal.
4. **Llegeix què diu.** Hauries de veure una línia per repetició, que acaba amb la taula que ha escrit.
5. **Obre el resultat** al visualitzador de 3DHeat: `out/<mapa>/<partida>.parquet` a la pestanya Mapa de
   calor, `<partida>.match.json` a la pestanya Partida. O llegeix-los amb qualsevol lector de Parquet o JSON.

![Una execució sobre una repetició sintètica: conversió, una altra execució, un fitxer trencat, una carpeta buida](../assets/img/convert.svg)

La imatge és una execució sobre una repetició que les proves construeixen en codi (cap repetició real):

- una repetició convertida: `<fitxer>: <n> positions of <n> ships at <freqüència> Hz (own <freqüència> Hz), <n> sunk, <mapa> (<versió del client>) -> <taula>`;
- executada de nou, la partida que ja hi és s'omet: `<fitxer>: already written, <taula>`;
- un fitxer que no és una repetició: `<fitxer>: not converted: <motiu>` (a la sortida d'errors; estat de
  sortida 1, les altres repeticions es converteixen igualment);
- cap repetició trobada: `no .wowsreplay files in <carpetes>` (estat de sortida 2).

## Opcions {#options}

| Opció | Per defecte | Fa |
|---|---|---|
| `replays` (una o més) | - | fitxers `.wowsreplay`, o carpetes on es busquen (també les subcarpetes) |
| `-o`, `--out` | obligatòria | la carpeta on escriure: una carpeta per mapa a dins |
| `--force` | desactivada | converteix de nou el que ja és escrit |
| `--ship-names JSON` | - | un fitxer JSON `{"<shipId>": "<nom>", ...}`: les repeticions només posen nom al vaixell del jugador que grava, i als altres pel número |
| `--version` | - | escriu `heat3d-wows-replay <versió>` i s'atura |
| `-h`, `--help` | - | escriu les opcions i s'atura |

Les opcions tal com les escriu el programa: [Referència d'ordres](../cli-reference.md).

## Què s'escriu {#what-is-written}

Només fitxers separats: aquest convertidor no escriu cap fitxer `.3dheat` (el visualitzador els pot empaquetar
en un: [Un fitxer per partida](https://holdi601.github.io/3DHeat/container.html)). Per cada repetició, dins de
`out/<mapa>/` (el nom del mapa sense el seu `spaces/`):

| Fitxer | Què és |
|---|---|
| `<partida>.parquet` | la taula: la posició de cada vaixell al llarg del temps i cada esdeveniment on va passar ([La taula](table.md)) |
| `<partida>.match.json` | el document de partida: mapa, versió del client, jugadors, enfonsaments, xat i tot el altre ([El document de partida](match-document.md)) |
| `<partida>.messages.parquet` | l'annex: cada element de la repetició que els dos fitxers anteriors no guarden sencer ([Completesa](completeness.md)) |

`<partida>` és l'identificador propi de la batalla, o el nom del fitxer quan la gravació es va aturar abans
dels resultats.

## Estat de sortida {#exit-status}

`0` quan totes les repeticions s'han convertit o omès, `1` quan n'ha fallat alguna (les altres es converteixen
igualment), `2` quan no s'ha trobat cap fitxer de repetició.

---

Part de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentació](https://holdi601.github.io/3DHeat/)). Font: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
