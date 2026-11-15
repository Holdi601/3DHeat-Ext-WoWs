---
title: Iomláine
nav_order: 8
lang: "ga"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Iomláine {#completeness}

Ní chaitear aon rud in athsheinm uait. Téann an méid a léann an tiontaire isteach sa tábla agus sa cháipéis chluiche; coinnítear gach mír eile iomlán sa chomhad cliatháin `<match>.messages.parquet`; agus comhairíonn `selfCheck.completeness` na cáipéise cluiche cad a tharla do gach cineál míre. Is é seo an riail a roinneann gach tiontaire 3DHeat: [Coimeádann tiontairí gach rud](https://holdi601.github.io/3DHeat/converters.html).

![Féinseiceáil athsheinm sintéisigh: gach mír a chonacthas, a léadh, a coinníodh nó a cailleadh](../assets/img/completeness.svg)

## An comhaireamh {#the-count}

Do gach cineál míre, tugann `selfCheck.completeness.types`:

| Comhaireamh | Ciallaíonn sé |
|---|---|
| `seen` | cé mhéad atá san athsheinm |
| `decoded` | léite iomlán |
| `partial` | léite i bpáirt, agus coinnithe iomlán sa chomhad cliatháin |
| `raw` | coinnithe iomlán sa chomhad cliatháin amháin, gan léamh |
| `lost` | caillte: i gcónaí `0` |

Is iad cineálacha na hathsheinme féin iad na cineálacha: `block <n>` (na bloic JSON), beartanna féin an choimeádáin, `packet <type>`, agus do ghlaonna ar eintitis `method <entity type>.<number>` agus `property <entity type>.<number>`. Deir `selfCheck.entities.roles` cén cineál eintitis avatar an imreora taifeadta agus cé acu na longa. Taispeántar cineál nach raibh ar eolas ag aon duine lena chomhaireamh.

## An comhad cliatháin {#the-sidecar}

| Colún | Cad é |
|---|---|
| `time` | clog na hathsheinme, mar atá sa tábla |
| `type`, `name` | an cineál míre; an t-ainm a thugann an tiontaire air, nuair a léann sé é |
| `entity` | an long nó an avatar dá mbaineann sé, mar `entity` an tábla |
| `decoded` | an méid a léadh de, mar JSON |
| `payload`, `text` | a bheartanna, iomlán; na bloic JSON, iomlán |
| `entityType`, `packet`, `method` | na huimhreacha |

Sórtáiltear sraitheanna de réir paicéid, modha, eintitis agus ama. Cén t-eintiteas cén t-imreoir: `entities` agus `players` na cáipéise cluiche.

## Cad a léitear, agus conas a seiceáladh é {#what-is-read-and-how-it-was-checked}

- **Na torthaí** (15.x, `results`): is é a n-id catha id an tsrutha, agus tá gach imreoir iontu i rolla an cheanntáisc.
- **An bloc id** (15.x, `blockIds`): an cuntas agus an cath, léite mar théacs ionas nach gcailltear digit ar bith.
- **Pitch agus roll** gach suímh: téann an roll le ráta an chasta, mar a chlaonann long i gcasadh; is 0 é an pitch beagnach i gcónaí.
- **Eintitis** (`entities`): cathain a tháinig gach ceann isteach i radharc an chliaint agus d'fhág. Níl aon suíomh ag long ar bith idir imeacht agus teacht ar ais.
- **An leagan sa sruth** (`streamVersion`): mar an gcéanna le leagan an cheanntáisc.

Tá gach rud eile a léadh (báthadh, damáiste, sláinte, sliogáin, torpéidí, cá ndeachaigh sliogáin chun deiridh, comhrá, glaonna picilte, taifid na n-imreoirí, suíomhanna) `partial`: sa tábla nó sa cháipéis chluiche, agus coinnithe iomlán sa chomhad cliatháin.

**Coinnithe ach gan léamh** (`raw`), na cineálacha is mó: nuashonruithe suímh nach bhfuil sa tábla (tar éis báite loinge, eintitis gan imreoir), na hairíonna agus na modhanna minice gan léitheoir, airíonna cruthaithe eintiteas, agus gach paicéad eile gan léitheoir.

## Gan a bheith ar fáil {#not-available}

- An méid nár sheol an freastalaí chuig an gcliant taifeadta riamh: aim, ceamara agus ionchuir imreoirí eile, naimhde nuair nár aimsíodh iad. Is é athsheinm an méid a dúradh le cliant amháin.
- Ainmneacha cineálacha eintitis, modhanna, airíonna agus eochracha na staitisticí: tá siad i gcomhaid shainmhínithe an chluiche, ní san athsheinm. Coinnítear na huimhreacha.
- Ainmneacha long d'uimhreacha na long (úsáid `--ship-names`), agus aon rud eile a theastaíonn comhaid féin an chluiche.
- Torthaí cliaint roimh 15.x: níl siad ina n-athsheinmeanna.

---

Cuid de [3DHeat](https://github.com/Holdi601/3DHeat) ([doiciméadúchán](https://holdi601.github.io/3DHeat/)). Foinse: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
