---
title: "对局文档"
nav_order: 6
lang: "zh"
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
# 对局文档 {#the-match-document}

`<对局>.match.json` 保存了录像中所有不属于表格中某一行的内容。查看器的 **对局** 标签页会读取它。（代码中称之为摘要。）

![合成对局文档的开头部分及其键](../assets/img/match-document.svg)

## 战斗 {#the-battle}

| 键 | 内容 |
|---|---|
| `format`、`version` | `heat3d-wows-match`、`2` |
| `game`、`match`、`map`、`mapName` | `World of Warships`；战斗的 ID；游戏给出的地图名（`spaces/<地图>`）及其显示名称 |
| `clientVersion`、`streamVersion` | 文件头中的游戏版本，以及数据包流所给出的版本 |
| `recorded` | 录像的录制时间，与游戏写入的格式相同 |
| `player`、`vehicle` | 录像播放者及其舰船 |
| `gameType`、`scenario` | 战斗的类型（`RandomBattle` 等）和剧本，来自文件头 |
| `duration` | 战斗的时间限制（秒），来自文件头 |
| `truncated` | 录制提前停止 |
| `battleStart`、`recordingSeconds` | 战斗的开始时间（任何舰船首次移动的时刻）和录像的长度，以秒计 |
| `positionPacket`、`ownPositionPacket` | 位置数据所在的数据包编号：其他舰船的，以及录像播放者自己的 |
| `deathMethod` | 找到沉没记录所在的方法编号 |
| `hz`、`ownHz`、`positions` | 其他舰船和己方舰船每秒的采样数；位置行 |
| `units` | 世界单位（按舰体计为 15 米，按游戏的射程计为 30 米）；x 朝东，y 朝上，z 朝北 |
| `events` | 每种事件的表格行数 |
| `decoded` | 为每类消息找到的方法和数据包编号 |

## 玩家与事件 {#players-and-events}

| 键 | 内容 |
|---|---|
| `players` | 每艘舰船一项：名称、`ally`（友军）或 `enemy`（敌军）、舰船编号和名称、实体、采样数、击杀、是否存活；`seen`（客户端所见的造成和受到的伤害、炮弹、鱼雷以及最后的生命值）；`header`（名单中的条目）和 `record`（数据流中该玩家的记录，按键编号） |
| `kills` | 每一次沉没：时间、受害者、击杀者、原因编号、位置 |
| `chat` | 每一行聊天，附带频道和发送者 |
| `damageStats` | 游戏保存的录像播放者自己的统计数据：按武器和类型，给出次数和数量（类型 0 为造成的伤害） |
| `avatarPickles` | 每一次发给录像播放者的 pickle 化调用，已解码，按方法编号排列 |

## 文件头、结果与核对 {#header-results-and-checks}

| 键 | 内容 |
|---|---|
| `header` | 第一个 JSON 块，除名单之外的全部内容：游戏模式、天气、地图边界、队伍人数等 |
| `moreBlocks` | 第一个之后的 JSON 块，保持原样 |
| `blockIds` | 15.x：录像播放者的账号和战斗 ID，以文本形式读取 |
| `results` | 15.x：结果，这些客户端将其保存在数据流中 |
| `entities` | 数据流创建的每个实体：其类型编号和角色、进入客户端视野的时间和离开的时间 |
| `selfCheck` | 完整性计数（[完整性](completeness.md)），以及对实体、结果、ID 和版本的核对 |

---

本页是 [3DHeat](https://github.com/Holdi601/3DHeat) 的一部分（[文档](https://holdi601.github.io/3DHeat/)）。来源：[3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
