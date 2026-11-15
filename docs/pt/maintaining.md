---
title: Manutenção
nav_order: 99
lang: "pt"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Manutenção da documentação {#maintaining-the-documentation}

Para quem publica uma nova versão. Faça os passos nesta ordem.

1. **Regenere as páginas de referência** a partir do código:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # tem que sair com 0
   ```

   Isso reescreve [Referência de comandos](../cli-reference.md) e [Lista de colunas](../columns.md).
   Nunca edite essas duas à mão.
2. **Liste o que mudou desde a última versão:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` é a última versão publicada (sem tag ainda: o `git log --oneline` inteiro). Cada
   recurso, opção ou coluna nova precisa da sua página e de uma linha na seção **Docs** do
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Revisão independente.** Alguém que não escreveu as páginas (uma pessoa ou um agente) lê o
   README, cada página e cada figura como três leitores: um iniciante que nunca usou um terminal,
   uma criança de 8 anos, e um profissional que confere cada opção, coluna e unidade com o código.
   Eles também conferem os diagramas com o código, e que nenhuma página cite um mapa, nível,
   jogador ou partida real, nem traga números de replays reais.
4. **Corrija o que a revisão encontrou.** Depois rode o passo 1 de novo e refaça as figuras cuja
   saída mudou.
5. **Traduções.** Cada página em `docs/<idioma>/` registra o hash da página em inglês de que foi
   traduzida. Traduza de novo cada página cuja fonte em inglês mudou, rótulos dos diagramas
   incluídos. Depois revise cada idioma: claro para os três leitores, rótulos corretos, e as mesmas
   palavras que o visualizador 3DHeat usa naquele idioma.
6. **Publicação:** suba o `VERSION` e crie a tag `v<VERSION>`. **Só envie depois do aval do dono.**

## Traduções: os comandos {#translations-the-commands}

O site é traduzido para os 40 idiomas do visualizador 3DHeat: o inglês fica em `docs/`, cada outro
idioma em `docs/<lang>/`, com os mesmos nomes de arquivo. `tools/docs_i18n.py` cuida da escrituração:

```bash
python tools/docs_i18n.py hashes             # depois de qualquer mudança em inglês: registra o hash de cada página
python tools/docs_i18n.py svg-strings        # depois de qualquer mudança em figura: os rótulos a traduzir
python tools/docs_i18n.py status             # por idioma: páginas atuais, desatualizadas e faltando
python tools/docs_i18n.py todo --lang de     # as páginas em alemão a (re)traduzir
python tools/docs_i18n.py svg-build --lang de    # as figuras em alemão a partir de docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # carimba as páginas em alemão com o hash inglês
python tools/docs_i18n.py check              # sai com 1 quando hashes ou rótulos estão desatualizados
```

Traduza só o que `todo` lista: mantenha Markdown, links, código, nomes de arquivo e de colunas como
estão, traduza títulos e descrições das figuras, e use as palavras do próprio visualizador 3DHeat
para seus botões e painéis (em `src/i18n/locales/<lang>/`). Páginas de referência geradas e figuras
de terminal continuam em inglês. No site, uma tradução desatualizada avisa isso e linka a página em
inglês; uma tradução faltando cai no inglês. O menu de idiomas do cabeçalho e o redirecionamento da
página inicial, por idioma do navegador, vêm de `docs/_includes/`.
