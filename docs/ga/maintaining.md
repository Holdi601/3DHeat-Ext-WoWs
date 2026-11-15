---
title: Cothabháil
nav_order: 99
lang: ga
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# An doiciméadúchán a chothabháil {#maintaining-the-documentation}

Don té a eisíonn leagan nua. Déan na céimeanna san ord seo.

1. **Athghin na leathanaigh tagartha** ón gcód:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   Athscríobhann sé seo an [Tagairt orduithe](../cli-reference.md) agus an [Liosta colún](../columns.md). Ná cuir an dá cheann sin in eagar de láimh choíche.
2. **Liostaigh an méid a d'athraigh ón eisiúint dheireanach:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   Is é `<VERSION>` an leagan eisithe deireanach (gan clib fós: an `git log --oneline` iomlán). Teastaíonn leathanach uaidh agus sraith in alt **Docs** de [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md) ó gach gné, rogha nó colún nua.
3. **Athbhreithniú neamhspleách.** Léann duine nár scríobh na leathanaigh (duine nó gníomhaire) an README, gach leathanach agus gach pictiúr mar thrí léitheoir: tosaitheoir nár úsáid teirminéal riamh, leanbh 8 mbliana d'aois, agus gairmí a sheiceálann gach rogha, colún agus aonad i gcoinne an chóid. Seiceálann siad na léaráidí i gcoinne an chóid freisin, agus nach n-ainmníonn aon leathanach léarscáil, leibhéal, imreoir ná cluiche fíor, ná nach dtugann figiúirí ó athsheinmeanna fíor.
4. **Ceartaigh an méid a fuair an t-athbhreithniú.** Ansin rith céim 1 arís agus aththarraing na pictiúir a d'athraigh a n-aschur.
5. **Aistriúcháin.** Taifeadann gach leathanach faoi `docs/<language>/` hais an leathanaigh Bhéarla óna aistríodh é. Aistrigh arís gach leathanach ar athraigh a fhoinse Bhéarla, lipéid léaráidí san áireamh. Ansin déan athbhreithniú ar gach teanga: soiléir do na trí léitheoir, lipéid ceart, agus na focail chéanna a úsáideann faire 3DHeat sa teanga sin.
6. **Eisiúint:** ardaigh `VERSION` agus clibeáil `v<VERSION>`. **Ná brúigh ach tar éis cead an úinéara.**

## Aistriúcháin: na horduithe {#translations-the-commands}

Aistrítear an suíomh go 40 teanga fhaire 3DHeat: Béarla i `docs/`, gach teanga eile i `docs/<lang>/` leis na hainmneacha comhaid chéanna. Déanann `tools/docs_i18n.py` an cuntasaíocht:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Ná haistrigh ach an méid a liostaíonn `todo`: fág Markdown, naisc, cód, ainmneacha comhad agus colún mar atá siad, aistrigh teidil agus tuairiscí pictiúr, agus úsáid focail féin faire 3DHeat dá cnaipí agus painéil (a `src/i18n/locales/<lang>/`). Fanann leathanaigh tagartha ginte agus pictiúir teirminéil i mBéarla. Ar an suíomh, deir aistriúchán atá as dáta é sin agus nascann sé leis an leathanach Béarla; titeann ceann atá ar iarraidh ar ais go Béarla. Tagann roghchlár teanga an cheanntáisc agus atreorú teanga brabhsálaí an leathanaigh baile ó `docs/_includes/`.
