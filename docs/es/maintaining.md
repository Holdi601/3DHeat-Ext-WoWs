---
title: Mantenimiento
nav_order: 99
lang: es
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Mantenimiento de la documentación {#maintaining-the-documentation}

Para quien publica una nueva versión. Haz los pasos en este orden.

1. **Regenera las páginas de referencia** a partir del código:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # debe terminar con código 0
   ```

   Esto reescribe [Referencia de comandos](../cli-reference.md) y
   [Lista de columnas](../columns.md). No edites nunca esas dos a mano.
2. **Lista lo que cambió desde la última versión publicada:**

   ```bash
   git log --oneline v<VERSIÓN>..HEAD
   ```

   `<VERSIÓN>` es la última versión publicada (si aún no hay etiqueta: todo el
   `git log --oneline`). Cada nueva función, opción o columna necesita su página
   y una fila en la sección **Docs** de
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Revisión independiente.** Alguien que no escribió las páginas (una persona o
   un agente) lee el README, cada página y cada imagen como tres
   lectores: un principiante que nunca ha usado una terminal, un niño de 8 años, y un
   profesional que comprueba cada opción, columna y unidad frente al código. También
   comprueban los diagramas frente al código, y que ninguna página nombre un
   mapa, nivel, jugador o partida reales, ni dé cifras de repeticiones reales.
4. **Corrige lo que encontró la revisión.** Después vuelve a hacer el paso 1 y redibuja las
   imágenes cuya salida cambió.
5. **Traducciones.** Cada página de `docs/<idioma>/` registra el hash de la
   página en inglés de la que se tradujo. Vuelve a traducir cada página cuyo
   origen en inglés cambió, incluidas las etiquetas de los diagramas. Luego revisa cada
   idioma: claro para los tres lectores, etiquetas correctas, y las mismas palabras
   que usa el visor de 3DHeat en ese idioma.
6. **Publicación:** sube `VERSION` y etiqueta `v<VERSIÓN>`. **Sube los cambios solo
   con el visto bueno del propietario.**

## Traducciones: los comandos {#translations-the-commands}

El sitio está traducido a los 40 idiomas del visor de 3DHeat: el inglés en `docs/`, cada otro
idioma en `docs/<idioma>/` con los mismos nombres de archivo. `tools/docs_i18n.py` lleva el registro:

```bash
python tools/docs_i18n.py hashes             # tras cualquier cambio en inglés: registra el hash de cada página
python tools/docs_i18n.py svg-strings        # tras cualquier cambio en una imagen: las etiquetas a traducir
python tools/docs_i18n.py status             # por idioma: al día, desactualizadas, páginas que faltan
python tools/docs_i18n.py todo --lang de     # las páginas en alemán que hay que (re)traducir
python tools/docs_i18n.py svg-build --lang de    # imágenes en alemán desde docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # marca las páginas en alemán con su hash en inglés
python tools/docs_i18n.py check              # sale con 1 cuando los hashes o etiquetas están obsoletos
```

Traduce solo lo que lista `todo`: deja como están el Markdown, los enlaces, el código, los nombres de archivo
y de columna; traduce los títulos y las descripciones de las imágenes, y usa las palabras propias
del visor de 3DHeat para sus botones y paneles (en `src/i18n/locales/<idioma>/`). Las páginas de referencia
generadas y las imágenes de terminal se quedan en inglés. En el sitio, una traducción desactualizada lo indica
y enlaza la página en inglés; una que falta recurre al inglés. El menú de idiomas del
encabezado y la redirección de la página de inicio según el idioma del navegador vienen de `docs/_includes/`.
