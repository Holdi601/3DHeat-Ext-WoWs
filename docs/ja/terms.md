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

2026-11-07 に読んだもの。Wargaming EULA のバージョン 14（2024 年 4 月 10 日発効。現行として掲載）。そのセクション 12.3 は World of Warships の MOD の方針を指していますが、そのページはブラウザーの外では表示されず、読んでいません。条文は英語の原文のまま引用します:

- 5.3 (b): unless authorised in writing, you must not "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content".
- 12.1 (k): prohibited is "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."
- 12.1 (l): "... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming".
- 12.1 (p): "Circumventing or bypassing enforcement and security measures
  implemented by Wargaming".

この変換ツールがすること: ゲームが戦闘の後に、ゲームの外で書いたファイルを読みます。ゲームの中では何も変えず、サーバーとは通信せず、戦闘中に何も表示しません。ストリームは、ゲームの鍵で復号します。これは 5.3 (b) と 12.1 (p) が対象とすると読めるかもしれません。使うかどうかはユーザー自身の判断です。だからこれは別のパッケージになっています。

## ライセンスと出典 {#licence-and-sources}

MIT（[`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)）。numpy（BSD-3-Clause）と pyarrow（Apache-2.0）が必要です。このプロジェクトのために書かれたものです。ここの Blowfish の暗号は独自のもので、その表は、暗号が定義するとおりに円周率の桁から計算されています。フォーマットについての事実は、リプレイツールの間では一般的に知られています。単位の尺度の注記は landaire/wows-toolkit（MIT）からです。ほかのどのプロジェクトのコードも、コピーされていません。

`bigworld.py` と `table.py` は、World of Tanks の変換ツール（[3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)）と同じファイルです。両方を一緒に変えてください。

---

[3DHeat](https://github.com/Holdi601/3DHeat)（[ドキュメント](https://holdi601.github.io/3DHeat/)）の一部です。ソース: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
