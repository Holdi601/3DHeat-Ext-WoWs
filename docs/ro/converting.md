---
title: Convertirea replay-urilor
nav_order: 4
lang: "ro"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Convertirea replay-urilor {#converting-replays}

## Pas cu pas {#step-by-step}

1. **Activați înregistrarea**: `isReplayEnabled` din `preferences.xml` al jocului, sau setarea proprie a jocului acolo unde există una. De atunci jocul salvează fiecare bătălie în folderul `replays` al
   instalării dumneavoastră World of Warships, de exemplu
   `C:\Games\World_of_Warships_EU\replays`.
2. **Deschideți un terminal** într-un folder în care rezultatele pot fi scrise
   ([Înainte de început](before-you-start.md)).
3. **Rulați convertorul** pe fișiere de replay, sau pe foldere care le conțin:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` este creat în folderul în care se află terminalul.
4. **Citiți ce afișează.** Ar trebui să vedeți câte o linie pentru fiecare replay, terminată cu
   tabelul pe care l-a scris.
5. **Deschideți rezultatul** în vizualizatorul 3DHeat: `out/<map>/<match>.parquet`
   în fila Hartă termică, `<match>.match.json` în fila Meci. Sau citiți-le
   cu orice cititor de Parquet sau JSON.

![O rulare pe un replay sintetic: convertire, rulare din nou, un fișier defect, un folder gol](../assets/img/convert.svg)

Imaginea este o rulare pe un replay pe care testele îl construiesc în cod (fără replay real):

- un replay convertit: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- rulat din nou, meciul deja scris este sărit: `<file>: already written, <table>`;
- un fișier care nu este un replay: `<file>: not converted: <why>` (la ieșirea de erori; codul de ieșire 1, celelalte replay-uri sunt convertite în continuare);
- niciun replay găsit: `no .wowsreplay files in <folders>` (codul de ieșire 2).

## Opțiuni {#options}

| Opțiune | Implicit | Ce face |
|---|---|---|
| `replays` (una sau mai multe) | - | fișiere `.wowsreplay`, sau foldere în care sunt căutate (și subfolderele) |
| `-o`, `--out` | obligatoriu | folderul în care se scrie: un folder pentru fiecare hartă, în interior |
| `--force` | oprit | convertește din nou ce este deja scris |
| `--ship-names JSON` | - | un fișier JSON `{"<shipId>": "<name>", ...}`: replay-urile numesc doar nava jucătorului care înregistrează, pe celelalte după număr |
| `--version` | - | afișează `heat3d-wows-replay <version>` și se oprește |
| `-h`, `--help` | - | afișează opțiunile și se oprește |

Opțiunile așa cum le afișează programul: [Referința comenzilor](../cli-reference.md).

## Ce se scrie {#what-is-written}

Doar fișiere separate: acest convertor nu scrie niciun fișier `.3dheat` (vizualizatorul le poate împacheta
într-unul: [Un fișier pentru un meci](https://holdi601.github.io/3DHeat/container.html)).
Pentru fiecare replay, în `out/<map>/` (numele hărții fără `spaces/`):

| Fișier | Ce este |
|---|---|
| `<match>.parquet` | tabelul: poziția fiecărei nave în timp și fiecare eveniment în care s-a întâmplat ([Tabelul](table.md)) |
| `<match>.match.json` | documentul meciului: harta, versiunea clientului, jucătorii, scufundările, chatul și tot restul ([Documentul meciului](match-document.md)) |
| `<match>.messages.parquet` | fișierul auxiliar: fiecare element al replay-ului pe care cele două fișiere de mai sus nu îl țin întreg ([Completitudinea](completeness.md)) |

`<match>` este id-ul propriu al bătăliei, sau numele fișierului când înregistrarea
s-a oprit înainte de rezultate.

## Codul de ieșire {#exit-status}

`0` când fiecare replay a fost convertit sau sărit, `1` când vreunul a eșuat (celelalte
sunt convertite în continuare), `2` când nu s-a găsit niciun fișier de replay.

---

Parte din [3DHeat](https://github.com/Holdi601/3DHeat) ([documentație](https://holdi601.github.io/3DHeat/)). Sursă: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
