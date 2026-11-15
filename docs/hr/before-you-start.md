---
title: Prije početka
nav_order: 2
lang: "hr"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Prije početka {#before-you-start}

Nikad nisi koristio naredbeni redak? Ova stranica te vodi od nule do radnog
`heat3d-wows-replay` za oko deset minuta. Ako već koristiš Python, idi ravno na
[Instalaciju](installing.md).

## 1. Instaliraj Python {#install-python}

1. Preuzmi Python **3.10 ili noviji** s [python.org/downloads](https://www.python.org/downloads/).
2. Na Windowsu u prvom prozoru instalacijskog programa označi **Add python.exe to PATH**,
   pa klikni **Install Now**.
3. Na macOS-u i Linuxu Python 3 je često već instaliran. Na mjestima gdje ove stranice pišu
   `python`, upiši `python3`, a umjesto `pip` upiši `pip3`.

## 2. Otvori terminal {#open-a-terminal}

Terminal je prozor u koji upisuješ naredbe.

- **Windows:** otvori mapu u File Exploreru, klikni na adresnu traku, upiši
  `cmd` i pritisni Enter. Otvara se prozor koji je već u toj mapi.
- **macOS:** otvori aplikaciju **Terminal**. **Linux:** desnom tipkom klikni u mapi
  i odaberi **Open in Terminal**.

Za odlazak u drugu mapu upiši `cd` i naziv mape:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Provjeri radi li Python {#check-that-python-works}

```bash
python --version
```

Trebao bi vidjeti `Python 3.` i broj 10 ili veći, na primjer
`Python 3.12.4`.

## 4. Preuzmi alat i instaliraj ga {#get-the-tool-and-install-it}

1. Na [GitHub stranici alata](https://github.com/Holdi601/3DHeat-Ext-WoWs) klikni
   zeleni gumb **Code**, zatim **Download ZIP**, pa raspakiraj zip.
2. Otvori terminal u raspakiranoj mapi (onoj u kojoj je `README.md`).
3. Upiši:

   ```bash
   pip install -e .
   ```

   Na kraju bi trebao vidjeti: `Successfully installed heat3d-ext-wows-0.1.0`
   (možda s još nekim nazivima).
4. Provjeri:

   ```bash
   heat3d-wows-replay --version
   ```

   Trebao bi vidjeti: `heat3d-wows-replay 0.1.0`

## Kako čitati naredbe na ovim stranicama {#how-to-read-the-commands-on-these-pages}

- Riječi u šiljastim zagradama, poput `<replays>`, su mjesta za upis: upiši svoju datoteku ili
  mapu bez zagrada.
- Put s razmacima treba navodnike: `"C:\Program Files (x86)\Steam"`.
- Tekst iza `#` je komentar: ne upisuješ ga.
- `-o out` zapisuje u mapu `out` unutar mape u kojoj je tvoj terminal.
  Ona se napravi ako ne postoji.

## Kako izgleda uspjeh {#what-success-looks-like}

Naredba ispiše jedan redak po snimci, na primjer:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

i završi sa statusom izlaza `0`. Nove datoteke su u mapi `out`.

## Česte greške {#common-errors}

| Vidiš | Što učiniti |
|---|---|
| `'python' is not recognized ...` ili `command not found` | Python nije u PATH-u: instaliraj ga ponovo s uključenim **Add python.exe to PATH**, ili na Windowsu upiši `py` umjesto `python` |
| `'pip' is not recognized ...` | upiši `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | upiši `python -m heat3d_ext_wows` umjesto `heat3d-wows-replay`; radi isto |
| `No module named heat3d_ext_wows` | nisi u mapi alata ili nije instaliran: `cd` u tu mapu i pokreni `pip install -e .` |
| `the following arguments are required: -o/--out` | dodaj `-o out` u naredbu |

Sljedeće: [Pretvaranje snimki](converting.md).
