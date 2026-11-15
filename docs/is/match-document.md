---
title: "Leikjaskjalið"
nav_order: 6
lang: is
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Leikjaskjalið {#the-match-document}

`<match>.match.json` geymir allt sem upptakan segir og er ekki röð í
töflunni. Flipinn Leikur í skoðaranum les það. (Kóðinn kallar það samantektina.)

![Upphaf tilbúins leikjaskjals og lyklar þess](../assets/img/match-document.svg)

## Bardaginn {#the-battle}

| Lykill | Hvað |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; auðkenni bardagans; kortið eins og leikurinn nefnir það (`spaces/<map>`) og birtingarnafn þess |
| `clientVersion`, `streamVersion` | leikjaútgáfan úr hausnum, og eins og pakkastraumurinn segir hana |
| `recorded` | hvenær upptakan var tekin, eins og leikurinn skrifar það |
| `player`, `vehicle` | upptökumaðurinn og skip hans |
| `gameType`, `scenario` | gerð bardagans (`RandomBattle`, ...) og sviðsmynd, úr hausnum |
| `duration` | tímamörk bardagans í sekúndum, úr hausnum |
| `truncated` | upptakan stöðvaðist snemma |
| `battleStart`, `recordingSeconds` | upphaf bardagans (fyrsta stund sem nokkurt skip hreyfist) og lengd upptökunnar, í sekúndum |
| `positionPacket`, `ownPositionPacket` | pakkanúmerin sem stöðurnar komu í: annarra skipa, upptökumannsins |
| `deathMethod` | aðferðarnúmerið sem sökkvanirnar fundust í |
| `hz`, `ownHz`, `positions` | sýni á sekúndu hjá öðrum skipum og eigin skipi; stöðuraðir |
| `units` | heimseiningar (15 m eftir skrokkum, 30 m eftir drægi leiksins); x austur, y upp, z norður |
| `events` | fjöldi taflaraða af hverjum atburði |
| `decoded` | aðferðar- og pakkanúmerin sem fundust fyrir hverja tegund skilaboða |

## Spilarar og atburðir {#players-and-events}

| Lykill | Hvað |
|---|---|
| `players` | ein færsla fyrir hvert skip: nafn, `ally` eða `enemy`, skipanúmer og nafn, eining, sýni, dráp, lifði af; `seen` (skaði veittur og tekinn, skeljar, tundurskeyti og síðasta heilsa sem biðlarinn sá); `header` (færsla listans yfir þátttakendur) og `record` (skrá spilarans úr straumnum, eftir lyklanúmeri) |
| `kills` | hver sökkvun: tími, fórnarlamb, drápsmaður, orsakanúmer, staður |
| `chat` | hver spjalllína, með rás og sendanda |
| `damageStats` | eigin tölfræði upptökumannsins eins og leikurinn heldur hana: á vopn og gerð, talning og magn (gerð 0 er skaði veittur) |
| `avatarPickles` | hvert pickle-kall til upptökumannsins, afkóðað, eftir aðferðarnúmeri |

## Haus, niðurstöður og athuganir {#header-results-and-checks}

| Lykill | Hvað |
|---|---|
| `header` | fyrsta JSON-blokkin, öll nema listinn yfir þátttakendur: leikjahamur, veður, kortamörk, stærðir liða og fleira |
| `moreBlocks` | JSON-blokkirnar á eftir þeirri fyrstu, eins og þær eru |
| `blockIds` | 15.x: reikningur upptökumannsins og auðkenni bardagans, lesið sem texti |
| `results` | 15.x: niðurstöðurnar, sem þessir biðlarar geyma í straumnum |
| `entities` | hver eining sem straumurinn býr til: tegundarnúmer hennar og hlutverk, hvenær hún kom inn í sjónsvið biðlarans og hvenær hún fór úr því |
| `selfCheck` | heilleikatalningin ([Heilleiki](completeness.md)) og athuganir á einingum, niðurstöðum, auðkennum og útgáfunni |

---

Hluti af [3DHeat](https://github.com/Holdi601/3DHeat) ([skjölun](https://holdi601.github.io/3DHeat/)). Frumkóði: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
