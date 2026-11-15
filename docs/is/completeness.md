---
title: "Heilleiki"
nav_order: 8
lang: is
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Heilleiki {#completeness}

Ekkert í upptöku er hent. Það sem umbreytirinn les fer í töfluna og
leikjaskjalið; hvert annað atriði er varðveitt í heild í hliðarskránni
`<match>.messages.parquet`; og `selfCheck.completeness` í leikjaskjalinu
telur hvað varð um hverja tegund atriða. Þetta er reglan sem allir 3DHeat
umbreytar deila:
[Umbreytar varðveita allt](https://holdi601.github.io/3DHeat/converters.html).

![Sjálfsathugun tilbúinnar upptöku: hvert atriði séð, lesið, varðveitt eða tapað](../assets/img/completeness.svg)

## Talningin {#the-count}

Fyrir hverja tegund atriða gefur `selfCheck.completeness.types`:

| Talning | Þýðir |
|---|---|
| `seen` | hversu mörg upptakan geymir |
| `decoded` | lesið í heild |
| `partial` | lesið að hluta, og varðveitt í heild í hliðarskránni |
| `raw` | aðeins varðveitt í heild í hliðarskránni, ekki lesið |
| `lost` | tapað: alltaf `0` |

Tegundirnar eru upptökunnar sjálfrar: `block <n>` (JSON-blokkirnar), eigin
bæti gámsins, `packet <type>`, og fyrir köll á einingar
`method <entity type>.<number>` og `property <entity type>.<number>`.
`selfCheck.entities.roles` segir hver einingartegund er avatar
upptökumannsins og hverjar eru skipin. Tegund sem enginn þekkti birtist með
talningu sinni.

## Hliðarskráin {#the-sidecar}

| Dálkur | Hvað |
|---|---|
| `time` | klukka upptökunnar, eins og í töflunni |
| `type`, `name` | tegund atriðisins; hvað umbreytirinn kallar það, þar sem hann les það |
| `entity` | skipið eða avatarinn sem það tilheyrir, eins og `entity` í töflunni |
| `decoded` | það sem var lesið úr því, sem JSON |
| `payload`, `text` | bæti þess, í heild; JSON-blokkirnar, í heild |
| `entityType`, `packet`, `method` | tölurnar |

Raðir eru raðaðar eftir pakka, aðferð, einingu og tíma. Hvaða eining er hvaða
spilari: `entities` og `players` í leikjaskjalinu.

## Hvað er lesið, og hvernig það var athugað {#what-is-read-and-how-it-was-checked}

- **Niðurstöðurnar** (15.x, `results`): bardagaauðkenni þeirra er straumsins, og
  hver spilari í þeim er í lista hausins yfir þátttakendur.
- **Auðkennablokkin** (15.x, `blockIds`): reikningurinn og bardaginn, lesið sem
  texti svo enginn tölustafur tapist.
- **Pitch og roll** hverrar stöðu: roll fylgir beygjuhraðanum, eins og skip hallast
  í beygju; pitch er nær alltaf 0.
- **Einingar** (`entities`): hvenær hver kom inn í sjónsvið biðlarans og fór úr því.
  Ekkert skip hefur stöðu milli þess að fara og koma aftur.
- **Útgáfan í straumnum** (`streamVersion`): sú sama og í hausnum.

Allt annað sem er lesið (sökkvanir, skaði, heilsa, skeljar, tundurskeyti, hvar
skeljar enduðu, spjall, pickle-köll, skrár spilaranna, stöður) er
`partial`: í töflunni eða leikjaskjalinu, og varðveitt í heild í
hliðarskránni.

**Varðveitt en ekki lesið** (`raw`), stærstu tegundirnar: stöðuuppfærslur sem eru ekki í
töflunni (eftir að skip sökk, einingar án spilara), tíðir
eiginleikar og aðferðir án lesara, eiginleikar einingarsköpunar,
og hver annar pakki án lesara.

## Ekki tiltækt {#not-available}

- Það sem þjónninn sendi aldrei upptökubiðlaranum: miðun, myndavél og
  inntak annarra spilara, óvinir meðan þeir eru ósénir. Upptaka er það sem einum biðlara
  var sagt.
- Nöfn einingartegunda, aðferða, eiginleika og lykla tölfræðinnar:
  þau eru í skilgreiningarskrám leiksins, ekki í upptökunni. Tölurnar
  eru varðveittar.
- Skipanöfn fyrir skipanúmerin (notaðu `--ship-names`), og allt annað
  sem þarf eigin skrár leiksins.
- Niðurstöður biðlara fyrir 15.x: ekki í upptökum þeirra.

---

Hluti af [3DHeat](https://github.com/Holdi601/3DHeat) ([skjölun](https://holdi601.github.io/3DHeat/)). Frumkóði: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
