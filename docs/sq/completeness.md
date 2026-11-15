---
title: "Plotësia"
nav_order: 8
lang: "sq"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Plotësia {#completeness}

Asgjë në një riluajtje nuk hidhet tutje. Çfarë lexon konvertuesi shkon në
tabelë dhe në dokumentin e ndeshjes; çdo element tjetër ruhet i plotë në skedarin anësor
`<match>.messages.parquet`; dhe `selfCheck.completeness` i dokumentit të ndeshjes
numëron çfarë u bë me çdo lloj elementi. Ky është rregulli që ndajnë të gjithë
konvertuesit e 3DHeat:
[Konvertuesit ruajnë gjithçka](https://holdi601.github.io/3DHeat/converters.html).

![Vetëkontrolli i një riluajtjeje sintetike: çdo element i parë, i lexuar, i ruajtur ose i humbur](../assets/img/completeness.svg)

## Numërimi {#the-count}

Për çdo lloj elementi, `selfCheck.completeness.types` jep:

| Numri | Do të thotë |
|---|---|
| `seen` | sa mban riluajtja |
| `decoded` | lexuar i plotë |
| `partial` | lexuar pjesërisht, dhe ruajtur i plotë në skedarin anësor |
| `raw` | vetëm ruajtur i plotë në skedarin anësor, jo i lexuar |
| `lost` | humbur: gjithmonë `0` |

Llojet janë të vetë riluajtjes: `block <n>` (blloqet JSON), bajtët e vetë
kontejnerit, `packet <type>`, dhe për thirrjet mbi entitete
`method <entity type>.<number>` dhe `property <entity type>.<number>`.
`selfCheck.entities.roles` thotë cili lloj entiteti është avatari i lojtarit
që regjistron dhe cili janë anijet. Një lloj që askush nuk e njihte shfaqet me
numrin e vet.

## Skedari anësor {#the-sidecar}

| Kolona | Çfarë |
|---|---|
| `time` | ora e riluajtjes, si në tabelë |
| `type`, `name` | lloji i elementit; si e quan konvertuesi, aty ku e lexon |
| `entity` | anija ose avatari të cilit i përket, si `entity` i tabelës |
| `decoded` | çfarë u lexua prej tij, si JSON |
| `payload`, `text` | bajtët e tij, të plotë; blloqet JSON, të plota |
| `entityType`, `packet`, `method` | numrat |

Rreshtat renditen sipas paketës, metodës, entitetit dhe kohës. Cili entitet është cili
lojtar: `entities` dhe `players` të dokumentit të ndeshjes.

## Çfarë lexohet, dhe si u kontrollua {#what-is-read-and-how-it-was-checked}

- **Rezultatet** (15.x, `results`): ID e betejës së tyre është ajo e rrjedhës, dhe
  çdo lojtar në to është në listën e header-it.
- **Blloku i ID-ve** (15.x, `blockIds`): llogaria dhe beteja, lexuar si
  tekst që të mos humbasë asnjë shifër.
- **Pitch dhe roll** i çdo pozicioni: roll shkon me shpejtësinë e kthesës,
  pasi një anije anohet në kthesë; pitch është pothuajse gjithmonë 0.
- **Entitetet** (`entities`): kur hyri secili në pamjen e klientit dhe kur doli.
  Asnjë anije nuk ka pozicion midis daljes dhe kthimit.
- **Versioni në rrjedhë** (`streamVersion`): i njëjti me atë të header-it.

Çdo gjë tjetër e lexuar (fundosjet, dëmi, shëndeti, predhat, silurët, ku mbaruan
predhat, biseda, thirrjet pickle, regjistrat e lojtarëve, pozicionet) është
`partial`: në tabelë ose në dokumentin e ndeshjes, dhe e ruajtur e plotë në skedarin
anësor.

**Të ruajtura por të palexuara** (`raw`), llojet më të mëdha: përditësimet e pozicionit që nuk janë në
tabelë (pasi një anije u fundos, entitetet pa lojtar), vetitë dhe metodat e
shpeshta pa lexues, vetitë e krijimeve të entiteteve, dhe çdo paketë tjetër pa lexues.

## Të padisponueshme {#not-available}

- Çfarë serveri nuk i dërgoi kurrë klientit që regjistron: synimi, kamera
  dhe hyrjet e lojtarëve të tjerë, armiqtë ndërsa nuk ishin të zbuluar. Një riluajtje është çfarë
  iu tha një klienti.
- Emrat e llojeve të entiteteve, metodave, vetive dhe çelësave të statistikave:
  janë në skedarët e përkufizimit të lojës, jo në riluajtje. Numrat
  ruhen.
- Emrat e anijeve për numrat e anijeve (përdor `--ship-names`), dhe çdo gjë tjetër
  që kërkon skedarët e vetë lojës.
- Rezultatet e klientëve para 15.x: nuk janë në riluajtjet e tyre.

---

Pjesë e [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacioni](https://holdi601.github.io/3DHeat/)). Burimi: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
