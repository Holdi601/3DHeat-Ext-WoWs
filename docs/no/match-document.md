---
title: "Kampdokumentet"
nav_order: 6
lang: no
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Kampdokumentet {#the-match-document}

`<kamp>.match.json` holder alt replayen sier som ikke er en rad i tabellen. Visningsprogrammets
fane Kamp leser den. (Koden kaller den oppsummeringen.)

![Starten på et syntetisk kampdokument, og dets nøkler](../assets/img/match-document.svg)

## Slaget {#the-battle}

| Nøkkel | Hva |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; slagets ID; kartet slik spillet navngir det (`spaces/<kart>`) og dets visningsnavn |
| `clientVersion`, `streamVersion` | spillversjonen fra headeren, og slik pakkestrømmen sier den |
| `recorded` | når replayen ble tatt opp, slik spillet skriver det |
| `player`, `vehicle` | opptakspilotens spiller og hans skip |
| `gameType`, `scenario` | slagets type (`RandomBattle`, ...) og scenario, fra headeren |
| `duration` | slagets tidsgrense i sekunder, fra headeren |
| `truncated` | opptaket stoppet tidlig |
| `battleStart`, `recordingSeconds` | slagets start (det første øyeblikket noe skip beveger seg) og opptakets lengde, i sekunder |
| `positionPacket`, `ownPositionPacket` | pakkenumrene posisjonene kom i: andre skips, opptakspilotens |
| `deathMethod` | metodenummeret senkingene ble funnet i |
| `hz`, `ownHz`, `positions` | samples i sekundet for andre skip og for eget skip; posisjonsrader |
| `units` | verdensenheter (15 m etter skrogene, 30 m etter spillets rekkevidder); x øst, y opp, z nord |
| `events` | antallet tabellrader for hver hendelse |
| `decoded` | metode- og pakkenumrene som ble funnet for hver type melding |

## Spillere og hendelser {#players-and-events}

| Nøkkel | Hva |
|---|---|
| `players` | én post per skip: navn, `ally` eller `enemy`, skipsnummer og navn, entitet, samples, drap, overlevde; `seen` (skade gjort og mottatt, granater, torpedoer og siste helse klienten så); `header` (deltakerlistens post) og `record` (spillerens post fra strømmen, etter nøkkelnummer) |
| `kills` | hver senking: tid, offer, dreper, årsaksnummer, sted |
| `chat` | hver chat-linje, med kanal og avsender |
| `damageStats` | opptakspilotens egen statistikk slik spillet fører den: per våpen og type, et antall og en mengde (type 0 er skade gjort) |
| `avatarPickles` | hvert pickle-kall til opptakspiloten, dekodet, etter metodenummer |

## Header, resultater og kontroller {#header-results-and-checks}

| Nøkkel | Hva |
|---|---|
| `header` | den første JSON-blokken, alt unntatt deltakerlisten: spillmodus, vær, kartkant, lagstørrelser med mer |
| `moreBlocks` | JSON-blokkene etter den første, som de er |
| `blockIds` | 15.x: opptakspilotens konto og slagets ID, lest som tekst |
| `results` | 15.x: resultatene, som disse klientene beholder i strømmen |
| `entities` | hver entitet strømmen oppretter: dens typenummer og rolle, når den kom inn i klientens syn og når den forlot det |
| `selfCheck` | fullstendighetstellingen ([Fullstendighet](completeness.md)) og kontrollene av entitetene, resultatene, ID-ene og versjonen |

---

Del av [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentasjon](https://holdi601.github.io/3DHeat/)). Kilde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
