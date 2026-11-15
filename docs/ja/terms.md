---
title: 用語とライセンス
nav_order: 9
lang: ja
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# 用語とライセンス {#terms-and-licence}

## Wargaming の規約 {#wargamings-terms}

2026-11-07 に読んだもの。Wargaming EULA のバージョン 14（2024 年 4 月 10 日発効。現行として掲載）。そのセクション 12.3 は World of Warships の MOD の方針を指していますが、そのページはブラウザーの外では表示されず、読んでいません:

- 5.3 (b): 書面による許可がない限り、「... コンテンツを逆コンパイル、逆アセンブル、リバースエンジニアリング、またはそれ以外の方法で無許可で使用すること」をしてはなりません。
- 12.1 (k): 禁止されているのは「無許可のソフトウェアやツールを作成、使用、提供、または配布すること。これには、ハック、チート、エクスプロイト、スクリプト、ボット、トレーナー、自動化プログラム、または目的を問わず製品と何らかの形で相互作用する、その他のソフトウェアが含まれる。Wargaming とそのようなソフトウェアとの間のいかなる通信も、傍受、エミュレート、またはリダイレクトすること」。
- 12.1 (l): 「... Wargaming が明示的に許可しない限り、製品を変更してユーザー体験を変える（「MOD」）ように設計されたソフトウェア」。
- 12.1 (p): 「Wargaming が実装した実施と安全の措置を回避またはバイパスすること」。

この変換ツールがすること: ゲームが戦闘の後に、ゲームの外で書いたファイルを読みます。ゲームの中では何も変えず、サーバーとは通信せず、戦闘中に何も表示しません。ストリームは、ゲームの鍵で復号します。これは 5.3 (b) と 12.1 (p) が対象とすると読めるかもしれません。使うかどうかはユーザー自身の判断です。だからこれは別のパッケージになっています。

## ライセンスと出典 {#licence-and-sources}

MIT（[`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)）。numpy（BSD-3-Clause）と pyarrow（Apache-2.0）が必要です。このプロジェクトのために書かれたものです。ここの Blowfish の暗号は独自のもので、その表は、暗号が定義するとおりに円周率の桁から計算されています。フォーマットについての事実は、リプレイツールの間では一般的に知られています。単位の尺度の注記は landaire/wows-toolkit（MIT）からです。ほかのどのプロジェクトのコードも、コピーされていません。

`bigworld.py` と `table.py` は、World of Tanks の変換ツール（[3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)）と同じファイルです。両方を一緒に変えてください。

---

[3DHeat](https://github.com/Holdi601/3DHeat)（[ドキュメント](https://holdi601.github.io/3DHeat/)）の一部です。ソース: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
