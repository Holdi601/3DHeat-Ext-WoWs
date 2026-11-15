---
title: So liest es ein Replay
nav_order: 7
lang: de
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# So liest es ein Replay {#how-it-reads-a-replay}

Ein Replay besteht aus einem Kopf aus JSON-Blöcken und dem Paketstrom des Spiels (Hinweise zum
Format in [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Der erste Block, im Klartext: die Karte, die Client-Version, der aufnehmende Spieler und sein
  Schiff und die Aufstellung - der Name jedes Spielers, Verbündeter oder Gegner, und seine
  Schiffsnummer. Neuere Clients (15.x) fügen zwei weitere Blöcke hinzu: einen leeren und das Konto
  des aufnehmenden Spielers und die Gefechts-ID als Text, gelesen in `blockIds`. Die Ergebnisse stehen
  nicht im JSON; 15.x bewahrt sie im Strom auf.
- Der Paketstrom, zlib-komprimiert und mit Blowfish verschlüsselt, mit einem Schlüssel, den das Spiel
  mitführt und den die Community-Werkzeuge, die diese Dateien lesen, veröffentlicht haben. Entschlüsselt
  enthält er:
  - die Positionsaktualisierungen der Engine von jedem Schiff, das der Client sehen konnte (durchgehend
    das eigene Team, Gegner, solange sie gesichtet oder in der Nähe sind), mehrmals pro Sekunde, während
    sie sich bewegen, und seltener, wenn nicht;
  - das eigene Schiff des aufnehmenden Spielers in einem eigenen Paket, etwa siebenmal pro Sekunde;
  - einmal, am Anfang, die Spielerdaten als Python-Pickle (eine Liste). Sie sagen, welche Entität im Strom
    welcher Spieler ist. Ihre Schlüssel sind nummeriert, und die Nummern ändern sich mit Patches, daher
    findet der Leser die Schlüssel an ihren Werten: den Schlüssel mit den Namen der Aufstellung und den
    Schlüssel mit den Entitäten, die Positionsaktualisierungen haben;
  - der Aufruf des Servers, der dem Client sagt, dass ein Schiff gesunken ist: Opfer, Killer,
    Ursache. Er wird an seiner Form gefunden (zwölf Bytes; die ersten beiden sind Schiffsentitäten; jedes
    Opfer erscheint einmal), nicht an seiner Nummer;
  - der Schaden jedes Schiffs: ein Feld aus (Angreifer, Schaden) je Treffer, auf dem getroffenen Schiff;
    und seine Lebenspunkte, eine Eigenschaftsänderung kurz davor;
  - jede Salve aus Granaten und Torpedos, von denen der Client erfuhr: die Granatenart, der Schütze, die
    Salve, und Start und Geschwindigkeit jeder Granate oder jedes Torpedos;
  - wo Granaten endeten: der Schütze, eine Trefferart und der Ort jeder Granate (bei Clients von 15.x mit
    mehr über die Granate an der Stelle, wo sie traf, was übersprungen wird);
  - der Chat: Absender, Kanal, Zeile;
  - Pickle-Aufrufe an den aufnehmenden Spieler: seine Schadensstatistik, Aktualisierungen der
    Spielerdaten, der Zustand des Gefechts;
  - auf Clients von 15.x die Ergebnisse des Gefechts am Ende: ein eigenes Paket, ein JSON-Objekt mit der
    Gefechts-ID, vollständig in `results` des Match-Dokuments gelesen (die eigenen Listen des Spiels, ohne
    Namen: `commonList`, `privateDataList`, `playersPublicInfo` je Konto, ...).

Paket- und Methodennummern, die sich zwischen den geprüften Versionen unterscheiden (das eigene Schiffspaket
ist 43 oder 44, der Versenkungsaufruf 76 oder 83, die Granaten 101, 102, 126 oder 127), werden alle an ihrer
Form gefunden - siehe [`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) -, sodass ein Patch,
der sie neu nummeriert, die Tabelle nicht leert. Die gefundenen Nummern stehen im `decoded` des Match-Dokuments.

**Die Pickle-Daten sind nicht vertrauenswürdig.** Ein Replay ist eine Datei von irgendwo, und eine Pickle
kann Code benennen, der läuft. Sie wird mit einem Entpacker geladen, der jeder Klasse und jeder Funktion, die
die Pickle nennt, einen leblosen Platzhalter gibt, sodass nur einfache Daten entstehen und sonst nichts. Ein
Test füttert ihn mit einer Pickle, die `os.system` aufruft.

**Versenkungen** haben die genaue Zeit des Aufrufs. Ihr Ort ist dort, wo das Opfer zuletzt gesehen wurde,
wenn das innerhalb von fünf Sekunden lag. **Der Beginn des Gefechts** ist der erste Moment, in dem sich
überhaupt ein Schiff bewegt (Schiffe liegen im Countdown still).

Alles, was keine Zeile der Tabelle ist, steht im [Match-Dokument](match-document.md).

**Was dem Client mitgeteilt wurde**, ist für das eigene Team vollständig und für Gegner teilweise: Ihre Schüsse,
Treffer und Lebenspunkte stehen drin, solange sie in Reichweite sind.

**Nicht gelesen:**

- Flugzeuge und ihre Staffeln (die Aufrufe, die sie tragen, wurden nicht auseinandergenommen), die
  Sichtaktualisierungen der Minikarte (gepackt), Aufklärung, Auszeichnungen, Brände und Flutungen als eigene
  Ereignisse (ihr Schaden steht bei den Treffern), Verbrauchsgüter, Eroberungspunkte und Teampunkte
  (Eigenschaften von Entitäten ohne Definition, nicht an der Form unterscheidbar), der Rest der Eigenschaften
  eines Schiffs (Zielen, Ruder, Geschwindigkeitseinstellung ...).
- Die Schlüsselnummern der Spielerdaten und der Schadensstatistik als Namen: Das Spiel nummeriert sie, und die
  Nummern ändern sich; sie werden als Nummern aufbewahrt.
- Die zusätzlichen Daten einer Granate an der Stelle, wo sie traf (15.x), und die Bytes nach Start und
  Geschwindigkeit einer Granate oder eines Torpedos.
- Ergebnisse von Clients vor 15.x: Ihre Replays enthalten keine.
- Die Schiffsnummer als Name: Die Namen stehen in den eigenen Parameterdateien des Spiels, nicht im Replay.

## So wurde das Lesen geprüft {#how-the-reading-was-checked}

Das Lesen wurde an öffentlichen Replays von Clients von 0.9 bis 15.x geprüft, jeder Wert gegen etwas, das
das Replay ein zweites Mal angibt:

- **Positionen:** Die Entität jedes Schiffs passte zu einem Namen der Aufstellung; die Kurse stimmen mit der
  Fahrtrichtung innerhalb von 0,1 rad überein; nach seiner Versenkung bewegt sich ein Schiff weniger als 0,1
  Einheiten. Ein stillliegendes Schiff wird seltener aktualisiert.
- **Lebenspunkte:** Jedes Schiff, das innerhalb der Sicht des Clients versenkt wurde, endet mit 0 Lebenspunkten.
  Etwa die Hälfte aller Treffer passt zu einem Abfall der Lebenspunkte in der Sekunde davor; der Rest fällt
  zusammen mit Reparaturen oder anderen Treffern.
- **Schaden gegen die eigenen Statistiken des Spiels:** Auf dem neuesten Client liegt der gelesene Schaden des
  aufnehmenden Spielers innerhalb von 0,1 % der Statistik. Auf älteren Clients sind die Statistiken höher: Dem
  Client wird nicht jeder Treffer gesendet, oder die Statistik zählt mehr als Treffer (nicht geklärt).
- **Granaten:** Eine Granate beginnt wenige Einheiten von der letzten bekannten Position ihres Schiffs (die
  Geschütze sind über den Rumpf verteilt); fast jedes Ende einer Granate folgt innerhalb einer Minute einem
  Schuss, den der Client sah.

Die Tests bauen Replays in demselben Aufbau, daher liegt in diesem Repository kein echtes Replay.

**Nicht geprüft:** Clients vor 0.9.6, der Client von Lesta (Mir Korabley), Operationen und Szenarien über eines
hinaus, Clan- und Ranggefechte und welche Schiffsnummer zu welchem Schiff gehört.

---

Teil von [3DHeat](https://github.com/Holdi601/3DHeat) ([Dokumentation](https://holdi601.github.io/3DHeat/)). Quelle: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
