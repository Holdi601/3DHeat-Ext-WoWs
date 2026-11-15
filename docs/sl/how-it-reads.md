---
title: Kako bere posnetek
nav_order: 7
lang: "sl"
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Kako bere posnetek {#how-it-reads-a-replay}

Posnetek je glava iz blokov JSON in paketni tok igre (opombe o formatu v
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Prvi blok, v čistem besedilu: zemljevid, različica odjemalca, igralec in ladja, ki sta snemala, ter seznam –
  ime vsakega igralca, zaveznik ali sovražnik, in številka ladje. Novejši odjemalci (15.x) dodajo še dva bloka:
  enega prazen in račun igralca, ki je snemal, ter identifikator bitke kot besedilo, prebrano v `blockIds`.
  Rezultati niso v JSON-u; 15.x jih hrani v toku.
- Paketni tok, stisnjen z zlib in šifriran z Blowfish s ključem, ki ga nosi igra, ki so ga skupnostna orodja za
  branje teh datotek objavila. Dešifriran vsebuje:
  - posodobitve položajev motorja vsake ladje, ki jo je odjemalec lahko videl (svoja ekipa ves čas, sovražniki
    med opazovanjem ali v bližini), večkrat na sekundo, ko se premikajo, in redkeje, ko ne;
  - lastno ladjo igralca, ki je snemal, v svojem paketu, približno sedemkrat na sekundo;
  - enkrat, na začetku, zapise igralcev kot seznam Pythona v pickle obliki. Ti povedo, katera entiteta v toku je
    kateri igralec. Njihovi ključi so oštevilčeni, številke pa se s popravki spreminjajo, zato bralnik ključe najde
    po njihovih vrednostih: ključ, ki hrani imena s seznama, in ključ, ki hrani entitete z posodobitvami položajev;
  - klic strežnika, ki odjemalcu pove, da je ladja potonila: žrtev, ubijalec, vzrok. Najden je po obliki (dvanajst
    bajtov; prva dva sta entiteti ladij; vsaka žrtev se pojavi enkrat), ne po številki;
  - poškodbe vsake ladje: polje (napadalec, škoda) na zadetek, na zadeti ladji; in njeno zdravje, lastnost, nastavljena
    trenutek prej;
  - vsak salvo izstrelkov in torpedov, o katerih je bil odjemalec obveščen: vrsta izstrelka, strelec, salvo ter začetek
    in hitrost vsakega izstrelka ali torpeda;
  - kje so se izstrelki končali: strelec, vrsta zadetka in mesto vsakega (na odjemalcih 15.x še več o izstrelku, kjer je
    zadel, kar se preskoči);
  - klepet: pošiljatelj, kanal, vrstica;
  - prejeti klici igralca, ki je snemal: njegova statistika poškodb, posodobitve zapisov igralcev, stanje bitke;
  - na odjemalcih 15.x so na koncu rezultati bitke: svoj paket, objekt JSON z identifikatorjem bitke, prebran celo v
    `results` dokumenta tekme (igrinih lastnih seznamov, brez imen: `commonList`, `privateDataList`,
    `playersPublicInfo` na račun, ...).

Številke paketov in metod, ki se razlikujejo med preverjenimi različicami (paket lastne ladje je 43 ali 44, klic
potopitve 76 ali 83, izstrelki 101, 102, 126 ali 127), so vse najdene po obliki – glejte
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) – zato popravek, ki
jih prešteje na novo, ne izprazni tabele. Najdene številke so v `decoded` dokumenta tekme.

**Pickle so nezaupanja vredni podatki.** Posnetek je datoteka od kjerkoli, pickle pa lahko imenuje kodo za izvajanje.
Naložen je z odpirači, ki vsakemu razredu ali funkciji, ki jo pickle imenuje, dajo nemo nadomestilo, zato zgradi samo
navadne podatke in nič drugega. Test mu poda pickle, ki kliče `os.system`.

**Potopitve** imajo točen čas klica. Njihovo mesto je, kjer je bila žrtev nazadnje videna, kadar je to bilo v petih
sekundah. **Začetek bitke** je prvi trenutek, ko se katerakoli ladja sploh premakne (ladje v odštevanju mirujejo).

Vse, kar ni vrstica tabele, je v [dokumentu tekme](match-document.md).

**Kar je bilo povedano odjemalcu,** je popolno za njegovo ekipo in delno za sovražnike: njihovi streli, zadetki in
zdravje so tam, dokler so bili v dosegu.

**Ni prebrano:**

- Letala in njihove eskadrilje (klici, ki jih nosijo, niso bili razstavljeni), posodobitve vidnosti mini zemljevida
  (stisnjene), opazovanje, trakovi, požari in poplave kot lastni dogodki (njihova škoda je v zadetkih), potrošni material,
  točke zajema in rezultati ekip (lastnosti entitet brez definicije, po obliki ne ločljive), preostale lastnosti ladje
  (cilj, krmilo, nastavitev hitrosti ...).
- Ključi števil zapisov igralcev in statistike škode kot imena: igra jih oštevilči, številke se spreminjajo; ohranjeni so
  kot številke.
- Dodatni podatki izstrelka, kjer je zadel (15.x), in bajti po začetku in hitrosti izstrelka ali torpeda.
- Rezultati odjemalcev pred 15.x: njihovi posnetki jih ne vsebujejo.
- Številka ladje kot ime: imena so v igrinih lastnih datotekah parametrov, ne v posnetku.

## Kako je bilo branje preverjeno {#how-the-reading-was-checked}

Branje je bilo preverjeno na javnih posnetkih odjemalcev od 0.9 do 15.x, vsaka vrednost z nečim, kar posnetek poda
drugič:

- **Položaji:** vsaka entiteta ladje se je ujemala z imenom s seznama; smeri se ujemajo s smerjo plovbe znotraj
  0,1 rad; po njeni potopitvi se ladja premakne manj kot 0,1 enote. Ladja, ki miruje, se posodablja redkeje.
- **Zdravje:** vsaka ladja, potopljena v pogledu odjemalca, konča z zdravjem 0. Približno polovica vseh zadetkov se
  ujema s padcem zdravja v sekundi pred tem; ostali padejo skupaj s popravili ali drugimi zadetki.
- **Škoda proti lastni statistiki igre:** na najnovejšem odjemalcu je prebrana škoda igralca, ki je snemal, znotraj 0,1 %
  statistike. Na starejših odjemalcih je statistika višja: odjemalcu ni poslan vsak zadetek ali pa statistika šteje več
  kot zadetke (ni razrešeno).
- **Izstrelki:** izstrelek se začne nekaj enot od zadnjega znanega položaja svoje ladje (topovi so razporejeni po trupu);
  skoraj vsak konec izstrelka v eni minuti sledi strelu, ki ga je odjemalec videl.

Testi sestavijo posnetke po isti postavitvi, zato v tem repozitoriju ni nobenega pravega posnetka.

**Ni preverjeno:** odjemalci pred 0.9.6, odjemalec Lesta (Mir Korabley), operacije in scenariji razen enega, klanske in
rangirane bitke ter katera številka ladje je katera ladja.

---

Del [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Vir: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
