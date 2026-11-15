---
title: 始める前に
nav_order: 2
lang: "ja"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# 始める前に {#before-you-start}

コマンドラインは初めてですか？ このページは、何もない状態から動く `heat3d-wows-replay` まで、約 10 分で案内します。すでに Python を使っている方は、[インストール](installing.md) に直接進んでください。

## 1. Python を入れる {#install-python}

1. [python.org/downloads](https://www.python.org/downloads/) から Python **3.10 以降** をダウンロードします。
2. Windows では、インストーラーの最初の画面で **Add python.exe to PATH** にチェックを入れてから、**Install Now** をクリックします。
3. macOS と Linux では、Python 3 がすでに入っていることがよくあります。このページで `python` と書いてあるところは `python3` と入力し、`pip` は `pip3` と入力してください。

## 2. ターミナルを開く {#open-a-terminal}

ターミナルとは、コマンドを入力するウィンドウのことです。

- **Windows:** エクスプローラーでフォルダーを開き、アドレスバーをクリックして `cmd` と入力し、Enter を押します。そのフォルダーがすでに開かれた状態でウィンドウが開きます。
- **macOS:** **ターミナル** アプリを開きます。**Linux:** フォルダーの中で右クリックし、**ターミナルで開く** を選びます。

別のフォルダーに移動するには、`cd` とフォルダーを入力します:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Python が動くか確かめる {#check-that-python-works}

```bash
python --version
```

`Python 3.` と、10 以上の番号が表示されるはずです。たとえば `Python 3.12.4` のように表示されます。

## 4. ツールを入手して入れる {#get-the-tool-and-install-it}

1. [ツールの GitHub ページ](https://github.com/Holdi601/3DHeat-Ext-WoWs) で、緑色の **Code** ボタン、次に **Download ZIP** をクリックし、zip を展開します。
2. 展開したフォルダー（`README.md` があるフォルダー）でターミナルを開きます。
3. 次のように入力します:

   ```bash
   pip install -e .
   ```

   最後に `Successfully installed heat3d-ext-wows-0.1.0` と表示されるはずです（ほかの名前も一緒に表示されることがあります）。
4. 動くか確かめます:

   ```bash
   heat3d-wows-replay --version
   ```

   `heat3d-wows-replay 0.1.0` と表示されるはずです。

## このページのコマンドの読み方 {#how-to-read-the-commands-on-these-pages}

- `<replays>` のように山かっこで囲まれた言葉は、置き換え用の場所です。かっこを除いて、ご自分のファイルやフォルダーの名前を入力してください。
- スペースを含むパスには引用符が必要です: `"C:\Program Files (x86)\Steam"`。
- `#` の後の文字はコメントです。入力しません。
- `-o out` は、ターミナルのいるフォルダーの中に `out` というフォルダーを作ってそこへ書き込みます。なければ作られます。

## 成功したときの見え方 {#what-success-looks-like}

コマンドは、リプレイ 1 つにつき 1 行を表示します。たとえば次のとおりです:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

そして終了ステータス `0` で終わります。新しいファイルは `out` フォルダーに入っています。

## よくあるエラー {#common-errors}

| 表示されたもの | 対処 |
|---|---|
| `'python' is not recognized ...` または `command not found` | Python が PATH に入っていません。**Add python.exe to PATH** にチェックを入れて入れ直すか、Windows では `python` の代わりに `py` と入力してください |
| `'pip' is not recognized ...` | 代わりに `python -m pip install -e .` と入力してください |
| `'heat3d-wows-replay' is not recognized ...` | `heat3d-wows-replay` の代わりに `python -m heat3d_ext_wows` と入力してください。同じことをします |
| `No module named heat3d_ext_wows` | ツールのフォルダーにいないか、まだ入っていません。そのフォルダーに `cd` で移動して `pip install -e .` を実行してください |
| `the following arguments are required: -o/--out` | コマンドに `-o out` を追加してください |

次へ: [リプレイの変換](converting.md)。
