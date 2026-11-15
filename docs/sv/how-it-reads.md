---
title: "Så läser den en repris"
nav_order: 7
lang: "sv"
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Så läser den en repris {#how-it-reads-a-replay}

En repris är en header av JSON-block och spelets paketström (formatanteckningar i
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Det första blocket, i klartext: kartan, klientversionen, den inspelande spelaren och fartyget, och
  listan - varje spelares namn, allierad eller fiende, och fartygsnummer. Nyare klienter (15.x) lägger
  till två block: ett tomt, och den inspelande spelarens konto och stridens id som text, lästa till
  `blockIds`. Resultaten finns inte i JSON:en; 15.x håller dem i strömmen.
- Paketströmmen, zlib-komprimerad och Blowfish-chifferskriven med en nyckel som spelet bär, vilken de
  gemenskapsverktyg som läser dessa filer har publicerat. Avkodad innehåller den:
  - motorns positionsuppdateringar för varje fartyg klienten kunde se (dess eget lag hela tiden,
    fiender medan de är upptäckta eller nära), flera gånger per sekund när de rör sig och mer sällan
    när de inte gör det;
  - den inspelande spelarens eget fartyg i ett eget paket, ungefär sju gånger per sekund;
  - en gång, i början, spelarnas poster som en inlagd Python-lista. Dessa säger vilken entitet i
    strömmen som är vilken spelare. Deras nycklar är numrerade, och numren ändras med patcharna, så
    läsaren hittar nycklarna via deras värden: nyckeln som håller listans namn, och nyckeln som håller
    entiteter som har positionsuppdateringar;
  - serverns anrop som berättar för klienten att ett fartyg sjunkit: offer, dödare, orsak. Det hittas
    via sin form (tolv byte; de två första är fartygsentiteter; varje offer förekommer en gång), inte
    via sitt nummer;
  - varje fartygs skada: en matris med (angripare, skada) per träff, på det träffade fartyget; och dess
    hälsa, en egenskap som sätts strax innan;
  - varje salva av granater och torpeder som klienten fick veta om: granattypen, skytten, salvan, och
    varje granats eller torpeds start och hastighet;
  - var granaterna slutade: skytten, en träfftyp, och platsen för var och en (på 15.x-klienter med mer
    om granaten där den träffade, vilket hoppas över);
  - chatten: avsändare, kanal, rad;
  - inlagda anrop till den inspelande spelaren: dess skadestatistik, uppdateringar av spelarnas poster,
    stridens tillstånd;
  - på 15.x-klienter, stridens resultat i slutet: ett eget paket, ett JSON-objekt med stridens id, läst
    helt till matchdokumentets `results` (spelets egna listor, onämnda: `commonList`,
    `privateDataList`, `playersPublicInfo` per konto, ...).

Paket- och metodnummer som skiljer sig mellan de kontrollerade versionerna (den egna fartygets paket är
43 eller 44, sänkningsanropet 76 eller 83, granaterna 101, 102, 126 eller 127) hittas alla via form - se
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - så
att en patch som numrerar om dem inte tömmer tabellen. De nummer som hittas står i matchdokumentets
`decoded`.

**Pickle-filen är otillförlitlig data.** En repris är en fil från vem som helst, och en pickle kan ange
kod att köra. Den läses med en avpickler som ger varje klass eller funktion som pickeln anger en inert
platshållare, så den bygger vanlig data och inget annat. Ett test matar den med en pickle som anropar
`os.system`.

**Sänkningar** har anropets exakta tid. Deras plats är där offret sist sågs, när det var inom fem
sekunder. **Stridens start** är det första ögonblick något fartyg alls rör sig (fartyg ligger stilla i
nedräkningen).

Allt som inte är en tabellrad finns i [matchdokumentet](match-document.md).

**Det klienten fick veta** är komplett för sitt eget lag och delvis för fiender: deras skott, träffar och
hälsa finns där medan de är inom räckhåll.

**Inte läst:**

- Flygplan och deras skvadroner (anropen som bär dem har inte tagits isär), minikartans synuppdateringar
  (packade), upptäckt, utmärkelser, bränder och översvämningar som egna händelser (deras skada finns i
  träffarna), förbrukningsartiklar, poänglägen och lagpoäng (egenskaper hos entiteter utan definition,
  inte åtskilda på form), resten av ett fartygs egenskaper (sikte, roder, hastighetsinställning ...).
- Spelarpostens och skadestatistikens nyckelnummer som namn: spelet numrerar dem, och numren ändras;
  de behålls som nummer.
- En granats extra data där den träffade (15.x) och byten efter en granats eller torpeds start och
  hastighet.
- Resultat från klienter före 15.x: deras repriser innehåller inga.
- Fartygsnumret som namn: namnen finns i spelets egna parameterfiler, inte i repriset.

## Så kontrollerades läsningen {#how-the-reading-was-checked}

Läsningen kontrollerades på publika repriser från klienter från 0.9 till 15.x, varje värde mot något
som repriset ger en andra gång:

- **Positioner:** varje fartygs entitet matchade ett namn i listan; kurserna stämmer med färdriktningen
  inom 0,1 rad; efter sin sänkning rör sig ett fartyg mindre än 0,1 enheter. Ett fartyg som ligger stilla
  uppdateras mer sällan.
- **Hälsa:** varje fartyg som sänktes inom klientens syn slutar med hälsa 0. Ungefär hälften av alla
  träffar motsvaras av en hälsominskning under sekunden före; resten sammanfaller med reparationer eller
  andra träffar.
- **Skada mot spelets egen statistik:** på den senaste klienten ligger den inspelande spelarens lästa
  skada inom 0,1 % från statistiken. På äldre klienter är statistiken högre: klienten får inte varje träff
  skickad, eller statistiken räknar mer än träffar (inte löst).
- **Granater:** en granat startar några enheter från sitt fartygs senast kända position (kanonerna är
  utspridda längs skrovet); nästan varje granats slut följer, inom en minut, ett skott som klienten såg.

Testerna bygger repriser i samma layout, så ingen riktig repris sparas i det här arkivet.

**Inte kontrollerat:** klienter före 0.9.6, Lesta-klienten (Mir Korabley), operationer och scenarier utöver
ett, klan- och rankade strider, och vilket fartygsnummer som är vilket fartyg.

---

Del av [3DHeat](https://github.com/Holdi601/3DHeat) ([dokumentation](https://holdi601.github.io/3DHeat/)). Källa: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
