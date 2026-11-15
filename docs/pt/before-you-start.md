---
title: Antes de começar
nav_order: 2
lang: pt
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Antes de começar {#before-you-start}

Nunca usou a linha de comando? Esta página leva você de zero até um `heat3d-wows-replay`
funcionando em cerca de dez minutos. Se você já usa Python, vá direto para
[Instalação](installing.md).

## 1. Instale o Python {#install-python}

1. Baixe o Python **3.10 ou mais recente** em
   [python.org/downloads](https://www.python.org/downloads/).
2. No Windows, marque **Add python.exe to PATH** na primeira janela do instalador e clique
   em **Install Now**.
3. No macOS e no Linux, o Python 3 costuma já estar instalado. Digite `python3` onde estas
   páginas dizem `python`, e `pip3` onde dizem `pip`.

## 2. Abra um terminal {#open-a-terminal}

O terminal é uma janela onde você digita comandos.

- **Windows:** abra a pasta no Explorador de Arquivos, clique na barra de endereço, digite
  `cmd` e pressione Enter. Uma janela abre, já nessa pasta.
- **macOS:** abra o aplicativo **Terminal**. **Linux:** clique com o botão direito dentro da
  pasta e escolha **Abrir no Terminal**.

Para ir a outra pasta, digite `cd` e o caminho da pasta:

```bash
cd "C:\Users\voce\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Verifique se o Python funciona {#check-that-python-works}

```bash
python --version
```

Você deve ver `Python 3.` e um número 10 ou maior, por exemplo `Python 3.12.4`.

## 4. Baixe a ferramenta e instale {#get-the-tool-and-install-it}

1. Na [página da ferramenta no GitHub](https://github.com/Holdi601/3DHeat-Ext-WoWs), clique no
   botão verde **Code** e depois em **Download ZIP**, e descompacte o zip.
2. Abra um terminal na pasta descompactada (a que tem o `README.md`).
3. Digite:

   ```bash
   pip install -e .
   ```

   No final, você deve ver: `Successfully installed heat3d-ext-wows-0.1.0` (talvez com mais nomes).
4. Confira:

   ```bash
   heat3d-wows-replay --version
   ```

   Você deve ver: `heat3d-wows-replay 0.1.0`

## Como ler os comandos destas páginas {#how-to-read-the-commands-on-these-pages}

- Palavras entre colchetes angulares, como `<replays>`, são lugares a preencher: digite ali o
  seu arquivo ou pasta, sem os colchetes.
- Um caminho com espaços precisa de aspas: `"C:\Program Files (x86)\Steam"`.
- O texto depois de `#` é um comentário: você não digita isso.
- `-o out` escreve numa pasta chamada `out`, dentro da pasta em que o seu terminal está. Ela é
  criada se não existir.

## Como é um resultado de sucesso {#what-success-looks-like}

O comando mostra uma linha por replay, por exemplo:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

e termina com o status de saída `0`. Os arquivos novos ficam na pasta `out`.

## Erros comuns {#common-errors}

| Você vê | O que fazer |
|---|---|
| `'python' is not recognized ...` ou `command not found` | o Python não está no PATH: instale de novo com **Add python.exe to PATH** marcado, ou digite `py` em vez de `python` (Windows) |
| `'pip' is not recognized ...` | digite `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | digite `python -m heat3d_ext_wows` em vez de `heat3d-wows-replay`; faz a mesma coisa |
| `No module named heat3d_ext_wows` | você não está na pasta da ferramenta, ou ela não está instalada: use `cd` para ir até lá e rode `pip install -e .` |
| `the following arguments are required: -o/--out` | acrescente `-o out` ao comando |

Próximo: [Converter replays](converting.md).
