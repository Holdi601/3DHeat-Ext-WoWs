---
title: "Replays émwandelen"
nav_order: 4
lang: "lb"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Replays émwandelen {#converting-replays}

## Schrëtt fir Schrëtt {#step-by-step}

1. **Schaltet d'Opnam un**: `isReplayEnabled` an der `preferences.xml` vum
   Spill, oder dem Spill seng eege Astellung, wou et eng huet. Vun do un
   späichert d'Spill all Gefecht am `replays`-Dossier vun Ärer World-of-
   Warships-Installatioun, zum Beispill
   `C:\Games\World_of_Warships_EU\replays`.
2. **Mécht en Terminal op** an engem Dossier, an dee d'Resultater däerfen goen
   ([Ier Dir ufänkt](before-you-start.md)).
3. **Loosst de Konverter lafen** op Replay-Dateien, oder op Dossieren, déi se enthalen:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` gëtt an dem Dossier gemaach, an deem Äre Terminal ass.
4. **Liest, wat et seet.** Dir sollt eng Zeil pro Replay gesinn, déi mat der
   Tabell ophält, déi geschriwwe gouf.
5. **Mécht d'Resultat op** am 3DHeat-Viewer: `out/<map>/<match>.parquet`
   am Heatmap-Tab, `<match>.match.json` am Match-Tab. Oder liest se
   mat engem Parquet- oder JSON-Reader.

![E Laf op engem synthetesche Replay: émwandelen, nach eng Kéier lafen, eng futtis Datei, en eidele Dossier](../assets/img/convert.svg)

D'Bild ass e Laf op engem Replay, deen d'Tester am Code bauen (kee richtege Replay):

- e Replay émgewandelt: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- nach eng Kéier gelaf, de Match, deen scho geschriwwe ass, gëtt iwwersprong: `<file>: already written, <table>`;
- eng Datei, déi kee Replay ass: `<file>: not converted: <why>` (op der Feeler-
  Ausgab; Exit-Status 1, déi aner Replays ginn trotzdem émgewandelt);
- kee Replay fonnt: `no .wowsreplay files in <folders>` (Exit-Status 2).

## Optiounen {#options}

| Optioun | Standard | Wat se mécht |
|---|---|---|
| `replays` (ee oder méi) | - | `.wowsreplay`-Dateien, oder Dossieren, an deenen no hinnen gesicht gëtt (och Ënnerdossieren) |
| `-o`, `--out` | erfuerderlech | den Dossier, an deen geschriwwe gëtt: dran een Dossier pro Kaart |
| `--force` | aus | nach eng Kéier émwandelen, wat scho geschriwwen ass |
| `--ship-names JSON` | - | eng JSON-Datei `{"<shipId>": "<name>", ...}`: Replays nennen nëmmen d'Schëff vum opuelende Spiller, d'anert no Nummer |
| `--version` | - | `heat3d-wows-replay <version>` drécken an ophalen |
| `-h`, `--help` | - | d'Optiounen drécken an ophalen |

D'Optioune sou, wéi de Programm se dréckt: [Befehlsreferenz](../cli-reference.md).

## Wat geschriwwe gëtt {#what-is-written}

Nëmme lose Dateien: dëse Konverter schreift keng `.3dheat`-Datei (de Viewer kann
se an eng paken: [Eng Datei pro Match](https://holdi601.github.io/3DHeat/container.html)).
Pro Replay, an `out/<map>/` (den Numm vun der Kaart ouni säin `spaces/`):

| Datei | Wat |
|---|---|
| `<match>.parquet` | d'Tabell: d'Positioun vun all Schëff iwwer d'Zäit an all Evenement do, wou et geschitt ass ([D'Tabell](table.md)) |
| `<match>.match.json` | d'Match-Dokument: Kaart, Clientversioun, Spiller, Versenkungen, Chat an alles anescht ([D'Match-Dokument](match-document.md)) |
| `<match>.messages.parquet` | d'Niewendatei: all Stéck vum Replay, dat déi zwou Dateie driwwer net ganz halen ([Vollstännegkeet](completeness.md)) |

`<match>` ass dem Gefecht seng eege ID, oder den Numm vun der Datei, wann d'Opnam
virun de Resultater opgehal huet.

## Exit-Status {#exit-status}

`0`, wann all Replay émgewandelt oder iwwersprong gouf, `1`, wann ee gescheitert ass (déi
aner ginn trotzdem émgewandelt), `2`, wann keng Replay-Datei fonnt gouf.

---

Deel vun [3DHeat](https://github.com/Holdi601/3DHeat) ([Dokumentatioun](https://holdi601.github.io/3DHeat/)). Quell: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
