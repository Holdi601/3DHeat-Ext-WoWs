---
title: "条款与许可"
nav_order: 9
lang: "zh"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# 条款与许可 {#terms-and-licence}

## Wargaming 的条款 {#wargamings-terms}

阅读日期为 2026-11-07，Wargaming 最终用户许可协议第 14 版（自 2024 年 4 月 10 日起生效，列为当前版本）。其第 12.3 条指向一份战舰世界的模组政策，该页面在浏览器之外无法显示，因此未被阅读：

- 5.3 (b)：除非获得书面授权，你不得 "... decompile,
  disassemble, reverse engineer or otherwise make unauthorized use of the
  Content"（反编译、反汇编、逆向工程，或以其他方式未经授权使用内容）。
- 12.1 (k)：被禁止的行为是 "Creating, using, making available, or distributing
  any unauthorized software or tools, including hacks, cheats, exploits,
  scripts, bots, trainers, automation programs, or other software that
  interacts with a Product in any way and for any purpose, including
  intercepts, emulates, or redirects any communication between such software
  and Wargaming."（创建、使用、提供或分发任何未经授权的软件或工具，包括外挂、作弊程序、漏洞利用、脚本、机器人、训练器、自动化程序，或以任何方式、为任何目的与产品交互的其他软件，包括拦截、模拟或重定向此类软件与 Wargaming 之间的任何通信。）
- 12.1 (l)：“... any software designed to modify a Product and change the user
  experience ("mods") unless expressly permitted by Wargaming”（旨在修改产品并改变用户体验的任何软件（"mods"），除非 Wargaming 明确许可。）
- 12.1 (p)：“Circumventing or bypassing enforcement and security measures
  implemented by Wargaming”（规避或绕过 Wargaming 实施的执行和安全措施。）

本转换器的作用是：它在对战结束后，在游戏之外读取游戏写入的一个文件。它不会改动游戏，不与任何服务器通信，并且在对战期间不显示任何内容。不过，它确实使用游戏的密钥解密数据流，而 5.3 (b) 和 12.1 (p) 可以被解读为涵盖这一点。是否使用它由用户自行决定；这也是它被单独打包的原因。

## 许可证与来源 {#licence-and-sources}

MIT（[`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)）。需要 numpy（BSD-3-Clause）和 pyarrow（Apache-2.0）。本项目为此专门编写：这里的 Blowfish 密码是自行实现的，其表由圆周率的数字按照该密码的定义计算得出。关于格式的事实是录像工具领域的常识；单位比例的说明来自 landaire/wows-toolkit（MIT）。没有从任何其他项目中复制代码。

`bigworld.py` 和 `table.py` 与坦克世界转换器（[3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)）中的文件相同；修改时请两者同时更改。

---

本页是 [3DHeat](https://github.com/Holdi601/3DHeat) 的一部分（[文档](https://holdi601.github.io/3DHeat/)）。来源：[3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
