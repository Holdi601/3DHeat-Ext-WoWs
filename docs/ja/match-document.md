---
title: マッチドキュメント
nav_order: 6
lang: "ja"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# マッチドキュメント {#the-match-document}

`<match>.match.json` には、テーブルの行にはならない、リプレイが伝えるすべてのことが入っています。ビューアの マッチ タブがこれを読みます。（コードではこれを要約（summary）と呼んでいます。）

![合成したマッチドキュメントの冒頭と、そのキー](../assets/img/match-document.svg)

## 戦闘 {#the-battle}

| キー | 内容 |
|---|---|
| `format`、`version` | `heat3d-wows-match`、`2` |
| `game`、`match`、`map`、`mapName` | `World of Warships`。戦闘の ID。ゲームが名付けたとおりのマップ（`spaces/<map>`）と、その表示名 |
| `clientVersion`、`streamVersion` | ヘッダーにあるゲームのバージョン。パケットの流れが示すバージョン |
| `recorded` | リプレイが録画された時刻。ゲームが書いたとおり |
| `player`、`vehicle` | 録画しているプレイヤーと、その艦船 |
| `gameType`、`scenario` | 戦闘の種類（`RandomBattle` など）とシナリオ。ヘッダーから |
| `duration` | 戦闘の制限時間（秒）。ヘッダーから |
| `truncated` | 録画が早く止まった |
| `battleStart`、`recordingSeconds` | 戦闘の開始（どの艦船かが初めて動いた瞬間）と、録画の長さ（秒） |
| `positionPacket`、`ownPositionPacket` | 位置が届いたパケットの番号: ほかの艦船のもの、録画しているプレイヤーのもの |
| `deathMethod` | 撃沈が見つかったメソッドの番号 |
| `hz`、`ownHz`、`positions` | ほかの艦船と自分の艦船の 1 秒あたりのサンプル数。位置の行 |
| `units` | ワールド単位（船体から見ると 15 m、ゲームの射程から見ると 30 m）。x は東、y は上、z は北 |
| `events` | 各イベントのテーブルの行の数 |
| `decoded` | メッセージの種類ごとに見つかったメソッドとパケットの番号 |

## プレイヤーとイベント {#players-and-events}

| キー | 内容 |
|---|---|
| `players` | 艦船 1 隻につき 1 つの項目: 名前、`ally`（味方）か `enemy`（敵）、艦船の番号と名前、エンティティ、サンプル数、キル、生存。`seen`（クライアントが見た、与えた・受けたダメージ、砲弾、魚雷、最後の体力）。`header`（名簿の項目）と `record`（ストリームからのプレイヤーの記録。キーの番号で） |
| `kills` | すべての撃沈: 時刻、犠牲者、キラー、原因の番号、場所 |
| `chat` | すべてのチャットの行。チャンネルと送信者つき |
| `damageStats` | 録画しているプレイヤー自身の統計。ゲームが保存しているとおり: 武器と種類ごとに、回数と量（種類 0 は与えたダメージ） |
| `avatarPickles` | 録画しているプレイヤーへのピクルされた呼び出しのすべて。復号され、メソッドの番号ごと |

## ヘッダー、結果、確認 {#header-results-and-checks}

| キー | 内容 |
|---|---|
| `header` | 最初の JSON のブロックのすべて（名簿を除く）: ゲームモード、天候、マップの境界、チームの人数など |
| `moreBlocks` | 最初のあとの JSON のブロック。そのままの形 |
| `blockIds` | 15.x: 録画しているプレイヤーのアカウントと戦闘の ID。テキストとして読まれたもの |
| `results` | 15.x: 結果。これらのクライアントはストリームの中に保存しています |
| `entities` | ストリームが作るすべてのエンティティ: その型の番号と役割、クライアントの視界に入った時刻と出た時刻 |
| `selfCheck` | 完全性の数（[完全性](completeness.md)）と、エンティティ、結果、ID、バージョンの確認 |

---

[3DHeat](https://github.com/Holdi601/3DHeat)（[ドキュメント](https://holdi601.github.io/3DHeat/)）の一部です。ソース: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
