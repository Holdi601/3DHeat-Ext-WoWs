---
title: "Ier s du ufänks"
nav_order: 2
lang: lb
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Ier s du ufänks {#before-you-start}

Nei op der Kommandozeil? Dës Säit bréngt dech a ronn zéng Minutten vun näischt zu engem
funktionéierenden `heat3d-wows-replay`. Wann s du schonn Python benotz, gëff direkt weider op
[Installéieren](installing.md).

## 1. Python installéieren {#install-python}

1. Luet Python **3.10 oder méi nei** vun
   [python.org/downloads](https://www.python.org/downloads/) erof.
2. Ënner Windows hak am éischte Fënster vum Installer **Add python.exe to PATH** un,
   dann klick op **Install Now**.
3. Ënner macOS a Linux ass Python 3 dacks schonn do. Tipp `python3`,
   wou dës Säiten `python` soen, an `pip3` fir `pip`.

## 2. E Terminal opmaachen {#open-a-terminal}

E Terminal ass e Fënster, an dat s du Befehler tippt.

- **Windows:** maach den Dossier am Datei-Explorer op, klick an d'Adressleist, tipp
  `cmd` an dréck Enter. Et geet e Fënster op, schonn an deem Dossier.
- **macOS:** maach d'**Terminal**-App op. **Linux:** klick mat der rietser Maustast am Dossier
  a wiel **Open in Terminal**.

Fir an en anere Dossier ze goen, tipp `cd` an den Dossier:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Préifen, ob Python funktionéiert {#check-that-python-works}

```bash
python --version
```

Du soll `Python 3.` gesinn an eng Zuel vun 10 oder méi, zum Beispill
`Python 3.12.4`.

## 4. D'Tool kréien an installéieren {#get-the-tool-and-install-it}

1. Klick op [der GitHub-Säit vum Tool](https://github.com/Holdi601/3DHeat-Ext-WoWs) op
   de gréngen **Code**-Knäppchen, dann op **Download ZIP**, a pak d'Zip aus.
2. Maach en Terminal am ausgepackten Dossier op (deen, an deem `README.md` ass).
3. Tipp:

   ```bash
   pip install -e .
   ```

   Um Enn soll een gesinn: `Successfully installed heat3d-ext-wows-0.1.0`
   (vläicht mat méi Nimm).
4. Préif et:

   ```bash
   heat3d-wows-replay --version
   ```

   Du soll gesinn: `heat3d-wows-replay 0.1.0`

## Wéi s du d'Befehler op dëse Säite liess {#how-to-read-the-commands-on-these-pages}

- Wierder a spitze Klammeren, wéi `<replays>`, sinn Platzhalter: tipp deng eege
  Datei oder däin eegenen Dossier do, ouni d'Klammeren.
- E Wee mat Espacen brauch Gänsefësschen: `"C:\Program Files (x86)\Steam"`.
- Text no `#` ass e Kommentar: en tipps du net.
- `-o out` schreift an en Dossier `out` am Dossier, an deem däin Terminal
  ass. Et gëtt gemaach, wann et en net gëtt.

## Wéi et ausgesäit, wann et geklappt huet {#what-success-looks-like}

De Befehl dréckt eng Zeil pro Replay, zum Beispill:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

an endet mam Exit-Status `0`. Déi nei Dateie sinn am Dossier `out`.

## Heefeg Feeler {#common-errors}

| Du gesäis | Wat maachen |
|---|---|
| `'python' is not recognized ...` oder `command not found` | Python ass net am PATH: installéier et nach eng Kéier mat ugehaakt **Add python.exe to PATH**, oder tipp `py` amplaz `python` (Windows) |
| `'pip' is not recognized ...` | tipp amplaz `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | tipp `python -m heat3d_ext_wows` amplaz `heat3d-wows-replay`; et mécht datselwecht |
| `No module named heat3d_ext_wows` | du bass net am Dossier vum Tool, oder et ass net installéiert: `cd` dohin a féier `pip install -e .` aus |
| `the following arguments are required: -o/--out` | setz `-o out` bei de Befehl derbäi |

Duerno: [Replays émwandelen](converting.md).
