---
title: Popolnost
nav_order: 8
lang: "sl"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Popolnost {#completeness}

Nič v posnetku se ne zavrže. Kar pretvornik prebere, gre v tabelo in dokument tekme; vsak drug del se
ohrani celo v spremljevalni datoteki `<match>.messages.parquet`; `selfCheck.completeness` v dokumentu tekme
šteje, kaj se je zgodilo z vsako vrsto dela. To je pravilo, ki ga delijo vsi pretvorniki 3DHeat:
[Pretvorniki ohranijo vse](https://holdi601.github.io/3DHeat/converters.html).

![Samopreverjanje sintetičnega posnetka: vsak del viden, prebran, ohranjen ali izgubljen](../assets/img/completeness.svg)

## Števila {#the-count}

Za vsako vrsto dela `selfCheck.completeness.types` navaja:

| Število | Pomeni |
|---|---|
| `seen` | koliko jih posnetek vsebuje |
| `decoded` | prebrano celo |
| `partial` | prebrano delno in ohranjeno celo v spremljevalni datoteki |
| `raw` | samo ohranjeno celo v spremljevalni datoteki, ni prebrano |
| `lost` | izgubljeno: vedno `0` |

Vrste so posnetkove lastne: `block <n>` (bloki JSON), lastni bajti vsebnika, `packet <type>`, za klice na
entitetah pa `method <entity type>.<number>` in `property <entity type>.<number>`. `selfCheck.entities.roles`
pove, kateri tip entitete je avatar igralca, ki je snemal, in kateri so ladje. Vrsta, ki je ni nihče poznal,
se pokaže s svojim številom.

## Spremljevalna datoteka {#the-sidecar}

| Stolpec | Kaj |
|---|---|
| `time` | ura posnetka, kot v tabeli |
| `type`, `name` | vrsta dela; kako ga pretvornik imenuje, kjer ga bere |
| `entity` | ladja ali avatar, kateremu pripada, kot `entity` v tabeli |
| `decoded` | kar je bilo prebrano iz njega, kot JSON |
| `payload`, `text` | njegovi bajti, celi; bloki JSON, celi |
| `entityType`, `packet`, `method` | številke |

Vrstice so razvrščene po paketu, metodi, entiteti in času. Katera entiteta je kateri igralec: `entities` in
`players` v dokumentu tekme.

## Kaj se bere in kako je bilo preverjeno {#what-is-read-and-how-it-was-checked}

- **Rezultati** (15.x, `results`): njihov identifikator bitke je tisti iz toka, vsak igralec v njih pa je na
  seznamu iz glave.
- **Blok identifikatorjev** (15.x, `blockIds`): račun in bitka, prebrana kot besedilo, da se ne izgubi nobena
  številka.
- **Naklon in zvitek** vsake pozicije: zvitek gre z hitrostjo zavijanja, kakor se ladja nagiba v zavoju;
  naklon je skoraj vedno 0.
- **Entitete** (`entities`): kdaj je vsaka prišla v pogled odjemalca in kdaj ga je zapustila. Nobena ladja
  nima položaja med odhodom in vrnitvijo.
- **Različica v toku** (`streamVersion`): enaka kot v glavi.

Vse drugo, kar je prebrano (potopitve, poškodbe, zdravje, izstrelki, torpedi, kje so se izstrelki končali,
klepet, vzete klice, zapisi igralcev, položaji), je `partial`: v tabeli ali dokumentu tekme in celo v
spremljevalni datoteki.

**Ohranjeno, a ni prebrano** (`raw`), največje vrste: posodobitve položajev, ki niso v tabeli (potem ko je
ladja potonila, entitete brez igralca), pogoste lastnosti in metode brez bralnika, lastnosti ustvarjanja
entitet ter vsak drug paket brez bralnika.

## Ni na voljo {#not-available}

- Kar strežnik nikoli ni poslal odjemalcu, ki je snemal: cilji drugih igralcev, kamera in vnosi, sovražniki,
  dokler niso opaženi. Posnetek je tisto, kar je bilo povedano enemu odjemalcu.
- Imena tipov entitet, metod, lastnosti in ključev statistike: so v datotekah definicij igre, ne v posnetku.
  Števila se hranijo.
- Imena ladij za številke ladij (uporabite `--ship-names`) in vse drugo, kar potrebuje igrine lastne datoteke.
- Rezultati odjemalcev pred 15.x: v njihovih posnetkih jih ni.

---

Del [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Vir: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
