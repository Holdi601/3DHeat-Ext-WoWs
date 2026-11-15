---
title: "Prije nego počnete"
nav_order: 2
lang: bs
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Prije nego počnete {#before-you-start}

Niste navikli na komandnu liniju? Ova stranica vas vodi od nule do radnog
`heat3d-wows-replay` za oko deset minuta. Ako već koristite Python, idite direktno na
[Instalacija](installing.md).

## 1. Instalirajte Python {#install-python}

1. Preuzmite Python **3.10 ili noviji** sa
   [python.org/downloads](https://www.python.org/downloads/).
2. Na Windowsu označite **Add python.exe to PATH** u prvom prozoru
   instalera, a zatim kliknite **Install Now**.
3. Na macOS-u i Linuxu Python 3 je često već instaliran. Upišite `python3`
   svugdje gdje ove stranice kažu `python`, i `pip3` umjesto `pip`.

## 2. Otvorite terminal {#open-a-terminal}

Terminal je prozor u koji upisujete naredbe.

- **Windows:** otvorite folder u File Exploreru, kliknite na adresnu traku, upišite
  `cmd` i pritisnite Enter. Otvara se prozor, već u tom folderu.
- **macOS:** otvorite aplikaciju **Terminal**. **Linux:** kliknite desnim tasterom u folderu
  i odaberite **Open in Terminal**.

Da biste otišli u drugi folder, upišite `cd` i naziv foldera:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Provjerite radi li Python {#check-that-python-works}

```bash
python --version
```

Trebali biste vidjeti `Python 3.` i broj 10 ili veći, na primjer
`Python 3.12.4`.

## 4. Nabavite alat i instalirajte ga {#get-the-tool-and-install-it}

1. Na [GitHub stranici alata](https://github.com/Holdi601/3DHeat-Ext-WoWs) kliknite
   zeleno dugme **Code**, zatim **Download ZIP**, i raspakirajte zip.
2. Otvorite terminal u raspakiranom folderu (onom u kojem je `README.md`).
3. Upišite:

   ```bash
   pip install -e .
   ```

   Na kraju biste trebali vidjeti: `Successfully installed heat3d-ext-wows-0.1.0`
   (možda s još imena).
4. Provjerite:

   ```bash
   heat3d-wows-replay --version
   ```

   Trebali biste vidjeti: `heat3d-wows-replay 0.1.0`

## Kako čitati naredbe na ovim stranicama {#how-to-read-the-commands-on-these-pages}

- Riječi u uglastim zagradama, poput `<replays>`, su rezervirana mjesta: upišite vlastitu
  datoteku ili folder umjesto njih, bez zagrada.
- Putanja s razmacima treba navodnike: `"C:\Program Files (x86)\Steam"`.
- Tekst poslije `#` je komentar: njega ne upisujete.
- `-o out` piše u folder po imenu `out` unutar foldera u kojem je vaš terminal.
  Napravi se ako ne postoji.

## Kako izgleda uspjeh {#what-success-looks-like}

Naredba ispisuje jedan red po replayu, na primjer:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

i završava sa izlaznim statusom `0`. Nove datoteke su u folderu `out`.

## Česte greške {#common-errors}

| Šta vidite | Šta učiniti |
|---|---|
| `'python' is not recognized ...` ili `command not found` | Python nije na PATH-u: instalirajte ga ponovo s označenim **Add python.exe to PATH**, ili upišite `py` umjesto `python` (Windows) |
| `'pip' is not recognized ...` | upišite `python -m pip install -e .` umjesto toga |
| `'heat3d-wows-replay' is not recognized ...` | upišite `python -m heat3d_ext_wows` umjesto `heat3d-wows-replay`; radi isto |
| `No module named heat3d_ext_wows` | niste u folderu alata, ili nije instaliran: uđite `cd` tamo i pokrenite `pip install -e .` |
| `the following arguments are required: -o/--out` | dodajte `-o out` naredbi |

Dalje: [Pretvaranje replayeva](converting.md).
