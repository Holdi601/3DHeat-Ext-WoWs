---
title: Täielikkus
nav_order: 8
lang: et
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Täielikkus {#completeness}

Kordusest ei visata midagi ära. See, mida konverter loeb, läheb tabelisse ja mängu dokumenti; kõik muu hoitakse
tervena lisafailis `<match>.messages.parquet`, ja mängu dokumendi `selfCheck.completeness` loeb, mis sai igast
liigist. See on reegel, mida jagavad kõik 3DHeati konverterid:
[Konverterid hoiavad kõike](https://holdi601.github.io/3DHeat/converters.html).

![Synteetilise kordase enesekontroll: iga üksus nähtud, loetud, alles hoitud või kadunud](../assets/img/completeness.svg)

## Loendus {#the-count}

Iga liigi kohta annab `selfCheck.completeness.types`:

| Loend | Tähendab |
|---|---|
| `seen` | mitu seda kordus sisaldab |
| `decoded` | loetud tervena |
| `partial` | loetud osaliselt ja hoitud lisafailis tervena |
| `raw` | ainult lisafailis tervena hoitud, mitte loetud |
| `lost` | kadunud: alati `0` |

Liigid on kordusest endast: `block <n>` (JSON-plokid), konteineri enda baidid, `packet <type>`, ning olemite
kutsete puhul `method <entity type>.<number>` ja `property <entity type>.<number>`. `selfCheck.entities.roles`
ütleb, milline olemi tüüp on salvestajamängija avatar ja milline laevad. Liik, mida keegi ei tundnud, ilmub oma
loendusega.

## Lisafail {#the-sidecar}

| Veerg | Mis see on |
|---|---|
| `time` | kordusa kell, nagu tabelis |
| `type`, `name` | üksuse liik; mida konverter selle nimetab, kus ta seda loeb |
| `entity` | laev või avatar, kuhu see kuulub, nagu tabeli `entity` |
| `decoded` | mis sellest loeti, JSON-ina |
| `payload`, `text` | tema baidid tervena; JSON-plokid tervena |
| `entityType`, `packet`, `method` | numbrid |

Read on sorteeritud paketi, meetodi, olemi ja aja järgi. Kumb olem on kumb mängija: mängu dokumendi `entities` ja
`players`.

## Mida loetakse ja kuidas kontrolliti {#what-is-read-and-how-it-was-checked}

- **Tulemused** (15.x, `results`): nende lahingu ID on voo oma ja iga mängija neis on päise nimekirjas.
- **ID-plokk** (15.x, `blockIds`): konto ja lahing, loetud tekstina, nii et ükski number ei kao.
- **Tõus ja rull** igal asukohal: rull käib pöörde kiirusega, nagu laev pöörates kallub; tõus on peaaegu alati 0.
- **Olemid** (`entities`): millal kumbki tuli kliendi vaatevälja ja lahkus sealt. Ühelgi laeval ei ole asukohta
  lahkumise ja tagasituleku vahel.
- **Voo versioon** (`streamVersion`): sama, mis päises.

Kõik muu loetu (uppumised, kahju, tervis, mürsud, torpeedod, kohad, kus mürsud lõppesid, vestlus, kurnatud kutsed,
mängijate kirjed, asukohad) on `partial`: tabelis või mängu dokumendis ning lisafailis tervena.

**Hoitud, aga mitte loetud** (`raw`), suurimad liigid: asukohauuendused, mida tabelis ei ole (pärast laeva
uppumist, olemid ilma mängijata), sagedased omadused ja meetodid ilma lugejata, olemite loomise omadused ning iga
muu pakett ilma lugejata.

## Pole saadaval {#not-available}

- Mida server ei saatnud kunagi salvestavale kliendile: teiste mängijate siht, kaamera ja sisendid, vaenlased,
  kui neid pole avastatud. Kordus on see, mida üks klient sai teada.
- Olemi tüüpide, meetodite, omaduste ja statistika võtmete nimed: need on mängu definitsioonifailides, mitte
  kordusses. Numbrid on alles.
- Laevade nimed laevanumbrite järgi (kasuta `--ship-names`), ja kõik muu, mis vajab mängu enda faile.
- Enne 15.x klientide tulemused: nende kordustes neid ei ole.

---

Osa [3DHeatist](https://github.com/Holdi601/3DHeat) ([dokumentatsioon](https://holdi601.github.io/3DHeat/)). Lähtekood: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
