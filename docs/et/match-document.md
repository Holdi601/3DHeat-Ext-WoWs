---
title: Mängu dokument
nav_order: 6
lang: et
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Mängu dokument {#the-match-document}

`<match>.match.json` hoiab kõike, mida kordus ütleb ja mis ei ole tabeli rida. Vaaturi vahekaart **Matš** loeb seda.
(Kood nimetab seda kokkuvõtteks.)

![Synteetilise mängu dokumendi algus ja selle võtmed](../assets/img/match-document.svg)

## Lahing {#the-battle}

| Võti | Mis see on |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; lahingu ID; kaart, nii nagu mäng seda nimetab (`spaces/<map>`), ja tema kuvatav nimi |
| `clientVersion`, `streamVersion` | mängu versioon päisest ja nii, nagu paketivoog seda ütleb |
| `recorded` | millal kordus salvestati, nii nagu mäng seda kirjutab |
| `player`, `vehicle` | salvestajamängija ja tema laev |
| `gameType`, `scenario` | lahingu tüüp (`RandomBattle`, ...) ja stsenaarium päisest |
| `duration` | lahingu ajapiir sekundites, päisest |
| `truncated` | salvestus katkes varakult |
| `battleStart`, `recordingSeconds` | lahingu algus (esimene hetk, kui mõni laev liigub) ja salvestuse pikkus sekundites |
| `positionPacket`, `ownPositionPacket` | paketinumbrid, millega asukohad tulid: teiste laevade, salvestajamängija oma |
| `deathMethod` | meetodi number, mille alt uppumised leiti |
| `hz`, `ownHz`, `positions` | näidised sekundis teiste laevade ja oma laeva kohta; asukohtade read |
| `units` | maailma ühikud (laevade kere järgi 15 m, mängu vahemike järgi 30 m); x ida, y üles, z põhja |
| `events` | iga sündmuse tabeli ridade arv |
| `decoded` | iga sõnumi liigi jaoks leitud meetodi ja paketi numbrid |

## Mängijad ja sündmused {#players-and-events}

| Võti | Mis see on |
|---|---|
| `players` | üks kirje laeva kohta: nimi, `ally` või `enemy`, laevanumber ja nimi, olem, näidised, tapmised, ellu jäänud; `seen` (kahju tekitatud ja saadud, mürsud, torpeedod ja viimane tervis, mida klient nägi); `header` (nimekirja kirje) ja `record` (mängija kirje voost, võtme numbri järgi) |
| `kills` | iga uppumine: aeg, ohver, tapja, põhjuse number, koht |
| `chat` | iga vestlusrida, kanali ja saatjaga |
| `damageStats` | salvestajamängija enda statistika, nii nagu mäng seda peab: relva ja liigi kaupa, arv ja summa (liik 0 on tekitatud kahju) |
| `avatarPickles` | iga pickle'itud kutse salvestajamängijale, dekodeeritud, meetodi numbri järgi |

## Päis, tulemused ja kontrollid {#header-results-and-checks}

| Võti | Mis see on |
|---|---|
| `header` | esimene JSON-plokk, kõik peale nimekirja: mängurežiim, ilm, kaardi piir, meeskondade suurused ja veel |
| `moreBlocks` | esimesele järgnevad JSON-plokid, nii nagu need on |
| `blockIds` | 15.x: salvestajamängija konto ja lahingu ID, loetud tekstina |
| `results` | 15.x: tulemused, mida need kliendid hoiavad voos |
| `entities` | iga olem, mille voog loob: tema tüübi number ja roll, millal ta tuli kliendi vaatevälja ja millal lahkus |
| `selfCheck` | täielikkuse loendus ([Täielikkus](completeness.md)) ning olemite, tulemuste, ID-de ja versiooni kontrollid |

---

Osa [3DHeatist](https://github.com/Holdi601/3DHeat) ([dokumentatsioon](https://holdi601.github.io/3DHeat/)). Lähtekood: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
