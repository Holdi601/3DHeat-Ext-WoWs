---
title: "转换录像"
nav_order: 4
lang: "zh"
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# 转换录像 {#converting-replays}

## 一步一步来 {#step-by-step}

1. **开启录制：** 在游戏的 `preferences.xml` 中设置 `isReplayEnabled`，或使用游戏自身提供该选项的设置。从此之后，游戏会把每场战斗保存在你的战舰世界安装的 `replays` 文件夹中，例如 `C:\Games\World_of_Warships_EU\replays`。
2. **打开终端**，并进入一个可以存放结果的文件夹（[开始之前](before-you-start.md)）。
3. **对录像文件运行转换器**，或对存放它们的文件夹运行：

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` 会在你终端所在的文件夹中创建。
4. **阅读输出的内容。** 每个录像应输出一行，结尾是它写入的表格。
5. **在 3DHeat 查看器中打开结果：** 在 **热力图** 标签页中打开 `out/<地图>/<对局>.parquet`，在 **对局** 标签页中打开 `<对局>.match.json`。也可以用任何 Parquet 或 JSON 读取器读取它们。

![在一段合成录像上的运行结果：转换、再次运行、一个损坏的文件、一个空文件夹](../assets/img/convert.svg)

这张图是在测试程序以代码生成的录像上运行的结果（没有真实录像）：

- 一个录像已转换：`<文件>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <地图> (<客户端版本>) -> <表格>`；
- 再次运行时，已写入的对局会被跳过：`<文件>: already written, <表格>`；
- 不是录像的文件：`<文件>: not converted: <原因>`（输出到错误输出；退出状态为 1，其他录像仍会被转换）；
- 没有找到录像：`no .wowsreplay files in <文件夹>`（退出状态为 2）。

## 选项 {#options}

| 选项 | 默认值 | 作用 |
|---|---|---|
| `replays`（一个或多个） | - | `.wowsreplay` 文件，或在其中搜索的文件夹（也包括子文件夹） |
| `-o`、`--out` | 必填 | 写入的文件夹：在其中为每张地图建立一个文件夹 |
| `--force` | 关闭 | 对已写入的内容重新转换 |
| `--ship-names JSON` | - | 一个 JSON 文件 `{"<舰船ID>": "<名称>", ...}`：录像只会为录像播放者自己的舰船命名，其他舰船按编号显示 |
| `--version` | - | 输出 `heat3d-wows-replay <版本>` 并退出 |
| `-h`、`--help` | - | 输出选项列表并退出 |

程序输出的选项列表见：[命令参考](../cli-reference.md)。

## 写入的内容 {#what-is-written}

只生成单独的文件：本转换器不会写入 `.3dheat` 文件（查看器可以将它们打包成一个文件：[一个对局一个文件](https://holdi601.github.io/3DHeat/container.html)）。每个录像会在 `out/<地图>/` 中生成（地图名称去掉其 `spaces/` 前缀）：

| 文件 | 内容 |
|---|---|
| `<对局>.parquet` | 表格：每艘舰船随时间变化的位置，以及它所在位置发生的每个事件（[表格](table.md)） |
| `<对局>.match.json` | 对局文档：地图、客户端版本、玩家、击沉、聊天以及其他所有内容（[对局文档](match-document.md)） |
| `<对局>.messages.parquet` | 附属文件：录像中上述两个文件未完整保存的每一项（[完整性](completeness.md)） |

`<对局>` 是战斗本身的 ID；如果录制在结果出现之前就停止了，则使用文件名。

## 退出状态 {#exit-status}

`0` 表示所有录像都已转换或跳过；`1` 表示有任何一个失败（其余录像仍会被转换）；`2` 表示没有找到录像文件。

---

本页是 [3DHeat](https://github.com/Holdi601/3DHeat) 的一部分（[文档](https://holdi601.github.io/3DHeat/)）。来源：[3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
