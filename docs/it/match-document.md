---
title: "Il documento della partita"
nav_order: 6
lang: "it"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# Il documento della partita {#the-match-document}

`<match>.match.json` contiene tutto ciò che il replay dice e che non è una riga della tabella. La scheda Partita del visualizzatore lo legge. (Nel codice si chiama riepilogo.)

![L'inizio di un documento di partita sintetico, e le sue chiavi](../assets/img/match-document.svg)

## La battaglia {#the-battle}

| Chiave | Cosa |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; l'id della battaglia; la mappa come la nomina il gioco (`spaces/<map>`) e il suo nome visualizzato |
| `clientVersion`, `streamVersion` | la versione del gioco dall'intestazione, e come la dice il flusso di pacchetti |
| `recorded` | quando è stato registrato il replay, come lo scrive il gioco |
| `player`, `vehicle` | il giocatore che registra e la sua nave |
| `gameType`, `scenario` | il tipo di battaglia (`RandomBattle`, ...) e lo scenario, dall'intestazione |
| `duration` | il limite di tempo della battaglia in secondi, dall'intestazione |
| `truncated` | la registrazione si è fermata prima |
| `battleStart`, `recordingSeconds` | l'inizio della battaglia (il primo istante in cui si muove una nave) e la durata della registrazione, in secondi |
| `positionPacket`, `ownPositionPacket` | i numeri di pacchetto da cui arrivano le posizioni: quelle delle altre navi, quelle del giocatore che registra |
| `deathMethod` | il numero del metodo in cui sono stati trovati gli affondamenti |
| `hz`, `ownHz`, `positions` | campioni al secondo delle altre navi e della propria nave; righe di posizione |
| `units` | unità del mondo (15 m per gli scafi, 30 m per le portate del gioco); x est, y su, z nord |
| `events` | il numero di righe della tabella per ogni evento |
| `decoded` | i numeri di metodo e di pacchetto trovati per ogni tipo di messaggio |

## Giocatori ed eventi {#players-and-events}

| Chiave | Cosa |
|---|---|
| `players` | una voce per nave: nome, `ally` o `enemy`, numero e nome della nave, entità, campioni, uccisioni, sopravvissuto; `seen` (danno inflitto e subito, proiettili, siluri e ultima salute visti dal client); `header` (la voce del roster) e `record` (il record del giocatore dal flusso, per numero di chiave) |
| `kills` | ogni affondamento: ora, vittima, assassino, numero della causa, luogo |
| `chat` | ogni riga di chat, con canale e mittente |
| `damageStats` | le statistiche proprie del giocatore che registra come le tiene il gioco: per arma e tipo, un conteggio e un importo (il tipo 0 è il danno inflitto) |
| `avatarPickles` | ogni chiamata pickle al giocatore che registra, decodificata, per numero di metodo |

## Intestazione, risultati e verifiche {#header-results-and-checks}

| Chiave | Cosa |
|---|---|
| `header` | il primo blocco JSON, tutto tranne il roster: modalità di gioco, meteo, bordo della mappa, dimensioni delle squadre e altro |
| `moreBlocks` | i blocchi JSON dopo il primo, così come sono |
| `blockIds` | 15.x: l'account del giocatore che registra e l'id della battaglia, letti come testo |
| `results` | 15.x: i risultati, che questi client conservano nel flusso |
| `entities` | ogni entità creata dal flusso: il suo numero di tipo e ruolo, quando è entrata nella vista del client e quando è uscita |
| `selfCheck` | il conteggio di completezza ([Completezza](completeness.md)) e le verifiche delle entità, dei risultati, degli id e della versione |

---

Parte di [3DHeat](https://github.com/Holdi601/3DHeat) ([documentazione](https://holdi601.github.io/3DHeat/)). Fonte: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
