---
title: Instalación
nav_order: 3
lang: "es"
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Instalación {#installing}

¿Es tu primera vez con la línea de comandos? Lee primero [Antes de empezar](before-you-start.md).
Necesita Python 3.10 o posterior; numpy y pyarrow se instalan con él.

## Paso a paso {#step-by-step}

1. Consigue el código: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   o descarga un zip desde [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   y descomprímelo.
2. Abre una terminal en esa carpeta y escribe `pip install -e .`. Esto pone el
   comando `heat3d-wows-replay` en tu ruta de comandos.
3. Compruébalo: `heat3d-wows-replay --version`. Deberías ver
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` lista las opciones:

![heat3d-wows-replay --help](../assets/img/help.svg)

Sin instalar, `python -m heat3d_ext_wows ...` en la carpeta de la herramienta hace
lo mismo.

El Watcher de 3DHeat ejecuta este comando sobre las repeticiones nuevas cuando está instalado,
y funciona sin él.

## Actualizaciones {#updates}

Cada inicio consulta antes las versiones publicadas del proyecto en GitHub (como
mucho una petición cada pocas horas; nunca detiene una conversión, con o sin
conexión). Cuando hay una versión nueva, el comando pregunta antes de instalarla:
un `git clone` se actualiza con `git pull --ff-only` (rechazado si tienes cambios
locales), y una copia descargada, desde el archivo de la versión. `HEAT3D_NO_UPDATE=1`
desactiva la consulta y la actualización.

---

Parte de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentación](https://holdi601.github.io/3DHeat/)). Código fuente: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
