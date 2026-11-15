---
title: Termos e licença
nav_order: 9
lang: pt
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# Termos e licença {#terms-and-licence}

## Os termos da Wargaming {#wargamings-terms}

Lidos em 2026-11-07, EULA da Wargaming versão 14 (em vigor desde 10 de abril de 2024, listada
como atual); a sua seção 12.3 aponta para uma política de mods do World of Warships, cuja página
não carregou fora de um navegador e não foi lida:

- 5.3 (b): a menos que autorizado por escrito, você não pode "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): é proibido "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

O que este conversor faz: lê um arquivo que o jogo gravou, depois da batalha, fora do jogo. Não
altera nada no jogo, não fala com nenhum servidor e não mostra nada durante uma batalha. Ele
decifra o fluxo com a chave do jogo, o que as cláusulas 5.3 (b) e 12.1 (p) podem ser lidas como
abrangendo. Usá-lo é decisão do usuário; por isso ele é um pacote separado.

## Licença e fontes {#licence-and-sources}

MIT ([`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)). Precisa de numpy
(BSD-3-Clause) e pyarrow (Apache-2.0). Escrito para este projeto: a cifra Blowfish daqui é própria,
com as suas tabelas calculadas a partir dos dígitos de pi, como a cifra define. Fatos sobre o formato
são conhecimento comum entre as ferramentas de replay; a nota sobre a escala das unidades vem de
landaire/wows-toolkit (MIT). Nenhum código foi tirado de nenhum outro projeto.

`bigworld.py` e `table.py` são os mesmos arquivos do conversor de World of Tanks
([3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)); altere os dois juntos.

---

Parte do [3DHeat](https://github.com/Holdi601/3DHeat) ([documentação](https://holdi601.github.io/3DHeat/)). Código: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
