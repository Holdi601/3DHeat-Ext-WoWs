---
title: "Condizioni e licenza"
nav_order: 9
lang: "it"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Condizioni e licenza {#terms-and-licence}

## Le condizioni di Wargaming {#wargamings-terms}

Lette il 2026-11-07, EULA di Wargaming versione 14 (in vigore dal 10 aprile 2024, indicata come attuale); la sua sezione 12.3 rimanda a una politica sulle mod di World of Warships, la cui pagina non si è visualizzata fuori dal browser e non è stata letta:

- 5.3 (b): salvo autorizzazione scritta, non si deve decompilare, smontare, eseguire il reverse engineering o usare in modo non autorizzato il Contenuto. Il testo in inglese:
  "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): è vietato creare, usare, mettere a disposizione o distribuire software o strumenti non autorizzati, inclusi hack, trucchi, exploit, script, bot, trainer, programmi di automazione o altro software. Il testo in inglese:
  "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): è vietato qualsiasi software progettato per modificare un Prodotto e cambiarne l'esperienza utente ("mod"), salvo espressa autorizzazione di Wargaming. Il testo in inglese:
  "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): è vietato aggirare o eludere le misure di applicazione e sicurezza messe in atto da Wargaming. Il testo in inglese:
  "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

Cosa fa questo convertitore: legge un file che il gioco ha scritto, dopo la battaglia, fuori dal gioco. Non cambia nulla nel gioco, non parla con nessun server e non mostra nulla durante una battaglia. Decifra però il flusso con la chiave del gioco, cosa che 5.3 (b) e 12.1 (p) possono essere letti come se la coprissero. Usarlo è una decisione dell'utente; per questo è un pacchetto separato.

## Licenza e fonti {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Richiede numpy (BSD-3-Clause) e pyarrow
(Apache-2.0). Scritto per questo progetto: il cifrario Blowfish qui è proprio,
con le sue tabelle calcolate dalle cifre di pi greco come il cifrario le definisce.
I fatti sul formato sono nozioni comuni tra gli strumenti per i replay; la nota sulla scala delle unità viene da landaire/wows-toolkit (MIT). Nessun codice è stato preso da nessun altro progetto.

`bigworld.py` e `table.py` sono gli stessi file del convertitore per World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); cambiali sempre insieme.

---

Parte di [3DHeat](https://github.com/Holdi601/3DHeat) ([documentazione](https://holdi601.github.io/3DHeat/)). Fonte: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
