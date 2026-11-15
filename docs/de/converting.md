---
title: Replays umwandeln
nav_order: 4
lang: "de"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Replays umwandeln {#converting-replays}

## Schritt für Schritt {#step-by-step}

1. **Aufnahme im Spiel einschalten**: `isReplayEnabled` in der `preferences.xml` des Spiels,
   oder die eigene Einstellung des Spiels, wo es eine gibt. Von da an speichert das Spiel jedes
   Gefecht im Ordner `replays` deiner World-of-Warships-Installation, zum Beispiel
   `C:\Games\World_of_Warships_EU\replays`.
2. **Ein Terminal öffnen** in einem Ordner, in den die Ergebnisse gelegt werden dürfen
   ([Bevor du anfängst](before-you-start.md)).
3. **Den Umwandler starten** mit Replay-Dateien oder mit Ordnern, die sie enthalten:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` wird in dem Ordner angelegt, in dem dein Terminal steht.
4. **Lies, was er meldet.** Du solltest pro Replay eine Zeile sehen, die mit der Tabelle endet,
   die geschrieben wurde.
5. **Öffne das Ergebnis** im 3DHeat-Viewer: `out/<map>/<match>.parquet` im Reiter Heatmap,
   `<match>.match.json` im Reiter Match. Oder lies sie mit einem beliebigen Parquet- oder JSON-Leser.

![Ein Lauf mit einem synthetischen Replay: Umwandeln, erneutes Starten, eine defekte Datei, ein leerer Ordner](../assets/img/convert.svg)

Das Bild zeigt einen Lauf mit einem Replay, das die Tests im Code erzeugen (kein echtes Replay):

- ein Replay umgewandelt: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- erneut gestartet, wird das schon geschriebene Match übersprungen: `<file>: already written, <table>`;
- eine Datei, die kein Replay ist: `<file>: not converted: <why>` (in der Fehlerausgabe; Exit-Status 1, die anderen Replays werden trotzdem umgewandelt);
- kein Replay gefunden: `no .wowsreplay files in <folders>` (Exit-Status 2).

## Optionen {#options}

| Option | Standard | Wirkung |
|---|---|---|
| `replays` (eine oder mehrere) | - | `.wowsreplay`-Dateien oder Ordner, in denen danach gesucht wird (auch in Unterordnern) |
| `-o`, `--out` | nötig | der Ordner, in den geschrieben wird: darin ein Ordner pro Karte |
| `--force` | aus | bereits Geschriebenes erneut umwandeln |
| `--ship-names JSON` | - | eine JSON-Datei `{"<shipId>": "<name>", ...}`: Replays benennen nur das Schiff des aufnehmenden Spielers, die übrigen nach Nummer |
| `--version` | - | gibt `heat3d-wows-replay <version>` aus und endet |
| `-h`, `--help` | - | gibt die Optionen aus und endet |

Die Optionen, so wie das Programm sie ausgibt: [Befehlsreferenz](../cli-reference.md).

## Was geschrieben wird {#what-is-written}

Nur Einzeldateien: Dieser Umwandler schreibt keine Datei `.3dheat` (der Viewer kann sie in eine
einzige packen: [Eine Datei pro Match](https://holdi601.github.io/3DHeat/container.html)).
Je Replay in `out/<map>/` (der Name der Karte ohne ihren `spaces/`-Teil):

| Datei | Was |
|---|---|
| `<match>.parquet` | die Tabelle: die Position jedes Schiffs über die Zeit und jedes Ereignis dort, wo es passierte ([Die Tabelle](table.md)) |
| `<match>.match.json` | das Match-Dokument: Karte, Client-Version, Spieler, Versenkungen, Chat und alles Übrige ([Das Match-Dokument](match-document.md)) |
| `<match>.messages.parquet` | der Sidecar: jeder Teil des Replays, den die beiden Dateien oben nicht ganz enthalten ([Vollständigkeit](completeness.md)) |

`<match>` ist die eigene Kennung des Gefechts oder der Dateiname, wenn die Aufnahme vor den
Ergebnissen endete.

## Exit-Status {#exit-status}

`0`, wenn jedes Replay umgewandelt oder übersprungen wurde, `1`, wenn eines fehlgeschlagen ist
(die übrigen werden trotzdem umgewandelt), `2`, wenn keine Replay-Datei gefunden wurde.

---

Teil von [3DHeat](https://github.com/Holdi601/3DHeat) ([Dokumentation](https://holdi601.github.io/3DHeat/)). Quelle: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
