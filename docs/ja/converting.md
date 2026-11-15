---
title: リプレイの変換
nav_order: 4
lang: "ja"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# リプレイの変換 {#converting-replays}

## 手順 {#step-by-step}

1. **ゲームで録画をオンにする。** ゲームの `preferences.xml` の `isReplayEnabled`、または設定があればゲーム自身の設定で行います。それ以降、ゲームは各戦闘を World of Warships のインストールの `replays` フォルダーに保存します。たとえば `C:\Games\World_of_Warships_EU\replays` です。
2. **ターミナルを開く。** 結果を置いてもよいフォルダーで開いてください（[始める前に](before-you-start.md)）。
3. **変換ツールを実行する** リプレイのファイル、またはそれを入れたフォルダーに対して:

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` はターミナルのいるフォルダーに作られます。
4. **表示された内容を読む。** リプレイ 1 つにつき 1 行が表示され、書き込んだテーブルで終わるはずです。
5. **結果を開く:** 3DHeat ビューアで `out/<map>/<match>.parquet` を ヒートマップ タブに、`<match>.match.json` を マッチ タブに読み込みます。または、任意の Parquet か JSON の読み取りツールで読んでください。

![合成リプレイでの実行: 変換、もう一度の実行、壊れたファイル、空のフォルダー](../assets/img/convert.svg)

この図は、テストがコードの中で作ったリプレイ（実際のリプレイは使わない）で実行した結果です:

- リプレイを変換した: `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`。
- もう一度実行した。すでに書かれたマッチは飛ばされる: `<file>: already written, <table>`。
- リプレイではないファイル: `<file>: not converted: <why>`（エラーの出力に。終了ステータス 1。ほかのリプレイは引き続き変換されます）。
- リプレイが見つからない: `no .wowsreplay files in <folders>`（終了ステータス 2）。

## オプション {#options}

| オプション | 既定 | 働き |
|---|---|---|
| `replays`（1 つ以上） | - | `.wowsreplay` のファイル、またはそれを探すフォルダー（サブフォルダーも含む） |
| `-o`、`--out` | 必須 | 書き込み先のフォルダー。中にマップごとのフォルダーが作られます |
| `--force` | オフ | すでに書かれているものを、もう一度変換する |
| `--ship-names JSON` | - | `{"<shipId>": "<name>", ...}` という形の JSON ファイル。リプレイが名前を付けるのは録画しているプレイヤーの艦船だけで、ほかは番号で示されます |
| `--version` | - | `heat3d-wows-replay <version>` を表示して終了する |
| `-h`、`--help` | - | オプションを表示して終了する |

プログラムが表示するとおりのオプション: [コマンドリファレンス](../cli-reference.md)。

## 書き出されるもの {#what-is-written}

ばらばらのファイルだけです。この変換ツールは `.3dheat` ファイルを書きません（ビューアは、それらを 1 つにまとめられます: [1 マッチを 1 ファイルに](https://holdi601.github.io/3DHeat/container.html)）。リプレイごとに、`out/<map>/` の中に（マップの名前から `spaces/` を除いたもの）:

| ファイル | 内容 |
|---|---|
| `<match>.parquet` | テーブル: すべての艦船の、時間ごとの位置と、それが起きたすべてのイベント（[テーブル](table.md)） |
| `<match>.match.json` | マッチドキュメント: マップ、クライアントのバージョン、プレイヤー、撃沈、チャット、そのほかすべて（[マッチドキュメント](match-document.md)） |
| `<match>.messages.parquet` | サイドカー: 上の 2 つのファイルが丸ごとは持たない、リプレイのすべての項目（[完全性](completeness.md)） |

`<match>` は、戦闘自身の ID です。録画が結果の前に止まった場合は、ファイルの名前になります。

## 終了ステータス {#exit-status}

すべてのリプレイが変換されたか飛ばされたら `0`、1 つでも失敗したら `1`（残りは引き続き変換されます）、リプレイファイルが見つからなければ `2` です。

---

[3DHeat](https://github.com/Holdi601/3DHeat)（[ドキュメント](https://holdi601.github.io/3DHeat/)）の一部です。ソース: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
