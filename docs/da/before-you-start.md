---
title: Før du går i gang
nav_order: 2
lang: "da"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Før du går i gang {#before-you-start}

Ny til kommandolinjen? Denne side fører dig fra ingenting til en fungerende
`heat3d-wows-replay` på ca. ti minutter. Hvis du allerede bruger Python, så gå
direkte til [Installation](installing.md).

## 1. Installer Python {#install-python}

1. Download Python **3.10 eller nyere** fra
   [python.org/downloads](https://www.python.org/downloads/).
2. På Windows skal du sætte fluebenet ved **Add python.exe to PATH** i det første
   vindue i installationsprogrammet og derefter klikke på **Install Now**.
3. På macOS og Linux er Python 3 ofte allerede installeret. Skriv `python3`,
   hvor siderne siger `python`, og `pip3` i stedet for `pip`.

## 2. Åbn en terminal {#open-a-terminal}

En terminal er et vindue, hvor du skriver kommandoer.

- **Windows:** åbn mappen i Stifinder, klik i adresselinjen, skriv `cmd` og tryk
  Enter. Et vindue åbner, allerede i den mappe.
- **macOS:** åbn appen **Terminal**. **Linux:** højreklik i mappen og vælg
  **Open in Terminal**.

For at gå til en anden mappe skriver du `cd` og mappen:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Tjek at Python virker {#check-that-python-works}

```bash
python --version
```

Du bør se `Python 3.` og et tal på 10 eller mere, for eksempel
`Python 3.12.4`.

## 4. Hent værktøjet og installer det {#get-the-tool-and-install-it}

1. Gå til [værktøjets GitHub-side](https://github.com/Holdi601/3DHeat-Ext-WoWs), klik på den grønne
   knap **Code**, derefter **Download ZIP**, og pak zip-filen ud.
2. Åbn en terminal i den udpakkede mappe (den med `README.md` i).
3. Skriv:

   ```bash
   pip install -e .
   ```

   Til sidst bør du se: `Successfully installed heat3d-ext-wows-0.1.0`
   (måske med flere navne).
4. Tjek det:

   ```bash
   heat3d-wows-replay --version
   ```

   Du bør se: `heat3d-wows-replay 0.1.0`

## Sådan læser du kommandoerne på disse sider {#how-to-read-the-commands-on-these-pages}

- Ord i spidse parenteser, som `<replays>`, er pladsholdere: skriv din egen fil
  eller mappe der, uden parenteserne.
- En sti med mellemrum skal have anførselstegn: `"C:\Program Files (x86)\Steam"`.
- Tekst efter `#` er en kommentar: den skal du ikke skrive.
- `-o out` skriver ind i en mappe ved navn `out`, som ligger i den mappe, din
  terminal står i. Den oprettes, hvis den ikke findes.

## Sådan ser succes ud {#what-success-looks-like}

Kommandoen skriver én linje pr. replay, for eksempel:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

og slutter med afslutningsstatus `0`. De nye filer ligger i mappen `out`.

## Almindelige fejl {#common-errors}

| Du ser | Det skal du gøre |
|---|---|
| `'python' is not recognized ...` eller `command not found` | Python er ikke på PATH: installer det igen med **Add python.exe to PATH** sat til, eller skriv `py` i stedet for `python` (Windows) |
| `'pip' is not recognized ...` | skriv `python -m pip install -e .` i stedet |
| `'heat3d-wows-replay' is not recognized ...` | skriv `python -m heat3d_ext_wows` i stedet for `heat3d-wows-replay`; den gør det samme |
| `No module named heat3d_ext_wows` | du står ikke i værktøjets mappe, eller det er ikke installeret: `cd` derhen og kør `pip install -e .` |
| `the following arguments are required: -o/--out` | tilføj `-o out` til kommandoen |

Næste: [Konvertering af replays](converting.md).
