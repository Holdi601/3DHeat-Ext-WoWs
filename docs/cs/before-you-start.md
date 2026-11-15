---
title: "Než začnete"
nav_order: 2
lang: "cs"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Než začnete {#before-you-start}

Nikdy jste nepracovali s příkazovým řádkem? Tato stránka vás provede od nuly
až k funkčnímu `heat3d-wows-replay` asi za deset minut. Pokud už Python používáte,
jděte rovnou na [Instalaci](installing.md).

## 1. Nainstalujte Python {#install-python}

1. Stáhněte Python **3.10 nebo novější** z
   [python.org/downloads](https://www.python.org/downloads/).
2. Na Windows zaškrtněte **Add python.exe to PATH** v prvním okně
   instalátoru a klikněte na **Install Now**.
3. Na macOS a Linuxu bývá Python 3 už nainstalovaný. Všude, kde stránky píší
   `python`, napište `python3`, a místo `pip` napište `pip3`.

## 2. Otevřete terminál {#open-a-terminal}

Terminál je okno, do kterého píšete příkazy.

- **Windows:** otevřete složku v Průzkumníkovi, klikněte na adresní řádek,
  napište `cmd` a stiskněte Enter. Otevře se okno, které je už v této složce.
- **macOS:** otevřete aplikaci **Terminál**. **Linux:** klikněte pravým tlačítkem
  do složky a zvolte **Otevřít v terminálu**.

Chcete-li přejít do jiné složky, napište `cd` a název složky:

```bash
cd "C:\Users\vy\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Ověřte, že Python funguje {#check-that-python-works}

```bash
python --version
```

Měli byste vidět `Python 3.` a číslo 10 nebo vyšší, například
`Python 3.12.4`.

## 4. Stáhněte nástroj a nainstalujte ho {#get-the-tool-and-install-it}

1. Na [GitHub stránce nástroje](https://github.com/Holdi601/3DHeat-Ext-WoWs) klikněte
   na zelené tlačítko **Code** a pak na **Download ZIP**, a zip rozbalte.
2. Otevřete terminál v rozbalené složce (té, ve které je `README.md`).
3. Napište:

   ```bash
   pip install -e .
   ```

   Na konci byste měli vidět: `Successfully installed heat3d-ext-wows-0.1.0`
   (případně s dalšími názvy).
4. Ověřte to:

   ```bash
   heat3d-wows-replay --version
   ```

   Měli byste vidět: `heat3d-wows-replay 0.1.0`

## Jak číst příkazy na těchto stránkách {#how-to-read-the-commands-on-these-pages}

- Slova v lomených závorkách, jako `<replays>`, jsou zástupné: na jejich místo
  napište svůj soubor nebo složku, bez závorek.
- Cesta s mezerami potřebuje uvozovky: `"C:\Program Files (x86)\Steam"`.
- Text za `#` je komentář: nepíšete ho.
- `-o out` zapíše do složky `out` uvnitř složky, ve které je váš terminál.
  Pokud tam není, vytvoří se.

## Jak vypadá úspěch {#what-success-looks-like}

Příkaz vypíše jeden řádek na replay, například:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

a skončí se stavem `0`. Nové soubory jsou ve složce `out`.

## Časté chyby {#common-errors}

| Co vidíte | Co dělat |
|---|---|
| `'python' is not recognized ...` nebo `command not found` | Python není v PATH: nainstalujte ho znovu se zaškrtnutým **Add python.exe to PATH**, nebo místo `python` napište `py` (Windows) |
| `'pip' is not recognized ...` | místo toho napište `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | místo `heat3d-wows-replay` napište `python -m heat3d_ext_wows`; dělá totéž |
| `No module named heat3d_ext_wows` | nejste ve složce nástroje, nebo není nainstalovaný: přejděte tam pomocí `cd` a spusťte `pip install -e .` |
| `the following arguments are required: -o/--out` | do příkazu přidejte `-o out` |

Dále: [Převod replayů](converting.md).
