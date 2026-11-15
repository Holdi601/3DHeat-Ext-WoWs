---
title: "完整性"
nav_order: 8
lang: "zh"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# 完整性 {#completeness}

录像中的任何内容都不会被丢弃。转换器读取的内容进入表格和对局文档；其他每一项都会完整保存在附属文件 `<对局>.messages.parquet` 中；对局文档中的 `selfCheck.completeness` 则统计每一类项目的去向。这是所有 3DHeat 转换器共同遵守的规则：[转换器保留所有内容](https://holdi601.github.io/3DHeat/converters.html)。

![一份合成录像的自我检查：每一项都已被看到、读取、保留或丢失](../assets/img/completeness.svg)

## 计数 {#the-count}

对于每一类项目，`selfCheck.completeness.types` 给出以下数值：

| 计数 | 含义 |
|---|---|
| `seen` | 录像中有多少个 |
| `decoded` | 完整读取的数量 |
| `partial` | 部分读取，并在附属文件中完整保存的数量 |
| `raw` | 仅在附属文件中完整保存、未被读取的数量 |
| `lost` | 丢失的数量：始终为 `0` |

这些类别来自录像本身：`block <n>`（JSON 块）、容器自身的字节、`packet <类型>`；对于实体上的调用，则为 `method <实体类型>.<编号>` 和 `property <实体类型>.<编号>`。`selfCheck.entities.roles` 说明哪个实体类型是录像播放者的化身，哪些是舰船。未知的类别会以其计数显示出来。

## 附属文件 {#the-sidecar}

| 列 | 内容 |
|---|---|
| `time` | 录像的时钟，与表格中相同 |
| `type`、`name` | 项目的类别；转换器如何称呼它，以及它在何处被读取 |
| `entity` | 它所属的舰船或化身，即表格中的 `entity` |
| `decoded` | 对它的读取内容，以 JSON 表示 |
| `payload`、`text` | 它的字节，完整保存；JSON 块，完整保存 |
| `entityType`、`packet`、`method` | 对应的编号 |

各行按数据包、方法、实体和时间排序。哪个实体属于哪位玩家：见对局文档中的 `entities` 和 `players`。

## 读取了什么，以及如何核对 {#what-is-read-and-how-it-was-checked}

- **结果**（15.x，`results`）：其战斗 ID 与数据流一致，其中的每位玩家都在文件头的名单中。
- **ID 块**（15.x，`blockIds`）：账号和战斗，以文本形式读取，因此不会丢失任何数字。
- **每个位置的俯仰和横滚**：横滚与转向速率相关，就像舰船在转弯时会倾斜一样；俯仰几乎总是 0。
- **实体**（`entities`）：每个实体何时进入客户端的视野，何时离开。舰船在离开与重新出现之间没有位置。
- **流中的版本**（`streamVersion`）：与文件头中的相同。

其余所有读取的内容（击沉、伤害、生命值、炮弹、鱼雷、炮弹的落点、聊天、pickle 调用、玩家记录、位置）都属于 `partial`：它们在表格或对局文档中，并在附属文件中完整保存。

**保留但未读取**（`raw`）的主要类别：不在表格中的位置更新（舰船沉没之后的，以及没有玩家的实体）；没有读取器的常见属性和方法；实体创建时的属性；以及其他没有读取器的数据包。

## 不可用的内容 {#not-available}

- 服务器从未发送给录像播放者客户端的内容：其他玩家的瞄准、相机和输入，未被发现的敌人。录像只反映一个客户端所被告知的内容。
- 实体类型、方法、属性以及统计数据的键名：它们位于游戏的定义文件中，而不在录像中。编号会被保留。
- 舰船编号对应的舰船名称（使用 `--ship-names`），以及任何需要游戏自身文件的其他内容。
- 15.x 之前的客户端的结果：它们的录像中不包含结果。

---

本页是 [3DHeat](https://github.com/Holdi601/3DHeat) 的一部分（[文档](https://holdi601.github.io/3DHeat/)）。来源：[3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
