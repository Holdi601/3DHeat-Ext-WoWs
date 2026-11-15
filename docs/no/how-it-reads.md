---
title: "Slik leser den en replay"
nav_order: 7
lang: "no"
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Slik leser den en replay {#how-it-reads-a-replay}

En replay er en header av JSON-blokker og spillets pakkestrøm (formatnotater i
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Den første blokken, i klartekst: kartet, klientversjonen, opptakspilotens spiller og skip, og deltakerlisten - hver
  spillers navn, allierte eller fiende, og skipsnummer. Nyere klienter (15.x) legger til to blokker til: en tom, og
  opptakspilotens konto og slagets ID som tekst, lest inn i `blockIds`. Resultatene står ikke i JSON-en; 15.x beholder
  dem i strømmen.
- Pakkestrømmen, zlib-komprimert og Blowfish-kryptert med en nøkkel spillet bærer, som fellesskapets verktøy som
  leser disse filene har publisert. Dekryptert inneholder den:
  - motorens posisjonsoppdateringer for hvert skip klienten kunne se (sitt eget lag hele tiden, fiender mens de er
    spottet eller i nærheten), flere ganger i sekundet mens de beveger seg og sjeldnere mens de ikke gjør det;
  - opptakspilotens eget skip i en pakke for seg selv, ca. sju ganger i sekundet;
  - én gang, i starten, spillernes poster som en pickle, en Python-liste. Disse sier hvilken entitet i strømmen som er
    hvilken spiller. Nøklene deres er nummerert, og nummerene endres med oppdateringer, så leseren finner nøklene
    etter verdiene deres: nøkkelen som holder deltakernes navn, og nøkkelen som holder entitetene som har
    posisjonsoppdateringer;
  - serverens kall som forteller klienten at et skip har sunket: offer, dreper, årsak. Det finnes etter sin form
    (tolv byte; de to første er skipsentiteter; hvert offer forekommer én gang), ikke etter sitt nummer;
  - hvert skips skade: en matrise med (angriper, skade) per treff, på skipet som ble truffet; og dets helse, en
    egenskapsverdi satt et øyeblikk før;
  - hver salve av granater og torpedoer klienten ble fortalt om: granattypen, skytteren, salven, og hver granats eller
    torpedos start og hastighet;
  - hvor granater endte: skytteren, en treffype, og stedet for hver (på 15.x-klienter med mer om granaten der den traff,
    som hoppes over);
  - chatten: avsender, kanal, linje;
  - pickle-kall til opptakspiloten: dens skadestatistikk, oppdateringer av spillernes poster, slagets tilstand;
  - på 15.x-klienter, slagets resultater til slutt: en pakke for seg selv, et JSON-objekt med slagets ID, lest helt inn i
    kampdokumentets `results` (spillets egne lister, uten navn: `commonList`, `privateDataList`, `playersPublicInfo`
    per konto, ...).

Pakke- og metodenumrene som varierer mellom de kontrollerte versjonene (opptakspilotens skip-pakke er 43 eller 44,
senkingskallet 76 eller 83, granatene 101, 102, 126 eller 127) finnes alle etter form - se
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - så en
omnummereringsoppdatering tømmer ikke tabellen. Tallene som ble funnet, står i kampdokumentets `decoded`.

**Pickle-en er ikke-pålitelige data.** En replay er en fil fra hvor som helst, og en pickle kan nevne kode som skal kjøres.
Den lastes med en avpakker som gir hver klasse eller funksjon pickle-en nevner en inert plassholder, så den bygger vanlige
data og ikke noe annet. En test mater den med en pickle som kaller `os.system`.

**Senkinger** har kallets nøyaktige tid. Deres sted er der offeret sist ble sett, når det var innen fem sekunder. **Slagets
start** er det første øyeblikket noe skip beveger seg i det hele (skip ligger stille i nedtellingen).

Alt som ikke er en tabellrad, står i [kampdokumentet](match-document.md).

**Det klienten ble fortalt** er fullstendig for sitt eget lag og delvis for fiender: deres skudd, treff og helse er der mens
de er i rekkevidde.

**Ikke lest:**

- Fly og deres eskadriller (kallene som bærer dem ble ikke tatt fra hverandre), minikartets synsoppdateringer (pakket),
  spotting, bånd, branner og oversvømmelser som hendelser for seg selv (skadene deres er i treffene), forbruksvarer,
  erobringspunkter og lagpoeng (egenskaper til entiteter uten definisjon, ikke skilt fra hverandre etter form), resten av et
  skips egenskaper (sikte, ror, fartsinnstilling ...).
- Nøklenes tall i spillerpostene og skadestatistikken som navn: spillet nummererer dem, og tallene endres; de beholdes som tall.
- Et skalls ekstra data der det traff (15.x) og bytene etter en granats eller torpedos start og hastighet.
- Resultater fra klienter før 15.x: deres replayer har ingen.
- Skipsnummeret som navn: navnene står i spillets egne parameterfiler, ikke i replayen.

## Hvordan lesingen ble kontrollert {#how-the-reading-was-checked}

Lesingen ble kontrollert på offentlige replayer fra klienter fra 0.9 til 15.x, hver verdi mot noe replayen gir en annen gang:

- **Posisjoner:** hvert skips entitet stemte med et navn i deltakerlisten; retninger stemmer med bevegelsesretningen innen
  0,1 rad; etter sin senking beveger et skip seg mindre enn 0,1 enheter. Et skip som ligger stille, oppdateres sjeldnere.
- **Helse:** hvert skip som sank innenfor klientens syn, ender med helse 0. Omtrent halvparten av alle treff stemmer med et
  helsefall i sekundet før; resten faller sammen med reparasjoner eller andre treff.
- **Skade mot spillets egen statistikk:** på den nyeste klienten er opptakspilotens leste skade innen 0,1 % av statistikken.
  På eldre klienter er statistikken høyere: klienten får ikke alle treff sendt, eller statistikken teller mer enn treff
  (ikke løst).
- **Granater:** en granat starter noen enheter fra skipets sist kjente posisjon (kanonene er spredt langs skroget); nesten
  hver granats slutt følger, innen et minutt, et skudd klienten så.

Testene bygger replayer i samme oppsett, så ingen ekte replay ligger i dette depotet.

**Ikke kontrollert:** klienter før 0.9.6, Lestas klient (Mir Korabley), operasjoner og scenarier utover ett, klan- og
rangerte slag, og hvilket skipsnummer som er hvilket skip.

---

Del av [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentasjon](https://holdi601.github.io/3DHeat/)). Kilde: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
