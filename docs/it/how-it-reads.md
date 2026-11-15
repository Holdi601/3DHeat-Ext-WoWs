---
title: "Come legge un replay"
nav_order: 7
lang: it
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Come legge un replay {#how-it-reads-a-replay}

Un replay è un'intestazione di blocchi JSON e il flusso di pacchetti del gioco (note sul formato in
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- Il primo blocco, in chiaro: la mappa, la versione del client, il giocatore che registra e la sua nave, e il roster - il nome di ogni giocatore, alleato o nemico, e il numero della sua nave. I client più recenti (15.x) aggiungono altri due blocchi: uno vuoto, e l'account del giocatore che registra e l'id della battaglia come testo, letti in
  `blockIds`. I risultati non sono nel JSON; la 15.x li conserva nel flusso.
- Il flusso di pacchetti, compresso con zlib e cifrato con Blowfish con una chiave che il gioco contiene, che gli strumenti della comunità che leggono questi file hanno pubblicato. Decifrato, contiene:
  - gli aggiornamenti di posizione del motore di ogni nave che il client poteva vedere (la propria squadra per tutta la battaglia, i nemici mentre sono avvistati o vicini), più volte al secondo mentre si muovono e meno spesso quando non si muovono;
  - la nave del giocatore che registra, in un pacchetto proprio, circa sette volte al secondo;
  - una volta, all'inizio, i record dei giocatori come lista Python serializzata (pickle). Dicono quale entità del flusso è quale giocatore. Le loro chiavi sono numerate, e i numeri cambiano con le patch, quindi il lettore trova le chiavi dai loro valori: la chiave che contiene i nomi del roster, e la chiave che contiene le entità con aggiornamenti di posizione;
  - la chiamata del server che dice al client che una nave è affondata: vittima, assassino, causa. Viene trovata dalla sua forma (dodici byte; i primi due sono entità navi; ogni vittima compare una volta), non dal suo numero;
  - il danno di ogni nave: un array di (attaccante, danno) per colpo, sulla nave colpita; e la sua salute, un'impostazione di proprietà un attimo prima;
  - ogni salva di proiettili e di siluri di cui il client è stato informato: il tipo di proiettile, il tiratore, la salva, e la partenza e la velocità di ogni proiettile o siluro;
  - dove sono finiti i proiettili: il tiratore, un tipo di colpo, e il punto di ciascuno (sui client 15.x con più dati sul proiettile nel punto in cui ha colpito, che vengono saltati);
  - la chat: mittente, canale, riga;
  - le chiamate pickle al giocatore che registra: le sue statistiche di danno, gli aggiornamenti dei record dei giocatori, lo stato della battaglia;
  - sui client 15.x, i risultati della battaglia alla fine: un pacchetto proprio, un oggetto JSON con l'id della battaglia, letto intero nel `results` del documento della partita (le liste proprie del gioco, senza nome: `commonList`, `privateDataList`, `playersPublicInfo` per account, ...).

I numeri di pacchetto e di metodo che differiscono tra le versioni verificate (il pacchetto della propria nave è 43 o 44, la chiamata di affondamento 76 o 83, i proiettili 101, 102, 126 o 127) vengono tutti trovati dalla forma - vedi [`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) - così una patch che li rinumera non svuota la tabella. I numeri trovati sono nel `decoded` del documento della partita.

**Il pickle è un dato non fidato.** Un replay è un file che può arrivare da chiunque, e un pickle può nominare codice da eseguire. Viene caricato con un unpickler che dà a ogni classe o funzione che il pickle nomina un segnaposto inerte, così costruisce solo dati semplici e nient'altro. Un test gli dà un pickle che chiama `os.system`.

**Gli affondamenti** hanno l'ora esatta della chiamata. Il loro luogo è dove la vittima è stata vista per l'ultima volta, quando ciò è avvenuto entro cinque secondi. **L'inizio della battaglia** è il primo istante in cui una nave si muove (nel conto alla rovescia le navi restano ferme).

Tutto ciò che non è una riga della tabella è nel [documento della partita](match-document.md).

**Ciò che è stato detto al client** è completo per la sua squadra e parziale per i nemici: i loro colpi, colpi a segno e salute ci sono mentre sono nel raggio.

**Non letto:**

- Aerei e le loro squadriglie (le chiamate che li portano non sono state scomposte), gli aggiornamenti di visione della minimappa (compressi), l'avvistamento, i nastri, incendi e allagamenti come eventi propri (il loro danno è nei colpi), i consumabili, i punti di cattura e i punteggi di squadra (proprietà di entità senza definizione, non distinguibili per forma), il resto delle proprietà di una nave (mira, timone, impostazione della velocità...).
- I numeri delle chiavi dei record dei giocatori e delle statistiche di danno come nomi: il gioco le numera, e i numeri cambiano; vengono conservati come numeri.
- I dati extra di un proiettile nel punto in cui ha colpito (15.x) e i byte dopo la partenza e la velocità di un proiettile o siluro.
- Risultati dei client precedenti alla 15.x: i loro replay non ne contengono.
- Il numero della nave come nome: i nomi stanno nei file dei parametri propri del gioco, non nel replay.

## Come è stata verificata la lettura {#how-the-reading-was-checked}

La lettura è stata verificata su replay pubblici di client dalla 0.9 alla 15.x, ogni valore confrontato con qualcosa che il replay dà una seconda volta:

- **Posizioni:** l'entità di ogni nave corrispondeva a un nome del roster; i rilevamenti concordano con la direzione di marcia entro 0,1 rad; dopo il suo affondamento, una nave si sposta di meno di 0,1 unità. Una nave ferma viene aggiornata meno spesso.
- **Salute:** ogni nave affondata nella vista del client finisce con salute 0. Circa la metà di tutti i colpi corrisponde a una caduta di salute nel secondo precedente; il resto cade insieme a riparazioni o altri colpi.
- **Danno confrontato con le statistiche proprie del gioco:** sul client più recente il danno letto del giocatore che registra è entro lo 0,1% delle statistiche. Sui client più vecchi le statistiche sono più alte: al client non viene inviato ogni colpo, oppure le statistiche contano più dei colpi (non risolto).
- **Proiettili:** un proiettile parte a qualche unità dall'ultima posizione nota della sua nave (i cannoni sono distribuiti lungo lo scafo); quasi ogni fine di proiettile segue, entro un minuto, un colpo che il client ha visto.

I test costruiscono i replay con lo stesso layout, quindi nessun replay reale è conservato in questo repository.

**Non verificato:** client precedenti alla 0.9.6, il client Lesta (Mir Korabley), operazioni e scenari oltre il primo, battaglie di clan e classificate, e quale numero di nave corrisponda a quale nave.

---

Parte di [3DHeat](https://github.com/Holdi601/3DHeat) ([documentazione](https://holdi601.github.io/3DHeat/)). Fonte: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
