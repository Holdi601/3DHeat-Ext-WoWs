---
title: "轉換回放"
nav_order: 4
lang: zh-Hant
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# 轉換回放 {#converting-replays}

## 逐步說明 {#step-by-step}

1. **開啟錄影：**在遊戲的 `preferences.xml` 中設定 `isReplayEnabled`，或使用遊戲自己有的設定。之後遊戲會把每場戰鬥存在你 World of Warships 安裝目錄中的 `replays` 資料夾裡，例如 `C:\Games\World_of_Warships_EU\replays`。
2. **開啟終端機**，位於可以存放結果的資料夾中（[開始之前](before-you-start.md)）。
3. **執行轉換器**，對象為回放檔案，或存放它們的資料夾：

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` 會建立在終端機所在的資料夾中。
4. **閱讀輸出內容。**你會看到每個回放一行，最後是它寫出的表格。
5. **開啟結果**，在 3DHeat 檢視器中：熱圖分頁開啟 `out/<map>/<match>.parquet`，對戰分頁開啟 `<match>.match.json`。或者用任何 Parquet 或 JSON 讀取器讀取它們。

![對合成回放執行的結果：轉換、再次執行、一個損壞的檔案、一個空資料夾](../assets/img/convert.svg)

圖片是對測試程式以程式碼建立的回放所做的執行結果（沒有真實回放）：

- 一個回放已轉換：`<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>`；
- 再次執行時，已寫出的對戰會被略過：`<file>: already written, <table>`；
- 不是回放的檔案：`<file>: not converted: <why>`（輸出在錯誤輸出中；結束狀態為 1，其他回放仍會轉換）；
- 找不到回放：`no .wowsreplay files in <folders>`（結束狀態為 2）。

## 選項 {#options}

| 選項 | 預設 | 作用 |
|---|---|---|
| `replays`（一個或多個） | - | `.wowsreplay` 檔案，或要在其中搜尋它們的資料夾（也包含子資料夾） |
| `-o`、`--out` | 必填 | 寫入的資料夾：其中會為每張地圖建立一個資料夾 |
| `--force` | 關閉 | 將已經寫好的內容再轉換一次 |
| `--ship-names JSON` | - | 一個 JSON 檔案 `{"<shipId>": "<name>", ...}`：回放只會命名錄製玩家的船，其他船則以編號表示 |
| `--version` | - | 印出 `heat3d-wows-replay <version>` 後停止 |
| `-h`、`--help` | - | 印出選項後停止 |

程式印出的選項：[指令參考](../cli-reference.md)。

## 會寫出什麼 {#what-is-written}

只會寫出獨立檔案：此轉換器不會寫出 `.3dheat` 檔案（檢視器可以把它們打包成一個：[每場對戰一個檔案](https://holdi601.github.io/3DHeat/container.html)）。每個回放會寫入 `out/<map>/`（地圖名稱不含其 `spaces/`）：

| 檔案 | 內容 |
|---|---|
| `<match>.parquet` | 表格：每艘船隨時間的位置，以及每個事件發生的地點（[表格](table.md)） |
| `<match>.match.json` | 對戰文件：地圖、客戶端版本、玩家、沉沒、聊天與其他一切（[對戰文件](match-document.md)） |
| `<match>.messages.parquet` | 附屬檔案：回放中上述兩個檔案未完整保存的每個項目（[完整性](completeness.md)） |

`<match>` 是戰鬥本身的 id；若錄製在結算出現前就停止，則為檔案名稱。

## 結束狀態 {#exit-status}

所有回放都已轉換或略過時為 `0`；任何一個失敗時為 `1`（其餘仍會轉換）；找不到任何回放檔案時為 `2`。

---

屬於 [3DHeat](https://github.com/Holdi601/3DHeat)（[說明文件](https://holdi601.github.io/3DHeat/)）的一部分。來源：[3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs)。
