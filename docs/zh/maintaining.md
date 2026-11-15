---
title: "维护文档"
nav_order: 99
lang: "zh"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# 维护文档 {#maintaining-the-documentation}

供发布新版本的人员使用。请按以下顺序操作。

1. **根据代码重新生成参考页面：**

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # 必须以 0 退出
   ```

   这会重写 [命令参考](../cli-reference.md) 和 [列清单](../columns.md)。这两页永远不要手动编辑。
2. **列出上一次发布以来的所有改动：**

   ```bash
   git log --oneline v<版本>..HEAD
   ```

   `<版本>` 是上一次发布的版本（如果还没有标签，则使用整个 `git log --oneline`）。每个新功能、选项或列，都需要有自己的页面，并在 [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md) 的 **Docs** 部分添加一行。
3. **独立审阅。** 由没有撰写这些页面的人（一个人或一个代理）从三类读者的角度阅读 README、每一页和每一张图片：一个从未用过终端的初学者、一个八岁的孩子，以及一个会对照代码检查每个选项、列和单位的专业人士。他们还要检查图表是否与代码一致，并确认没有任何页面提到真实的地图、关卡、玩家或对局，或给出来自真实录像的数据。
4. **修正审阅发现的问题。** 然后再次执行第 1 步，并重新绘制输出发生变化的图片。
5. **翻译。** `docs/<语言>/` 下的每一页都记录了它所翻译自的英文页面的哈希值。英文页面有改动时，需要重新翻译该页，包括图表标签。然后审阅每种语言：要让三类读者都能看懂，标签正确，并且使用 3DHeat 查看器在该语言中所用的词语。
6. **发布：** 提高 `VERSION` 并打上 `v<版本>` 标签。**只有在仓库所有者同意后才能推送。**

## 翻译：相关命令 {#translations-the-commands}

网站已翻译为 3DHeat 查看器的 40 种语言：英文位于 `docs/`，其他每种语言位于 `docs/<语言>/`，文件名相同。`tools/docs_i18n.py` 负责整理这些记录：

```bash
python tools/docs_i18n.py hashes             # 英文有任何改动后：记录每页的哈希值
python tools/docs_i18n.py svg-strings        # 图片有任何改动后：需要翻译的标签
python tools/docs_i18n.py status             # 每种语言：是否最新、过期或缺失的页面
python tools/docs_i18n.py todo --lang de     # 需要（重新）翻译的德语页面
python tools/docs_i18n.py svg-build --lang de    # 根据 docs/assets/i18n/svg/de.json 生成德语图片
python tools/docs_i18n.py finish --lang de   # 用英文哈希给德语页面加上标记
python tools/docs_i18n.py check              # 哈希或标签过期时以 1 退出
```

只翻译 `todo` 列出的页面：Markdown、链接、代码、文件名和列名保持原样；翻译标题和图片说明，并使用 3DHeat 查看器自己的词语来称呼其按钮和面板（即 `src/i18n/locales/<语言>/` 中的用词）。生成的参考页面和终端图片保持英文。在网站上，过期的译文会注明这一点，并链接到英文页面；缺失的译文则回退为英文。页眉的语言菜单和主页按浏览器语言的自动跳转，都来自 `docs/_includes/`。
