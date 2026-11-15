---
title: "Kif taqra ripetizzjoni"
nav_order: 7
lang: mt
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Kif taqra ripetizzjoni {#how-it-reads-a-replay}

Ripetizzjoni hija header ta' blokok JSON u l-fluss tal-pakketti tal-logħba (noti
dwar il-format f'[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- L-ewwel blokk, bla ċifrar: il-mappa, il-verżjoni tal-klijent, il-plejer u
  l-vapur li rreġistraw, u r-roster - l-isem ta' kull plejer, alleat jew għadu, u
  n-numru tal-vapur. Klijenti ġodda (15.x) iżidu żewġ blokok oħra: wieħed vojt, u
  l-kont tal-plejer li rreġistra u l-id tal-battalja bħala test, moqrijin f'`blockIds`.
  Ir-riżultati mhumiex fil-JSON; 15.x iżommhom fil-fluss.
- Il-fluss tal-pakketti, ikkompressat b'zlib u ċifrat b'Blowfish b'ċavetta li
  tġorr il-logħba, u li l-għodod tal-komunità li jaqraw dawn il-fajls ippubblikaw.
  Deċifrat, fih:
  - l-aġġornamenti tal-pożizzjoni tal-magna ta' kull vapur li l-klijent seta' jara
    (it-tim tiegħu kollu, l-għedewwa waqt li ġew spotted jew qrib), diversi drabi
    fit-tieni waqt li jiċċaqalqu u inqas spiss waqt li ma jiċċaqalqux;
  - il-vapur proprju tal-plejer li rreġistra f'pakkett għalih, madwar seba' darbiet
    fit-tieni;
  - darba, fil-bidu, ir-records tal-plejers bħala lista Python pickled. Dawn jgħidu
    liema entità fil-fluss hija liema plejer. Iċ-ċwievet tagħhom huma innumerati, u
    n-numri jinbidlu mal-patches, għalhekk il-qarrej isib iċ-ċwievet mill-valuri
    tagħhom: iċ-ċavetta li żżomm l-ismijiet tar-roster, u ċ-ċavetta li żżomm
    entitajiet li għandhom aġġornamenti tal-pożizzjoni;
  - is-sejħa tas-server li tgħid lill-klijent li vapur għereq: vittma, qattiel,
    kawża. Tinstab mill-forma tagħha (tnax-il byte; l-ewwel tnejn huma entitajiet
    ta' vapuri; kull vittma tidher darba), mhux min-numru tagħha;
  - il-ħsara ta' kull vapur: firxa ta' (attakkant, ħsara) għal kull daqqa, fuq
    il-vapur li nħabat; u s-saħħa tiegħu, proprjetà mwaħħla ftit qabel;
  - kull salvo ta' qxur u ta' torpidnijiet li l-klijent ġie mgħarraf bih: it-tip
    ta' qoxra, ix-xutter, is-salvo, u l-bidu u l-veloċità ta' kull qoxra jew torpidni;
  - fejn spiċċaw il-qxur: ix-xutter, tip ta' daqqa, u l-post ta' kull waħda (fuq
    klijenti 15.x b'aktar dwar il-qoxra fejn laqtet, li jinqabeż);
  - iċ-chat: min bagħat, il-kanal, il-linja;
  - sejħiet pickled lill-plejer li rreġistra: l-istatistika tal-ħsara tiegħu,
    aġġornamenti tar-records tal-plejers, l-istat tal-battalja;
  - fuq klijenti 15.x, ir-riżultati tal-battalja fl-aħħar: pakkett għalihom, oġġett
    JSON bl-id tal-battalja, moqri sħiħ f'`results` tad-dokument tal-partita (il-listi
    proprji tal-logħba, mingħajr ismijiet: `commonList`, `privateDataList`,
    `playersPublicInfo` għal kull kont, ...).

In-numri tal-pakketti u tal-metodi li jvarjaw bejn il-verżjonijiet ikkontrollati (il-pakkett
tal-vapur proprju huwa 43 jew 44, is-sejħa tal-għerq 76 jew 83, il-qxur 101, 102, 126 jew 127)
jinstabu kollha mill-forma - ara
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - biex patch li jbiddel in-numri
ma jħallix it-tabella vojta. In-numri misjuba jinsabu fid-`decoded` tad-dokument tal-partita.

**Il-pickle huwa data li ma tistax tafdaha.** Ripetizzjoni hija fajl minn kullimkien, u pickle jista'
isemmi kodiċi li jitħaddem. Jitgħabba b'unpickler li jagħti kull klassi jew funzjoni li l-pickle
jsemmi placeholder inerti, biex jibni data sempliċi u xejn aktar. Test jitfgħalu pickle li
jsejjaħ `os.system`.

L-**għarqiet** għandhom il-ħin eżatt tas-sejħa. Il-post tagħhom huwa fejn il-vittma dehret
l-aħħar, meta dan kien fi żmien ħames sekondi. **Il-bidu tal-battalja** huwa l-ewwel mument li
xi vapur jiċċaqlaq xejn (il-vapuri jibqgħu bla moviment fil-countdown).

Kull ħaġa li mhix ringiela tat-tabella tinsab fid-[dokument tal-partita](match-document.md).

**Dak li l-klijent ġie mgħarraf** huwa komplut għat-tim tiegħu u parzjali għall-għedewwa:
is-sparaturi, id-daqqiet u s-saħħa tagħhom jinsabu hemm waqt li kienu fil-firxa.

**Mhux moqri:**

- Ajruplani u l-iskwadrunijiet tagħhom (is-sejħiet li jġorruhom ma tqassmux), l-aġġornamenti
  tal-vista tal-minimap (ippakkjati), spotting, ribbons, nirien u għargħar bħala avvenimenti
  għalihom (il-ħsara tagħhom tinsab fid-daqqiet), consumables, punti ta' qbid u skors tat-timijiet
  (proprjetajiet ta' entitajiet mingħajr definizzjoni, ma jintgħarfux mill-forma), il-bqija tal-proprjetajiet
  ta' vapur (aim, rudder, setting tal-veloċità...).
- In-numri taċ-ċwievet tar-records tal-plejers u tal-istatistika tal-ħsara bħala ismijiet:
  il-logħba tinnumerahom, u n-numri jinbidlu; jinżammu bħala numri.
- Data żejda ta' qoxra fejn laqtet (15.x) u l-bytes wara l-bidu u l-veloċità ta' qoxra
  jew torpidni.
- Riżultati ta' klijenti qabel 15.x: ir-ripetizzjonijiet tagħhom ma jġorru ebda.
- In-numru tal-vapur bħala isem: l-ismijiet jinsabu fil-fajls proprji tal-parametri
  tal-logħba, mhux fir-ripetizzjoni.

## Kif ġie kkontrollat il-qari {#how-the-reading-was-checked}

Il-qari ġie kkontrollat fuq ripetizzjonijiet pubbliċi ta' klijenti minn 0.9 sa 15.x, kull
valur kontra xi ħaġa li r-ripetizzjoni tagħti darba oħra:

- **Pożizzjonijiet:** l-entità ta' kull vapur taqbel ma' isem fir-roster; id-direzzjonijiet
  jaqblu mad-direzzjoni tal-vjaġġ fi ħdan 0.1 rad; wara l-għerq tiegħu, vapur jiċċaqlaq inqas
  minn 0.1 unità. Vapur li jinsab bla moviment jiġi aġġornat inqas spiss.
- **Saħħa:** kull vapur li għereq fil-vista tal-klijent jispiċċa b'saħħa 0. Madwar nofs
  id-daqqiet kollha jaqblu ma' waqgħa tas-saħħa fit-tieni ta' qabel; il-bqija jaqgħu
  flimkien ma' tiswijiet jew daqqiet oħra.
- **Ħsara kontra l-istatistika proprja tal-logħba:** fuq l-aħħar klijent il-ħsara tal-plejer
  li rreġistra moqrija hija fi ħdan 0.1% tal-istatistika. Fuq klijenti eqdem l-istatistika
  hija ogħla: il-klijent ma jiġix mibgħut kull daqqa, jew l-istatistika tgħodd aktar minn
  daqqiet (mhux solvut).
- **Qxur:** qoxra tibda ftit unitajiet mill-aħħar pożizzjoni magħrufa tal-vapur tagħha
  (il-kanuni huma mifruxa mal-iskoss); kważi kull tmiem ta' qoxra jsegwi, fi ħdan minuta,
  sparatura li ra l-klijent.

It-testijiet jibnu ripetizzjonijiet bl-istess layout, għalhekk ebda ripetizzjoni vera
ma tinżamm f'dan ir-repożitorju.

**Mhux ikkontrollat:** klijenti qabel 0.9.6, il-klijent ta' Lesta (Mir Korabley),
operazzjonijiet u skenarji lil hinn minn wieħed, battaljiet tal-clan u ranked, u liema
numru ta' vapur huwa liema vapur.

---

Parti mid-[3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentazzjoni](https://holdi601.github.io/3DHeat/)). Sors: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
