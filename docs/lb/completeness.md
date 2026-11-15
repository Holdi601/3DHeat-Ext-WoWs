---
title: "Vollstännegkeet"
nav_order: 8
lang: lb
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Vollstännegkeet {#completeness}

Näischt an engem Replay gëtt ewechgeheit. Wat de Konverter liest, kënnt an d'
Tabell an d'Match-Dokument; all anert Stéck gëtt ganz am Sidecar
`<match>.messages.parquet` behalen; an dem Match-Dokument säin
`selfCheck.completeness` zielt, wat aus all Aart Stéck ginn ass. Dat ass
d'Regel, déi all 3DHeat-Konverter deelen:
[Konverteren behalen alles](https://holdi601.github.io/3DHeat/converters.html).

![D'Selbstkontroll vun engem synthetesche Replay: all Stéck gesinn, gelies, behalen oder verluer](../assets/img/completeness.svg)

## D'Zielung {#the-count}

Fir all Aart Stéck gëtt `selfCheck.completeness.types`:

| Zuel | Bedeit |
|---|---|
| `seen` | wéi vill de Replay hält |
| `decoded` | ganz gelies |
| `partial` | zum Deel gelies, a ganz am Sidecar behalen |
| `raw` | nëmmen ganz am Sidecar behalen, net gelies |
| `lost` | verluer: émmer `0` |

D'Aarte sinn déi vum Replay selwer: `block <n>` (d'JSON-Blöck), d'eege Bytes
vum Container, `packet <type>`, a fir Opruffer op Entitéite
`method <entity type>.<number>` an `property <entity type>.<number>`.
`selfCheck.entities.roles` seet, wéi eng Entitéitstyp dem opuelende Spiller säin
Avatar ass a wéi eng d'Schëffer. Eng Aart, déi keen kannt huet, erschéngt mat hirer Zuel.

## De Sidecar {#the-sidecar}

| Kolonn | Wat |
|---|---|
| `time` | d'Auer vum Replay, wéi an der Tabell |
| `type`, `name` | d'Aart vum Stéck; wéi de Konverter et nennt, wou en et liest |
| `entity` | d'Schëff oder den Avatar, zu deem et gehéiert, wéi d'`entity` vun der Tabell |
| `decoded` | wat dovunner gelies gouf, als JSON |
| `payload`, `text` | seng Bytes, ganz; d'JSON-Blöck, ganz |
| `entityType`, `packet`, `method` | d'Nummeren |

D'Zeile sinn no Paket, Method, Entitéit an Zäit sortéiert. Wéi eng Entitéit wéi e
Spiller ass: dem Match-Dokument seng `entities` an `players`.

## Wat gelies gëtt, a wéi et gepréift gouf {#what-is-read-and-how-it-was-checked}

- **D'Resultater** (15.x, `results`): hir Gefechts-ID ass déi vum Stroum, an
  all Spiller dran ass an der Roster vum Header.
- **Den IDen-Block** (15.x, `blockIds`): de Kont an d'Gefecht, als
  Text gelies, sou datt keng Zifferen verluer ginn.
- **Pitch a Roll** vun all Positioun: d'Roll geet mat der Dréiraten, wéi e
  Schëff sech an enger Kéier neigt; d'Pitch ass bal émmer 0.
- **Entitéiten** (`entities`): wéini all an de Bléck vum Client koum a fortgaang ass.
  Kee Schëff huet eng Positioun tëscht dem Fortgoen an dem Zréckkommen.
- **D'Versioun am Stroum** (`streamVersion`): déiselwecht wéi déi vum Header.

Alles anescht, wat gelies gëtt (Versenkungen, Schued, Liewen, Granaten, Torpedoen, wou
Granaten opgehalen hunn, Chat, gepickelt Opruffer, d'Enregistremente vun de Spiller, Positiounen), ass
`partial`: an der Tabell oder dem Match-Dokument, a ganz am
Sidecar behalen.

**Behalen, awer net gelies** (`raw`), déi gréissten Aarten: Positiouns-Updates, déi net an
der Tabell sinn (nodeems e Schëff versonk ass, Entitéiten ouni Spiller), déi heefeg
Propriétéiten a Methoden ouni Reader, d'Propriétéite vun Entitéit-Erstellungen,
an all aner Paket ouni Reader.

## Net verfügbar {#not-available}

- Wat de Server dem opuelende Client ni geschéckt huet: d'Ziel, d'Kamera an d'Inputs vun
  anere Spiller, Feinde, wann net entdeckt. E Replay ass dat, wat een Client
  gesot krut.
- D'Nimm vun Entitéitstypen, Methoden, Propriétéiten an de Schlësselen vun de Statistiken:
  si sinn an den Definitiounsdateie vum Spill, net am Replay. D'Nummere
  ginn behalen.
- Schëffsnimm fir d'Schëffsnummeren (benotz `--ship-names`), an alles anescht,
  wat dem Spill seng eege Dateie brauch.
- Resultater vu Clienten virun 15.x: net an hire Replays.

---

Deel vun [3DHeat](https://github.com/Holdi601/3DHeat) ([Dokumentatioun](https://holdi601.github.io/3DHeat/)). Quell: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
