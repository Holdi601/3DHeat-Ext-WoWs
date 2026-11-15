---
title: Conas a léann sé athsheinm
nav_order: 7
lang: ga
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Conas a léann sé athsheinm {#how-it-reads-a-replay}

Is ceanntásc de bhloic JSON agus sruth paicéad an chluiche athsheinm (nótaí formáide i [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- An chéad bhloc, go soiléir: an léarscáil, leagan an chliaint, an t-imreoir taifeadta agus a long, agus an rolla - ainm gach imreora, cara nó namhaid, agus uimhir loinge. Cuireann cliaint níos nuaí (15.x) dhá bhloc eile leis: ceann folamh, agus cuntas an imreora taifeadta agus id an chatha mar théacs, léite isteach i `blockIds`. Níl na torthaí sa JSON; coinníonn 15.x sa sruth iad.
- An sruth paicéad, comhbhrúite le zlib agus criptithe le Blowfish le heochair a iompraíonn an cluiche, a bhfuil foilsithe ag uirlisí an phobail a léann na comhaid seo. Díchriptithe, coinníonn sé:
  - nuashonruithe suímh an einsin de gach long a bhféadfadh an cliant í a fheiceáil (a fhoireann féin ar fud an chatha, naimhde nuair a aimsítear iad nó in aice), arís agus arís sa soicind fad a ghluaiseann siad agus níos annamha nuair nach ngluaiseann;
  - long féin an imreora taifeadta i bpaicéad dá cuid féin, thart ar seacht n-uaire sa soicind;
  - uair amháin, ag an tús, taifid na n-imreoirí mar liosta picilte Python. Deir siad cén t-eintiteas sa sruth cén t-imreoir é. Tá a n-eochracha uimhrithe, agus athraíonn na huimhreacha le paistí, mar sin aimsíonn an léitheoir na heochracha de réir a luachanna: an eochair a choinníonn ainmneacha an rolla, agus an eochair a choinníonn eintitis a bhfuil nuashonruithe suímh acu;
  - glao an fhreastalaí a insíonn don chliant gur báthadh long: íobartach, marfóir, cúis. Aimsítear é de réir a chruth (dhá bheart déag; is eintitis long an chéad dá cheann; tá gach íobartach ann uair amháin), ní de réir a uimhir;
  - damáiste gach loinge: eagar de (ionsaitheoir, damáiste) in aghaidh an bhuille, ar an long a bualadh; agus a sláinte, airí a socraíodh nóiméad roimhe sin;
  - gach sailve sliogán agus torpéidí a dúradh leis an gcliant: cineál an tsligéin, an lámhachóir, an tsailve, agus tús agus treoluas gach sligéin nó torpéido;
  - cá ndeachaigh sliogáin chun deiridh: an lámhachóir, cineál buille, agus áit gach ceann (ar chliaint 15.x le níos mó faoin sliogán san áit ar bhuail sé, a scipeáiltear);
  - an comhrá: seoltóir, cainéal, líne;
  - glaonna picilte chuig an imreoir taifeadta: a staitisticí damáiste, nuashonruithe taifead na n-imreoirí, stát an chatha;
  - ar chliaint 15.x, torthaí an chatha ag an deireadh: paicéad dá chuid féin, réad JSON le id an chatha, léite iomlán isteach i `results` na cáipéise cluiche (liostaí féin an chluiche, gan ainm: `commonList`, `privateDataList`, `playersPublicInfo` in aghaidh an chuntais, ...).

Aimsítear uimhreacha paicéad agus modha a athraíonn idir na leaganacha a seiceáladh (is 43 nó 44 é paicéad na loinge féin, 76 nó 83 an glao báite, 101, 102, 126 nó 127 na sliogáin) go léir de réir cruth - féach [`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - mar sin ní fholmhaíonn paiste athuimhrithe an tábla. Tá na huimhreacha a fuarthas i `decoded` na cáipéise cluiche.

**Is sonraí neamhiontaofa é an pickle.** Is comhad ó áit ar bith é athsheinm, agus is féidir le pickle cód le rith a ainmniú. Luchtaítear é le neamhphicilteoir a thugann áitchoinneálaí támh do gach aicme nó feidhm a ainmníonn an pickle, mar sin tógann sé sonraí simplí agus aon rud eile. Beathaíonn tástáil pickle dó a ghlaonn `os.system`.

**Tá am cruinn an ghlao ag báthadh.** Is é a n-áit an áit inar chonacthas an t-íobartach go deireanach, nuair a bhí sin laistigh de chúig soicind. **Tús an chatha** is é an chéad nóiméad a ghluaiseann long ar bith (luíonn longa socair sa chomhaireamh síos).

Tá gach rud nach sraith tábla é sa [cháipéis chluiche](match-document.md).

**An méid a dúradh leis an gcliant** tá sé iomlán dá fhoireann féin agus páirteach do naimhde: tá a gcuid lámhaigh, buillí agus sláinte ann fad a bhí siad i raon.

**Gan léamh:**

- Aerárthaigh agus a scuadrúin (níor scoilteadh na glaonna a iompraíonn iad), nuashonruithe radhairc na mionléarscáile (pacáilte), aimsiú, ribíní, tinte agus tuilte mar imeachtaí dá gcuid féin (tá a ndamáiste sna buillí), earraí inchaite, pointí gabhála agus scóir foirne (airíonna eintiteas gan sainmhíniú, nár idirdhealaíodh de réir cruth), an chuid eile d'airíonna loinge (aim, rudar, socrú luais...).
- Uimhreacha eochrach taifead na n-imreoirí agus staitisticí damáiste mar ainmneacha: uimhríonn an cluiche iad, agus athraíonn na huimhreacha; coinnítear mar uimhreacha iad.
- Sonraí breise sligéin san áit ar bhuail sé (15.x) agus na beartanna tar éis tús agus treoluas sligéin nó torpéido.
- Torthaí cliaint roimh 15.x: níl aon cheann ag a n-athsheinmeanna.
- Uimhir na loinge mar ainm: tá na hainmneacha i gcomhaid pharaiméadair an chluiche féin, ní san athsheinm.

## Conas a seiceáladh an léamh {#how-the-reading-was-checked}

Seiceáladh an léamh ar athsheinmeanna poiblí de chliaint ó 0.9 go 15.x, gach luach i gcoinne ruda a thugann an athsheinm an dara huair:

- **Suíomhanna:** mheaitseáil eintiteas gach loinge ainm rolla; aontaíonn treo gach loinge le treo an taistil laistigh de 0.1 rad; tar éis a báite, bogann long níos lú ná 0.1 aonad. Nuashonraítear long socair níos annamha.
- **Sláinte:** críochnaíonn gach long a báitear laistigh de radharc an chliaint le sláinte 0. Meaitseálann thart ar leath de na buillí go léir titim sláinte sa soicind roimhe sin; titeann an chuid eile le deisiúcháin nó buillí eile.
- **Damáiste i gcoinne staitisticí an chluiche féin:** ar an gcliant is nuaí tá damáiste an imreora taifeadta a léadh laistigh de 0.1% de na staitisticí. Ar chliaint níos sine tá na staitisticí níos airde: ní sheoltar gach buille chuig an gcliant, nó comhairíonn na staitisticí níos mó ná buillí (gan réiteach).
- **Sliogáin:** tosaíonn sliogán cúpla aonad ó shuíomh aitheanta deireanach a loinge (tá na gunnaí scaipthe feadh an choirp); leanann deireadh beagnach gach sligéin, laistigh de nóiméad, lámhaigh a chonaic an cliant.

Tógann na tástálacha athsheinmeanna sa leagan amach céanna, mar sin ní choinnítear aon athsheinm fíor sa stóras seo.

**Gan seiceáil:** cliaint roimh 0.9.6, cliant Lesta (Mir Korabley), oibríochtaí agus cásanna thar cheann amháin, cathanna clainne agus rangaithe, agus cén uimhir loinge is cén long.

---

Cuid de [3DHeat](https://github.com/Holdi601/3DHeat) ([doiciméadúchán](https://holdi601.github.io/3DHeat/)). Foinse: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
