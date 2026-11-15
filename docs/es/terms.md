---
title: Términos y licencia
nav_order: 9
lang: "es"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Términos y licencia {#terms-and-licence}

## Los términos de Wargaming {#wargamings-terms}

Leído el 2026-11-07, EULA de Wargaming versión 14 (vigente desde el 10 de abril de 2024, figura
como la actual); su sección 12.3 remite a una política de mods de World of Warships, cuya
página no se mostró fuera de un navegador y no se leyó:

- 5.3 (b): unless authorised in writing, you must not "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): prohibited is "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Lo que hace este convertidor: lee un archivo que escribió el juego, después de la batalla,
fuera del juego. No cambia nada del juego, no habla con ningún servidor, y no muestra nada
durante una batalla. Sí descifra el flujo con la clave del juego, que se puede leer como
cubierta por 5.3 (b) y 12.1 (p). Usarlo es decisión del usuario; por eso es un paquete aparte.

## Licencia y fuentes {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Necesita numpy (BSD-3-Clause) y pyarrow
(Apache-2.0). Escrito para este proyecto: el cifrado Blowfish de aquí es propio,
con sus tablas calculadas a partir de los dígitos de pi tal como las define el cifrado.
Los datos sobre el formato son conocimiento común entre las herramientas de repeticiones; la nota
de escala de unidades procede de landaire/wows-toolkit (MIT). No se tomó código de ningún otro
proyecto.

`bigworld.py` y `table.py` son los mismos archivos que en el convertidor de World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); cámbialos siempre en los dos a la vez.

---

Parte de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentación](https://holdi601.github.io/3DHeat/)). Código fuente: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
