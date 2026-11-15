---
title: "Dokument zápasu"
nav_order: 6
lang: "cs"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Dokument zápasu {#the-match-document}

`<match>.match.json` drží vše, co replay říká a co není řádkem tabulky. Čte ho záložka Zápas prohlížeče.
(Kód to nazývá souhrn.)

![Začátek syntetického dokumentu zápasu a jeho klíče](../assets/img/match-document.svg)

## Bitva {#the-battle}

| Klíč | Co |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; id bitvy; mapa tak, jak ji hra pojmenovává (`spaces/<map>`), a její zobrazovaný název |
| `clientVersion`, `streamVersion` | verze hry z hlavičky a tak, jak ji říká proud paketů |
| `recorded` | kdy byl replay nahrán, tak jak to zapisuje hra |
| `player`, `vehicle` | hráč, který nahrával, a jeho loď |
| `gameType`, `scenario` | typ bitvy (`RandomBattle`, ...) a scénář, z hlavičky |
| `duration` | časový limit bitvy v sekundách, z hlavičky |
| `truncated` | nahrávání skončilo předčasně |
| `battleStart`, `recordingSeconds` | začátek bitvy (první okamžik, kdy se nějaká loď pohne) a délka nahrávky, v sekundách |
| `positionPacket`, `ownPositionPacket` | čísla paketů, ve kterých přišly pozice: ostatních lodí, hráče, který nahrával |
| `deathMethod` | číslo metody, ve které byla potopení nalezena |
| `hz`, `ownHz`, `positions` | vzorky za vteřinu ostatních lodí a vlastní lodi; řádky pozic |
| `units` | světové jednotky (podle trupů 15 m, podle dostřelů hry 30 m); x na východ, y nahoru, z na sever |
| `events` | počet řádků tabulky každé události |
| `decoded` | čísla metod a paketů nalezená pro každý druh zprávy |

## Hráči a události {#players-and-events}

| Klíč | Co |
|---|---|
| `players` | jeden záznam na loď: jméno, `ally` nebo `enemy`, číslo a název lodi, entita, vzorky, zabití, přežití; `seen` (poškození způsobené a přijaté, granáty, torpéda a poslední zdraví, které klient viděl); `header` (záznam ze soupisky) a `record` (záznam hráče ze streamu, podle čísla klíče) |
| `kills` | každé potopení: čas, oběť, zabiják, číslo příčiny, místo |
| `chat` | každý řádek chatu, s kanálem a odesílatelem |
| `damageStats` | vlastní statistiky hráče, který nahrával, tak, jak je hra vede: na zbraň a druh počet a částka (druh 0 je způsobené poškození) |
| `avatarPickles` | každé volání pickle hráči, který nahrával, dekódované, podle čísla metody |

## Hlavička, výsledky a kontroly {#header-results-and-checks}

| Klíč | Co |
|---|---|
| `header` | první blok JSON, celý kromě soupisky: herní režim, počasí, hranice mapy, velikosti týmů a další |
| `moreBlocks` | bloky JSON za prvním, tak, jak jsou |
| `blockIds` | 15.x: účet hráče, který nahrával, a id bitvy, čteno jako text |
| `results` | 15.x: výsledky, které tyto klienty drží v proudu |
| `entities` | každá entita, kterou proud vytvoří: číslo typu a role, kdy vstoupila do zorného pole klienta a kdy z něj odešla |
| `selfCheck` | počet úplnosti ([Úplnost](completeness.md)) a kontroly entit, výsledků, id a verze |

---

Součást [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentace](https://holdi601.github.io/3DHeat/)). Zdroj: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
