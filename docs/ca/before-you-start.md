---
title: Abans de començar
nav_order: 2
lang: ca
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Abans de començar {#before-you-start}

No n'has fet mai servir la línia d'ordres? Aquesta pàgina et porta de no tenir res a tenir
`heat3d-wows-replay` a punt en uns deu minuts. Si ja fas servir Python, ves directament a
[Instal·lació](installing.md).

## 1. Instal·la Python {#install-python}

1. Descarrega Python **3.10 o posterior** de
   [python.org/downloads](https://www.python.org/downloads/).
2. A Windows, marca **Add python.exe to PATH** a la primera finestra de l'instal·lador, i després fes
   clic a **Install Now**.
3. A macOS i Linux, Python 3 sovint ja hi és. Escriu `python3` on aquestes pàgines diuen `python`, i
   `pip3` en lloc de `pip`.

## 2. Obre un terminal {#open-a-terminal}

Un terminal és una finestra on escrius ordres.

- **Windows:** obre la carpeta a l'Explorador de fitxers, fes clic a la barra d'adreces, escriu `cmd` i
  prem Enter. S'obre una finestra, ja a aquella carpeta.
- **macOS:** obre l'aplicació **Terminal**. **Linux:** fes clic dret a la carpeta i tria **Open in
  Terminal**.

Per anar a una altra carpeta, escriu `cd` i la carpeta:

```bash
cd "C:\Users\tu\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Comprova que Python funciona {#check-that-python-works}

```bash
python --version
```

Hauries de veure `Python 3.` i un número de 10 o més, per exemple `Python 3.12.4`.

## 4. Obtén l'eina i instal·la-la {#get-the-tool-and-install-it}

1. A [la pàgina de l'eina a GitHub](https://github.com/Holdi601/3DHeat-Ext-WoWs), fes clic al botó verd
   **Code** i després a **Download ZIP**, i descomprimeix el zip.
2. Obre un terminal a la carpeta descomprimida (la que té `README.md`).
3. Escriu:

   ```bash
   pip install -e .
   ```

   Al final hauries de veure: `Successfully installed heat3d-ext-wows-0.1.0` (potser amb més noms).
4. Comprova-ho:

   ```bash
   heat3d-wows-replay --version
   ```

   Hauries de veure: `heat3d-wows-replay 0.1.0`

## Com llegir les ordres d'aquestes pàgines {#how-to-read-the-commands-on-these-pages}

- Les paraules entre angles, com `<replays>`, són marcadors de posició: escriu-hi el teu fitxer o la teva
  carpeta, sense els angles.
- Un camí amb espais necessita cometes: `"C:\Program Files (x86)\Steam"`.
- El text després de `#` és un comentari: no l'escrius.
- `-o out` escriu dins d'una carpeta que es diu `out` a la carpeta on és el teu terminal. Es crea si no hi
  és.

## Com és l'èxit {#what-success-looks-like}

L'ordre escriu una línia per repetició, per exemple:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<mapa>/<partida>.parquet
```

i acaba amb l'estat de sortida `0`. Els fitxers nous són a la carpeta `out`.

## Errors habituals {#common-errors}

| Veus | Què fer |
|---|---|
| `'python' is not recognized ...` o `command not found` | Python no és al PATH: instal·la'l de nou amb **Add python.exe to PATH** marcat, o escriu `py` en lloc de `python` (Windows) |
| `'pip' is not recognized ...` | escriu `python -m pip install -e .` en lloc d'això |
| `'heat3d-wows-replay' is not recognized ...` | escriu `python -m heat3d_ext_wows` en lloc de `heat3d-wows-replay`; fa el mateix |
| `No module named heat3d_ext_wows` | no ets a la carpeta de l'eina, o no està instal·lada: fes `cd` fins allà i executa `pip install -e .` |
| `the following arguments are required: -o/--out` | afegeix `-o out` a l'ordre |

Següent: [Conversió de repeticions](converting.md).
