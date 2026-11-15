---
title: Kampdokumentet
nav_order: 6
lang: "da"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Kampdokumentet {#the-match-document}

`<match>.match.json` indeholder alt det, replayet siger, som ikke er en række i tabellen. Viewerens Kamp-fane
læser den. (Koden kalder den resuméet.)

![Starten af et syntetisk kampdokument, og dets nøgler](../assets/img/match-document.svg)

## Slaget {#the-battle}

| Nøgle | Hvad |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; kampens id; kortet, som spillet navngiver det (`spaces/<map>`), og dets visningsnavn |
| `clientVersion`, `streamVersion` | spilversionen fra headeren, og som pakkestrømmen siger den |
| `recorded` | hvornår replayet blev optaget, som spillet skriver det |
| `player`, `vehicle` | den optagende spiller og dennes skib |
| `gameType`, `scenario` | kampens type (`RandomBattle`, ...) og scenario, fra headeren |
| `duration` | kampens tidsgrænse i sekunder, fra headeren |
| `truncated` | optagelsen stoppede tidligt |
| `battleStart`, `recordingSeconds` | kampens start (det første øjeblik, et skib bevæger sig) og optagelsens længde, i sekunder |
| `positionPacket`, `ownPositionPacket` | pakkenumrene positionerne kom i: andre skibes, den optagende spillers |
| `deathMethod` | metodenummeret, søenkningerne blev fundet i |
| `hz`, `ownHz`, `positions` | samples i sekundet for andre skibe og for det egne skib; positionsrækker |
| `units` | verdensenheder (15 m efter skrogene, 30 m efter spillets rækkevidder); x øst, y op, z nord |
| `events` | antallet af tabelrækker for hver begivenhed |
| `decoded` | metode- og pakkenumrene, der er fundet for hver slags meddelelse |

## Spillere og begivenheder {#players-and-events}

| Nøgle | Hvad |
|---|---|
| `players` | én post pr. skib: navn, `ally` eller `enemy`, skibsnummer og -navn, entitet, samples, drab, overlevet; `seen` (skade forvoldt og modtaget, granater, torpedoer og det sidste liv klienten så); `header` (rosterens post) og `record` (spillerens optegnelse fra strømmen, efter nøglenummer) |
| `kills` | hver søenkning: tidspunkt, offer, dræber, årsagsnummer, sted |
| `chat` | hver chatlinje, med kanal og afsender |
| `damageStats` | den optagende spillers egen statistik, som spillet fører den: pr. våben og slags, en tælling og et beløb (slag 0 er forvoldt skade) |
| `avatarPickles` | hvert indpakkede kald til den optagende spiller, afkodet, efter metodenummer |

## Header, resultater og kontroller {#header-results-and-checks}

| Nøgle | Hvad |
|---|---|
| `header` | den første JSON-blok, hele den undtagen rosteren: spiltilstand, vejr, kortets grænse, holdstørrelser og mere |
| `moreBlocks` | JSON-blokkene efter den første, som de er |
| `blockIds` | 15.x: den optagende spillers konto og kampens id, læst som tekst |
| `results` | 15.x: resultaterne, som disse klienter gemmer i strømmen |
| `entities` | hver entitet strømmen opretter: dens typenummer og rolle, hvornår den kom ind i klientens udsyn, og hvornår den forlod det |
| `selfCheck` | fuldstændighedstællingen ([Fuldstændighed](completeness.md)) og kontrollerne af entiteterne, resultaterne, id'erne og versionen |

---

Del af [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentation](https://holdi601.github.io/3DHeat/)). Kilde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
