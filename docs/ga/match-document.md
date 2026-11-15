---
title: An cháipéis chluiche
nav_order: 6
lang: "ga"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# An cháipéis chluiche {#the-match-document}

Coinníonn `<match>.match.json` gach rud a deir an athsheinm nach sraith den tábla é. Léann cluaisín Cluiche an amharcáin é. (Glaonn an cód an achoimre air.)

![Tús cáipéise cluiche sintéisigh, agus a heochracha](../assets/img/match-document.svg)

## An cath {#the-battle}

| Eochair | Cad é |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; id an chatha; an léarscáil mar a ainmníonn an cluiche í (`spaces/<map>`) agus a hainm taispeána |
| `clientVersion`, `streamVersion` | leagan an chluiche ón gceanntásc, agus mar a deir an sruth paicéad é |
| `recorded` | cathain a taifeadadh an athsheinm, mar a scríobhann an cluiche é |
| `player`, `vehicle` | an t-imreoir taifeadta agus a long |
| `gameType`, `scenario` | cineál an chatha (`RandomBattle`, ...) agus an cás, ón gceanntásc |
| `duration` | teorainn ama an chatha i soicindí, ón gceanntásc |
| `truncated` | stop an taifeadadh go luath |
| `battleStart`, `recordingSeconds` | tús an chatha (an chéad nóiméad a ghluaiseann long ar bith) agus fad an taifeadta, i soicindí |
| `positionPacket`, `ownPositionPacket` | uimhreacha na bpaicéad inar tháinig na suíomhanna: longa eile, an t-imreoir taifeadta |
| `deathMethod` | uimhir an mhodha inar aimsíodh na báthadh |
| `hz`, `ownHz`, `positions` | samplaí sa soicind de longa eile agus den long féin; sraitheanna suímh |
| `units` | aonaid shaoil (15 m de réir na gcorp, 30 m de réir raon an chluiche); x soir, y suas, z ó thuaidh |
| `events` | líon sraitheanna an tábla de gach imeacht |
| `decoded` | an modh agus uimhreacha paicéad a fuarthas do gach cineál teachtaireachta |

## Imreoirí agus imeachtaí {#players-and-events}

| Eochair | Cad é |
|---|---|
| `players` | iontráil amháin do gach long: ainm, `ally` nó `enemy`, uimhir agus ainm loinge, eintiteas, samplaí, maruithe, slán; `seen` (damáiste a rinneadh agus a fuarthas, sliogáin, torpéidí agus sláinte dheireanach a chonaic an cliant); `header` (iontráil an rolla) agus `record` (taifead an imreora ón sruth, de réir uimhir eochrach) |
| `kills` | gach báthadh: am, íobartach, marfóir, uimhir chúise, áit |
| `chat` | gach líne chomhrá, le cainéal agus seoltóir |
| `damageStats` | staitisticí féin an imreora taifeadta mar a choinníonn an cluiche iad: in aghaidh an airm agus an chineáil, comhaireamh agus méid (is damáiste a rinneadh é cineál 0) |
| `avatarPickles` | gach glao picilte chuig an imreoir taifeadta, díchódaithe, de réir uimhir modha |

## Ceanntásc, torthaí agus seiceálacha {#header-results-and-checks}

| Eochair | Cad é |
|---|---|
| `header` | an chéad bhloc JSON, é ar fad ach amháin an rolla: mód cluiche, aimsir, teorainn léarscáile, méideanna foirne agus níos mó |
| `moreBlocks` | na bloic JSON tar éis an chéad cheann, mar atá siad |
| `blockIds` | 15.x: cuntas an imreora taifeadta agus id an chatha, léite mar théacs |
| `results` | 15.x: na torthaí, a choinníonn na cliaint seo sa sruth |
| `entities` | gach eintiteas a chruthaíonn an sruth: a uimhir chineáil agus a ról, cathain a tháinig isteach i radharc an chliaint agus cathain a d'fhág |
| `selfCheck` | comhaireamh na hiomláine ([Iomláine](completeness.md)) agus seiceálacha na n-eintiteas, na dtorthaí, na n-id agus an leagain |

---

Cuid de [3DHeat](https://github.com/Holdi601/3DHeat) ([doiciméadúchán](https://holdi601.github.io/3DHeat/)). Foinse: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
