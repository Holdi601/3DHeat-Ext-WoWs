---
title: Start
nav_order: 1
lang: "de"
source: index.md
source_hash: "833e00fa8116"
nav_exclude: true
search_exclude: true
permalink: /de/
---
# 3DHeat-World-of-Warships-Replays {#dheat-world-of-warships-replays}

**Was ist das?** World of Warships kann jedes Gefecht, das du spielst, als Replay-Datei
speichern. Dieses Werkzeug macht aus diesen Dateien eine Tabelle und ein Match-Dokument
(die Zusammenfassung des Gefechts), die der [3DHeat-Viewer](https://holdi601.github.io/3DHeat/)
in 3D zeigt: wohin jedes Schiff gefahren ist, geschossen hat und getroffen wurde.

**Wozu braucht man das?** Um ein Gefecht noch einmal von oben zu sehen, alle Schiffe
zugleich; um Heatmaps zu sehen, wo du und andere über hunderte Gefechte hinweg fahren,
kämpfen und versenkt werden; um zu sehen, wohin Granaten und Torpedos gingen; oder um ein
Replay mit eigenen Skripten zu lesen, denn die Ausgabe ist einfaches Parquet und JSON.

**Beispiel:** Eine Replay-Datei hinein, eine Tabelle und ein Match-Dokument heraus:

![Vom Replay zum 3DHeat-Viewer](../assets/img/de/pipeline.svg)

## Schnellstart {#quick-start}

Du brauchst Windows, Python 3.10 oder neuer (im Installer "Add python.exe to PATH"
ankreuzen) und World of Warships mit eingeschalteter Replay-Aufzeichnung: `isReplayEnabled`
in der `preferences.xml` des Spiels, oder die eigene Einstellung des Spiels, wo es eine
hat (das Spiel speichert dann jedes Gefecht im Ordner `replays` seiner Installation); Git ist nicht nötig.
Neu auf der Kommandozeile? Lies zuerst [Bevor du anfängst](before-you-start.md).

```bash
python -m pip install https://github.com/Holdi601/3DHeat-Ext-WoWs/archive/refs/tags/v0.1.0.zip
heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
```

Du solltest pro Replay eine Zeile sehen, die mit der geschriebenen Datei endet:
`... -> out/<map>/<match>.parquet`. Daneben liegen `<match>.match.json` (das
Match-Dokument) und `<match>.messages.parquet`. Läuft es später noch einmal, werden
nur die neuen Replays umgewandelt.
Replays nennen nur dein eigenes Schiff; `--ship-names names.json` (eine JSON-Datei
`{"<shipId>": "<name>", ...}`) benennt die anderen.

Dann öffne die Dateien im [3DHeat-Viewer](https://github.com/Holdi601/3DHeat#quick-start):
herunterladen (**Code -> Download ZIP**, entpacken), `start.bat` doppelklicken (es bietet
an, Node.js zu installieren, wenn es fehlt, und öffnet `http://127.0.0.1:5273`), dann
**Quelle -> Dateien...** und die `<match>.parquet`-Dateien wählen (oder sie auf das
Quelle-Panel ziehen) für den Heatmap-Tab; für das Gefecht selbst im **Match**-Tab
**Match-Dateien laden...** und die `<match>.match.json`
([Match-Analyse](https://holdi601.github.io/3DHeat/match-analysis.html)).
Alles bleibt auf deinem Rechner.

Wenn ein neues Release erscheint, sagt das Werkzeug es beim Start und bietet an, sich
selbst zu aktualisieren.

## Diese Dokumentation {#this-documentation}

| Seite | Was sie behandelt |
|---|---|
| [Bevor du anfängst](before-you-start.md) | Python, ein Terminal und wie Erfolg aussieht |
| [Installation](installing.md) | Installation, Prüfung, Aktualisierungen |
| [Replays umwandeln](converting.md) | Schritt für Schritt, jede Option, Meldungen, Exit-Status |
| [Die Tabelle](table.md) | jede Spalte und jedes Ereignis von `<match>.parquet` |
| [Das Match-Dokument](match-document.md) | jeder Schlüssel von `<match>.match.json` |
| [So liest es ein Replay](how-it-reads.md) | das Format und wie das Lesen geprüft wurde |
| [Vollständigkeit](completeness.md) | die Begleitdateien und die Selbstprüfung |
| [Nutzungsbedingungen und Lizenz](terms.md) | was er liest, Lizenz, Quellen |
| [Befehlsreferenz](../cli-reference.md), [Spaltenliste](../columns.md) | aus dem Code erzeugt |

## Teil von 3DHeat {#part-of-3dheat}

Dieser Umwandler ist eines der Werkzeuge von [3DHeat](https://github.com/Holdi601/3DHeat),
eines Viewers für 3D-Telemetrie und Replays in Echtzeit ([Dokumentation](https://holdi601.github.io/3DHeat/)).
Der Viewer öffnet die Tabelle im Heatmap-Tab und das Match-Dokument im Match-Tab. Er kann die
Dateien eines Matches in eine einzige Datei packen:
[Eine Datei pro Match](https://holdi601.github.io/3DHeat/container.html). Was jeder
Umwandler behalten muss: [Umwandler behalten alles](https://holdi601.github.io/3DHeat/converters.html).

Jeder Spiel-Leser ist ein eigenes kleines Projekt mit eigener Lizenzdatei,
eigenen Releases und eigenem Issue-Tracker, sodass er für sich installiert,
aktualisiert, gepflegt - oder auf Wunsch eines Rechteinhabers zurückgezogen -
werden kann, ohne den Viewer oder die anderen Werkzeuge zu berühren. Der
Watcher führt diesen Umwandler aus, wenn er installiert ist, und funktioniert
auch ohne ihn. Was der Umwandler liest: [Nutzungsbedingungen und Lizenz](terms.md).

| Werkzeug | Was es tut | Quelle | Dokumentation |
|---|---|---|---|
| 3DHeat-Viewer | zeigt die Daten in 3D: Heatmaps, Replays, Rennanalyse | [3DHeat](https://github.com/Holdi601/3DHeat) | [Seite](https://holdi601.github.io/3DHeat/) |
| GameFiles | Strecken und Level aus den Dateien, die Spiele mitliefern | [3DHeat-GameFiles](https://github.com/Holdi601/3DHeat-GameFiles) | [Seite](https://holdi601.github.io/3DHeat-GameFiles/) |
| GameCapture | Rundentelemetrie und Level, die aus Spielvideos nachgebaut werden | [3DHeat-GameCapture](https://github.com/Holdi601/3DHeat-GameCapture) | [Seite](https://holdi601.github.io/3DHeat-GameCapture/) |
| Unreal Exporter | ein Plugin für den Unreal Editor, das ein Level exportiert | [3DHeat-UnrealExporter](https://github.com/Holdi601/3DHeat-UnrealExporter) | [Seite](https://holdi601.github.io/3DHeat-UnrealExporter/) |
| CS2 | Demos und Karten von Counter-Strike 2 | [3DHeat-CS2](https://github.com/Holdi601/3DHeat-CS2) | [Seite](https://holdi601.github.io/3DHeat-CS2/) |
| Watcher | nimmt auf, was Spiele veröffentlichen, während du spielst | [3DHeat-Watcher](https://github.com/Holdi601/3DHeat-Watcher) | [Seite](https://holdi601.github.io/3DHeat-Watcher/) |
| War-Thunder-Replays | `.wrpl`-Replays und Level von War Thunder | [3DHeat-Ext-WarThunder](https://github.com/Holdi601/3DHeat-Ext-WarThunder) | [Seite](https://holdi601.github.io/3DHeat-Ext-WarThunder/) |
| World-of-Tanks-Replays | `.wotreplay`-Replays | [3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT) | [Seite](https://holdi601.github.io/3DHeat-Ext-WoT/) |
| World-of-Warships-Replays | `.wowsreplay`-Replays | [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs) | [Seite](https://holdi601.github.io/3DHeat-Ext-WoWs/) |
| Squad-Demos | Demos von Squad-Servern | [3DHeat-Ext-Squad](https://github.com/Holdi601/3DHeat-Ext-Squad) | [Seite](https://holdi601.github.io/3DHeat-Ext-Squad/) |
| DCS-Karten | Karten von DCS World als 3D-Level | [3DHeat-Ext-DCS](https://github.com/Holdi601/3DHeat-Ext-DCS) | [Seite](https://holdi601.github.io/3DHeat-Ext-DCS/) |
| IL-2-Karten | Karten von IL-2 Great Battles als 3D-Level | [3DHeat-Ext-IL2](https://github.com/Holdi601/3DHeat-Ext-IL2) | [Seite](https://holdi601.github.io/3DHeat-Ext-IL2/) |
| Dota-2-Karte | die Dota-2-Karte aus deiner eigenen Installation als 3D-Level | [3DHeat-Ext-Dota](https://github.com/Holdi601/3DHeat-Ext-Dota) | [Seite](https://holdi601.github.io/3DHeat-Ext-Dota/) |
| Dota-2-Replays | Replays von Dota 2 | [3DHeat-Ext-DotaReplay](https://github.com/Holdi601/3DHeat-Ext-DotaReplay) | [Seite](https://holdi601.github.io/3DHeat-Ext-DotaReplay/) |
| Riot-Replays | Replays von League of Legends und VALORANT (was sie unverschlüsselt enthalten) | [3DHeat-Ext-Riot](https://github.com/Holdi601/3DHeat-Ext-Riot) | [Seite](https://holdi601.github.io/3DHeat-Ext-Riot/) |
| Forza-Karten | Forza-Strecken, Rennen und Autos aus deiner eigenen Installation | [3DHeat-Ext-Forza](https://github.com/Holdi601/3DHeat-Ext-Forza) | [Seite](https://holdi601.github.io/3DHeat-Ext-Forza/) |
| Battlefield-Karten | Battlefield-Level (Frostbite) als 3D-Level | [3DHeat-Ext-Battlefield](https://github.com/Holdi601/3DHeat-Ext-Battlefield) | [Seite](https://holdi601.github.io/3DHeat-Ext-Battlefield/) |
| BeamNG-Karten | Strecken von BeamNG.drive | [3DHeat-Ext-BeamNG](https://github.com/Holdi601/3DHeat-Ext-BeamNG) | [Seite](https://holdi601.github.io/3DHeat-Ext-BeamNG/) |
| AC-Rally-Karten | Etappen von Assetto Corsa Rally als Strecken | [3DHeat-Ext-ACRally](https://github.com/Holdi601/3DHeat-Ext-ACRally) | [Seite](https://holdi601.github.io/3DHeat-Ext-ACRally/) |
| Reforger-Karten | Welten von Arma Reforger (Enfusion) als 3D-Level | [3DHeat-Ext-Reforger](https://github.com/Holdi601/3DHeat-Ext-Reforger) | [Seite](https://holdi601.github.io/3DHeat-Ext-Reforger/) |
| R6-Replays | Replays von Rainbow Six Siege | [3DHeat-Ext-R6](https://github.com/Holdi601/3DHeat-Ext-R6) | [Seite](https://holdi601.github.io/3DHeat-Ext-R6/) |

---

Quelle: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
