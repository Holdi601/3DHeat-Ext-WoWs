---
title: Mača dokuments
nav_order: 6
lang: lv
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Mača dokuments {#the-match-document}

`<match>.match.json` satur visu, ko atkārtojums saka un kas nav tabulas rinda. Skatītāja Mača cilne to nolasa. (Kods to sauc par kopsavilkumu.)

![Sintētiska mača dokumenta sākums un tā atslēgas](../assets/img/match-document.svg)

## Kauja {#the-battle}

| Atslēga | Ko tā nozīmē |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; kaujas ID; karte, kā to nosauc spēle (`spaces/<map>`), un tās parādāmais nosaukums |
| `clientVersion`, `streamVersion` | spēles versija no galvenes un kā to saka paketes straume |
| `recorded` | kad atkārtojums ierakstīts, kā to raksta spēle |
| `player`, `vehicle` | ierakstošais spēlētājs un viņa kuģis |
| `gameType`, `scenario` | kaujas tips (`RandomBattle`, ...) un scenārijs no galvenes |
| `duration` | kaujas laika ierobežojums sekundēs, no galvenes |
| `truncated` | ieraksts apstājās agri |
| `battleStart`, `recordingSeconds` | kaujas sākums (pirmais brīdis, kad jebkurš kuģis kustas) un ieraksta garums sekundēs |
| `positionPacket`, `ownPositionPacket` | paketes numuri, kuros nāca pozīcijas: citi kuģi, ierakstošā spēlētāja kuģis |
| `deathMethod` | metodes numurs, kurā atrastas nogrimšanas |
| `hz`, `ownHz`, `positions` | paraugi sekundē citiem kuģiem un pašam kuģim; pozīciju rindas |
| `units` | pasaules vienības (15 m pēc korpusiem, 30 m pēc spēles diapazoniem); x austrumi, y augšā, z ziemeļi |
| `events` | katra notikuma tabulas rindu skaits |
| `decoded` | metodes un paketes numuri, kas atrasti katram ziņojuma veidam |

## Spēlētāji un notikumi {#players-and-events}

| Atslēga | Ko tā nozīmē |
|---|---|
| `players` | viens ieraksts katram kuģim: vārds, `ally` vai `enemy`, kuģa numurs un nosaukums, entītija, paraugi, nogalinājumi, izdzīvoja; `seen` (nodarītie un saņemtie bojājumi, čaulas, torpēdas un pēdējā veselība, ko klients redzēja); `header` (ieraksts no sastāva) un `record` (spēlētāja ieraksts no straumes, pēc atslēgas numura) |
| `kills` | katra nogrimšana: laiks, upuris, slepkava, iemesla numurs, vieta |
| `chat` | katra tērzēšanas rinda, ar kanālu un sūtītāju |
| `damageStats` | ieraksta spēlētāja paša statistika, kā to glabā spēle: pa ieroci un veidu, skaits un summa (veids 0 ir nodarītie bojājumi) |
| `avatarPickles` | katrs pickled izsaukums ieraksta spēlētājam, atšifrēts, pēc metodes numura |

## Galvene, rezultāti un pārbaudes {#header-results-and-checks}

| Atslēga | Ko tā nozīmē |
|---|---|
| `header` | pirmais JSON bloks, viss, izņemot sastāvu: spēles režīms, laika apstākļi, kartes robeža, komandu lielumi un vēl |
| `moreBlocks` | JSON bloki pēc pirmā, kā tie ir |
| `blockIds` | 15.x: ieraksta spēlētāja konts un kaujas ID, nolasīti kā teksts |
| `results` | 15.x: rezultāti, ko šie klienti glabā straumē |
| `entities` | katra entītija, ko straume izveido: tās tipa numurs un loma, kad tā ieiet klienta redzeslokā un kad aizgāja |
| `selfCheck` | pilnības skaits ([Pilnība](completeness.md)) un entītiju, rezultātu, ID un versijas pārbaudes |

---

Daļa no [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentācija](https://holdi601.github.io/3DHeat/)). Avots: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
