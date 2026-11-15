---
title: El document de partida
nav_order: 6
lang: "ca"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# El document de partida {#the-match-document}

`<partida>.match.json` guarda tot el que diu la repetició que no és una fila de la taula. La pestanya Partida del
visualitzador el llegeix. (El codi l'anomena el resum.)

![L'inici d'un document de partida sintètic, i les seves claus](../assets/img/match-document.svg)

## La batalla {#the-battle}

| Clau | Què és |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; l'identificador de la batalla; el mapa tal com el nomena el joc (`spaces/<mapa>`) i el seu nom per mostrar |
| `clientVersion`, `streamVersion` | la versió del joc de la capçalera, i tal com l'indica el flux de paquets |
| `recorded` | quan es va gravar la repetició, tal com ho escriu el joc |
| `player`, `vehicle` | el jugador que grava i el seu vaixell |
| `gameType`, `scenario` | el tipus de batalla (`RandomBattle`, ...) i l'escenari, de la capçalera |
| `duration` | el límit de temps de la batalla en segons, de la capçalera |
| `truncated` | la gravació es va aturar abans |
| `battleStart`, `recordingSeconds` | l'inici de la batalla (el primer moment en què es mou cap vaixell) i la durada de la gravació, en segons |
| `positionPacket`, `ownPositionPacket` | els números de paquet en què van arribar les posicions: les dels altres vaixells, les del jugador que grava |
| `deathMethod` | el número de mètode en què es van trobar els enfonsaments |
| `hz`, `ownHz`, `positions` | mostres per segon dels altres vaixells i del propi vaixell; files de posició |
| `units` | unitats de món (15 m segons els cascos, 30 m segons els abastos del joc); x est, y amunt, z nord |
| `events` | el nombre de files de la taula de cada esdeveniment |
| `decoded` | el mètode i els números de paquet trobats per a cada tipus de missatge |

## Jugadors i esdeveniments {#players-and-events}

| Clau | Què és |
|---|---|
| `players` | una entrada per vaixell: nom, `ally` o `enemy`, número i nom del vaixell, entitat, mostres, morts, supervivència; `seen` (dany fet i rebut, obusos, torpedes i l'última salut que va veure el client); `header` (l'entrada de la llista) i `record` (el registre del jugador del flux, per número de clau) |
| `kills` | cada enfonsament: hora, víctima, assassí, número de causa, lloc |
| `chat` | cada línia de xat, amb canal i remitent |
| `damageStats` | les estadístiques pròpies del jugador que grava tal com les guarda el joc: per arma i tipus, un recompte i una quantitat (el tipus 0 és dany fet) |
| `avatarPickles` | cada crida en `pickle` al jugador que grava, desxifrada, per número de mètode |

## Capçalera, resultats i comprovacions {#header-results-and-checks}

| Clau | Què és |
|---|---|
| `header` | el primer bloc JSON, tot menys la llista de jugadors: mode de joc, clima, límit del mapa, mides dels equips i més |
| `moreBlocks` | els blocs JSON després del primer, tal com són |
| `blockIds` | 15.x: el compte del jugador que grava i l'identificador de la batalla, llegits com a text |
| `results` | 15.x: els resultats, que aquests clients guarden al flux |
| `entities` | cada entitat que crea el flux: el seu número de tipus i el seu rol, quan va entrar a la vista del client i quan en va sortir |
| `selfCheck` | el recompte de completesa ([Completesa](completeness.md)) i les comprovacions de les entitats, els resultats, els identificadors i la versió |

---

Part de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentació](https://holdi601.github.io/3DHeat/)). Font: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
