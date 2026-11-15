---
title: Completude
nav_order: 8
lang: "pt"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Completude {#completeness}

Nada de um replay é descartado. O que o conversor lê vai para a tabela e para o documento da
partida; todo outro item é guardado inteiro no arquivo auxiliar `<match>.messages.parquet`; e
`selfCheck.completeness` no documento da partida conta o que aconteceu com cada tipo de item.
Esta é a regra que todos os conversores do 3DHeat seguem:
[Conversores mantêm tudo](https://holdi601.github.io/3DHeat/converters.html).

![A autoverificação de um replay sintético: cada item visto, lido, guardado ou perdido](../assets/img/completeness.svg)

## A contagem {#the-count}

Para cada tipo de item, `selfCheck.completeness.types` dá:

| Contagem | Significa |
|---|---|
| `seen` | quantos o replay contém |
| `decoded` | lidos inteiros |
| `partial` | lidos em parte, e guardados inteiros no arquivo auxiliar |
| `raw` | só guardados inteiros no arquivo auxiliar, não lidos |
| `lost` | perdidos: sempre `0` |

Os tipos são os do próprio replay: `block <n>` (os blocos JSON), os próprios bytes do contêiner,
`packet <type>`, e, para chamadas em entidades, `method <entity type>.<number>` e
`property <entity type>.<number>`. `selfCheck.entities.roles` diz qual tipo de entidade é o avatar
do jogador que grava e quais são os navios. Um tipo que ninguém conhecia aparece com a sua contagem.

## O arquivo auxiliar {#the-sidecar}

| Coluna | O que é |
|---|---|
| `time` | o relógio do replay, como na tabela |
| `type`, `name` | o tipo do item; como o conversor o chama, onde o lê |
| `entity` | o navio ou avatar a que pertence, como o `entity` da tabela |
| `decoded` | o que foi lido dele, em JSON |
| `payload`, `text` | seus bytes, inteiros; os blocos JSON, inteiros |
| `entityType`, `packet`, `method` | os números |

As linhas são ordenadas por pacote, método, entidade e tempo. Qual entidade é qual jogador: o
`entities` e o `players` do documento da partida.

## O que é lido, e como foi conferido {#what-is-read-and-how-it-was-checked}

- **Os resultados** (15.x, `results`): o id da batalha deles é o do fluxo, e todo jogador neles
  está na lista de participantes do cabeçalho.
- **O bloco de ids** (15.x, `blockIds`): a conta e a batalha, lidas como texto para que nenhum
  dígito se perca.
- **Arfagem e rolamento** de cada posição: o rolamento acompanha a taxa de giro, como um navio
  inclina numa curva; a arfagem é quase sempre 0.
- **Entidades** (`entities`): quando cada uma entrou na visão do cliente e quando saiu. Nenhum
  navio tem posição entre sair e voltar.
- **A versão no fluxo** (`streamVersion`): igual à do cabeçalho.

Todo o resto lido (afundamentos, dano, vida, projéteis, torpedos, onde os projéteis terminaram,
chat, chamadas em pickle, os registros dos jogadores, posições) é `partial`: na tabela ou no
documento da partida, e guardado inteiro no arquivo auxiliar.

**Guardado mas não lido** (`raw`), os tipos maiores: atualizações de posição que não estão na
tabela (depois que um navio afundou, entidades sem jogador), as propriedades e métodos frequentes
sem leitor, as propriedades das criações de entidades, e todo outro pacote sem leitor.

## Não disponível {#not-available}

- O que o servidor nunca enviou ao cliente que gravou: a mira, a câmera e os comandos de outros
  jogadores, inimigos enquanto não foram vistos. Um replay é o que um cliente foi informado.
- Os nomes dos tipos de entidade, métodos, propriedades e as chaves das estatísticas: estão nos
  arquivos de definição do jogo, não no replay. Os números são guardados.
- Nomes dos navios para os números de navio (use `--ship-names`), e qualquer outra coisa que
  precise dos arquivos próprios do jogo.
- Resultados de clientes anteriores a 15.x: não estão nos seus replays.

---

Parte do [3DHeat](https://github.com/Holdi601/3DHeat) ([documentação](https://holdi601.github.io/3DHeat/)). Código: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
