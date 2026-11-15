---
title: "D'Match-Dokument"
nav_order: 6
lang: lb
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# D'Match-Dokument {#the-match-document}

`<match>.match.json` enthält alles, wat de Replay seet an net eng Zeil vun der
Tabell ass. Dem Viewer säi Match-Tab liest et. (De Code nennt et d'Zesummefaassung.)

![Den Ufank vun engem synthetesche Match-Dokument, a seng Schlësselen](../assets/img/match-document.svg)

## D'Gefecht {#the-battle}

| Schlëssel | Wat |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; d'ID vum Gefecht; d'Kaart, wéi d'Spill se nennt (`spaces/<map>`), a säin Uweisungsnumm |
| `clientVersion`, `streamVersion` | d'Spillversioun aus dem Header, an dat, wat de Paketstroum seet |
| `recorded` | wéini de Replay opgeholl gouf, wéi d'Spill et schreift |
| `player`, `vehicle` | den opuelende Spiller a säi Schëff |
| `gameType`, `scenario` | den Typ vum Gefecht (`RandomBattle`, ...) a säi Szenario, aus dem Header |
| `duration` | d'Zäitlimit vum Gefecht a Sekonnen, aus dem Header |
| `truncated` | d'Opnam huet fréi opgehalen |
| `battleStart`, `recordingSeconds` | den Ufank vum Gefecht (dee Moment, wou e Schëff fir d'éischt beweegt gëtt) an d'Längt vun der Opnam, a Sekonnen |
| `positionPacket`, `ownPositionPacket` | d'Paketnummeren, an deenen d'Positioune koumen: vun anere Schëffer, vum opuelende Spiller |
| `deathMethod` | d'Methodennummer, an där d'Versenkunge fonnt goufen |
| `hz`, `ownHz`, `positions` | Echantillonen d'Sekonn vun anere Schëffer a vum eegene Schëff; Positiounszeilen |
| `units` | Weltenheeten (15 m no de Rümp, 30 m no de Reechwäite vum Spill); x Ouschten, y erop, z Norden |
| `events` | d'Zuel vun den Tabellzeile vun all Evenement |
| `decoded` | d'Method an d'Paketnummere, déi fir all Aart Message fonnt goufen |

## Spiller an Evenementer {#players-and-events}

| Schlëssel | Wat |
|---|---|
| `players` | een Androung pro Schëff: Numm, `ally` oder `enemy`, Schëffsnummer an -numm, Entitéit, Echantillonen, Kills, iwwerlieft; `seen` (ausgedeelte a kritte Schued, Granaten, Torpedoen a leschtes Liewen, dat de Client gesinn huet); `header` (d'Androung vun der Roster) an `record` (dem Spiller säin Enregistrement aus dem Stroum, no Schlësselnummer) |
| `kills` | all Versenkung: Zäit, Affer, Killer, Ursaachnummer, Plaz |
| `chat` | all Chat-Zeil, mat Kanal a Sender |
| `damageStats` | dem opuelende Spiller seng eege Statistiken, wéi d'Spill se hält: pro Waff an Aart, eng Zuel an e Betrag (Aart 0 ass ausgedeelte Schued) |
| `avatarPickles` | all gepickelten Opruff un den opuelende Spiller, decodéiert, no Methodennummer |

## Header, Resultater a Kontrollen {#header-results-and-checks}

| Schlëssel | Wat |
|---|---|
| `header` | deen éischte JSON-Block, alles ausser der Roster: Spillmodus, Wieder, Kaartegrenz, Teamgréissten a méi |
| `moreBlocks` | d'JSON-Blöck nom éischten, esou wéi se sinn |
| `blockIds` | 15.x: de Kont vum opuelende Spiller an d'ID vum Gefecht, als Text gelies |
| `results` | 15.x: d'Resultater, déi dës Clienten am Stroum halen |
| `entities` | all Entitéit, déi de Stroum erstellt: hir Typnummer a Roll, wéini se an de Bléck vum Client koum a wéini se fortgaang ass |
| `selfCheck` | d'Vollstännegkeetszielung ([Vollstännegkeet](completeness.md)) an d'Kontrolle vun den Entitéiten, de Resultater, den IDen an der Versioun |

---

Deel vun [3DHeat](https://github.com/Holdi601/3DHeat) ([Dokumentatioun](https://holdi601.github.io/3DHeat/)). Quell: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
