---
title: "Áður en þú byrjar"
nav_order: 2
lang: "is"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Áður en þú byrjar {#before-you-start}

Hefurðu aldrei notað skipanalínu? Þessi síða fer með þig frá engu að virkri
`heat3d-wows-replay` á um tíu mínútum. Ef þú notar Python nú þegar skaltu fara beint í
[Uppsetning](installing.md).

## 1. Settu upp Python {#install-python}

1. Sæktu Python **3.10 eða nýrra** á
   [python.org/downloads](https://www.python.org/downloads/).
2. Í Windows skaltu haka við **Add python.exe to PATH** í fyrsta glugga
   uppsetningarforritsins og smella svo á **Install Now**.
3. Í macOS og Linux er Python 3 oft þegar til staðar. Skrifaðu `python3`
   þar sem þessar síður segja `python`, og `pip3` fyrir `pip`.

## 2. Opnaðu skipanalínu {#open-a-terminal}

Skipanalína (terminal) er gluggi þar sem þú skrifar skipanir.

- **Windows:** opnaðu möppuna í File Explorer, smelltu á vistfangastikuna,
  skrifaðu `cmd` og ýttu á Enter. Gluggi opnast, þegar í þeirri möppu.
- **macOS:** opnaðu forritið **Terminal**. **Linux:** hægrismelltu í möppunni
  og veldu **Open in Terminal**.

Til að fara í aðra möppu skaltu skrifa `cd` og möppuna:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Athugaðu hvort Python virkar {#check-that-python-works}

```bash
python --version
```

Þú ættir að sjá `Python 3.` og tölu sem er 10 eða hærri, til dæmis
`Python 3.12.4`.

## 4. Náðu í verkfærið og settu það upp {#get-the-tool-and-install-it}

1. Á [GitHub-síðu verkfærisins](https://github.com/Holdi601/3DHeat-Ext-WoWs) skaltu smella á
   græna hnappinn **Code**, svo á **Download ZIP**, og pakka zip-skránni upp.
2. Opnaðu skipanalínu í möppunni sem þú pakkaðir upp (þeirri sem hefur `README.md`).
3. Skrifaðu:

   ```bash
   pip install -e .
   ```

   Þú ættir að sjá í lokin: `Successfully installed heat3d-ext-wows-0.1.0`
   (kannski með fleiri nöfnum).
4. Athugaðu það:

   ```bash
   heat3d-wows-replay --version
   ```

   Þú ættir að sjá: `heat3d-wows-replay 0.1.0`

## Hvernig á að lesa skipanirnar á þessum síðum {#how-to-read-the-commands-on-these-pages}

- Orð í oddsvigum, eins og `<replays>`, eru staðgenglar: skrifaðu þína eigin
  skrá eða möppu þar, án oddsviganna.
- Slóð með bilum þarf gæsalappir: `"C:\Program Files (x86)\Steam"`.
- Texti á eftir `#` er athugasemd: þú skrifar hann ekki.
- `-o out` skrifar í möppu sem heitir `out` inni í möppunni sem skipanalínan
  þín er í. Hún er búin til ef hún er ekki til.

## Hvernig árangur lítur út {#what-success-looks-like}

Skipunin prentar eina línu fyrir hverja upptöku, til dæmis:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

og endar með útgöngustöðuna `0`. Nýju skrárnar eru í möppunni `out`.

## Algengar villur {#common-errors}

| Þú sérð | Hvað á að gera |
|---|---|
| `'python' is not recognized ...` eða `command not found` | Python er ekki í PATH: settu það upp aftur með **Add python.exe to PATH** hakað, eða skrifaðu `py` í stað `python` (Windows) |
| `'pip' is not recognized ...` | skrifaðu `python -m pip install -e .` í staðinn |
| `'heat3d-wows-replay' is not recognized ...` | skrifaðu `python -m heat3d_ext_wows` í stað `heat3d-wows-replay`; það gerir það sama |
| `No module named heat3d_ext_wows` | þú ert ekki í möppu verkfærisins, eða það er ekki uppsett: farðu þangað með `cd` og keyrðu `pip install -e .` |
| `the following arguments are required: -o/--out` | bættu `-o out` við skipunina |

Næst: [Upptökum breytt](converting.md).
