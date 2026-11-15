---
title: "Completezza"
nav_order: 8
lang: it
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Completezza {#completeness}

Nulla di un replay viene buttato via. Ciò che il convertitore legge va nella tabella e nel documento della partita; ogni altro elemento viene conservato intero nel file accessorio
`<match>.messages.parquet`; e il `selfCheck.completeness` del documento della partita conta cosa è diventato ogni tipo di elemento. Questa è la regola che condividono tutti i convertitori 3DHeat:
[I convertitori conservano tutto](https://holdi601.github.io/3DHeat/converters.html).

![L'autocontrollo di un replay sintetico: ogni elemento visto, letto, conservato o perso](../assets/img/completeness.svg)

## Il conteggio {#the-count}

Per ogni tipo di elemento, `selfCheck.completeness.types` dà:

| Conteggio | Significa |
|---|---|
| `seen` | quanti ne contiene il replay |
| `decoded` | letti interi |
| `partial` | letti in parte, e conservati interi nel file accessorio |
| `raw` | solo conservati interi nel file accessorio, non letti |
| `lost` | persi: sempre `0` |

I tipi sono quelli del replay stesso: `block <n>` (i blocchi JSON), i byte propri del contenitore,
`packet <type>`, e per le chiamate alle entità `method <entity type>.<number>`
e `property <entity type>.<number>`.
`selfCheck.entities.roles` dice quale tipo di entità è l'avatar del giocatore che registra e quale sono le navi. Un tipo che nessuno conosceva compare con il suo conteggio.

## Il file accessorio {#the-sidecar}

| Colonna | Cosa |
|---|---|
| `time` | l'orologio del replay, come nella tabella |
| `type`, `name` | il tipo di elemento; come lo chiama il convertitore, dove lo legge |
| `entity` | la nave o l'avatar a cui appartiene, come `entity` della tabella |
| `decoded` | ciò che ne è stato letto, come JSON |
| `payload`, `text` | i suoi byte, interi; i blocchi JSON, interi |
| `entityType`, `packet`, `method` | i numeri |

Le righe sono ordinate per pacchetto, metodo, entità e tempo. Quale entità è quale giocatore: `entities` e `players` del documento della partita.

## Cosa viene letto, e come è stato verificato {#what-is-read-and-how-it-was-checked}

- **I risultati** (15.x, `results`): il loro id di battaglia è quello del flusso, e ogni giocatore che contengono è nel roster dell'intestazione.
- **Il blocco degli id** (15.x, `blockIds`): l'account e la battaglia, letti come testo perché non si perda nessuna cifra.
- **Beccheggio e rollio** di ogni posizione: il rollio va con il tasso di virata, come una nave si inclina in virata; il beccheggio è quasi sempre 0.
- **Entità** (`entities`): quando ciascuna è entrata nella vista del client e quando è uscita. Nessuna nave ha una posizione tra l'uscita e il rientro.
- **La versione nel flusso** (`streamVersion`): uguale a quella dell'intestazione.

Tutto il resto letto (affondamenti, danni, salute, proiettili, siluri, dove sono finiti i proiettili, chat, chiamate pickle, i record dei giocatori, posizioni) è `partial`: nella tabella o nel documento della partita, e conservato intero nel file accessorio.

**Conservato ma non letto** (`raw`), i tipi più grossi: aggiornamenti di posizione non nella tabella (dopo che una nave è affondata, entità senza giocatore), le proprietà e i metodi frequenti senza un lettore, le proprietà delle creazioni di entità, e ogni altro pacchetto senza un lettore.

## Non disponibile {#not-available}

- Ciò che il server non ha mai inviato al client che registrava: la mira, la telecamera e i comandi di altri giocatori, i nemici finché non sono avvistati. Un replay è ciò che è stato detto a un solo client.
- I nomi dei tipi di entità, dei metodi, delle proprietà e le chiavi delle statistiche: stanno nei file di definizione del gioco, non nel replay. I numeri vengono conservati.
- I nomi delle navi per i numeri delle navi (usa `--ship-names`), e qualsiasi altra cosa che richieda i file propri del gioco.
- Risultati dei client precedenti alla 15.x: non sono nei loro replay.

---

Parte di [3DHeat](https://github.com/Holdi601/3DHeat) ([documentazione](https://holdi601.github.io/3DHeat/)). Fonte: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
