---
title: Atkārtojumu pārvēršana
nav_order: 4
lang: lv
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Atkārtojumu pārvēršana {#converting-replays}

## Soli pa solim {#step-by-step}

1. **Ieslēdz ierakstīšanu:** `isReplayEnabled` spēles failā `preferences.xml`, vai spēles pašu iestatījumu, ja tam ir. No tā brīža spēle saglabā katru kauju World of Warships instalācijas mapē `replays`, piemēram `C:\Games\World_of_Warships_EU\replays`.
2. **Atver termināli** mapē, kurā rezultāti drīkst tikt rakstīti ([Pirms sākat](before-you-start.md)).
3. **Palaid konvertētāju** atkārtojumu failiem vai mapēm, kurās tie ir:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` tiek izveidota mapē, kurā atrodas tavs termināls.
4. **Izlasi, ko tas saka.** Vajadzētu redzēt vienu rindu katram atkārtojumam, kas beidzas ar tabulu, ko tas uzrakstīja.
5. **Atver rezultātu** 3DHeat skatītājā: `out/<map>/<match>.parquet` Siltumkartes cilnē, `<match>.match.json` Mača cilnē. Vai arī lasi tos ar jebkuru Parquet vai JSON lasītāju.

![Izpilde ar sintētisku atkārtojumu: konvertēšana, atkārtota palaišana, bojāts fails, tukša mape](../assets/img/convert.svg)

Attēls ir izpilde ar atkārtojumu, ko testi izveido kodā (ne īsts atkārtojums):

- atkārtojums pārvērsts: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- atkārtoti palaižot, jau uzrakstītais mačs tiek izlaists: `<file>: already written, <table>`;
- fails, kas nav atkārtojums: `<file>: not converted: <why>` (kļūdu izvadā; izejas statuss 1, pārējie atkārtojumi joprojām tiek pārvērsti);
- atkārtojums nav atrasts: `no .wowsreplay files in <folders>` (izejas statuss 2).

## Iespējas {#options}

| Iespēja | Noklusējums | Ko dara |
|---|---|---|
| `replays` (viens vai vairāki) | - | `.wowsreplay` faili vai mapes, kurās tie tiek meklēti (arī apakšmapēs) |
| `-o`, `--out` | obligāta | mape, kurā rakstīt: mape katrai kartei iekšā |
| `--force` | izslēgts | pārvērst vēlreiz to, kas jau ir uzrakstīts |
| `--ship-names JSON` | - | JSON fails `{"<shipId>": "<name>", ...}`: atkārtojumi nosauc tikai ieraksta spēlētāja kuģi, pārējos — pēc numura |
| `--version` | - | izdrukāt `heat3d-wows-replay <version>` un apstāties |
| `-h`, `--help` | - | izdrukāt iespējas un apstāties |

Iespējas tā, kā tās izdrukā programma: [Komandu atsauce](../cli-reference.md).

## Kas tiek rakstīts {#what-is-written}

Tikai atsevišķi faili: šis konvertētājs neraksta `.3dheat` failu (skatītājs to var iepakot vienā: [Viens fails vienam mačam](https://holdi601.github.io/3DHeat/container.html)). Katram atkārtojumam mapē `out/<map>/` (kartes nosaukums bez `spaces/`):

| Fails | Kas tas ir |
|---|---|
| `<match>.parquet` | tabula: katra kuģa pozīcija laika gaitā un katrs notikums, kur tas notika ([Tabula](table.md)) |
| `<match>.match.json` | mača dokuments: karte, klienta versija, spēlētāji, nogrimšanas, tērzēšana un viss pārējais ([Mača dokuments](match-document.md)) |
| `<match>.messages.parquet` | papildfails: katrs atkārtojuma vienums, ko abi iepriekšējie faili nesatur pilnībā ([Pilnība](completeness.md)) |

`<match>` ir paša kaujas ID, vai faila nosaukums, ja ierakstīšana apstājās pirms rezultātiem.

## Izejas statuss {#exit-status}

`0`, kad katrs atkārtojums ir pārvērsts vai izlaists, `1`, kad kāds neizdevās (pārējie joprojām tiek pārvērsti), `2`, kad neviens atkārtojuma fails nav atrasts.

---

Daļa no [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentācija](https://holdi601.github.io/3DHeat/)). Avots: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
