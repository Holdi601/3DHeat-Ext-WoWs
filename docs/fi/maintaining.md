---
title: Dokumentaation ylläpito
nav_order: 99
lang: "fi"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Dokumentaation ylläpito {#maintaining-the-documentation}

Sille, joka julkaisee uuden version. Tee vaiheet tässä järjestyksessä.

1. **Luo viitesivut uudelleen** koodista:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # täytyy päättyä koodiin 0
   ```

   Tämä kirjoittaa uudelleen [Komentoviitteen](../cli-reference.md) ja [Sarakeluettelon](../columns.md). Älä koskaan
   muokaa näitä kahta käsin.
2. **Listaa, mikä on muuttunut edellisen julkaisun jälkeen:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` on viimeisin julkaistu versio (ei tagia vielä: koko `git log --oneline`). Jokaisella uudella
   ominaisuudella, valinnalla tai sarakkeella on oltava oma sivunsa ja rivi
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md)-tiedoston **Docs**-osiossa.
3. **Riippumaton arvio.** Joku, joka ei kirjoittanut sivuja (ihminen tai agentti), lukee README:n, jokaisen sivun
   ja jokaisen kuvan kolmena lukijana: aloittelija, joka ei ole koskaan käyttänyt päätettä, kahdeksanvuotias ja
   ammattilainen, joka tarkistaa jokaisen valinnan, sarakkeen ja yksikön koodia vasten. He tarkistavat myös
   kaaviot koodia vasten, ja sen, ettei mikään sivu nimeä oikeaa karttaa, kenttää, pelaajaa tai ottelua, eikä
   anna lukuja oikeista replayista.
4. **Korjaa arvion löydökset.** Aja sitten vaihe 1 uudelleen ja piirrä uudelleen ne kuvat, joiden tulos muuttui.
5. **Käännökset.** Jokainen sivu kansiossa `docs/<language>/` tallentaa englanninkielisen sivun tiivisteen, josta
   se käännettiin. Käännä uudelleen jokainen sivu, jonka englanninkielinen lähde muuttui, kaaviomerkinnät mukaan
   lukien. Tarkista sitten jokainen kieli: selkeä kaikille kolmelle lukijalle, merkinnät oikein, ja samat sanat
   kuin 3DHeat-katselin käyttää kyseisellä kielellä.
6. **Julkaisu:** korota `VERSION` ja tagaa `v<VERSION>`. **Työnnä vain omistajan luvalla.**

## Käännökset: komennot {#translations-the-commands}

Sivusto on käännetty 3DHeat-katselimen 40 kielelle: englanti kansiossa `docs/`, muut kielet kansiossa
`docs/<lang>/` samoilla tiedostonimillä. `tools/docs_i18n.py` hoitaa kirjanpidon:

```bash
python tools/docs_i18n.py hashes             # minkä tahansa englanninkielisen muutoksen jälkeen: tallenna jokaisen sivun tiiviste
python tools/docs_i18n.py svg-strings        # kuvamuutosten jälkeen: käännettävät merkinnät
python tools/docs_i18n.py status             # kielikohtaisesti: ajantasaiset, vanhentuneet ja puuttuvat sivut
python tools/docs_i18n.py todo --lang de     # saksankieliset sivut, jotka pitää (uudelleen)kääntää
python tools/docs_i18n.py svg-build --lang de    # saksankieliset kuvat kohteesta docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # leimaa saksankieliset sivut englanninkielisellä tiivisteellä
python tools/docs_i18n.py check              # päättyy koodiin 1, kun tiivisteet tai merkinnät ovat vanhentuneet
```

Käännä vain se, minkä `todo` luettelee: säilytä Markdown, linkit, koodi sekä tiedosto- ja sarakenimet sellaisinaan,
käännä otsikot ja kuvien kuvaukset, ja käytä 3DHeat-katselimen omia sanoja sen painikkeille ja paneeleille (sen
`src/i18n/locales/<lang>/`). Generoidut viitesivut ja päätekuvat pysyvät englanniksi. Sivustolla vanhentunut
käännös sanoo sen ja linkittää englanninkieliseen sivuun; puuttuva käännös putoaa englanniksi. Otsikon kielivalikko
ja etusivun selaimen kielen uudelleenohjaus tulevat kansiosta `docs/_includes/`.
