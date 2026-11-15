---
title: "開始之前"
nav_order: 2
lang: zh-Hant
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# 開始之前 {#before-you-start}

第一次使用命令列嗎？本頁會帶你從零開始，約十分鐘內完成可以正常運作的 `heat3d-wows-replay`。如果你已經會用 Python，請直接前往[安裝](installing.md)。

## 1. 安裝 Python {#install-python}

1. 從 [python.org/downloads](https://www.python.org/downloads/) 下載 Python **3.10 或更新版本**。
2. 在 Windows 上，於安裝程式的第一個視窗勾選 **Add python.exe to PATH**，然後按 **Install Now**。
3. 在 macOS 與 Linux 上，通常已經有 Python 3。本頁提到 `python` 的地方，請改打 `python3`；提到 `pip` 的地方，請改打 `pip3`。

## 2. 開啟終端機 {#open-a-terminal}

終端機是一個讓你輸入指令的視窗。

- **Windows：**在檔案總管中開啟資料夾，點擊網址列，輸入 `cmd` 後按 Enter。會開啟一個視窗，且已經位於該資料夾。
- **macOS：**開啟 **Terminal** 應用程式。**Linux：**在資料夾中按右鍵，選擇 **Open in Terminal**。

要前往另一個資料夾，輸入 `cd` 加上資料夾路徑：

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. 確認 Python 可以運作 {#check-that-python-works}

```bash
python --version
```

你應該會看到 `Python 3.`，後面是 10 或更大的數字，例如 `Python 3.12.4`。

## 4. 取得工具並安裝 {#get-the-tool-and-install-it}

1. 前往[工具的 GitHub 頁面](https://github.com/Holdi601/3DHeat-Ext-WoWs)，按綠色的 **Code** 按鈕，再選 **Download ZIP**，然後解壓縮。
2. 在解壓縮後的資料夾中開啟終端機（就是裡面有 `README.md` 的那個資料夾）。
3. 輸入：

   ```bash
   pip install -e .
   ```

   最後你應該會看到：`Successfully installed heat3d-ext-wows-0.1.0`（後面可能還有其他名稱）。
4. 檢查安裝：

   ```bash
   heat3d-wows-replay --version
   ```

   你應該會看到：`heat3d-wows-replay 0.1.0`

## 如何閱讀這些頁面中的指令 {#how-to-read-the-commands-on-these-pages}

- 角括號中的文字，例如 `<replays>`，是佔位符：把你自己的檔案或資料夾放在那裡，不要保留括號。
- 含有空白的路徑需要加引號：`"C:\Program Files (x86)\Steam"`。
- `#` 後面的文字是註解：你不需要輸入。
- `-o out` 會寫入終端機所在資料夾中一個名為 `out` 的資料夾。如果它不存在，會自動建立。

## 成功的樣子 {#what-success-looks-like}

指令會為每個回放印出一行，例如：

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

並以結束狀態 `0` 結束。新檔案會在 `out` 資料夾中。

## 常見錯誤 {#common-errors}

| 你看到的訊息 | 該怎麼做 |
|---|---|
| `'python' is not recognized ...` 或 `command not found` | Python 不在 PATH 中：重新安裝並勾選 **Add python.exe to PATH**，或在 Windows 上改打 `py` 取代 `python` |
| `'pip' is not recognized ...` | 改打 `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | 改打 `python -m heat3d_ext_wows`，取代 `heat3d-wows-replay`；效果相同 |
| `No module named heat3d_ext_wows` | 你不在工具的資料夾中，或尚未安裝：用 `cd` 前往該資料夾，再執行 `pip install -e .` |
| `the following arguments are required: -o/--out` | 在指令後加上 `-o out` |

下一步：[轉換回放](converting.md)。
