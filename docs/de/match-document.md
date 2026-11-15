---
title: Das Match-Dokument
nav_order: 6
lang: "de"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Das Match-Dokument {#the-match-document}

`<match>.match.json` enthält alles, was das Replay sagt und das keine Zeile der Tabelle ist.
Der Reiter Match des Viewers liest es. (Der Code nennt es die Zusammenfassung.)

![Der Anfang eines synthetischen Match-Dokuments und seine Schlüssel](../assets/img/match-document.svg)

## Das Gefecht {#the-battle}

| Schlüssel | Was |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; die Kennung des Gefechts; die Karte, so wie das Spiel sie nennt (`spaces/<map>`), und ihr Anzeigename |
| `clientVersion`, `streamVersion` | die Spielversion aus dem Kopf und so, wie der Paketstrom sie angibt |
| `recorded` | wann das Replay aufgenommen wurde, so wie das Spiel es schreibt |
| `player`, `vehicle` | der aufnehmende Spieler und sein Schiff |
| `gameType`, `scenario` | die Gefechtsart (`RandomBattle`, ...) und das Szenario, aus dem Kopf |
| `duration` | das Zeitlimit des Gefechts in Sekunden, aus dem Kopf |
| `truncated` | die Aufnahme stoppte früh |
| `battleStart`, `recordingSeconds` | der Beginn des Gefechts (der erste Moment, in dem sich ein Schiff bewegt) und die Länge der Aufnahme, in Sekunden |
| `positionPacket`, `ownPositionPacket` | die Paketnummern, in denen die Positionen kamen: die der anderen Schiffe, die des aufnehmenden Spielers |
| `deathMethod` | die Methodennummer, in der die Versenkungen gefunden wurden |
| `hz`, `ownHz`, `positions` | Messwerte pro Sekunde der anderen Schiffe und des eigenen Schiffs; Zeilen der Positionen |
| `units` | Welteinheiten (15 m nach den Rümpfen, 30 m nach den Reichweiten des Spiels); x Osten, y oben, z Norden |
| `events` | die Anzahl der Zeilen der Tabelle für jedes Ereignis |
| `decoded` | die Methoden- und Paketnummern, die für jede Art von Nachricht gefunden wurden |

## Spieler und Ereignisse {#players-and-events}

| Schlüssel | Was |
|---|---|
| `players` | ein Eintrag je Schiff: Name, `ally` oder `enemy`, Schiffsnummer und Name, Entität, Messwerte, Abschüsse, überlebt; `seen` (verursachter und erhaltener Schaden, Granaten, Torpedos und die letzten Lebenspunkte, die der Client sah); `header` (der Eintrag der Aufstellung) und `record` (die Spielerdaten aus dem Strom, nach Schlüsselnummer) |
| `kills` | jede Versenkung: Zeit, Opfer, Killer, Ursachennummer, Ort |
| `chat` | jede Chatzeile, mit Kanal und Absender |
| `damageStats` | die eigenen Statistiken des aufnehmenden Spielers, so wie das Spiel sie führt: je Waffe und Art eine Anzahl und ein Betrag (Art 0 ist der verursachte Schaden) |
| `avatarPickles` | jeder Pickle-Aufruf an den aufnehmenden Spieler, dekodiert, nach Methodennummer |

## Kopf, Ergebnisse und Prüfungen {#header-results-and-checks}

| Schlüssel | Was |
|---|---|
| `header` | der erste JSON-Block, vollständig bis auf die Aufstellung: Spielmodus, Wetter, Kartenrand, Teamgrößen und mehr |
| `moreBlocks` | die JSON-Blöcke nach dem ersten, so wie sie sind |
| `blockIds` | 15.x: das Konto des aufnehmenden Spielers und die Gefechts-ID, als Text gelesen |
| `results` | 15.x: die Ergebnisse, die diese Clients im Strom aufbewahren |
| `entities` | jede Entität, die der Strom erzeugt: ihre Typnummer und Rolle, wann sie in die Sicht des Clients kam und wann sie sie verließ |
| `selfCheck` | die Zählung der Vollständigkeit ([Vollständigkeit](completeness.md)) und die Prüfungen der Entitäten, der Ergebnisse, der IDs und der Version |

---

Teil von [3DHeat](https://github.com/Holdi601/3DHeat) ([Dokumentation](https://holdi601.github.io/3DHeat/)). Quelle: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
