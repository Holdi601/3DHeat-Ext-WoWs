---
title: Enne alustamist
nav_order: 2
lang: "et"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Enne alustamist {#before-you-start}

Uus käsurea kasutamisel? See leht viib sind nullist töötava `heat3d-wows-replay` käsuni umbes kümne minutiga.
Kui kasutad juba Pythonit, mine otse lehele [Paigaldamine](installing.md).

## 1. Paigalda Python {#install-python}

1. Laadi alla Python **3.10 või uuem** lehelt
   [python.org/downloads](https://www.python.org/downloads/).
2. Windowsis märgi paigaldaja esimeses aknas **Add python.exe to PATH**, seejärel klõpsa **Install Now**.
3. macOS-is ja Linuxis on Python 3 sageli juba olemas. Kirjuta `python3` kohas, kus need lehed ütlevad `python`,
   ja `pip3` kohas, kus ütlevad `pip`.

## 2. Ava terminal {#open-a-terminal}

Terminal on aken, kuhu kirjutad käske.

- **Windows:** ava kaust Failihalduris, klõpsa aadressiribal, kirjuta `cmd` ja vajuta Enter. Avaneb aken,
  mis on juba selles kaustas.
- **macOS:** ava rakendus **Terminal**. **Linux:** tee kaustas parem klõps ja vali **Open in Terminal**.

Teise kausta minemiseks kirjuta `cd` ja kausta nimi:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Kontrolli, et Python töötab {#check-that-python-works}

```bash
python --version
```

Peaksid nägema `Python 3.` ja numbrit 10 või suuremat, näiteks `Python 3.12.4`.

## 4. Hangi tööriist ja paigalda see {#get-the-tool-and-install-it}

1. Tööriista GitHubi lehel ([tööriista GitHubi leht](https://github.com/Holdi601/3DHeat-Ext-WoWs)) klõpsa rohelist
   nuppu **Code**, seejärel **Download ZIP**, ja paki zip lahti.
2. Ava terminal lahtipakitud kaustas (see, kus on `README.md`).
3. Kirjuta:

   ```bash
   pip install -e .
   ```

   Lõpus peaksid nägema: `Successfully installed heat3d-ext-wows-0.1.0` (võib olla ka rohkem nimesid).
4. Kontrolli seda:

   ```bash
   heat3d-wows-replay --version
   ```

   Peaksid nägema: `heat3d-wows-replay 0.1.0`

## Kuidas lugeda neid lehti käske {#how-to-read-the-commands-on-these-pages}

- Sõnad nurksulgudes, näiteks `<replays>`, on kohatäiteid: kirjuta sinna oma fail või kaust ilma nurksulgudeta.
- Tee, millel on tühikuid, vajab jutumärke: `"C:\Program Files (x86)\Steam"`.
- Tekst pärast `#` on kommentaar: seda sa ei kirjuta.
- `-o out` kirjutab kausta nimega `out`, mis on sinu terminali kaustas. Kui seda seal ei ole, luuakse see.

## Mis tähendab edu {#what-success-looks-like}

Käsk prindib ühe rea iga kordus kohta, näiteks:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

ja lõpeb väljumisolekuga `0`. Uued failid on kaustas `out`.

## Levinud vead {#common-errors}

| Mida näed | Mida teha |
|---|---|
| `'python' is not recognized ...` või `command not found` | Python ei ole PATH-is: paigalda see uuesti, märkides **Add python.exe to PATH**, või kirjuta `python` asemel `py` (Windows) |
| `'pip' is not recognized ...` | kirjuta selle asemel `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | kirjuta `heat3d-wows-replay` asemel `python -m heat3d_ext_wows`; see teeb sama |
| `No module named heat3d_ext_wows` | sa ei ole tööriista kaustas või seda pole paigaldatud: mine sinna `cd`-käsuga ja käivita `pip install -e .` |
| `the following arguments are required: -o/--out` | lisa käsule `-o out` |

Järgmine: [Kordustete konverteerimine](converting.md).
