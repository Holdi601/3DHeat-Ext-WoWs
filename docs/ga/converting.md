---
title: Athsheinmeanna a thiontú
nav_order: 4
lang: ga
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Athsheinmeanna a thiontú {#converting-replays}

## Céim ar chéim {#step-by-step}

1. **Cuir taifeadadh ar siúl**: `isReplayEnabled` i `preferences.xml` an chluiche, nó socrú an chluiche féin nuair atá ceann aige. As sin amach sábhálann an cluiche gach cath i bhfillteán `replays` do shuiteála World of Warships, mar shampla `C:\Games\World_of_Warships_EU\replays`.
2. **Oscail teirminéal** i bhfillteán inar féidir na torthaí a chur ([Sula dtosaíonn tú](before-you-start.md)).
3. **Rith an tiontaire** ar chomhaid athsheinm, nó ar fhillteáin ina bhfuil siad:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   Déantar `out` sa fhillteán a bhfuil do theirminéal ann.
4. **Léigh an méid a deir sé.** Ba cheart duit líne amháin a fheiceáil do gach athsheinm, ag críochnú leis an tábla a scríobh sé.
5. **Oscail an toradh** i bhfaire 3DHeat: `out/<map>/<match>.parquet` sa chluaisín Léarscáil teasa, `<match>.match.json` sa chluaisín Cluiche. Nó léigh iad le léitheoir Parquet nó JSON ar bith.

![Rith ar athsheinm shintéiseach: tiontú, rith arís, comhad briste, fillteán folamh](../assets/img/convert.svg)

Is rith é an pictiúr ar athsheinm a thógann na tástálacha sa chód (gan athsheinm fíor):

- athsheinm tiontaithe: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- rith arís, preabtar thar an gcluiche atá scríofa cheana: `<file>: already written, <table>`;
- comhad nach athsheinm é: `<file>: not converted: <why>` (ar an aschur earráide; stádas scoir 1, tiontaítear na hathsheinmeanna eile ar aon nós);
- níor aimsíodh aon athsheinm: `no .wowsreplay files in <folders>` (stádas scoir 2).

## Roghanna {#options}

| Rogha | Réamhshocrú | Cad a dhéanann sí |
|---|---|---|
| `replays` (ceann amháin nó níos mó) | - | comhaid `.wowsreplay`, nó fillteáin a ndéantar cuardach iontu orthu (fo-fhillteáin freisin) |
| `-o`, `--out` | riachtanach | an fillteán inar scríobhfar: fillteán do gach léarscáil istigh |
| `--force` | as | tiontaigh arís an méid atá scríofa cheana |
| `--ship-names JSON` | - | comhad JSON `{"<shipId>": "<name>", ...}`: ní ainmníonn athsheinmeanna ach long an imreora taifeadta, na cinn eile de réir uimhreach |
| `--version` | - | priontáil `heat3d-wows-replay <version>` agus stop |
| `-h`, `--help` | - | priontáil na roghanna agus stop |

Na roghanna mar a phriontálann an clár iad: [Tagairt orduithe](../cli-reference.md).

## Cad a scríobhtar {#what-is-written}

Comhaid scaoilte amháin: ní scríobhann an tiontaire seo aon chomhad `.3dheat` (is féidir leis an bhfaire iad a phacáil i gcomhad amháin: [Comhad amháin an cluiche](https://holdi601.github.io/3DHeat/container.html)). In aghaidh an athsheinm, isteach i `out/<map>/` (ainm na léarscáile gan a `spaces/`):

| Comhad | Cad é |
|---|---|
| `<match>.parquet` | an tábla: suíomh gach loinge le himeacht ama agus gach imeacht san áit ar tharla sé ([An tábla](table.md)) |
| `<match>.match.json` | an cháipéis chluiche: léarscáil, leagan cliaint, imreoirí, báthadh, comhrá agus gach rud eile ([An cháipéis chluiche](match-document.md)) |
| `<match>.messages.parquet` | an comhad cliatháin: gach mír den athsheinm nach gcoinníonn an dá chomhad thuas iomlán ([Iomláine](completeness.md)) |

Is é `<match>` id féin an chatha, nó ainm an chomhaid nuair a stop an taifeadadh roimh na torthaí.

## Stádas scoir {#exit-status}

`0` nuair a tiontaíodh nó a preabadh thar gach athsheinm, `1` nuair a theip ar aon cheann (tiontaítear an chuid eile ar aon nós), `2` nuair nár aimsíodh aon chomhad athsheinm.

---

Cuid de [3DHeat](https://github.com/Holdi601/3DHeat) ([doiciméadúchán](https://holdi601.github.io/3DHeat/)). Foinse: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
