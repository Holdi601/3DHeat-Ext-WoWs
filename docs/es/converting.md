---
title: Convertir repeticiones
nav_order: 4
lang: es
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Convertir repeticiones {#converting-replays}

## Paso a paso {#step-by-step}

1. **Activa la grabación**: `isReplayEnabled` en el `preferences.xml` del juego, o el ajuste propio del juego donde lo tenga. A partir de entonces el juego guarda cada batalla en la carpeta `replays` de tu
   instalación de World of Warships, por ejemplo
   `C:\Games\World_of_Warships_EU\replays`.
2. **Abre una terminal** en una carpeta donde puedan ir los resultados
   ([Antes de empezar](before-you-start.md)).
3. **Ejecuta el convertidor** sobre archivos de repetición, o sobre carpetas que los contienen:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` se crea en la carpeta donde está tu terminal.
4. **Lee lo que dice.** Deberías ver una línea por repetición, que termina con la
   tabla que escribió.
5. **Abre el resultado** en el visor de 3DHeat: `out/<mapa>/<partida>.parquet`
   en la pestaña Mapa de calor, `<partida>.match.json` en la pestaña Partida. O léelos
   con cualquier lector de Parquet o JSON.

![Una ejecución con una repetición sintética: convertir, volver a ejecutar, un archivo roto, una carpeta vacía](../assets/img/convert.svg)

La imagen es una ejecución sobre una repetición que las pruebas construyen en código (sin repetición real):

- una repetición convertida: `<archivo>: <n> positions of <n> ships at <frecuencia> Hz (own <frecuencia> Hz), <n> sunk, <mapa> (<versión del cliente>) -> <tabla>`;
- ejecutada de nuevo, la partida ya escrita se omite: `<archivo>: already written, <tabla>`;
- un archivo que no es una repetición: `<archivo>: not converted: <motivo>` (en la salida de errores;
  estado de salida 1, las demás repeticiones se siguen convirtiendo);
- no se encuentra ninguna repetición: `no .wowsreplay files in <carpetas>` (estado de salida 2).

## Opciones {#options}

| Opción | Por defecto | Qué hace |
|---|---|---|
| `replays` (una o más) | - | archivos `.wowsreplay`, o carpetas donde buscarlos (también subcarpetas) |
| `-o`, `--out` | obligatoria | la carpeta donde escribir: una carpeta por mapa dentro |
| `--force` | desactivada | convierte de nuevo lo que ya está escrito |
| `--ship-names JSON` | - | un archivo JSON `{"<idBarco>": "<nombre>", ...}`: las repeticiones nombran solo el barco del jugador que graba, los demás por número |
| `--version` | - | muestra `heat3d-wows-replay <versión>` y termina |
| `-h`, `--help` | - | muestra las opciones y termina |

Las opciones tal como las muestra el programa: [Referencia de comandos](../cli-reference.md).

## Qué se escribe {#what-is-written}

Solo archivos sueltos: este convertidor no escribe ningún archivo `.3dheat` (el visor puede
empaquetarlos en uno: [Un archivo por partida](https://holdi601.github.io/3DHeat/container.html)).
Por repetición, en `out/<mapa>/` (el nombre del mapa sin su `spaces/`):

| Archivo | Qué es |
|---|---|
| `<partida>.parquet` | la tabla: la posición de cada barco a lo largo del tiempo y cada evento donde ocurrió ([La tabla](table.md)) |
| `<partida>.match.json` | el documento de la partida: mapa, versión del cliente, jugadores, hundimientos, chat y todo lo demás ([El documento de la partida](match-document.md)) |
| `<partida>.messages.parquet` | el archivo auxiliar: cada elemento de la repetición que los dos archivos anteriores no contienen completo ([Completitud](completeness.md)) |

`<partida>` es el id propio de la batalla, o el nombre del archivo cuando la
grabación se detuvo antes de los resultados.

## Estado de salida {#exit-status}

`0` cuando se convirtió u omitió cada repetición, `1` cuando alguna falló (las
demás se siguen convirtiendo), `2` cuando no se encontró ningún archivo de repetición.

---

Parte de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentación](https://holdi601.github.io/3DHeat/)). Código fuente: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
