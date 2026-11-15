---
title: Completitud
nav_order: 8
lang: "es"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Completitud {#completeness}

Nada de una repetición se descarta. Lo que lee el convertidor va a la tabla y al documento de la partida; cada otro elemento se guarda completo en el archivo auxiliar `<partida>.messages.parquet`; y el `selfCheck.completeness` del documento de la partida cuenta qué pasó con cada tipo de elemento. Es la regla que comparten todos los convertidores de 3DHeat:
[Los convertidores lo conservan todo](https://holdi601.github.io/3DHeat/converters.html).

![La autocomprobación de una repetición sintética: cada elemento visto, leído, conservado o perdido](../assets/img/completeness.svg)

## El recuento {#the-count}

Para cada tipo de elemento, `selfCheck.completeness.types` da:

| Recuento | Significa |
|---|---|
| `seen` | cuántos contiene la repetición |
| `decoded` | leídos completos |
| `partial` | leídos en parte, y guardados completos en el archivo auxiliar |
| `raw` | solo guardados completos en el archivo auxiliar, sin leer |
| `lost` | perdidos: siempre `0` |

Los tipos son los propios de la repetición: `block <n>` (los bloques JSON), los bytes propios del
contenedor, `packet <tipo>`, y para las llamadas a entidades `method <tipo de entidad>.<número>`
y `property <tipo de entidad>.<número>`. `selfCheck.entities.roles` indica qué tipo de entidad es el
avatar del jugador que graba y cuáles los barcos. Un tipo que nadie conocía aparece con su recuento.

## El archivo auxiliar {#the-sidecar}

| Columna | Qué es |
|---|---|
| `time` | el reloj de la repetición, como en la tabla |
| `type`, `name` | el tipo de elemento; cómo lo llama el convertidor, y dónde lo lee |
| `entity` | el barco o avatar al que pertenece, como `entity` de la tabla |
| `decoded` | lo que se leyó de él, como JSON |
| `payload`, `text` | sus bytes, completos; los bloques JSON, completos |
| `entityType`, `packet`, `method` | los números |

Las filas se ordenan por paquete, método, entidad y tiempo. Qué entidad es qué
jugador: `entities` y `players` del documento de la partida.

## Qué se lee, y cómo se comprobó {#what-is-read-and-how-it-was-checked}

- **Los resultados** (15.x, `results`): su id de batalla es el del flujo, y
  cada jugador de ellos está en la lista de la cabecera.
- **El bloque de ids** (15.x, `blockIds`): la cuenta y la batalla, leídas como texto para que no se pierda ningún dígito.
- **Cabeceo y balanceo** de cada posición: el balanceo va con la velocidad de giro,
  como escora un barco en un giro; el cabeceo es casi siempre 0.
- **Entidades** (`entities`): cuándo entró cada una en la vista del cliente y cuándo salió.
  Ningún barco tiene posición entre su salida y su regreso.
- **La versión del flujo** (`streamVersion`): la misma que la de la cabecera.

Todo lo demás que se lee (hundimientos, daño, vida, obuses, torpedos, dónde terminaron
los obuses, chat, llamadas en pickle, las fichas de los jugadores, posiciones) es
`partial`: va a la tabla o al documento de la partida, y se guarda completo en el
auxiliar.

**Guardado pero no leído** (`raw`), los tipos más grandes: actualizaciones de posición que no están en
la tabla (tras hundirse un barco, entidades sin jugador), las propiedades y métodos frecuentes
sin lector, las propiedades de las creaciones de entidades, y cada otro paquete sin lector.

## No disponible {#not-available}

- Lo que el servidor nunca envió al cliente que grababa: la mira, la cámara y las entradas de
  otros jugadores, los enemigos mientras no fueron detectados. Una repetición es lo que le
  dijeron a un cliente.
- Los nombres de los tipos de entidad, métodos, propiedades y las claves de las estadísticas:
  están en los archivos de definición del juego, no en la repetición. Los números se conservan.
- Los nombres de los barcos para los números de barco (usa `--ship-names`), y cualquier otra cosa
  que necesite los archivos propios del juego.
- Resultados de clientes anteriores a 15.x: sus repeticiones no los contienen.

---

Parte de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentación](https://holdi601.github.io/3DHeat/)). Código fuente: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
