---
title: "Matchdokumentet"
nav_order: 6
lang: "sv"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Matchdokumentet {#the-match-document}

`<match>.match.json` håller allt repriset säger som inte är en rad i tabellen. Visarens
Match-flik läser det. (Koden kallar det sammanfattningen.)

![Början av ett syntetiskt matchdokument, och dess nycklar](../assets/img/match-document.svg)

## Striden {#the-battle}

| Nyckel | Vad |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; stridens id; kartan så som spelet namnger den (`spaces/<map>`) och dess visningsnamn |
| `clientVersion`, `streamVersion` | spelversionen ur headern, och så som paketströmmen anger den |
| `recorded` | när repriset spelades in, så som spelet skriver det |
| `player`, `vehicle` | den inspelande spelaren och dess fartyg |
| `gameType`, `scenario` | stridens typ (`RandomBattle`, ...) och scenario, ur headern |
| `duration` | stridens tidsgräns i sekunder, ur headern |
| `truncated` | inspelningen stoppade tidigt |
| `battleStart`, `recordingSeconds` | stridens start (det första ögonblick något fartyg rör sig) och inspelningens längd, i sekunder |
| `positionPacket`, `ownPositionPacket` | paketnumren positionerna kom i: andra fartygs, den inspelande spelarens |
| `deathMethod` | metodnumret sänkningarna hittades i |
| `hz`, `ownHz`, `positions` | mätpunkter per sekund för andra fartyg och för det egna fartyget; positionsrader |
| `units` | världsenheter (15 m enligt skrovens mått, 30 m enligt spelets räckvidder); x öster, y upp, z norr |
| `events` | antalet tabellrader för varje händelse |
| `decoded` | metod- och paketnumren som hittats för varje slag av meddelande |

## Spelare och händelser {#players-and-events}

| Nyckel | Vad |
|---|---|
| `players` | en post per fartyg: namn, `ally` eller `enemy`, fartygsnummer och namn, entitet, mätpunkter, sänkningar, överlevde; `seen` (skada given och fått, granater, torpeder och sist sedda hälsa som klienten såg); `header` (listans post) och `record` (spelarens post ur strömmen, under nyckelnumret) |
| `kills` | varje sänkning: tid, offer, dödare, orsaksnummer, plats |
| `chat` | varje chattrad, med kanal och avsändare |
| `damageStats` | den inspelande spelarens egen statistik så som spelet för den: per vapen och slag, ett antal och ett belopp (slag 0 är given skada) |
| `avatarPickles` | varje inlagt anrop till den inspelande spelaren, avkodat, efter metodnummer |

## Header, resultat och kontroller {#header-results-and-checks}

| Nyckel | Vad |
|---|---|
| `header` | det första JSON-blocket, allt utom listan: spelläge, väder, kartans gräns, lagstorlekar med mera |
| `moreBlocks` | JSON-blocken efter det första, så som de är |
| `blockIds` | 15.x: den inspelande spelarens konto och stridens id, lästa som text |
| `results` | 15.x: resultaten, som de här klienterna håller i strömmen |
| `entities` | varje entitet strömmen skapar: dess typnummer och roll, när den kom in i klientens syn och när den lämnade den |
| `selfCheck` | fullständighetsräkningen ([Fullständighet](completeness.md)) och kontrollerna av entiteterna, resultaten, id:na och versionen |

---

Del av [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentation](https://holdi601.github.io/3DHeat/)). Källa: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
