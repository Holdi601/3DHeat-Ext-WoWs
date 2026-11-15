---
title: Manteniment
nav_order: 99
lang: ca
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Manteniment de la documentació {#maintaining-the-documentation}

Per a qui publica una versió nova. Fes els passos en aquest ordre.

1. **Regenera les pàgines de referència** a partir del codi:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # ha de sortir amb 0
   ```

   Això reescriu [Referència d'ordres](../cli-reference.md) i [Llista de columnes](../columns.md). Mai no edites
   aquestes dues a mà.
2. **Llista què ha canviat des de l'última versió:**

   ```bash
   git log --oneline v<VERSIÓ>..HEAD
   ```

   `<VERSIÓ>` és l'última versió publicada (si encara no hi ha etiqueta: tot el `git log --oneline`). Cada
   funció, opció o columna nova necessita la seva pàgina i una fila a la secció **Docs** de
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Revisió independent.** Algú que no ha escrit les pàgines (una persona o un agent) llegeix el README,
   cada pàgina i cada imatge com a tres lectors: un principiant que mai no ha fet servir un terminal, un nen
   de vuit anys, i una professional que comprova cada opció, columna i unitat amb el codi. També comproven els
   diagrames amb el codi, i que cap pàgina no nomeni un mapa, nivell, jugador o partida reals, ni doni xifres
   de repeticions reals.
4. **Corregeix el que ha trobat la revisió.** Després torna a fer el pas 1 i redibuixa les imatges els
   resultats de les quals han canviat.
5. **Traduccions.** Cada pàgina sota `docs/<idioma>/` guarda el hash de la pàgina anglesa des de la qual es va
   traduir. Torna a traduir cada pàgina el text anglès de la qual ha canviat, amb les etiquetes dels diagrames
   incloses. Després revisa cada idioma: clar per als tres lectors, les etiquetes bé, i les mateixes paraules
   que fa servir el visualitzador de 3DHeat en aquell idioma.
6. **Publicació:** puja `VERSION` i etiqueta `v<VERSIÓ>`. **Puja només amb el vistiplau del propietari.**

## Traduccions: les ordres {#translations-the-commands}

El lloc està traduït als 40 idiomes del visualitzador de 3DHeat: l'anglès a `docs/`, cada altre idioma a
`docs/<idioma>/` amb els mateixos noms de fitxer. `tools/docs_i18n.py` fa la comptabilitat:

```bash
python tools/docs_i18n.py hashes             # després de qualsevol canvi en anglès: registra el hash de cada pàgina
python tools/docs_i18n.py svg-strings        # després de qualsevol canvi en una imatge: les etiquetes a traduir
python tools/docs_i18n.py status             # per idioma: al dia, desfasades, pàgines que falten
python tools/docs_i18n.py todo --lang de     # les pàgines en alemany a (re)traduir
python tools/docs_i18n.py svg-build --lang de    # imatges en alemany a partir de docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # marca les pàgines en alemany amb el hash de l'anglès
python tools/docs_i18n.py check              # surt amb 1 quan els hashes o les etiquetes estan desfasats
```

Tradueix només el que llista `todo`: mantén el Markdown, els enllaços, el codi i els noms de fitxers i de
columnes tal com són, tradueix els títols i les descripcions de les imatges, i fes servir les paraules pròpies
del visualitzador de 3DHeat per als seus botons i panells (el seu `src/i18n/locales/<idioma>/`). Les pàgines de
referència generades i les imatges de terminal es queden en anglès. Al lloc, una traducció desfasada ho diu i
enllaça la pàgina anglesa; una que falta torna a l'anglès. El menú d'idiomes de la capçalera i la redirecció per
idioma del navegador a la pàgina d'inici surten de `docs/_includes/`.
