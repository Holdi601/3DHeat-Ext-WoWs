---
title: Converter replays
nav_order: 4
lang: "pt"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Converter replays {#converting-replays}

## Passo a passo {#step-by-step}

1. **Ative a gravação**: `isReplayEnabled` no `preferences.xml` do jogo, ou a opção própria do
   jogo onde ela existe. A partir daí, o jogo salva cada batalha na pasta `replays` da sua
   instalação do World of Warships, por exemplo `C:\Games\World_of_Warships_EU\replays`.
2. **Abra um terminal** numa pasta onde os resultados possam ser gravados
   ([Antes de começar](before-you-start.md)).
3. **Rode o conversor** sobre arquivos de replay, ou sobre pastas que os contenham:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` é criada na pasta em que o seu terminal está.
4. **Leia o que ele diz.** Você deve ver uma linha por replay, terminando na tabela que foi
   gravada.
5. **Abra o resultado** no visualizador 3DHeat: `out/<map>/<match>.parquet` na aba Mapa de
   calor, `<match>.match.json` na aba Partida. Ou leia os arquivos com qualquer leitor de
   Parquet ou JSON.

![Uma execução em um replay sintético: convertendo, executando de novo, um arquivo com defeito, uma pasta vazia](../assets/img/convert.svg)

A figura mostra uma execução em um replay que os testes criam em código (sem replay real):

- um replay convertido: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`;
- executado de novo, a partida já gravada é pulada: `<file>: already written, <table>`;
- um arquivo que não é um replay: `<file>: not converted: <why>` (na saída de erros; status de
  saída 1, os demais replays são convertidos mesmo assim);
- nenhum replay encontrado: `no .wowsreplay files in <folders>` (status de saída 2).

## Opções {#options}

| Opção | Padrão | Faz |
|---|---|---|
| `replays` (uma ou mais) | - | arquivos `.wowsreplay`, ou pastas onde eles são procurados (as subpastas também) |
| `-o`, `--out` | obrigatória | a pasta onde gravar: uma pasta por mapa dentro |
| `--force` | desligada | converte de novo o que já está gravado |
| `--ship-names JSON` | - | um arquivo JSON `{"<shipId>": "<name>", ...}`: os replays nomeiam só o navio do jogador que grava; os demais, pelo número |
| `--version` | - | mostra `heat3d-wows-replay <versão>` e para |
| `-h`, `--help` | - | mostra as opções e para |

As opções como o programa as mostra: [Referência de comandos](../cli-reference.md).

## O que é gravado {#what-is-written}

Só arquivos soltos: este conversor não grava nenhum arquivo `.3dheat` (o visualizador pode
empacotá-los num só: [Um arquivo por partida](https://holdi601.github.io/3DHeat/container.html)).
Por replay, em `out/<map>/` (o nome do mapa sem o seu `spaces/`):

| Arquivo | O que é |
|---|---|
| `<match>.parquet` | a tabela: a posição de cada navio ao longo do tempo e cada evento onde aconteceu ([A tabela](table.md)) |
| `<match>.match.json` | o documento da partida: mapa, versão do cliente, jogadores, afundamentos, chat e todo o resto ([O documento da partida](match-document.md)) |
| `<match>.messages.parquet` | o arquivo auxiliar: cada item do replay que os dois arquivos acima não guardam inteiro ([Completude](completeness.md)) |

`<match>` é o id da própria batalha, ou o nome do arquivo quando a gravação parou antes dos
resultados.

## Status de saída {#exit-status}

`0` quando todos os replays foram convertidos ou pulados, `1` quando algum falhou (os demais
são convertidos mesmo assim), `2` quando nenhum arquivo de replay foi encontrado.

---

Parte do [3DHeat](https://github.com/Holdi601/3DHeat) ([documentação](https://holdi601.github.io/3DHeat/)). Código: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
