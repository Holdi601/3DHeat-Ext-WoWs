---
title: Dokumentatsiooni hooldus
nav_order: 99
lang: et
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Dokumentatsiooni hooldus {#maintaining-the-documentation}

Järgmisele versioonile väljalaskjale. Tee sammud selles järjekorras.

1. **Genereeri viitelehed uuesti** koodist:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # peab lõppema koodiga 0
   ```

   See kirjutab üle [Käskude viite](../cli-reference.md) ja [Veergude loendi](../columns.md). Neid kahte ei muudeta
   kunagi käsitsi.
2. **Loetle, mis on muutunud viimase väljalaske järel:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` on viimane avaldatud versioon (kui silti veel ei ole: kogu `git log --oneline`). Iga uus funktsioon,
   valik või veerg vajab oma lehte ja rida [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md)
   jaotises **Docs**.
3. **Sõltumatu ülevaatus.** Keegi, kes ei kirjutanud lehti (inimene või agent), loeb README-d, iga lehte ja iga
   pilti kolme lugejana: algaja, kes pole kunagi terminali kasutanud, 8-aastane laps ja professionaal, kes kontrollib
   iga valikut, veergu ja ühikut koodi vastu. Nad kontrollivad ka diagramme koodi vastu ning seda, et ükski leht ei
   nimeta päris kaarti, tasemet, mängijat ega lahingut ega too arve päris kordustest.
4. **Paranda, mida ülevaatus leidis.** Seejärel käivita samm 1 uuesti ja joonista uuesti need pildid, mille väljund
   muutus.
5. **Tõlked.** Iga lehe all `docs/<language>/` on kirjas räsi inglisekeelsest lehest, millest see tõlgiti. Tõlgi
   uuesti iga leht, mille inglisekeelne lähe muutus, sealhulgas diagrammide sildid. Seejärel vaata iga keel üle:
   kõigile kolmele lugejale selge, sildid õiged ning samad sõnad, mida 3DHeati vaatur selles keeles kasutab.
6. **Väljalase:** tõsta `VERSION` ja märgi silt `v<VERSION>`. **Lükka üles alles pärast omaniku luba.**

## Tõlked: käsud {#translations-the-commands}

Sait on tõlgitud 3DHeati vaaturi 40 keelde: inglise keel on `docs/` kaustas, iga teine keel on `docs/<lang>/` kaustas
samade failinimedega. `tools/docs_i18n.py` teeb arvepidamise:

```bash
python tools/docs_i18n.py hashes             # after any English change: record each page's hash
python tools/docs_i18n.py svg-strings        # after any picture change: the labels to translate
python tools/docs_i18n.py status             # per language: current, outdated, missing pages
python tools/docs_i18n.py todo --lang de     # the German pages to (re)translate
python tools/docs_i18n.py svg-build --lang de    # German pictures from docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # stamp the German pages with their English hash
python tools/docs_i18n.py check              # exit 1 when hashes or labels are stale
```

Tõlgi ainult see, mida `todo` loetleb: säilita Markdown, lingid, kood, failide ja veergude nimed, tõlgi pealkirjad ja
pildikirjeldused ning kasuta 3DHeati vaaturi enda sõnu oma nuppude ja paneelide jaoks (tema
`src/i18n/locales/<lang>/`). Genereeritud viitelehed ja terminalipildid jäävad inglisekeelseks. Saidil ütleb aegunud
tõlge seda ja lingib inglisekeelsele lehele; puuduv tõlge taandub inglise keelele. Päises oleva keelemenüü ja
avalehe brauseri keele ümbersuunamise annab `docs/_includes/`.
