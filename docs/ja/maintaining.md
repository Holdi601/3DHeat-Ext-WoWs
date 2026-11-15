---
title: ドキュメントの保守
nav_order: 99
lang: ja
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# ドキュメントの保守 {#maintaining-the-documentation}

新しいバージョンを公開する人向けです。次の順番で手順を行ってください。

1. **参照ページをコードから再生成する:**

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # 終了コード 0 でなければならない
   ```

   これで [コマンドリファレンス](../cli-reference.md) と [列の一覧](../columns.md) が書き直されます。この 2 つのページは手で編集しないでください。
2. **前回のリリース以降の変更を一覧にする:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` は最後に公開されたバージョンです（タグがまだない場合は、`git log --oneline` 全体）。新しい機能、オプション、列には、それぞれのページと、[CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md) の **Docs** の節への 1 行が必要です。
3. **独立したレビュー。** ページを書いていない人（人でもエージェントでもよい）が、README、すべてのページ、すべての図を 3 種類の読者として読みます。3 種類とは、ターミナルを使ったことがない初心者、8 歳の子ども、そしてすべてのオプション、列、単位をコードと照らし合わせるプロの読者です。図がコードと合っているか、実在のマップ、レベル、プレイヤー、マッチを名指ししたり、実際のリプレイから得た数値を載せたりしていないかも確認します。
4. **レビューで見つかったことを直す。** そのうえで手順 1 をもう一度行い、出力が変わった図は描き直します。
5. **翻訳。** `docs/<言語>/` の各ページには、翻訳元の英語ページのハッシュが記録されています。英語のソースが変わったページは、図のラベルを含めて、もう一度翻訳してください。そのうえで各言語を確認します。3 種類の読者すべてにとって分かりやすいか、ラベルは正しいか、3DHeat ビューアがその言語で使っている言葉と同じか。
6. **公開:** `VERSION` を上げて、`v<VERSION>` のタグを付けます。**公開する (push) のはオーナーの許可を得てからにしてください。**

## 翻訳: コマンド {#translations-the-commands}

サイトは 3DHeat ビューアの 40 言語に翻訳されています。英語は `docs/` に、ほかの各言語は同じファイル名で `docs/<lang>/` に置かれます。`tools/docs_i18n.py` が管理を行います:

```bash
python tools/docs_i18n.py hashes             # 英語を変えたら: 各ページのハッシュを記録
python tools/docs_i18n.py svg-strings        # 図を変えたら: 翻訳するラベル
python tools/docs_i18n.py status             # 言語ごと: 最新、古い、欠けているページ
python tools/docs_i18n.py todo --lang de     # 翻訳（または翻訳し直す）ドイツ語のページ
python tools/docs_i18n.py svg-build --lang de    # docs/assets/i18n/svg/de.json からドイツ語の図を作る
python tools/docs_i18n.py finish --lang de   # ドイツ語のページに英語のハッシュを押す
python tools/docs_i18n.py check              # ハッシュかラベルが古いと終了コード 1
```

`todo` が挙げたものだけを翻訳します。Markdown、リンク、コード、ファイル名と列名はそのままにし、タイトルと図の説明は訳します。ボタンやパネルの名前には、3DHeat ビューア自身の言葉を使ってください（`src/i18n/locales/<lang>/`）。生成された参照ページとターミナルの図は英語のままです。サイトでは、古い翻訳には、その旨と英語ページへのリンクが表示されます。欠けているページは英語にフォールバックします。ヘッダーの言語メニューと、トップページのブラウザー言語へのリダイレクトは `docs/_includes/` から来ます。
