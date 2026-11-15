---
title: "維護文件"
nav_order: 99
lang: "zh-Hant"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# 維護說明文件 {#maintaining-the-documentation}

供負責發布新版本的人閱讀。請依下列順序執行各步驟。

1. **從程式碼重新產生參考頁面：**

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # 必須以 0 結束
   ```

   這會重寫[指令參考](../cli-reference.md)與[欄位清單](../columns.md)。絕對不要手動編輯這兩頁。
2. **列出自上次發布以來的變更：**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` 是上一個發布的版本（尚無標籤時，列出整個 `git log --oneline`）。每個新功能、選項或欄位，都需要它自己的頁面，以及 [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md) 中 **Docs** 區段的一列。
3. **獨立審閱。**由沒有撰寫這些頁面的人（一個人或一個代理程式）以三種讀者的角度閱讀 README、每一頁與每張圖片：從未使用過終端機的初學者、一位 8 歲的孩子，以及會對照程式碼檢查每個選項、欄位與單位的專業人士。他們也會對照程式碼檢查圖表，並確認沒有任何頁面提到真實的地圖、關卡、玩家或對戰，也沒有提供來自真實回放的數據。
4. **修正審閱發現的問題。**然後再執行步驟 1，並重新繪製輸出有變更的圖片。
5. **翻譯。**`docs/<語言>/` 下的每一頁，都記錄了它所翻譯的英文頁面的雜湊值。英文來源有變動的每一頁都要重新翻譯，包括圖表中的標籤。然後審閱每種語言：三種讀者都能看懂，標籤正確，並使用 3DHeat 檢視器在該語言中所用的相同詞彙。
6. **發布：**提高 `VERSION` 並標記 `v<VERSION>`。**只有在擁有者同意後才推送。**

## 翻譯：指令 {#translations-the-commands}

網站會被翻譯成 3DHeat 檢視器支援的 40 種語言：英文位於 `docs/`，其他每種語言位於 `docs/<lang>/`，檔名相同。`tools/docs_i18n.py` 負責維護這些記錄：

```bash
python tools/docs_i18n.py hashes             # 英文有任何變更後：記錄每一頁的雜湊值
python tools/docs_i18n.py svg-strings        # 圖片有任何變更後：需要翻譯的標籤
python tools/docs_i18n.py status             # 每種語言：最新、過時或缺少的頁面
python tools/docs_i18n.py todo --lang de     # 需要（重新）翻譯的德文頁面
python tools/docs_i18n.py svg-build --lang de    # 依 docs/assets/i18n/svg/de.json 產生德文圖片
python tools/docs_i18n.py finish --lang de   # 以英文雜湊值標記德文頁面
python tools/docs_i18n.py check              # 若雜湊值或標籤過時，結束狀態為 1
```

只翻譯 `todo` 列出的內容：保留 Markdown、連結、程式碼、檔案與欄位名稱不變，翻譯標題與圖片說明，並使用 3DHeat 檢視器自己的詞彙來稱呼其按鈕與面板（即 `src/i18n/locales/<lang>/`）。產生的參考頁面與終端機圖片維持英文。在網站上，過時的翻譯會註明此事並連結到英文頁面；缺少的翻譯則退回英文。標頭的語言選單與首頁依瀏覽器語言的重新導向，都來自 `docs/_includes/`。
