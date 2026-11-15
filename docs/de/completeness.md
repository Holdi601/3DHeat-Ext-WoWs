---
title: Vollständigkeit
nav_order: 8
lang: "de"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Vollständigkeit {#completeness}

Nichts aus einem Replay wird weggeworfen. Was der Umwandler liest, geht in die Tabelle
und das Match-Dokument; jeder andere Teil wird vollständig im Sidecar
`<match>.messages.parquet` aufbewahrt; und `selfCheck.completeness` im Match-Dokument
zählt, was aus jeder Art von Teil geworden ist. Das ist die Regel, die alle
3DHeat-Umwandler teilen:
[Umwandler behalten alles](https://holdi601.github.io/3DHeat/converters.html).

![Die Selbstprüfung eines synthetischen Replays: jeder Teil gesehen, gelesen, behalten oder verloren](../assets/img/completeness.svg)

## Die Zählung {#the-count}

Für jede Art von Teil gibt `selfCheck.completeness.types` an:

| Zählung | Bedeutung |
|---|---|
| `seen` | wie viele das Replay enthält |
| `decoded` | ganz gelesen |
| `partial` | teilweise gelesen, und vollständig im Sidecar aufbewahrt |
| `raw` | nur vollständig im Sidecar aufbewahrt, nicht gelesen |
| `lost` | verloren: immer `0` |

Die Arten sind die des Replays selbst: `block <n>` (die JSON-Blöcke), die eigenen Bytes
des Containers, `packet <type>`, und für Aufrufe an Entitäten `method <entity type>.<number>`
und `property <entity type>.<number>`. `selfCheck.entities.roles` sagt, welcher Entitätstyp
der Avatar des aufnehmenden Spielers ist und welche die Schiffe. Eine Art, die niemand kannte,
erscheint mit ihrer Zählung.

## Der Sidecar {#the-sidecar}

| Spalte | Was |
|---|---|
| `time` | die Uhr des Replays, wie in der Tabelle |
| `type`, `name` | die Art des Teils; wie der Umwandler es nennt, wo er es liest |
| `entity` | das Schiff oder der Avatar, zu dem es gehört, wie das `entity` der Tabelle |
| `decoded` | was davon gelesen wurde, als JSON |
| `payload`, `text` | seine Bytes, vollständig; die JSON-Blöcke, vollständig |
| `entityType`, `packet`, `method` | die Nummern |

Die Zeilen sind nach Paket, Methode, Entität und Zeit sortiert. Welche Entität welcher
Spieler ist: `entities` und `players` im Match-Dokument.

## Was gelesen wird, und wie es geprüft wurde {#what-is-read-and-how-it-was-checked}

- **Die Ergebnisse** (15.x, `results`): Ihre Gefechts-ID ist die des Stroms, und jeder Spieler
  darin steht in der Aufstellung des Kopfes.
- **Der Block der IDs** (15.x, `blockIds`): das Konto und das Gefecht, als Text gelesen, damit
  keine Ziffer verloren geht.
- **Nicken und Rollen** jeder Position: Die Rolle hängt mit der Drehrate zusammen, wie ein Schiff
  sich in einer Kurve neigt; das Nicken ist fast immer 0.
- **Entitäten** (`entities`): wann jede in die Sicht des Clients kam und sie verließ.
  Kein Schiff hat zwischen Verlassen und Wiederkommen eine Position.
- **Die Version im Strom** (`streamVersion`): dieselbe wie im Kopf.

Alles andere, was gelesen wird (Versenkungen, Schaden, Lebenspunkte, Granaten, Torpedos, wo
Granaten endeten, Chat, Pickle-Aufrufe, die Spielerdaten, Positionen), ist `partial`: in der
Tabelle oder im Match-Dokument, und vollständig im Sidecar aufbewahrt.

**Aufbewahrt, aber nicht gelesen** (`raw`), die größten Arten: Positionsaktualisierungen, die nicht
in der Tabelle stehen (nach dem Untergang eines Schiffs, Entitäten ohne Spieler), die häufigen
Eigenschaften und Methoden ohne Leser, die Eigenschaften der Entitätserzeugungen und jedes andere
Paket ohne Leser.

## Nicht verfügbar {#not-available}

- Was der Server dem aufnehmenden Client nie gesendet hat: das Zielen, die Kamera und die Eingaben
  anderer Spieler, Gegner, solange sie nicht gesichtet sind. Ein Replay ist das, was einem Client
  mitgeteilt wurde.
- Die Namen der Entitätstypen, Methoden, Eigenschaften und der Schlüssel der Statistiken: Sie stehen
  in den Definitionsdateien des Spiels, nicht im Replay. Die Nummern werden aufbewahrt.
- Schiffsnamen zu den Schiffsnummern (mit `--ship-names`), und alles andere, was die eigenen Dateien
  des Spiels braucht.
- Ergebnisse von Clients vor 15.x: Sie stehen nicht in deren Replays.

---

Teil von [3DHeat](https://github.com/Holdi601/3DHeat) ([Dokumentation](https://holdi601.github.io/3DHeat/)). Quelle: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
