---
title: "Innan du börjar"
nav_order: 2
lang: "sv"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Innan du börjar {#before-you-start}

Ny i kommandoraden? Den här sidan tar dig från noll till en fungerande
`heat3d-wows-replay` på ungefär tio minuter. Om du redan använder Python, gå
direkt till [Installera](installing.md).

## 1. Installera Python {#install-python}

1. Ladda ner Python **3.10 eller senare** från
   [python.org/downloads](https://www.python.org/downloads/).
2. På Windows, bocka i **Add python.exe to PATH** i installerarens första fönster,
   klicka sedan på **Install Now**.
3. På macOS och Linux finns Python 3 ofta redan. Skriv `python3` där sidorna
   säger `python`, och `pip3` i stället för `pip`.

## 2. Öppna en terminal {#open-a-terminal}

En terminal är ett fönster där du skriver kommandon.

- **Windows:** öppna mappen i Utforskaren, klicka i adressfältet, skriv
  `cmd` och tryck på Enter. Ett fönster öppnas, redan i den mappen.
- **macOS:** öppna appen **Terminal**. **Linux:** högerklicka i mappen och
  välj **Öppna i terminal**.

För att gå till en annan mapp skriver du `cd` och mappen:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Kontrollera att Python fungerar {#check-that-python-works}

```bash
python --version
```

Du bör se `Python 3.` och ett tal på 10 eller mer, till exempel
`Python 3.12.4`.

## 4. Hämta verktyget och installera det {#get-the-tool-and-install-it}

1. Klicka på den gröna knappen **Code** på [verktygets GitHub-sida](https://github.com/Holdi601/3DHeat-Ext-WoWs),
   sedan på **Download ZIP**, och packa upp zip-filen.
2. Öppna en terminal i den uppackade mappen (den med `README.md` i sig).
3. Skriv:

   ```bash
   pip install -e .
   ```

   Till slut bör du se: `Successfully installed heat3d-ext-wows-0.1.0`
   (kanske med fler namn).
4. Kontrollera det:

   ```bash
   heat3d-wows-replay --version
   ```

   Du bör se: `heat3d-wows-replay 0.1.0`

## Så läser du kommandona på de här sidorna {#how-to-read-the-commands-on-these-pages}

- Ord inom vinkelparenteser, som `<replays>`, är platshållare: skriv din egen fil
  eller mapp där, utan parenteserna.
- En sökväg med mellanslag behöver citattecken: `"C:\Program Files (x86)\Steam"`.
- Text efter `#` är en kommentar: den skriver du inte.
- `-o out` skriver till en mapp som heter `out` i mappen din terminal står i.
  Den skapas om den inte finns.

## Så ser en lyckad körning ut {#what-success-looks-like}

Kommandot skriver en rad per repris, till exempel:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

och avslutas med exitstatus `0`. De nya filerna finns i mappen `out`.

## Vanliga fel {#common-errors}

| Du ser | Gör så här |
|---|---|
| `'python' is not recognized ...` eller `command not found` | Python finns inte på PATH: installera om det med **Add python.exe to PATH** ibockat, eller skriv `py` i stället för `python` (Windows) |
| `'pip' is not recognized ...` | skriv `python -m pip install -e .` i stället |
| `'heat3d-wows-replay' is not recognized ...` | skriv `python -m heat3d_ext_wows` i stället för `heat3d-wows-replay`; det gör samma sak |
| `No module named heat3d_ext_wows` | du står inte i verktygets mapp, eller det är inte installerat: `cd` dit och kör `pip install -e .` |
| `the following arguments are required: -o/--out` | lägg till `-o out` i kommandot |

Nästa: [Konvertera repriser](converting.md).
