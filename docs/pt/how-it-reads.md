---
title: Como ele lê um replay
nav_order: 7
lang: "pt"
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Como ele lê um replay {#how-it-reads-a-replay}

Um replay é um cabeçalho de blocos JSON e o fluxo de pacotes do jogo (notas sobre o formato em
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- O primeiro bloco, sem cifra: o mapa, a versão do cliente, o jogador que grava e o seu navio, e a
  lista de participantes - o nome de cada jogador, aliado ou inimigo, e o número do navio. Clientes
  mais novos (15.x) acrescentam dois blocos: um vazio, e a conta do jogador que grava e o id da
  batalha como texto, lidos em `blockIds`. Os resultados não estão no JSON; a 15.x os guarda no fluxo.
- O fluxo de pacotes, comprimido com zlib e cifrado com Blowfish, com uma chave que o jogo traz
  consigo, e que as ferramentas da comunidade que leem esses arquivos publicaram. Decifrado, ele traz:
  - as atualizações de posição do motor de cada navio que o cliente podia ver (a própria equipe o
    tempo todo, os inimigos enquanto detectados ou próximos), várias vezes por segundo enquanto se
    movem e com menos frequência quando não se movem;
  - o próprio navio do jogador que grava, em um pacote à parte, cerca de sete vezes por segundo;
  - uma vez, no começo, os registros dos jogadores como uma lista Python em pickle. Eles dizem qual
    entidade do fluxo é qual jogador. Suas chaves são numeradas, e os números mudam com os patches,
    então o leitor acha as chaves pelos seus valores: a chave que tem os nomes da lista, e a chave que
    tem as entidades com atualizações de posição;
  - a chamada do servidor que informa ao cliente que um navio afundou: vítima, abatedor, causa. Ela é
    encontrada pela forma (doze bytes; os dois primeiros são entidades de navio; cada vítima aparece
    uma vez), não pelo número;
  - o dano de cada navio: um vetor de (atacante, dano) por acerto, no navio atingido; e a sua vida,
    um conjunto de propriedades um momento antes;
  - cada salva de projéteis e de torpedos de que o cliente foi informado: o tipo do projétil, o
    atirador, a salva, e o início e a velocidade de cada projétil ou torpedo;
  - onde os projéteis terminaram: o atirador, um tipo de acerto, e o lugar de cada um (em clientes
    15.x, com mais dados sobre o projétil onde atingiu, que são pulados);
  - o chat: remetente, canal, linha;
  - chamadas em pickle ao jogador que grava: suas estatísticas de dano, atualizações dos registros dos
    jogadores, o estado da batalha;
  - em clientes 15.x, os resultados da batalha no fim: um pacote próprio, um objeto JSON com o id da
    batalha, lido inteiro no `results` do documento da partida (as listas próprias do jogo, sem nome:
    `commonList`, `privateDataList`, `playersPublicInfo` por conta, ...).

Números de pacote e de método que diferem entre as versões conferidas (o pacote do navio próprio é 43
ou 44, a chamada de afundamento 76 ou 83, os projéteis 101, 102, 126 ou 127) são todos encontrados
pela forma - veja [`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py) -, então um patch que renumera não esvazia a
tabela. Os números encontrados estão no `decoded` do documento da partida.

**O pickle é dado não confiável.** Um replay é um arquivo de qualquer origem, e um pickle pode nomear
código a executar. Ele é carregado com um desserializador que dá a cada classe ou função que o pickle
nomeia um substituto inerte, então constrói apenas dados simples e mais nada. Um teste lhe dá um pickle
que chama `os.system`.

**Afundamentos** têm o tempo exato da chamada. O seu lugar é onde a vítima foi vista pela última vez,
quando isso ocorreu a menos de cinco segundos. **O início da batalha** é o primeiro momento em que
algum navio se move (os navios ficam parados na contagem regressiva).

Tudo o que não é linha da tabela está em [o documento da partida](match-document.md).

**O que o cliente foi informado** é completo para a própria equipe e parcial para os inimigos: seus
tiros, acertos e vida estão ali enquanto estavam no alcance.

**Não lido:**

- Aviões e seus esquadrões (as chamadas que os trazem não foram desmontadas), as atualizações de
  visão do minimapa (compactadas), detecção, faixas, incêndios e inundações como eventos próprios (o
  seu dano está nos acertos), consumíveis, pontos de captura e pontuações de equipe (propriedades de
  entidades sem definição, não distinguidas pela forma), e o resto das propriedades de um navio (mira,
  leme, ajuste de velocidade...).
- Os números-chave dos registros dos jogadores e das estatísticas de dano como nomes: o jogo os
  numera, e os números mudam; são guardados como números.
- Os dados extras de um projétil onde atingiu (15.x) e os bytes depois do início e da velocidade de um
  projétil ou torpedo.
- Resultados de clientes anteriores a 15.x: seus replays não os trazem.
- O número do navio como nome: os nomes estão nos arquivos de parâmetros do próprio jogo, não no replay.

## Como a leitura foi conferida {#how-the-reading-was-checked}

A leitura foi conferida em replays públicos de clientes de 0.9 a 15.x, cada valor contra algo que o
replay dá uma segunda vez:

- **Posições:** a entidade de cada navio casou com um nome da lista de participantes; os rumos
  concordam com a direção do deslocamento a 0,1 rad; depois do seu afundamento, um navio se move
  menos de 0,1 unidade. Um navio parado é atualizado com menos frequência.
- **Vida:** cada navio afundado dentro da visão do cliente termina com vida 0. Cerca de metade de todos
  os acertos coincide com uma queda de vida no segundo anterior; os demais caem junto com reparos ou
  outros acertos.
- **Dano contra as estatísticas próprias do jogo:** no cliente mais novo, o dano lido do jogador que
  grava fica a 0,1% das estatísticas. Nos clientes mais antigos, as estatísticas são maiores: o cliente
  não recebe todos os acertos, ou as estatísticas contam mais do que acertos (não resolvido).
- **Projéteis:** um projétil começa a alguns unidades da última posição conhecida do seu navio (os
  canhões estão espalhados pelo casco); quase todo fim de projétil segue, em até um minuto, um tiro que
  o cliente viu.

Os testes criam replays no mesmo layout, então nenhum replay real é guardado neste repositório.

**Não conferido:** clientes anteriores a 0.9.6, o cliente da Lesta (Mir Korabley), operações e cenários
além de um, batalhas de clã e ranqueadas, e qual número de navio é qual navio.

---

Parte do [3DHeat](https://github.com/Holdi601/3DHeat) ([documentação](https://holdi601.github.io/3DHeat/)). Código: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
