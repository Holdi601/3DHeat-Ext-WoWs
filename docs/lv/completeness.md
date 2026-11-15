---
title: Pilnība
nav_order: 8
lang: lv
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Pilnība {#completeness}

Neviens atkārtojuma saturs netiek izmests. Ko konvertētājs nolasa, nonāk tabulā un mača dokumentā; katrs cits vienums tiek paturēts pilnībā papildfailā `<match>.messages.parquet`; un mača dokumenta `selfCheck.completeness` skaita, kas notika ar katru vienuma veidu. Tas ir noteikums, ko ievēro visi 3DHeat konvertētāji: [Konvertētāji saglabā visu](https://holdi601.github.io/3DHeat/converters.html).

![Pašpārbaude sintētiskam atkārtojumam: katrs redzētais vienums, nolasīts, paturēts vai zaudēts](../assets/img/completeness.svg)

## Skaits {#the-count}

Katram vienuma veidam `selfCheck.completeness.types` dod:

| Skaits | Nozīmē |
|---|---|
| `seen` | cik to atkārtojumā ir |
| `decoded` | nolasīti pilnībā |
| `partial` | nolasīti daļēji un paturēti pilnībā papildfailā |
| `raw` | tikai paturēti pilnībā papildfailā, nav nolasīti |
| `lost` | zaudēti: vienmēr `0` |

Veidi ir paša atkārtojuma: `block <n>` (JSON bloki), konteinera paša baiti, `packet <type>`, un izsaukumiem uz entītijām `method <entity type>.<number>` un `property <entity type>.<number>`. `selfCheck.entities.roles` saka, kurš entītijas tips ir ieraksta spēlētāja avatārs un kurš — kuģi. Veids, par kuru neviens nezināja, parādās ar savu skaitu.

## Papildfails {#the-sidecar}

| Kolonna | Ko tā nozīmē |
|---|---|
| `time` | atkārtojuma pulkstenis, kā tabulā |
| `type`, `name` | vienuma veids; ko konvertētājs to sauc un kur to nolasa |
| `entity` | kuģis vai avatārs, kam tas pieder, kā tabulas `entity` |
| `decoded` | kas no tā nolasīts, kā JSON |
| `payload`, `text` | tā baiti, pilnībā; JSON bloki, pilnībā |
| `entityType`, `packet`, `method` | numuri |

Rindas tiek sakārtotas pēc paketes, metodes, entītijas un laika. Kurš entītijas numurs ir kurš spēlētājs: mača dokumenta `entities` un `players`.

## Ko lasa un kā tas pārbaudīts {#what-is-read-and-how-it-was-checked}

- **Rezultāti** (15.x, `results`): to kaujas ID ir tāds pats kā straumes, un katrs spēlētājs tajos ir galvenes sastāvā.
- **ID bloks** (15.x, `blockIds`): konts un kauja, nolasīti kā teksts, lai neviens cipars nepazustu.
- **Pitch un roll** katrai pozīcijai: roll iet kopā ar pagrieziena ātrumu, kā kuģis sašķiebjas pagriezienā; pitch gandrīz vienmēr ir 0.
- **Entītijas** (`entities`): kad katra ienāca klienta redzeslokā un aizgāja no tā. Neviens kuģis nav pozīcijā starp aiziešanu un atgriešanos.
- **Versija straumē** (`streamVersion`): tā pati kā galvenē.

Viss pārējais, kas nolasīts (nogrimšanas, bojājumi, veselība, čaulas, torpēdas, vieta, kur čaulas beidzās, tērzēšana, pickled izsaukumi, spēlētāju ieraksti, pozīcijas), ir `partial`: tabulā vai mača dokumentā, un paturēts pilnībā papildfailā.

**Paturēts, bet nav nolasīts** (`raw`), lielākie veidi: pozīciju atjauninājumi, kas nav tabulā (pēc kuģa nogrimšanas, entītijas bez spēlētāja), bieži īpašības un metodes bez lasītāja, entītiju izveides īpašības un katra cita paketes, kam nav lasītāja.

## Nav pieejams {#not-available}

- Tas, ko serveris nekad nenosūtīja ierakstošajam klientam: citu spēlētāju tēmēšana, kamera un ievades, ienaidnieki, kamēr tie nav pamanīti. Atkārtojums ir tas, ko viens klients tika pateicis.
- Entītiju tipu, metožu, īpašību un statistikas atslēgu nosaukumi: tie ir spēles definīciju failos, ne atkārtojumā. Numuri ir paturēti.
- Kuģu nosaukumi kuģu numuriem (izmanto `--ship-names`) un viss cits, kam vajadzīgi spēles paši faili.
- 15.x priekšā esošo klientu rezultāti: to atkārtojumos tādu nav.

---

Daļa no [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentācija](https://holdi601.github.io/3DHeat/)). Avots: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
