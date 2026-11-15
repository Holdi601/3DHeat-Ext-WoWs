---
title: "Kompletezza"
nav_order: 8
lang: mt
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Kompletezza {#completeness}

Xejn f'ripetizzjoni ma jintrema. Dak li l-konvertitur jaqra jmur fit-tabella u
fid-dokument tal-partita; kull element ieħor jinżamm sħiħ fis-sidecar
`<match>.messages.parquet`; u `selfCheck.completeness` tad-dokument tal-partita
jgħodd x'sar minn kull tip ta' element. Din hija r-regola li jaqsmu l-konvertituri
kollha tad-3DHeat:
[Il-konvertituri jżommu kollox](https://holdi601.github.io/3DHeat/converters.html).

![L-awto-kontroll ta' ripetizzjoni sintetika: kull element li deher, ġie moqri, miżmum jew mitluf](../assets/img/completeness.svg)

## L-għadd {#the-count}

Għal kull tip ta' element, `selfCheck.completeness.types` jagħti:

| Għadd | Tfisser |
|---|---|
| `seen` | kemm fiha r-ripetizzjoni |
| `decoded` | moqri sħiħ |
| `partial` | moqri parzjalment, u miżmum sħiħ fis-sidecar |
| `raw` | miżmum sħiħ biss fis-sidecar, mhux moqri |
| `lost` | mitluf: dejjem `0` |

It-tipi huma dawk tar-ripetizzjoni nnifisha: `block <n>` (il-blokok JSON), il-bytes tal-kontenitur
nnifsu, `packet <type>`, u għal sejħiet fuq entitajiet `method <entity type>.<number>` u
`property <entity type>.<number>`. `selfCheck.entities.roles` jgħid liema tip ta' entità huwa
l-avatar tal-plejer li rreġistra u liema huma l-vapuri. Tip li ħadd ma kien jaf bih jidher bl-għadd tiegħu.

## Is-sidecar {#the-sidecar}

| Kolonna | X'inhi |
|---|---|
| `time` | l-arloġġ tar-ripetizzjoni, bħal fit-tabella |
| `type`, `name` | it-tip ta' element; kif isejjaħlu l-konvertitur, fejn jaqrah |
| `entity` | il-vapur jew l-avatar li jappartjeni lilu, bħall-`entity` tat-tabella |
| `decoded` | dak li ntqara minnu, bħala JSON |
| `payload`, `text` | il-bytes tiegħu, sħaħ; il-blokok JSON, sħaħ |
| `entityType`, `packet`, `method` | in-numri |

Ir-ringieli huma ordnati skont pakkett, metodu, entità u ħin. Liema entità hija liema plejer:
`entities` u `players` tad-dokument tal-partita.

## X'jinqara, u kif ġie kkontrollat {#what-is-read-and-how-it-was-checked}

- **Ir-riżultati** (15.x, `results`): l-id tal-battalja tagħhom huwa dak tal-fluss, u kull plejer
  fihom jinsab fir-roster tal-header.
- **Il-blokk tal-ids** (15.x, `blockIds`): il-kont u l-battalja, moqrija bħala test biex ebda
  ċifra ma tintilef.
- **Pitch u roll** ta' kull pożizzjoni: ir-roll imur mal-veloċità tal-iduru, hekk kif vapur
  jimtedd f'dawra; il-pitch kważi dejjem huwa 0.
- **Entitajiet** (`entities`): meta kull waħda daħlet fil-vista tal-klijent u ħarġet.
  Ebda vapur m'għandu pożizzjoni bejn meta joħroġ u meta jerġa' jiġi.
- **Il-verżjoni fil-fluss** (`streamVersion`): l-istess bħal dik tal-header.

Kull ħaġa oħra moqrija (għarqiet, ħsara, saħħa, qxur, torpidnijiet, fejn spiċċaw il-qxur, chat,
sejħiet pickled, ir-records tal-plejers, pożizzjonijiet) hija `partial`: fit-tabella jew fid-dokument
tal-partita, u miżmuma sħiħa fis-sidecar.

**Miżmum imma mhux moqri** (`raw`), l-akbar tipi: aġġornamenti tal-pożizzjoni li mhumiex
fit-tabella (wara li vapur għereq, entitajiet mingħajr plejer), il-proprjetajiet u l-metodi
frekwenti mingħajr qarrej, il-proprjetajiet tal-ħolqien tal-entitajiet, u kull pakkett ieħor mingħajr qarrej.

## Mhux disponibbli {#not-available}

- Dak li s-server qatt ma bagħat lill-klijent li rreġistra: l-aim, il-kamera u l-inputs
  ta' plejers oħra, l-għedewwa waqt li ma ġewx spotted. Ripetizzjoni hija dak li ntqal
  lil klijent wieħed.
- L-ismijiet tat-tipi tal-entitajiet, tal-metodi, tal-proprjetajiet u taċ-ċwievet tal-istatistika:
  jinsabu fil-fajls tad-definizzjoni tal-logħba, mhux fir-ripetizzjoni. In-numri jinżammu.
- L-ismijiet tal-vapuri għan-numri tal-vapuri (uża `--ship-names`), u kull ħaġa oħra li teħtieġ
  il-fajls proprji tal-logħba.
- Riżultati ta' klijenti qabel 15.x: mhumiex fir-ripetizzjonijiet tagħhom.

---

Parti mid-[3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentazzjoni](https://holdi601.github.io/3DHeat/)). Sors: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
