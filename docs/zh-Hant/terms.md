---
title: "名詞與授權"
nav_order: 9
lang: "zh-Hant"
source: terms.md
source_hash: "3326635d2603"
nav_exclude: true
search_exclude: true
---
# 條款與授權 {#terms-and-licence}

## Wargaming 的條款 {#wargamings-terms}

於 2026-11-07 閱讀，Wargaming EULA 第 14 版（自 2024 年 4 月 10 日生效，目前列為現行版本）；其第 12.3 條指向一份戰艦世界的模組政策，該頁面在瀏覽器之外無法呈現，因此未被閱讀：

- 5.3 (b)：除非經書面授權，你不得 "... decompile, disassemble, reverse engineer or otherwise make unauthorized use of the Content"。
- 12.1 (k)：禁止 "Creating, using, making available, or distributing any unauthorized software or tools, including hacks, cheats, exploits, scripts, bots, trainers, automation programs, or other software that interacts with a Product in any way and for any purpose, including intercepts, emulates, or redirects any communication between such software and Wargaming."
- 12.1 (l)："... any software designed to modify a Product and change the user experience ("mods") unless expressly permitted by Wargaming"。
- 12.1 (p)："Circumventing or bypassing enforcement and security measures implemented by Wargaming"。

此轉換器的作用：它讀取遊戲在戰鬥結束後寫出的檔案，且是在遊戲之外進行的。它不會更改遊戲中的任何東西，不與任何伺服器通訊，也不會在戰鬥中顯示任何東西。它確實會使用遊戲的金鑰解密串流，而 5.3 (b) 與 12.1 (p) 可被解讀為涵蓋此行為。使用它是使用者自己的決定；這也是它被做成獨立套件的原因。

## 授權與來源 {#licence-and-sources}

MIT（[`LICENSE`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/LICENSE)）。需要 numpy（BSD-3-Clause）與 pyarrow（Apache-2.0）。為本專案編寫：此處的 Blowfish 加密是其自有的實作，其表格由 Blowfish 加密法定義的圓周率數字計算而來。
回放工具圈對格式的事實（容器、加密法、位置封包）已有共通的認識；單位比例的說明來自 landaire/wows-toolkit（MIT）。沒有從任何其他專案複製任何程式碼。

`bigworld.py` 與 `table.py` 與坦克世界（World of Tanks）轉換器（[3DHeat-Ext-WoT](https://github.com/Holdi601/3DHeat-Ext-WoT)）中的檔案相同；修改時請兩邊一起改。

---

屬於 [3DHeat](https://github.com/Holdi601/3DHeat)（[說明文件](https://holdi601.github.io/3DHeat/)）的一部分。來源：[3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
