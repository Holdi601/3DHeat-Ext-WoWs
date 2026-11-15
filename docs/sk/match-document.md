---
title: "Dokument zápasu"
nav_order: 6
lang: "sk"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Dokument zápasu {#the-match-document}

`<match>.match.json` drží všetko, čo replay hovorí a nie je riadkom tabuľky. Karta Zápas v prehliadači ho číta.
(Kód ho volá súhrn.)

![Začiatok syntetického dokumentu zápasu a jeho kľúče](../assets/img/match-document.svg)

## Bitka {#the-battle}

| Kľúč | Čo |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; id bitky; mapa tak, ako ju hra pomenúva (`spaces/<map>`) a jej zobrazovaný názov |
| `clientVersion`, `streamVersion` | verzia hry z hlavičky a tak, ako ju hovorí tok paketov |
| `recorded` | kedy bol replay nahraný, tak, ako ho hra zapisuje |
| `player`, `vehicle` | hráč, ktorý replay nahral, a jeho loď |
| `gameType`, `scenario` | typ bitky (`RandomBattle`, ...) a scenár, z hlavičky |
| `duration` | časový limit bitky v sekundách, z hlavičky |
| `truncated` | nahrávanie sa skončilo predčasne |
| `battleStart`, `recordingSeconds` | začiatok bitky (prvý okamih, keď sa niektorá loď pohne) a dĺžka nahrávania, v sekundách |
| `positionPacket`, `ownPositionPacket` | čísla paketov, v ktorých prišli polohy: iných lodí, hráča, ktorý replay nahral |
| `deathMethod` | číslo volania, v ktorom sa našli potopenia |
| `hz`, `ownHz`, `positions` | vzorky za sekundu iných lodí a vlastnej lode; riadky polôh |
| `units` | jednotky sveta (15 m podľa trupov, 30 m podľa dostrelu hry); x na východ, y nahor, z na sever |
| `events` | počet riadkov tabuľky každej udalosti |
| `decoded` | metóda a čísla paketov nájdené pre každý druh správy |

## Hráči a udalosti {#players-and-events}

| Kľúč | Čo |
|---|---|
| `players` | jeden záznam na loď: meno, `ally` alebo `enemy`, číslo lode a názov, entita, vzorky, zabitia, prežitie; `seen` (poškodenie spôsobené a prijaté, granáty, torpéda a posledné zdravie, ktoré klient videl); `header` (záznam zo súpisky) a `record` (záznam hráča z toku, podľa čísla kľúča) |
| `kills` | každé potopenie: čas, obeť, vrah, číslo príčiny, miesto |
| `chat` | každý riadok chatu, s kanálom a odosielateľom |
| `damageStats` | vlastné štatistiky hráča, ktorý replay nahral, tak, ako ich hra vedie: na zbraň a druh počet a suma (druh 0 je spôsobené poškodenie) |
| `avatarPickles` | každé vyčlenené volanie hráčovi, ktorý replay nahral, dekódované, podľa čísla metódy |

## Hlavička, výsledky a kontroly {#header-results-and-checks}

| Kľúč | Čo |
|---|---|
| `header` | prvý blok JSON, všetko okrem súpisky: herný režim, počasie, hranica mapy, veľkosti tímov a ďalšie |
| `moreBlocks` | bloky JSON za prvým, tak, ako sú |
| `blockIds` | 15.x: účet hráča, ktorý replay nahral, a id bitky, čítané ako text |
| `results` | 15.x: výsledky, ktoré tieto klienty držia v toku |
| `entities` | každá entita, ktorú tok vytvorí: jej číslo typu a úloha, kedy sa dostala do pohľadu klienta a kedy z neho odišla |
| `selfCheck` | počet úplnosti ([Úplnosť](completeness.md)) a kontroly entít, výsledkov, id a verzie |

---

Súčasť [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentácia](https://holdi601.github.io/3DHeat/)). Zdroj: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
