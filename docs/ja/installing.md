---
title: インストール
nav_order: 3
lang: ja
source: installing.md
source_hash: "39ecfa59d182"
nav_exclude: true
search_exclude: true
---
# インストール {#installing}

コマンドラインは初めてですか？ 先に [始める前に](before-you-start.md) を読んでください。
Python 3.10 以降が必要です。numpy と pyarrow はこれと一緒に入ります。

## 手順 {#step-by-step}

1. コードを入手します: `git clone https://github.com/Holdi601/3DHeat-Ext-WoWs.git`。
   または [Releases](https://github.com/Holdi601/3DHeat-Ext-WoWs/releases) から zip をダウンロードして展開します。
2. そのフォルダーでターミナルを開き、`pip install -e .` と入力します。これで `heat3d-wows-replay` コマンドが PATH に入ります。
3. 確かめます: `heat3d-wows-replay --version`。`heat3d-wows-replay 0.1.0` と表示されるはずです。`heat3d-wows-replay --help` でオプションの一覧が出ます:

![heat3d-wows-replay --help](../assets/img/help.svg)

インストールせずに使うには、ツールのフォルダーで `python -m heat3d_ext_wows ...` を実行します。同じことをします。

3DHeat Watcher は、インストールされていれば新しいリプレイに対してこのコマンドを実行します。なくても動きます。

## 更新 {#updates}

起動するたびに、まずプロジェクトの GitHub リリースを確認します（数時間に 1 回までの問い合わせです。変換を止めることはなく、オンラインでもオフラインでも動きます）。新しいリリースがあると、コマンドはインストールする前に確認を求めます。`git clone` で入れたものは `git pull --ff-only` で更新されます（手元に変更があるときは拒否されます）。ダウンロードしたものは、リリースのアーカイブから更新されます。`HEAT3D_NO_UPDATE=1` を設定すると、確認と更新の両方を止められます。

---

[3DHeat](https://github.com/Holdi601/3DHeat)（[ドキュメント](https://holdi601.github.io/3DHeat/)）の一部です。ソース: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
