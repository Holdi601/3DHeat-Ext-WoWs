---
title: Kaip įrankis skaito įrašą
nav_order: 7
lang: "lt"
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Kaip įrankis skaito įrašą {#how-it-reads-a-replay}

Įrašas yra JSON blokų antraštė ir žaidimo paketų srautas (formato pastabos
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Pirmas blokas, be šifravimo: žemėlapis, kliento versija, įrašantis žaidėjas ir laivas, bei sąrašas - kiekvieno
  žaidėjo vardas, `ally` arba `enemy`, ir laivo numeris. Naujesni klientai (15.x) prideda dar du blokus: tuščią ir
  įrašančio žaidėjo paskyrą bei mūšio id tekstu, perskaitytus į `blockIds`. Rezultatų JSON'e nėra; 15.x juos saugo
  sraute.
- Paketų srautas, suspaustas zlib ir užšifruotas Blowfish raktu, kurį turi žaidimas; bendruomenės įrankiai, skaitantys
  šiuos failus, jį paskelbė. Iššifruotas jis turi:
  - variklio pozicijų atnaujinimus kiekvieno laivo, kurį klientas galėjo matyti (jo paties komanda visą laiką, priešai,
    kol pastebėti arba arti), kelis kartus per sekundę, kol jie juda, ir rečiau, kai nejuda;
  - įrašančio žaidėjo paties laivo paketą atskirame pakete, maždaug septynis kartus per sekundę;
  - kartą, pradžioje, žaidėjų įrašus kaip įraugintą Python sąrašą. Jie nurodo, kuri srauto esybė yra kuris žaidėjas.
    Jų raktai sunumeruoti, o numeriai keičiasi su pataisomis, todėl skaitytuvas raktus randa pagal jų reikšmes: raktą,
    kuriame yra sąrašo vardai, ir raktą, kuriame yra esybės su pozicijų atnaujinimais;
  - serverio iškvietimą, pranešantį klientui, kad laivas nuskendo: auka, žudikas, priežastis. Jis randamas pagal formą
    (dvylika baitų; pirmi du - laivo esybės; kiekviena auka pasirodo vieną kartą), o ne pagal numerį;
  - kiekvieno laivo žalą: masyvą (atakuotojas, žala) kiekvienam pataikymui į pataikytą laivą, ir jo sveikatą - savybės
    reikšmę akimirka anksčiau;
  - kiekvieną sviedinių ir torpedų salvę, apie kurią klientui buvo pranešta: sviedinio tipą, šaulį, salvę ir kiekvieno
    sviedinio ar torpedos pradžią bei greitį;
  - kur baigėsi sviediniai: šaulį, pataikymo tipą ir kiekvieno vietą (15.x klientuose - daugiau apie sviedinį, kur jis
    trenkė, ir tai praleidžiama);
  - pokalbį: siuntėjas, kanalas, eilutė;
  - užšifruotus iškvietimus įrašančiam žaidėjui: jo žalos statistiką, žaidėjų įrašų atnaujinimus, mūšio būseną;
  - 15.x klientuose - mūšio rezultatus pabaigoje: atskirą paketą, JSON objektą su mūšio id, perskaitytą pilnai į rungtynių
    dokumento `results` (žaidimo paties sąrašai, nepavadinti: `commonList`, `privateDataList`, `playersPublicInfo`
    pagal paskyrą, ...).

Paketų ir metodų numeriai, kurie skiriasi tarp patikrintų versijų (savojo laivo paketas yra 43 ar 44, nuskandinimo
iškvietimas 76 ar 83, sviediniai 101, 102, 126 ar 127), visi randami pagal formą - žr.
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - todėl
pataisa, perrikiuojanti numerius, nepaverčia lentelės tuščia. Rasti numeriai yra rungtynių dokumento `decoded` skiltyje.

**Pickle yra nepatikimi duomenys.** Įrašas yra failas iš bet kur, o Python pickle gali įvardyti kodą, kurį
reikia vykdyti. Jis įkeliamas su unpickler'iu, kuris kiekvienai klasei ar funkcijai, kurią pickle įvardija, duoda inertišką
vietos laikiklį, todėl sukuria tik paprastus duomenis ir nieko daugiau. Testas paduoda jam pickle, kuris kviečia
`os.system`.

**Nuskandinimai** turi tikslų iškvietimo laiką. Jų vieta yra ten, kur auka paskutinį kartą matyta, jei tai buvo per
penkias sekundes. **Mūšio pradžia** yra pirmoji akimirka, kai kuris nors laivas apskritai pajuda (laivai stovi vietoje
atgaline skaičiavimo metu).

Viskas, kas nėra lentelės eilutė, yra [rungtynių dokumente](match-document.md).

**Tai, ką klientui buvo pasakyta,** yra pilna jo komandai ir dalinė priešams: jų šūviai, pataikymai ir sveikata yra
įrašyti, kol jie buvo nuotolyje.

**Neskaityta:**

- Lėktuvai ir jų eskadrilės (iškvietimai, kurie juos neša, nebuvo išnagrinėti), mini žemėlapio matymo atnaujinimai
  (supakuoti), žvalgyba, ženklai (ribbons), gaisrai ir potvyniai kaip atskiri įvykiai (jų žala yra pataikymuose),
  sunaudojamos priemonės, taškai užimti ir komandų balai (esybių savybės be apibrėžimo, nesurandamos pagal formą),
  kitos laivo savybės (taikymas, vairas, greičio nustatymas...).
- Žaidėjų įrašų ir žalos statistikos raktų numeriai kaip vardai: žaidimas juos numeruoja, o numeriai keičiasi; jie
  išsaugomi kaip skaičiai.
- Papildomi sviedinio duomenys jo trenkimo vietoje (15.x) ir baitai po sviedinio ar torpedos pradžios bei greičio.
- Rezultatai klientų, senesnių nei 15.x: jų įrašuose jų nėra.
- Laivo numeris kaip vardas: vardai yra žaidimo paties parametrų failuose, o ne įraše.

## Kaip patikrintas skaitymas {#how-the-reading-was-checked}

Skaitymas patikrintas viešuose klientų nuo 0.9 iki 15.x įrašuose, kiekviena reikšmė - su kitu kartu įraše pateikta verte:

- **Pozicijos:** kiekvieno laivo esybė atitiko sąrašo vardą; kryptys sutampa su judėjimo kryptimi 0,1 rad tikslumu;
  po nuskendimo laivas pajuda mažiau nei 0,1 vieneto. Laivas, stovintis vietoje, atnaujinamas rečiau.
- **Sveikata:** kiekvienas laivas, nuskendęs kliento matymo lauke, baigiasi su sveikata 0. Maždaug pusė visų pataikymų
  sutampa su sveikatos kritimu per sekundę prieš tai; likę kartu su remontu ar kitais pataikymais.
- **Žala palyginus su žaidimo statistika:** naujausiame kliente įrašančio žaidėjo perskaityta žala yra per 0,1 % nuo
  statistikos. Senesniuose kliento versijose statistika didesnė: klientui nesiunčiamas kiekvienas pataikymas, arba
  statistika skaičiuoja daugiau nei pataikymus (neišspręsta).
- **Sviediniai:** sviedinys prasideda kelių vienetų atstumu nuo paskutinės žinomos laivo pozicijos (patrankos išsidėsčiusios
  išilgai korpuso); beveik kiekvieno sviedinio pabaiga per minutę seka šūvį, kurį klientas matė.

Testai sukuria įrašus tokiu pačiu išdėstymu, todėl šioje saugykloje joks tikras įrašas nelaikomas.

**Nepatikrinta:** kliento versijos prieš 0.9.6, Lesta klientas (Mir Korabley), operacijos ir scenarijai, išskyrus vieną,
klano ir reitinginiai mūšiai, ir kuris laivo numeris yra kuris laivas.

---

Dalis [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentacija](https://holdi601.github.io/3DHeat/)). Šaltinis: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
