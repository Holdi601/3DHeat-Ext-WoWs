---
title: El documento de la partida
nav_order: 6
lang: es
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# El documento de la partida {#the-match-document}

`<partida>.match.json` contiene todo lo que dice la repetición y que no es una fila de la
tabla. La pestaña Partida del visor lo lee. (El código lo llama el resumen.)

![El inicio de un documento de la partida sintético, y sus claves](../assets/img/match-document.svg)

## La batalla {#the-battle}

| Clave | Qué es |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; el id de la batalla; el mapa tal como lo nombra el juego (`spaces/<mapa>`) y su nombre para mostrar |
| `clientVersion`, `streamVersion` | la versión del juego según la cabecera, y tal como la indica el flujo de paquetes |
| `recorded` | cuándo se grabó la repetición, tal como lo escribe el juego |
| `player`, `vehicle` | el jugador que graba y su barco |
| `gameType`, `scenario` | el tipo de batalla (`RandomBattle`, ...) y el escenario, según la cabecera |
| `duration` | el límite de tiempo de la batalla en segundos, según la cabecera |
| `truncated` | la grabación se detuvo antes |
| `battleStart`, `recordingSeconds` | el inicio de la batalla (el primer instante en que se mueve cualquier barco) y la duración de la grabación, en segundos |
| `positionPacket`, `ownPositionPacket` | los números de paquete por los que llegaron las posiciones: las de otros barcos, las del jugador que graba |
| `deathMethod` | el número de método en el que se encontraron los hundimientos |
| `hz`, `ownHz`, `positions` | muestras por segundo de otros barcos y del barco propio; filas de posición |
| `units` | unidades de mundo (15 m según los cascos, 30 m según los alcances del juego); x este, y arriba, z norte |
| `events` | el número de filas de la tabla de cada evento |
| `decoded` | los números de método y de paquete encontrados para cada tipo de mensaje |

## Jugadores y eventos {#players-and-events}

| Clave | Qué es |
|---|---|
| `players` | una entrada por barco: nombre, `ally` o `enemy`, número y nombre del barco, entidad, muestras, bajas, sobrevivió; `seen` (daño causado y recibido, obuses, torpedos y última vida que vio el cliente); `header` (la entrada de la lista) y `record` (la ficha del jugador en el flujo, por número de clave) |
| `kills` | cada hundimiento: hora, víctima, asesino, número de causa, lugar |
| `chat` | cada línea de chat, con canal y remitente |
| `damageStats` | las estadísticas propias del jugador que graba, tal como las lleva el juego: por arma y tipo, un recuento y una cantidad (el tipo 0 es el daño causado) |
| `avatarPickles` | cada llamada en pickle al jugador que graba, decodificada, por número de método |

## Cabecera, resultados y comprobaciones {#header-results-and-checks}

| Clave | Qué es |
|---|---|
| `header` | el primer bloque JSON, todo menos la lista: modo de juego, clima, borde del mapa, tamaños de equipo y más |
| `moreBlocks` | los bloques JSON tras el primero, tal como están |
| `blockIds` | 15.x: la cuenta del jugador que graba y el id de la batalla, leídos como texto |
| `results` | 15.x: los resultados, que estos clientes guardan en el flujo |
| `entities` | cada entidad que crea el flujo: su número de tipo y su papel, cuándo entró en la vista del cliente y cuándo salió |
| `selfCheck` | el recuento de completitud ([Completitud](completeness.md)) y las comprobaciones de las entidades, los resultados, los ids y la versión |

---

Parte de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentación](https://holdi601.github.io/3DHeat/)). Código fuente: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
