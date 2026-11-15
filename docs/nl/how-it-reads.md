---
title: "Hoe het een replay leest"
nav_order: 7
lang: nl
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Hoe het een replay leest {#how-it-reads-a-replay}

Een replay is een kop van JSON-blokken en de pakketstroom van het spel (notities over het formaat staan in
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Het eerste blok, ongeversleuteld: de kaart, de clientversie, de opnemende speler en zijn schip, en de
  deelnemerslijst - de naam van elke speler, vriend of vijand, en zijn schipnummer. Nieuwere clients (15.x) voegen
  twee blokken toe: een leeg blok, en het account van de opnemende speler en het id van het gevecht als tekst, gelezen
  in `blockIds`. De resultaten staan niet in de JSON; 15.x bewaart ze in de stroom.
- De pakketstroom, met zlib gecomprimeerd en met Blowfish versleuteld met een sleutel die het spel meedraagt,
  die de communitytools die deze bestanden lezen hebben gepubliceerd. Na ontcijfering bevat hij:
  - de positie-updates van de engine van elk schip dat de client kon zien (het eigen team de hele tijd, vijanden
    zolang ze gespot waren of dichtbij), meerdere keren per seconde terwijl ze bewegen en minder vaak als ze stilliggen;
  - het eigen schip van de opnemende speler in een eigen pakket, ongeveer zeven keer per seconde;
  - eenmaal, aan het begin, de records van de spelers als een gepickelde Python-lijst. Die zeggen welke entiteit in de
    stroom welke speler is. Hun sleutels zijn genummerd, en de nummers veranderen met patches, dus de lezer vindt de
    sleutels aan hun waarden: de sleutel met de namen van de deelnemerslijst, en de sleutel met de entiteiten die
    positie-updates hebben;
  - de aanroep van de server die de client vertelt dat een schip gezonken is: slachtoffer, killer, oorzaak. Hij wordt
    gevonden aan zijn vorm (twaalf bytes; de eerste twee zijn schipentiteiten; elk slachtoffer komt één keer voor),
    niet aan zijn nummer;
  - de schade van elk schip: een reeks (aanvaller, schade) per treffer, op het getroffen schip; en zijn gezondheid,
    een eigenschap die even eerder gezet werd;
  - elk salvo granaten en torpedo's waarvan de client op de hoogte gesteld werd: het type granaat, de schutter, het
    salvo, en het begin en de snelheid van elke granaat of torpedo;
  - waar granaten eindigden: de schutter, een treffertype, en de plaats van elk (bij clients van 15.x met meer over de
    granaat op de plek waar hij trof, wat overgeslagen wordt);
  - de chat: afzender, kanaal, regel;
  - gepickelde aanroepen naar de opnemende speler: zijn schadestatistieken, wijzigingen van de records van de spelers, de
    toestand van het gevecht;
  - bij clients van 15.x, de resultaten van het gevecht aan het eind: een eigen pakket, een JSON-object met het id van het
    gevecht, volledig gelezen in `results` van het wedstrijddocument (de eigen lijsten van het spel, zonder naam:
    `commonList`, `privateDataList`, `playersPublicInfo` per account, ...).

Pakket- en methodenummers die verschillen tussen de gecontroleerde versies (het eigen schip-pakket is 43 of 44, de
zinkingsaanroep 76 of 83, de granaten 101, 102, 126 of 127) worden allemaal aan hun vorm gevonden - zie
[`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - zodat een patch die
ze hernummert de tabel niet leegmaakt. De gevonden nummers staan in `decoded` van het wedstrijddocument.

**De pickle is onbetrouwbare data.** Een replay is een bestand van overal vandaan, en een pickle kan code noemen om uit te
voeren. Hij wordt geladen met een unpickler die elke klasse of functie die de pickle noemt een inert plaatshouder geeft, zodat
hij gewone data bouwt en niets anders. Een test voedt hem een pickle die `os.system` aanroept.

**Zinkingen** hebben de exacte tijd van de aanroep. Hun plaats is waar het slachtoffer het laatst gezien werd, als dat binnen
vijf seconden was. **Het begin van het gevecht** is het eerste moment dat een schip überhaupt beweegt (schepen liggen stil tijdens het aftellen).

Alles wat geen tabelrij is, staat in [het wedstrijddocument](match-document.md).

**Wat de client te horen kreeg** is volledig voor het eigen team en gedeeltelijk voor vijanden: hun schoten, treffers en
gezondheid staan erin zolang ze binnen bereik waren.

**Niet gelezen:**

- Vliegtuigen en hun squadrons (de aanroepen die ze dragen zijn niet uitgepluisd), de zichtupdates van de minimap (gepakt),
  spotten, lintjes, branden en overstromingen als eigen gebeurtenissen (hun schade staat in de treffers), verbruiksgoederen,
  veroveringspunten en teamscores (eigenschappen van entiteiten zonder definitie, die niet aan hun vorm onderscheiden zijn),
  de rest van de eigenschappen van een schip (richting, roer, snelheidsinstelling...).
- De sleutelnummers van de records van de spelers en de schadestatistieken als namen: het spel nummert ze, en de nummers
  veranderen; ze worden als nummers bewaard.
- De extra gegevens van een granaat op de plek waar hij trof (15.x) en de bytes na het begin en de snelheid van een
  granaat of torpedo.
- Resultaten van clients vóór 15.x: hun replays bevatten er geen.
- Het schipnummer als naam: de namen staan in de eigen parameterbestanden van het spel, niet in de replay.

## Hoe de lezing gecontroleerd is {#how-the-reading-was-checked}

De lezing is gecontroleerd op openbare replays van clients van 0.9 tot 15.x, elke waarde tegen iets dat de replay
een tweede keer geeft:

- **Posities:** de entiteit van elk schip kwam overeen met een naam uit de deelnemerslijst; headings komen overeen met de
  richting van de beweging binnen 0,1 rad; na zijn zinking beweegt een schip minder dan 0,1 eenheid. Een schip dat stilligt,
  wordt minder vaak bijgewerkt.
- **Gezondheid:** elk schip dat in het zicht van de client gezonken is, eindigt op gezondheid 0. Ongeveer de helft van alle
  treffers komt overeen met een daling van de gezondheid in de seconde ervoor; de rest valt samen met reparaties of andere treffers.
- **Schade tegenover de eigen statistieken van het spel:** op de nieuwste client ligt de gelezen schade van de opnemende
  speler binnen 0,1% van de statistieken. Op oudere clients zijn de statistieken hoger: de client krijgt niet elke treffer
  gestuurd, of de statistieken tellen meer dan treffers (niet opgelost).
- **Granaten:** een granaat begint een paar eenheden van de laatst bekende positie van zijn schip (de kanonnen staan verspreid
  langs de romp); bijna het einde van elke granaat volgt, binnen een minuut, op een schot dat de client zag.

De tests bouwen replays in dezelfde indeling, dus er wordt geen echte replay in deze repository bewaard.

**Niet gecontroleerd:** clients vóór 0.9.6, de client van Lesta (Mir Korabley), operaties en scenario's, behalve één scenario,
clan- en gerangschikte gevechten, en welk schipnummer welk schip is.

---

Onderdeel van [3DHeat](https://github.com/Holdi601/3DHeat) ([documentatie](https://holdi601.github.io/3DHeat/)). Bron: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
