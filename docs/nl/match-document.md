---
title: "Het wedstrijddocument"
nav_order: 6
lang: "nl"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Het wedstrijddocument {#the-match-document}

`<match>.match.json` bevat alles wat de replay zegt dat geen rij van de tabel is. Het tabblad Match van de viewer leest het. (De code noemt het de samenvatting.)

![Het begin van een synthetisch wedstrijddocument, en zijn sleutels](../assets/img/match-document.svg)

## Het gevecht {#the-battle}

| Sleutel | Wat |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; het id van het gevecht; de kaart zoals het spel haar noemt (`spaces/<map>`) en haar weergavenaam |
| `clientVersion`, `streamVersion` | de versie van het spel uit de kop, en zoals de pakketstroom die noemt |
| `recorded` | wanneer de replay is opgenomen, zoals het spel het schrijft |
| `player`, `vehicle` | de opnemende speler en zijn schip |
| `gameType`, `scenario` | het type gevecht (`RandomBattle`, ...) en het scenario, uit de kop |
| `duration` | de tijdslimiet van het gevecht in seconden, uit de kop |
| `truncated` | de opname stopte vroeg |
| `battleStart`, `recordingSeconds` | het begin van het gevecht (het eerste moment dat een schip beweegt) en de lengte van de opname, in seconden |
| `positionPacket`, `ownPositionPacket` | de pakketnummers waarin de posities kwamen: die van andere schepen, die van de opnemende speler |
| `deathMethod` | het methodenummer waarin de zinkingen gevonden zijn |
| `hz`, `ownHz`, `positions` | samples per seconde van andere schepen en van het eigen schip; positierijen |
| `units` | wereldeenheden (15 m volgens de rompen, 30 m volgens de bereiken van het spel); x oost, y omhoog, z noord |
| `events` | het aantal tabelrijen van elke gebeurtenis |
| `decoded` | de methode- en pakketnummers die gevonden zijn voor elke soort bericht |

## Spelers en gebeurtenissen {#players-and-events}

| Sleutel | Wat |
|---|---|
| `players` | één item per schip: naam, `ally` of `enemy`, schipnummer en -naam, entiteit, samples, kills, overleefd; `seen` (toegebrachte en ontvangen schade, granaten, torpedo's en de laatste gezondheid die de client zag); `header` (het item van de deelnemerslijst) en `record` (het record van de speler uit de stroom, per sleutelnummer) |
| `kills` | elke zinking: tijd, slachtoffer, killer, oorzaaknummer, plaats |
| `chat` | elke chatregel, met kanaal en afzender |
| `damageStats` | de eigen statistieken van de opnemende speler zoals het spel ze bijhoudt: per wapen en soort een telling en een bedrag (soort 0 is toegebrachte schade) |
| `avatarPickles` | elke gepickelde aanroep naar de opnemende speler, gedecodeerd, per methodenummer |

## Kop, resultaten en controles {#header-results-and-checks}

| Sleutel | Wat |
|---|---|
| `header` | het eerste JSON-blok, alles behalve de deelnemerslijst: spelmodus, weer, kaartrand, teamgroottes en meer |
| `moreBlocks` | de JSON-blokken na het eerste, zoals ze zijn |
| `blockIds` | 15.x: het account van de opnemende speler en het id van het gevecht, als tekst gelezen |
| `results` | 15.x: de resultaten, die deze clients in de stroom bewaren |
| `entities` | elke entiteit die de stroom aanmaakt: zijn typenummer en rol, wanneer hij in het zicht van de client kwam en wanneer hij weg was |
| `selfCheck` | de telling van volledigheid ([Volledigheid](completeness.md)) en de controles van de entiteiten, de resultaten, de id's en de versie |

---

Onderdeel van [3DHeat](https://github.com/Holdi601/3DHeat) ([documentatie](https://holdi601.github.io/3DHeat/)). Bron: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
