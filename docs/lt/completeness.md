---
title: Pilnumas
nav_order: 8
lang: lt
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Pilnumas {#completeness}

Niekas įraše neišmetama. Tai, ką konverteris perskaito, patenka į lentelę ir rungtynių dokumentą; kiekvienas
kitas elementas išsaugomas pilnai papildomame faile `<match>.messages.parquet`; o rungtynių dokumento
`selfCheck.completeness` suskaičiuoja, kas nutiko kiekvienos rūšies elementui. Tai taisyklė, kurios laikosi visi
3DHeat konverteriai: [Konverteriai išsaugo viską](https://holdi601.github.io/3DHeat/converters.html).

![The self-check of a synthetic replay: every item seen, read, kept or lost](../assets/img/completeness.svg)

## Skaičius {#the-count}

Kiekvienai elementų rūšiai `selfCheck.completeness.types` pateikia:

| Skaičius | Reiškia |
|---|---|
| `seen` | kiek jų yra įraše |
| `decoded` | perskaityta pilnai |
| `partial` | perskaityta iš dalies, o pilnai išsaugota papildomame faile |
| `raw` | tik pilnai išsaugota papildomame faile, neskaityta |
| `lost` | prarasta: visada `0` |

Rūšys yra paties įrašo: `block <n>` (JSON blokai), paties konteinerio baitai, `packet <type>`, o esybių
iškvietimams - `method <entity type>.<number>` ir `property <entity type>.<number>`.
`selfCheck.entities.roles` nurodo, kuris esybės tipas yra įrašančio žaidėjo avataras, o kuris - laivai. Rūšis,
apie kurią niekas nežinojo, pasirodo su savo skaičiumi.

## Papildomas failas {#the-sidecar}

| Stulpelis | Ką reiškia |
|---|---|
| `time` | įrašo laikrodis, kaip lentelėje |
| `type`, `name` | elemento rūšis; kaip konverteris jį vadina ir kur jį skaito |
| `entity` | laivas ar avataras, kuriam jis priklauso, kaip lentelės `entity` |
| `decoded` | kas buvo perskaityta, JSON formatu |
| `payload`, `text` | jo baitai, pilnai; JSON blokai, pilnai |
| `entityType`, `packet`, `method` | skaičiai |

Eilutės surūšiuotos pagal paketą, metodą, esybę ir laiką. Kuri esybė yra kuris žaidėjas: rungtynių dokumento
`entities` ir `players` skiltys.

## Ką skaitome ir kaip tai patikrinta {#what-is-read-and-how-it-was-checked}

- **Rezultatai** (15.x, `results`): jų mūšio id sutampa su srauto id, o kiekvienas juose esantis žaidėjas yra
  antraštės sąraše.
- **Id blokas** (15.x, `blockIds`): paskyra ir mūšis, perskaityti kaip tekstas, kad neprarastų nė vieno skaitmens.
- **Kėlimas ir posūkis** kiekvienos pozicijos: posūkis eina kartu su laivo sukimosi greičiu, nes laivas posūkyje
  pasvyra; kėlimas beveik visada 0.
- **Esybės** (`entities`): kada kiekviena pateko į kliento matymo lauką ir kada iš jo išėjo. Joks laivas nėra
  pozicijoje tarp išėjimo ir grįžimo.
- **Versija srautuose** (`streamVersion`): tokia pati kaip antraštės.

Viskas kita, kas perskaityta (nuskandinimai, žala, sveikata, sviediniai, torpedos, kur baigėsi sviediniai, pokalbis,
užšifruoti iškvietimai, žaidėjų įrašai, pozicijos), yra `partial`: lentelėje arba rungtynių dokumente, ir pilnai
išsaugota papildomame faile.

**Išsaugota, bet neskaityta** (`raw`), didžiausios rūšys: pozicijų atnaujinimai, kurių nėra lentelėje (kai laivas
nuskendo, esybės be žaidėjo), dažnai kintančios savybės ir metodai be skaitytuvo, esybių sukūrimų savybės ir kiekvienas
kitas paketas be skaitytuvo.

## Nėra prieinama {#not-available}

- Tai, ko serveris niekada nesiuntė įrašančiam klientui: kitų žaidėjų taikymas, kamera ir įvestys, priešai, kol jie
  nepastebėti. Įrašas - tai tai, ką vienas klientas buvo pasakytas.
- Esybių tipų, metodų, savybių ir statistikos raktų vardai: jie yra žaidimo apibrėžimų failuose, o ne įraše.
  Skaičiai išsaugomi.
- Laivų vardai pagal laivų numerius (naudokite `--ship-names`) ir viskas kita, kam reikia žaidimo paties failų.
- Rezultatai klientų, senesnių nei 15.x: jų įrašuose jų nėra.

---

Dalis [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Šaltinis: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
