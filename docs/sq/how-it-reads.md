---
title: "Si e lexon një riluajtje"
nav_order: 7
lang: sq
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Si e lexon një riluajtje {#how-it-reads-a-replay}

Një riluajtje është një header me blloqe JSON dhe rrjedha e paketave të lojës (shënime
për formatin te [`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Blloku i parë, i hapur: harta, versioni i klientit, lojtari dhe anija që regjistron,
  dhe lista - emri i secilit lojtar, aleat ose armik, dhe numri i anijes. Klientët
  më të rinj (15.x) shtojnë dy blloqe të tjera: një bosh, dhe llogarinë e lojtarit
  që regjistron dhe ID-në e betejës si tekst, të lexuar te `blockIds`. Rezultatet
  nuk janë në JSON; 15.x i mban në rrjedhë.
- Rrjedha e paketave, e kompresuar me zlib dhe e shifruar me Blowfish me një çelës që
  e mban loja, të cilin mjetet e komunitetit që i lexojnë këto skedarë e kanë
  publikuar. E deshifruar, mban:
  - përditësimet e pozicionit të motorit për çdo anije që klienti mund ta shihte (skuadrën e
    vet gjatë gjithë kohës, armiqtë ndërsa u zbuluan ose ishin afër), disa herë
    në sekondë ndërsa lëvizin dhe më rrallë kur nuk lëvizin;
  - anijen e vetë lojtarit që regjistron në një paketë më vete, rreth shtatë herë
    në sekondë;
  - një herë, në fillim, regjistrat e lojtarëve si listë Python të serializuar (pickle). Këta
    thonë cili entitet në rrjedhë është cili lojtar. Çelësat e tyre janë të numëruar,
    dhe numrat ndryshojnë me patch-et, kështu që lexuesi i gjen çelësat sipas
    vlerave të tyre: çelësi që mban emrat e listës, dhe çelësi që mban
    entitetet që kanë përditësime pozicioni;
  - thirrja e serverit që i thotë klientit se një anije u fundos: viktima, vrasësi,
    shkaku. Gjendet sipas formës së saj (dymbëdhjetë bajtë; dy të parët janë entitete
    anijesh; çdo viktimë shfaqet një herë), jo sipas numrit të saj;
  - dëmi i çdo anijeje: një varg (sulmues, dëm) për goditje, mbi anijen e goditur; dhe
    shëndeti i saj, një veti e vendosur një çast para;
  - çdo breshëri predhash dhe silurësh për të cilën iu tha klientit: lloji i
    predhës, gjuajtësi, breshëria, dhe fillimi dhe shpejtësia e çdo predhe ose silurit;
  - ku mbaruan predhat: gjuajtësi, një lloj goditjeje, dhe vendi i secilës (në klientët 15.x
    me më shumë për predhën aty ku goditi, që anashkalohet);
  - biseda: dërguesi, kanali, rreshti;
  - thirrje të serializuara (pickle) për lojtarin që regjistron: statistikat e dëmit të tij, përditësimet e
    regjistrave të lojtarëve, gjendja e betejës;
  - në klientët 15.x, rezultatet e betejës në fund: një paketë më vete, një
    objekt JSON me ID-në e betejës, lexuar i plotë te `results` i dokumentit të ndeshjes
    (listat e vetë lojës, të paemërtuara: `commonList`,
    `privateDataList`, `playersPublicInfo` për llogari, ...).

Numrat e paketave dhe metodave që ndryshojnë midis versioneve të kontrolluara (paketa e
anijes së vet është 43 ose 44, thirrja e fundosjes 76 ose 83, predhat 101, 102,
126 ose 127) gjenden të gjithë sipas formës - shih
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - kështu që një patch
që rinumëron nuk e boshatis tabelën. Numrat e gjetur janë te `decoded` i dokumentit të ndeshjes.

**Pickle janë të dhëna të pabesueshme.** Një riluajtje është një skedar nga kudo,
dhe një pickle mund të emërtojë kod për t'u ekzekutuar. Ngarkohet me një unpickler që i jep
çdo klase ose funksioni që emërton pickle një vendmbajtës të pavlefshëm, kështu që ndërton
të dhëna të thjeshta dhe asgjë tjetër. Një test i jep një pickle që thërret `os.system`.

**Fundosjet** kanë kohën e saktë të thirrjes. Vendi i tyre është ku u pa viktima
së fundmi, kur kjo ishte brenda pesë sekondash. **Fillimi i betejës** është
çasti i parë kur lëviz fare ndonjë anije (anijet qëndrojnë të palëvizura gjatë numërimit mbrapsht).

Gjithçka që nuk është rresht tabele është te [dokumenti i ndeshjes](match-document.md).

**Ajo që iu tha klientit** është e plotë për skuadrën e vet dhe e pjesshme për
armiqtë: të shtënat, goditjet dhe shëndeti i tyre janë aty ndërsa ishin në rreze.

**Të palexuara:**

- Aeroplanët dhe skuadronet e tyre (thirrjet që i mbartin nuk u zbërthyen), përditësimet e
  pamjes së minihartës (të paketuara), zbulimi, shiritat, zjarret dhe përmbytjet si ngjarje
  më vete (dëmi i tyre është te goditjet), konsumueshmet, pikat e kapjes dhe pikët e
  skuadrave (veti të entiteteve pa përkufizim, që nuk dallohen sipas formës), pjesa
  tjetër e vetive të një anijeje (synimi, timoni, cilësimi i shpejtësisë...).
- Numrat e çelësave të regjistrave të lojtarëve dhe të statistikave të dëmit si emra: loja
  i numëron, dhe numrat ndryshojnë; ruhen si numra.
- Të dhënat shtesë të një predhe aty ku goditi (15.x) dhe bajtët pas fillimit dhe
  shpejtësisë së një predhe ose silurit.
- Rezultatet e klientëve para 15.x: riluajtjet e tyre nuk mbartin asnjë.
- Numri i anijes si emër: emrat janë në skedarët e parametrave të vetë lojës,
  jo në riluajtje.

## Si u kontrollua leximi {#how-the-reading-was-checked}

Leximi u kontrollua në riluajtje publike të klientëve nga 0.9 deri 15.x, çdo
vlerë ndaj diçkaje që riluajtja e jep për herë të dytë:

- **Pozicionet:** entiteti i çdo anijeje përputhej me një emër të listës; heading
  përputhet me drejtimin e udhëtimit brenda 0.1 rad; pas fundosjes, një anije
  lëviz më pak se 0.1 njësi. Një anije e palëvizur përditësohet më rrallë.
- **Shëndeti:** çdo anije e fundosur brenda pamjes së klientit mbaron me shëndet 0.
  Rreth gjysma e të gjitha goditjeve përputhen me një rënie shëndeti në sekondën para;
  pjesa tjetër bie bashkë me riparime ose goditje të tjera.
- **Dëmi ndaj statistikave të vetë lojës:** në klientin më të ri dëmi i lexuar i
  lojtarit që regjistron është brenda 0.1% të statistikave. Në klientët më të vjetër
  statistikat janë më të larta: klientit nuk i dërgohet çdo goditje, ose
  statistikat numërojnë më shumë se goditjet (e pazgjidhur).
- **Predhat:** një predhë fillon disa njësi nga pozicioni i fundit i njohur i anijes së saj
  (topat shpërndahen përgjatë trupit); fundi i pothuajse çdo predhe ndjek,
  brenda një minute, një të shtënë që pa klienti.

Testet i ndërtojnë riluajtjet me të njëjtën strukturë, kështu që asnjë riluajtje e vërtetë nuk
mbahet në këtë depo.

**Të pakontrolluara:** klientët para 0.9.6, klienti Lesta (Mir Korabley),
operacionet dhe skenarët përtej njërit, betejat e klaneve dhe të renditura, dhe
cili numër anijeje është cila anije.

---

Pjesë e [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacioni](https://holdi601.github.io/3DHeat/)). Burimi: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
