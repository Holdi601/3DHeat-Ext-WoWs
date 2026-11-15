---
title: Dokumentation pflegen
nav_order: 99
lang: "de"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Dokumentation pflegen {#maintaining-the-documentation}

Für alle, die eine neue Version veröffentlichen. Die Schritte in dieser Reihenfolge ausführen.

1. **Die Referenzseiten aus dem Code neu erzeugen:**

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # muss mit 0 enden
   ```

   Das schreibt [Befehlsreferenz](../cli-reference.md) und
   [Spaltenliste](../columns.md) neu. Diese beiden nie von Hand bearbeiten.
2. **Auflisten, was seit dem letzten Release geändert wurde:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` ist die zuletzt veröffentlichte Version (ohne Tag: das ganze
   `git log --oneline`). Jede neue Funktion, Option oder Spalte braucht ihre Seite und
   eine Zeile im Abschnitt **Docs** der
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Unabhängige Prüfung.** Jemand, der die Seiten nicht geschrieben hat (eine Person
   oder ein Agent), liest die README, jede Seite und jedes Bild aus drei Blickwinkeln:
   ein Anfänger, der noch nie ein Terminal benutzt hat, ein Achtjähriger und ein
   Profi, der jede Option, Spalte und Einheit gegen den Code prüft. Sie prüfen auch die
   Diagramme gegen den Code und ob keine Seite eine echte Karte, ein echtes Level, einen
   echten Spieler oder ein echtes Match nennt oder Zahlen aus echten Replays angibt.
4. **Beheben, was die Prüfung gefunden hat.** Dann Schritt 1 erneut ausführen und die
   Bilder neu zeichnen, deren Ausgabe sich geändert hat.
5. **Übersetzungen.** Jede Seite unter `docs/<Sprache>/` vermerkt den Hash der englischen
   Seite, aus der sie übersetzt wurde. Jede Seite neu übersetzen, deren englische Quelle
   sich geändert hat, die Beschriftungen der Diagramme eingeschlossen. Danach jede Sprache
   prüfen: verständlich für alle drei Leser, Beschriftungen richtig und dieselben Wörter,
   die der 3DHeat-Viewer in dieser Sprache verwendet.
6. **Veröffentlichen:** `VERSION` erhöhen und `v<VERSION>` taggen. **Erst pushen, wenn der
   Eigentümer zustimmt.**

## Übersetzungen: die Befehle {#translations-the-commands}

Die Dokumentation ist in die 40 Sprachen des 3DHeat-Viewers übersetzt: Englisch in `docs/`, jede andere
Sprache in `docs/<lang>/` mit denselben Dateinamen. `tools/docs_i18n.py` führt die Buchhaltung:

```bash
python tools/docs_i18n.py hashes             # nach jeder englischen Änderung: den Hash jeder Seite festhalten
python tools/docs_i18n.py svg-strings        # nach jeder Bildänderung: die zu übersetzenden Beschriftungen
python tools/docs_i18n.py status             # je Sprache: aktuell, veraltet, fehlende Seiten
python tools/docs_i18n.py todo --lang de     # die deutschen Seiten, die (neu) übersetzt werden müssen
python tools/docs_i18n.py svg-build --lang de    # deutsche Bilder aus docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # die deutschen Seiten mit ihrem englischen Hash versehen
python tools/docs_i18n.py check              # Exit 1, wenn Hashes oder Beschriftungen veraltet sind
```

Nur übersetzen, was `todo` auflistet: Markdown, Links, Code, Datei- und Spaltennamen so lassen,
wie sie sind, Titel und Bildbeschreibungen übersetzen, und für Schaltflächen und Bereiche des
3DHeat-Viewers dessen eigene Wörter verwenden (`src/i18n/locales/<lang>/`). Generierte
Referenzseiten und Terminal-Bilder bleiben englisch. Auf der Seite zeigt eine veraltete
Übersetzung das an und verlinkt die englische Seite; eine fehlende fällt auf Englisch zurück.
Das Sprachmenü im Kopf und die Weiterleitung der Startseite nach Browsersprache kommen aus
`docs/_includes/`.
