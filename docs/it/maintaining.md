---
title: "Manutenzione della documentazione"
nav_order: 99
lang: it
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Manutenzione della documentazione {#maintaining-the-documentation}

Per chi rilascia una nuova versione. Esegui i passi in quest'ordine.

1. **Rigenera le pagine di riferimento** dal codice:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # deve uscire con 0
   ```

   Questo riscrive il [Riferimento dei comandi](../cli-reference.md) e
   l'[Elenco delle colonne](../columns.md). Non modificare mai a mano queste due.
2. **Elenca cosa è cambiato dall'ultima release:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` è l'ultima versione rilasciata (senza tag ancora: l'intero
   `git log --oneline`). Ogni nuova funzione, opzione o colonna richiede la sua pagina
   e una riga nella sezione **Docs** di
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Revisione indipendente.** Qualcuno che non ha scritto le pagine (una persona o
   un agente) legge il README, ogni pagina e ogni immagine come tre
   lettori: un principiante che non ha mai usato un terminale, un bambino di 8 anni,
   e un professionista che controlla ogni opzione, colonna e unità con il codice.
   Controllano anche i diagrammi rispetto al codice, e che nessuna pagina nomini una vera mappa, un vero livello, un vero giocatore o una vera partita, o riporti dati di replay reali.
4. **Correggi ciò che la revisione ha trovato.** Poi esegui di nuovo il passo 1 e ridisegna le immagini
   i cui output sono cambiati.
5. **Traduzioni.** Ogni pagina sotto `docs/<lingua>/` registra l'hash della pagina inglese da cui è stata tradotta. Ritraduci ogni pagina
   la cui fonte inglese è cambiata, comprese le etichette dei diagrammi. Poi rivedi ogni lingua: chiara per tutti e tre
   i lettori, etichette giuste, e le stesse parole che usa il visualizzatore 3DHeat in quella lingua.
6. **Rilascio:** alza `VERSION` e crea il tag `v<VERSION>`. **Pubblica solo dopo il via libera del proprietario.**

## Traduzioni: i comandi {#translations-the-commands}

Il sito è tradotto nelle 40 lingue del visualizzatore 3DHeat: l'inglese in `docs/`, ogni altra
lingua in `docs/<lang>/` con gli stessi nomi di file. `tools/docs_i18n.py` tiene la contabilità:

```bash
python tools/docs_i18n.py hashes             # dopo ogni modifica all'inglese: registra l'hash di ogni pagina
python tools/docs_i18n.py svg-strings        # dopo ogni modifica di immagine: le etichette da tradurre
python tools/docs_i18n.py status             # per lingua: pagine aggiornate, superate, mancanti
python tools/docs_i18n.py todo --lang de     # le pagine tedesche da (ri)tradurre
python tools/docs_i18n.py svg-build --lang de    # immagini tedesche da docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # marca le pagine tedesche con l'hash inglese
python tools/docs_i18n.py check              # esce con 1 quando gli hash o le etichette sono superati
```

Traduci solo ciò che elenca `todo`: mantieni Markdown, link, codice, nomi di file e di colonne così come sono,
traduci i titoli e le descrizioni delle immagini, e usa le parole proprie del visualizzatore 3DHeat per i suoi pulsanti
e pannelli (il suo `src/i18n/locales/<lang>/`). Le pagine di riferimento generate e le immagini del terminale restano
in inglese. Sul sito, una traduzione superata lo dice e rimanda alla pagina inglese; una traduzione mancante
ricade sull'inglese. Il menu delle lingue nell'intestazione e il reindirizzamento alla lingua del browser della home page
vengono da `docs/_includes/`.
