---
title: O documento da partida
nav_order: 6
lang: "pt"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# O documento da partida {#the-match-document}

`<match>.match.json` guarda tudo o que o replay diz e que não é uma linha da tabela. A aba Partida
do visualizador lê esse arquivo. (O código o chama de resumo.)

![O início de um documento da partida sintético, e as suas chaves](../assets/img/match-document.svg)

## A batalha {#the-battle}

| Chave | O que é |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; o id da batalha; o mapa como o jogo o nomeia (`spaces/<map>`) e o seu nome de exibição |
| `clientVersion`, `streamVersion` | a versão do jogo no cabeçalho, e como o fluxo de pacotes a informa |
| `recorded` | quando o replay foi gravado, como o jogo o escreve |
| `player`, `vehicle` | o jogador que grava e o seu navio |
| `gameType`, `scenario` | o tipo da batalha (`RandomBattle`, ...) e o cenário, do cabeçalho |
| `duration` | o limite de tempo da batalha em segundos, do cabeçalho |
| `truncated` | a gravação parou cedo |
| `battleStart`, `recordingSeconds` | o início da batalha (o primeiro momento em que qualquer navio se move) e a duração da gravação, em segundos |
| `positionPacket`, `ownPositionPacket` | os números dos pacotes em que chegaram as posições: dos outros navios, e do próprio navio do jogador que grava |
| `deathMethod` | o número do método em que os afundamentos foram encontrados |
| `hz`, `ownHz`, `positions` | amostras por segundo dos outros navios e do próprio navio; linhas de posição |
| `units` | unidades do mundo (15 m pelos cascos, 30 m pelos alcances do jogo); x leste, y cima, z norte |
| `events` | o número de linhas da tabela de cada evento |
| `decoded` | o método e os números de pacote encontrados para cada tipo de mensagem |

## Jogadores e eventos {#players-and-events}

| Chave | O que é |
|---|---|
| `players` | uma entrada por navio: nome, `ally` ou `enemy`, número e nome do navio, entidade, amostras, abates, sobreviveu; `seen` (dano causado e recebido, projéteis, torpedos e a última vida que o cliente viu); `header` (a entrada da lista de participantes) e `record` (o registro do jogador no fluxo, pelo número da chave) |
| `kills` | cada afundamento: tempo, vítima, abatedor, número da causa, lugar |
| `chat` | cada linha do chat, com canal e remetente |
| `damageStats` | as estatísticas de dano do próprio jogador que grava, como o jogo as mantém: por arma e tipo, uma contagem e um valor (o tipo 0 é o dano causado) |
| `avatarPickles` | cada chamada em pickle ao jogador que grava, decodificada, por número de método |

## Cabeçalho, resultados e verificações {#header-results-and-checks}

| Chave | O que é |
|---|---|
| `header` | o primeiro bloco JSON, inteiro menos a lista de participantes: modo de jogo, clima, limite do mapa, tamanhos das equipes e mais |
| `moreBlocks` | os blocos JSON depois do primeiro, como estão |
| `blockIds` | 15.x: a conta do jogador que grava e o id da batalha, lidos como texto |
| `results` | 15.x: os resultados, que esses clientes guardam no fluxo |
| `entities` | cada entidade que o fluxo cria: seu número de tipo e papel, quando entrou na visão do cliente e quando saiu |
| `selfCheck` | a contagem de completude ([Completude](completeness.md)) e as verificações das entidades, dos resultados, dos ids e da versão |

---

Parte do [3DHeat](https://github.com/Holdi601/3DHeat) ([documentação](https://holdi601.github.io/3DHeat/)). Código: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
