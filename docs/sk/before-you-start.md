---
title: "Než začnete"
nav_order: 2
lang: sk
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Než začnete {#before-you-start}

Ste noví v príkazovom riadku? Táto stránka vás za asi desať minút dovedie od
nuly k funkčnému `heat3d-wows-replay`. Ak už Python používate, choďte rovno na
[Inštaláciu](installing.md).

## 1. Nainštalujte Python {#install-python}

1. Stiahnite si Python **3.10 alebo novší** z
   [python.org/downloads](https://www.python.org/downloads/).
2. Vo Windows zaškrtnite **Add python.exe to PATH** v prvom okne inštalátora,
   potom kliknite na **Install Now**.
3. Na macOS a Linuxe bývá Python 3 už nainštalovaný. Všade, kde tieto stránky
   píšu `python`, napíšte `python3`, a namiesto `pip` napíšte `pip3`.

## 2. Otvorte terminál {#open-a-terminal}

Terminál je okno, do ktorého píšete príkazy.

- **Windows:** otvorte priečinok v Prieskumníkovi, kliknite na adresný riadok,
  napíšte `cmd` a stlačte Enter. Otvorí sa okno, ktoré je už v tom priečinku.
- **macOS:** otvorte aplikáciu **Terminal**. **Linux:** kliknite pravým tlačidlom
  v priečinku a zvoľte **Otvoriť v termináli**.

Ak chcete ísť do iného priečinka, napíšte `cd` a názov priečinka:

```bash
cd "C:\Users\vy\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Skontrolujte, že Python funguje {#check-that-python-works}

```bash
python --version
```

Mali by ste vidieť `Python 3.` a číslo 10 alebo vyššie, napríklad
`Python 3.12.4`.

## 4. Stiahnite nástroj a nainštalujte ho {#get-the-tool-and-install-it}

1. Na [GitHub stránke nástroja](https://github.com/Holdi601/3DHeat-Ext-WoWs) kliknite
   na zelené tlačidlo **Code**, potom na **Download ZIP**, a zip rozbaľte.
2. Otvorte terminál v rozbalenom priečinku (tom, v ktorom je `README.md`).
3. Napíšte:

   ```bash
   pip install -e .
   ```

   Na konci by ste mali vidieť: `Successfully installed heat3d-ext-wows-0.1.0`
   (možno s ďalšími názvami).
4. Skontrolujte to:

   ```bash
   heat3d-wows-replay --version
   ```

   Mali by ste vidieť: `heat3d-wows-replay 0.1.0`

## Ako čítať príkazy na týchto stránkach {#how-to-read-the-commands-on-these-pages}

- Slová v lomených zátvorkách, napríklad `<replays>`, sú zástupné znaky: napíšte
  tam svoj súbor alebo priečinok bez zátvoriek.
- Cesta s medzerami potrebuje úvodzovky: `"C:\Program Files (x86)\Steam"`.
- Text za `#` je komentár: nepíšete ho.
- `-o out` zapíše do priečinka `out`, ktorý je vnútri priečinka, v ktorom je
  váš terminál. Ak neexistuje, vytvorí sa.

## Ako vyzerá úspech {#what-success-looks-like}

Príkaz vypíše jeden riadok na každý replay, napríklad:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

a skončí s návratovým stavom `0`. Nové súbory sú v priečinku `out`.

## Bežné chyby {#common-errors}

| Čo vidíte | Čo urobiť |
|---|---|
| `'python' is not recognized ...` alebo `command not found` | Python nie je v PATH: nainštalujte ho znova so zaškrtnutým **Add python.exe to PATH**, alebo napíšte `py` namiesto `python` (Windows) |
| `'pip' is not recognized ...` | napíšte namiesto toho `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | napíšte `python -m heat3d_ext_wows` namiesto `heat3d-wows-replay`; robí to isté |
| `No module named heat3d_ext_wows` | nie ste v priečinku nástroja, alebo nie je nainštalovaný: `cd` do neho a spustite `pip install -e .` |
| `the following arguments are required: -o/--out` | pridajte do príkazu `-o out` |

Ďalej: [Konverzia replayov](converting.md).
