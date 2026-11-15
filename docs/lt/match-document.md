---
title: Rungtynių dokumentas
nav_order: 6
lang: lt
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Rungtynių dokumentas {#the-match-document}

`<match>.match.json` laiko viską, ką įrašas sako ir kas nėra lentelės eilutė. Žiūryklės Rungtynių skirtukas
skaito jį. (Kode jis vadinamas santrauka.)

![The start of a synthetic match document, and its keys](../assets/img/match-document.svg)

## Mūšis {#the-battle}

| Raktas | Ką reiškia |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; mūšio id; žemėlapis, kaip jį vadina žaidimas (`spaces/<map>`), ir jo rodomas pavadinimas |
| `clientVersion`, `streamVersion` | žaidimo versija iš antraštės ir kaip ją nurodo paketų srautas |
| `recorded` | kada įrašas buvo įrašytas, kaip jį rašo žaidimas |
| `player`, `vehicle` | įrašantis žaidėjas ir jo laivas |
| `gameType`, `scenario` | mūšio tipas (`RandomBattle`, ...) ir scenarijus, iš antraštės |
| `duration` | mūšio laiko riba sekundėmis, iš antraštės |
| `truncated` | įrašymas sustojo anksti |
| `battleStart`, `recordingSeconds` | mūšio pradžia (pirmoji akimirka, kai kuris nors laivas pajuda) ir įrašo ilgis sekundėmis |
| `positionPacket`, `ownPositionPacket` | paketų numeriai, kuriuose atėjo pozicijos: kitų laivų ir įrašančio žaidėjo |
| `deathMethod` | metodo numeris, kuriame rasti nuskandinimai |
| `hz`, `ownHz`, `positions` | pavyzdžiai per sekundę kitiems laivams ir savajam; pozicijų eilutės |
| `units` | pasaulio vienetai (15 m pagal korpusus, 30 m pagal žaidimo nuotolius); x - į rytus, y - aukštyn, z - į šiaurę |
| `events` | kiekvieno įvykio lentelės eilučių skaičius |
| `decoded` | metodo ir paketo numeriai, rasti kiekvienai pranešimų rūšiai |

## Žaidėjai ir įvykiai {#players-and-events}

| Raktas | Ką reiškia |
|---|---|
| `players` | vienas įrašas laivui: vardas, `ally` arba `enemy`, laivo numeris ir vardas, esybė, pavyzdžiai, nužudymai, ar išgyveno; `seen` (padaryta ir gauta žala, sviediniai, torpedos ir paskutinė sveikata, kurią matė klientas); `header` (sąrašo įrašas) ir `record` (žaidėjo įrašas iš srauto, pagal raktą su numeriu) |
| `kills` | kiekvienas nuskandinimas: laikas, auka, žudikas, priežasties numeris, vieta |
| `chat` | kiekviena pokalbio eilutė, su kanalu ir siuntėju |
| `damageStats` | įrašančio žaidėjo paties statistika, kaip ją saugo žaidimas: pagal ginklą ir rūšį, skaičius ir suma (0 rūšis yra padaryta žala) |
| `avatarPickles` | kiekvienas įrašančiam žaidėjui skirtas užšifruotas iškvietimas, iššifruotas, pagal metodo numerį |

## Antraštė, rezultatai ir patikrinimai {#header-results-and-checks}

| Raktas | Ką reiškia |
|---|---|
| `header` | pirmasis JSON blokas, visas, išskyrus sąrašą: žaidimo režimas, oras, žemėlapio riba, komandų dydžiai ir dar |
| `moreBlocks` | JSON blokai po pirmojo, kaip jie yra |
| `blockIds` | 15.x: įrašančio žaidėjo paskyra ir mūšio id, perskaityti kaip tekstas |
| `results` | 15.x: rezultatai, kuriuos šie klientai saugo sraute |
| `entities` | kiekviena esybė, kurią sukuria srautas: jos tipo numeris ir vaidmuo, kada ji pateko į kliento matymo lauką ir kada išėjo |
| `selfCheck` | pilnumo skaičiai ([Pilnumas](completeness.md)) ir esybių, rezultatų, id ir versijos patikrinimai |

---

Dalis [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Šaltinis: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
