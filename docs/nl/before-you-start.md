---
title: "Voordat je begint"
nav_order: 2
lang: nl
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Voordat je begint {#before-you-start}

Nieuw met de opdrachtregel? Deze pagina brengt je van niets naar een werkende
`heat3d-wows-replay` in ongeveer tien minuten. Gebruik je al Python, ga dan meteen naar
[Installeren](installing.md).

## 1. Installeer Python {#install-python}

1. Download Python **3.10 of nieuwer** via
   [python.org/downloads](https://www.python.org/downloads/).
2. Op Windows zet je het vinkje bij **Add python.exe to PATH** in het eerste venster van de
   installatie, en klik je daarna op **Install Now**.
3. Op macOS en Linux staat Python 3 vaak al klaar. Typ `python3`
   waar deze pagina's `python` zeggen, en `pip3` in plaats van `pip`.

## 2. Open een terminal {#open-a-terminal}

Een terminal is een venster waarin je opdrachten typt.

- **Windows:** open de map in Verkenner, klik op de adresbalk, typ
  `cmd` en druk op Enter. Er opent een venster dat al in die map staat.
- **macOS:** open de app **Terminal**. **Linux:** klik met de rechtermuisknop in de map
  en kies **Openen in Terminal**.

Om naar een andere map te gaan, typ je `cd` en de map:

```bash
cd "C:\Users\jij\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Controleer of Python werkt {#check-that-python-works}

```bash
python --version
```

Je ziet `Python 3.` en een getal van 10 of hoger, bijvoorbeeld
`Python 3.12.4`.

## 4. Haal de tool op en installeer hem {#get-the-tool-and-install-it}

1. Klik op [de GitHub-pagina van de tool](https://github.com/Holdi601/3DHeat-Ext-WoWs) op de
   groene knop **Code**, daarna op **Download ZIP**, en pak het zip-bestand uit.
2. Open een terminal in de uitgepakte map (die met `README.md` erin).
3. Typ:

   ```bash
   pip install -e .
   ```

   Aan het eind zie je: `Successfully installed heat3d-ext-wows-0.1.0`
   (misschien met meer namen erbij).
4. Controleer het:

   ```bash
   heat3d-wows-replay --version
   ```

   Je ziet: `heat3d-wows-replay 0.1.0`

## Hoe je de opdrachten op deze pagina's leest {#how-to-read-the-commands-on-these-pages}

- Woorden tussen punthaken, zoals `<replays>`, zijn plaatshouders: typ daar je eigen
  bestand of map, zonder de punthaken.
- Een pad met spaties heeft aanhalingstekens nodig: `"C:\Program Files (x86)\Steam"`.
- Tekst na `#` is commentaar: die typ je niet.
- `-o out` schrijft naar een map die `out` heet, binnenin de map waarin je terminal
  staat. Die wordt gemaakt als hij er nog niet is.

## Hoe succes eruitziet {#what-success-looks-like}

De opdracht drukt één regel per replay af, bijvoorbeeld:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

en eindigt met afsluitstatus `0`. De nieuwe bestanden staan in de map `out`.

## Veelvoorkomende fouten {#common-errors}

| Je ziet | Wat je doet |
|---|---|
| `'python' is not recognized ...` of `command not found` | Python staat niet op het PATH: installeer het opnieuw met **Add python.exe to PATH** aangevinkt, of typ `py` in plaats van `python` (Windows) |
| `'pip' is not recognized ...` | typ in plaats daarvan `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | typ `python -m heat3d_ext_wows` in plaats van `heat3d-wows-replay`; dat doet hetzelfde |
| `No module named heat3d_ext_wows` | je staat niet in de map van de tool, of hij is niet geïnstalleerd: ga daarheen met `cd` en voer `pip install -e .` uit |
| `the following arguments are required: -o/--out` | voeg `-o out` toe aan de opdracht |

Volgende: [Replays omzetten](converting.md).
