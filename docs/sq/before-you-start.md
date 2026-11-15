---
title: "Para se të fillosh"
nav_order: 2
lang: sq
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Para se të fillosh {#before-you-start}

Je i ri me rreshtin e komandave? Kjo faqe të çon nga zero te një
`heat3d-wows-replay` që funksionon, për rreth dhjetë minuta. Nëse e përdor tashmë Python, shko drejt te
[Instalimi](installing.md).

## 1. Instalo Python {#install-python}

1. Shkarko Python **3.10 ose më të ri** nga
   [python.org/downloads](https://www.python.org/downloads/).
2. Në Windows, shëno **Add python.exe to PATH** në dritaren e parë të
   instaluesit, pastaj kliko **Install Now**.
3. Në macOS dhe Linux, Python 3 shpesh është tashmë aty. Shkruaj `python3`
   kudo ku këto faqe thonë `python`, dhe `pip3` në vend të `pip`.

## 2. Hap një terminal {#open-a-terminal}

Terminali është një dritare ku shkruan komanda.

- **Windows:** hap dosjen në File Explorer, kliko shiritin e adresës, shkruaj
  `cmd` dhe shtyp Enter. Hapet një dritare, tashmë në atë dosje.
- **macOS:** hap aplikacionin **Terminal**. **Linux:** kliko me të djathtën në dosje
  dhe zgjidh **Open in Terminal**.

Për të shkuar në një dosje tjetër, shkruaj `cd` dhe dosjen:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Kontrollo që Python funksionon {#check-that-python-works}

```bash
python --version
```

Duhet të shohësh `Python 3.` dhe një numër 10 ose më të madh, për shembull
`Python 3.12.4`.

## 4. Merr mjetin dhe instaloje {#get-the-tool-and-install-it}

1. Te [faqja e mjetit në GitHub](https://github.com/Holdi601/3DHeat-Ext-WoWs), kliko
   butonin e gjelbër **Code**, pastaj **Download ZIP**, dhe shpaketo zip-in.
2. Hap një terminal në dosjen e shpaketuar (atë ku ndodhet `README.md`).
3. Shkruaj:

   ```bash
   pip install -e .
   ```

   Në fund duhet të shohësh: `Successfully installed heat3d-ext-wows-0.1.0`
   (ndoshta me më shumë emra).
4. Kontrolloje:

   ```bash
   heat3d-wows-replay --version
   ```

   Duhet të shohësh: `heat3d-wows-replay 0.1.0`

## Si t'i lexosh komandat në këto faqe {#how-to-read-the-commands-on-these-pages}

- Fjalët në kllapa këndore, si `<replays>`, janë vendmbajtëse: shkruaj aty skedarin
  ose dosjen tënde, pa kllapat.
- Një shteg me hapësira ka nevojë për thonjëza: `"C:\Program Files (x86)\Steam"`.
- Teksti pas `#` është koment: nuk e shkruan.
- `-o out` shkruan në një dosje me emrin `out` brenda dosjes ku është terminali yt.
  Krijohet nëse nuk ekziston.

## Si duket suksesi {#what-success-looks-like}

Komanda printon një rresht për çdo riluajtje, për shembull:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

dhe mbaron me statusin e daljes `0`. Skedarët e rinj janë në dosjen `out`.

## Gabimet e zakonshme {#common-errors}

| Çfarë sheh | Çfarë të bësh |
|---|---|
| `'python' is not recognized ...` ose `command not found` | Python nuk është në PATH: instaloje përsëri me **Add python.exe to PATH** të shënuar, ose shkruaj `py` në vend të `python` (Windows) |
| `'pip' is not recognized ...` | shkruaj `python -m pip install -e .` në vend të tij |
| `'heat3d-wows-replay' is not recognized ...` | shkruaj `python -m heat3d_ext_wows` në vend të `heat3d-wows-replay`; bën të njëjtën gjë |
| `No module named heat3d_ext_wows` | nuk je në dosjen e mjetit, ose nuk është instaluar: bëj `cd` aty dhe nis `pip install -e .` |
| `the following arguments are required: -o/--out` | shtoje `-o out` te komanda |

Tjetra: [Konvertimi i riluajtjeve](converting.md).
