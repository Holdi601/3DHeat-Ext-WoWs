---
title: Instalação
nav_order: 3
lang: pt
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# Instalação {#installing}

Nunca usou a linha de comando? Leia primeiro [Antes de começar](before-you-start.md).
Precisa de Python 3.10 ou mais recente; numpy e pyarrow são instalados junto.

## Passo a passo {#step-by-step}

1. Obtenha o código: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`,
   ou baixe um zip em [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases)
   e descompacte.
2. Abra um terminal nessa pasta e digite `pip install -e .`. Isso põe o comando
   `heat3d-wows-replay` no seu caminho (PATH).
3. Confira: `heat3d-wows-replay --version`. Você deve ver
   `heat3d-wows-replay 0.1.0`. `heat3d-wows-replay --help` lista as opções:

![heat3d-wows-replay --help](../assets/img/help.svg)

Sem instalar, `python -m heat3d_ext_wows ...` na pasta da ferramenta faz a mesma coisa.

O 3DHeat Watcher executa este comando nos replays novos quando está instalado, e funciona
sem ele.

## Atualizações {#updates}

A cada início, o comando verifica primeiro as releases do projeto no GitHub (no máximo um
pedido a cada poucas horas; nunca interrompe uma conversão, com ou sem internet). Quando há
uma versão nova, o comando pergunta antes de instalá-la: um `git clone` é atualizado com
`git pull --ff-only` (recusado se você tiver mudanças locais), uma cópia baixada pelo arquivo
da release. `HEAT3D_NO_UPDATE=1` desliga a verificação e a atualização.

---

Parte do [3DHeat](https://github.com/Holdi601/3DHeat) ([documentação](https://holdi601.github.io/3DHeat/)). Código: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
