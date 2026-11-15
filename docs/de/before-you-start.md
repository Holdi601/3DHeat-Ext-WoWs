---
title: Bevor du anfängst
nav_order: 2
lang: de
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Bevor du anfängst {#before-you-start}

Neu auf der Kommandozeile? Diese Seite führt dich in etwa zehn Minuten von
null bis zu einem funktionierenden `heat3d-wows-replay`. Wenn du Python schon
kennst, geh direkt zu [Installation](installing.md).

## 1. Python installieren {#install-python}

1. Lade Python **3.10 oder neuer** von
   [python.org/downloads](https://www.python.org/downloads/) herunter.
2. Unter Windows setzt du im ersten Fenster des Installers den Haken bei
   **python.exe zum PATH hinzufügen** und klickst dann auf **Jetzt installieren**.
3. Unter macOS und Linux ist Python 3 oft schon vorhanden. Wo diese Seiten
   `python` schreiben, tippst du `python3`, und statt `pip` tippst du `pip3`.

## 2. Ein Terminal öffnen {#open-a-terminal}

Ein Terminal ist ein Fenster, in das du Befehle tippst.

- **Windows:** Öffne den Ordner im Explorer, klicke in die Adressleiste, tippe
  `cmd` und drücke Enter. Ein Fenster öffnet sich, das schon in diesem Ordner ist.
- **macOS:** Öffne die App **Terminal**. **Linux:** Klicke im Ordner mit der
  rechten Maustaste und wähle **Im Terminal öffnen**.

Um in einen anderen Ordner zu wechseln, tippst du `cd` und den Ordner:

```bash
cd "C:\Users\du\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Prüfen, ob Python funktioniert {#check-that-python-works}

```bash
python --version
```

Du solltest `Python 3.` und eine Zahl von 10 oder mehr sehen, zum Beispiel
`Python 3.12.4`.

## 4. Das Werkzeug holen und installieren {#get-the-tool-and-install-it}

1. Klicke auf [der GitHub-Seite des Werkzeugs](https://github.com/Holdi601/3DHeat-Ext-WoWs)
   auf den grünen Knopf **Code** und dann auf **Download ZIP**. Entpacke die ZIP-Datei.
2. Öffne ein Terminal im entpackten Ordner (dem Ordner, in dem `README.md` liegt).
3. Tippe:

   ```bash
   pip install -e .
   ```

   Am Ende solltest du sehen: `Successfully installed heat3d-ext-wows-0.1.0`
   (vielleicht mit weiteren Namen).
4. Prüfe es:

   ```bash
   heat3d-wows-replay --version
   ```

   Du solltest sehen: `heat3d-wows-replay 0.1.0`

## So liest du die Befehle auf diesen Seiten {#how-to-read-the-commands-on-these-pages}

- Wörter in spitzen Klammern, wie `<replays>`, sind Platzhalter: Schreibe dort
  deine eigene Datei oder deinen eigenen Ordner hin, ohne die Klammern.
- Ein Pfad mit Leerzeichen braucht Anführungszeichen: `"C:\Program Files (x86)\Steam"`.
- Text nach `#` ist ein Kommentar: Den tippst du nicht.
- `-o out` schreibt in einen Ordner namens `out` im Ordner, in dem dein
  Terminal steht. Er wird angelegt, wenn er nicht da ist.

## So sieht Erfolg aus {#what-success-looks-like}

Der Befehl gibt pro Replay eine Zeile aus, zum Beispiel:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

und endet mit dem Exit-Status `0`. Die neuen Dateien liegen im Ordner `out`.

## Häufige Fehler {#common-errors}

| Du siehst | Was du tun kannst |
|---|---|
| `'python' is not recognized ...` oder `command not found` | Python ist nicht im PATH: Installiere es erneut mit gesetztem Haken bei **python.exe zum PATH hinzufügen**, oder tippe unter Windows `py` statt `python` |
| `'pip' is not recognized ...` | tippe stattdessen `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | tippe `python -m heat3d_ext_wows` statt `heat3d-wows-replay`; das macht dasselbe |
| `No module named heat3d_ext_wows` | du bist nicht im Ordner des Werkzeugs, oder es ist nicht installiert: Wechsle mit `cd` dorthin und führe `pip install -e .` aus |
| `the following arguments are required: -o/--out` | füge `-o out` zum Befehl hinzu |

Weiter: [Replays umwandeln](converting.md).
