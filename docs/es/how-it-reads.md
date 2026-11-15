---
title: Cómo lee una repetición
nav_order: 7
lang: es
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Cómo lee una repetición {#how-it-reads-a-replay}

Una repetición es una cabecera de bloques JSON y el flujo de paquetes del juego (notas sobre el formato
en [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- El primer bloque, en claro: el mapa, la versión del cliente, el jugador que graba y su barco, y la
  lista - el nombre de cada jugador, aliado o enemigo, y su número de barco. Los clientes nuevos
  (15.x) añaden dos bloques más: uno vacío, y la cuenta del jugador que graba y el id de la
  batalla como texto, leídos en `blockIds`. Los resultados no están en el JSON; en 15.x
  van en el flujo.
- El flujo de paquetes, comprimido con zlib y cifrado con Blowfish con una clave que trae el
  juego, que las herramientas de la comunidad que leen estos archivos han publicado. Descifrado, contiene:
  - las actualizaciones de posición del motor de cada barco que el cliente podía ver (su
    propio equipo todo el tiempo, los enemigos mientras están detectados o cerca),
    varias veces por segundo mientras se mueven y con menos frecuencia cuando no;
  - el barco propio del jugador que graba en un paquete propio, unas siete veces
    por segundo;
  - una vez, al principio, las fichas de los jugadores como una lista de Python en pickle. Dicen
    qué entidad del flujo es cada jugador. Sus claves están numeradas, y los números cambian con
    los parches, así que el lector encuentra las claves por sus valores: la clave que contiene los
    nombres de la lista, y la clave que contiene las entidades con actualizaciones de posición;
  - la llamada del servidor que avisa al cliente de que un barco se ha hundido: víctima, asesino,
    causa. Se encuentra por su forma (doce bytes; los dos primeros son entidades de barco; cada
    víctima aparece una vez), no por su número;
  - el daño de cada barco: una lista de (atacante, daño) por impacto, en el barco alcanzado; y su
    vida, una propiedad que se fija un momento antes;
  - cada salva de obuses y de torpedos de las que se avisó al cliente: el tipo de obús, el tirador, la
    salva, y el inicio y la velocidad de cada obús o torpedo;
  - dónde terminaron los obuses: el tirador, un tipo de impacto, y el lugar de cada uno (en clientes
    15.x con más datos sobre el obús donde impactó, que se omiten);
  - el chat: remitente, canal, línea;
  - llamadas en pickle al jugador que graba: sus estadísticas de daño, actualizaciones de las
    fichas de los jugadores, el estado de la batalla;
  - en clientes 15.x, los resultados de la batalla al final: un paquete propio, un objeto JSON con el
    id de la batalla, leído completo en `results` del documento de la partida (las listas propias
    del juego, sin nombrar: `commonList`, `privateDataList`, `playersPublicInfo` por cuenta, ...).

Los números de paquete y de método que difieren entre las versiones comprobadas (el paquete del
barco propio es el 43 o el 44, la llamada de hundimiento el 76 u 83, los obuses el 101, 102,
126 o 127) se encuentran todos por la forma - véase
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - así que un
parche que los renumere no vacía la tabla. Los números encontrados están en el `decoded` del
documento de la partida.

**El pickle no es de confianza.** Una repetición es un archivo de cualquier procedencia, y un
pickle puede nombrar código para ejecutar. Se carga con un deserializador que da a cada clase o
función que nombra el pickle un sustituto inerte, así que construye solo datos planos y nada más. Una prueba le
da un pickle que llama a `os.system`.

**Los hundimientos** tienen la hora exacta de la llamada. Su lugar es donde se vio por última vez a
la víctima, cuando eso fue a menos de cinco segundos. **El inicio de la batalla** es el primer
instante en que se mueve algún barco (los barcos están quietos en la cuenta atrás).

Todo lo que no es una fila de la tabla está en [el documento de la partida](match-document.md).

**Lo que se le dijo al cliente** está completo para su propio equipo y parcial para
los enemigos: sus disparos, impactos y vida están mientras estuvieron al alcance.

**No se lee:**

- Aviones y sus escuadrillas (las llamadas que los llevan no se desarmaron), las actualizaciones
  de visión del minimapa (empaquetadas), la detección, las cintas, los incendios e inundaciones como
  eventos propios (su daño está en los impactos), los consumibles, los puntos de captura y las
  puntuaciones de equipo (propiedades de entidades sin definición, que no se distinguen por la forma),
  el resto de las propiedades de un barco (puntería, timón, ajuste de velocidad...).
- Los números clave de las fichas de los jugadores y de las estadísticas de daño como nombres: el juego
  los numera, y los números cambian; se conservan como números.
- Los datos extra de un obús donde impactó (15.x) y los bytes tras el inicio y la velocidad de un
  obús o torpedo.
- Resultados de clientes anteriores a 15.x: sus repeticiones no los traen.
- El número de barco como nombre: los nombres están en los archivos de parámetros propios del juego,
  no en la repetición.

## Cómo se comprobó la lectura {#how-the-reading-was-checked}

La lectura se comprobó con repeticiones públicas de clientes desde la 0.9 hasta la 15.x, cada
valor frente a algo que la repetición da por una segunda vía:

- **Posiciones:** la entidad de cada barco coincidió con un nombre de la lista; los rumbos coinciden con la
  dirección de avance a menos de 0,1 rad; tras su hundimiento, un barco se mueve menos de 0,1 unidades.
  Un barco quieto se actualiza con menos frecuencia.
- **Vida:** cada barco hundido dentro de la vista del cliente termina con vida 0.
  Cerca de la mitad de todos los impactos coinciden con una caída de vida en el segundo anterior; el
  resto caen junto con reparaciones u otros impactos.
- **Daño frente a las estadísticas propias del juego:** en el cliente más nuevo, el daño leído del
  jugador que graba está a menos del 0,1 % de las estadísticas. En los clientes más antiguos las
  estadísticas son más altas: al cliente no se le envía cada impacto, o las estadísticas cuentan
  más que los impactos (sin resolver).
- **Obuses:** un obús empieza a unas pocas unidades de la última posición conocida de su barco
  (los cañones están repartidos a lo largo del casco); casi el final de cada obús sigue,
  en menos de un minuto, a un disparo que vio el cliente.

Los tests construyen repeticiones con la misma disposición, así que en este repositorio no se guarda
ninguna repetición real.

**No comprobado:** clientes anteriores a 0.9.6, el cliente de Lesta (Mir Korabley),
operaciones y escenarios más allá de uno, batallas de clan y clasificatorias, y
qué número de barco es qué barco.

---

Parte de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentación](https://holdi601.github.io/3DHeat/)). Código fuente: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
