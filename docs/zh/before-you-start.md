---
title: "开始之前"
nav_order: 2
lang: "zh"
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# 开始之前 {#before-you-start}

刚接触命令行？本页带你从零开始，大约十分钟就能让 `heat3d-wows-replay` 正常运行。如果你已经会用 Python，可以直接前往 [安装](installing.md)。

## 1. 安装 Python {#install-python}

1. 从 [python.org/downloads](https://www.python.org/downloads/) 下载 Python **3.10 或更高版本**。
2. 在 Windows 上，在安装程序的第一个窗口中勾选 **Add python.exe to PATH**，然后点击 **Install Now**。
3. 在 macOS 和 Linux 上，通常已经自带 Python 3。本页中写 `python` 的地方，请输入 `python3`；写 `pip` 的地方，请输入 `pip3`。

## 2. 打开终端 {#open-a-terminal}

终端是一个让你输入命令的窗口。

- **Windows：** 在文件资源管理器中打开文件夹，点击地址栏，输入 `cmd` 并按回车。一个已经位于该文件夹中的窗口会打开。
- **macOS：** 打开 **终端** 应用。**Linux：** 在文件夹中右键单击，选择 **在终端中打开**。

要进入另一个文件夹，输入 `cd` 加上文件夹的路径：

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. 检查 Python 能否运行 {#check-that-python-works}

```bash
python --version
```

你应该会看到 `Python 3.`，后面是 10 或更大的数字，例如 `Python 3.12.4`。

## 4. 获取工具并安装 {#get-the-tool-and-install-it}

1. 打开 [该工具的 GitHub 页面](https://github.com/Holdi601/3DHeat-Ext-WoWs)，点击绿色的 **Code** 按钮，然后点击 **Download ZIP**，并解压该压缩包。
2. 在解压后的文件夹中打开终端（即其中有 `README.md` 的那个文件夹）。
3. 输入：

   ```bash
   pip install -e .
   ```

   最后你应该会看到：`Successfully installed heat3d-ext-wows-0.1.0`（后面可能还有其他名称）。
4. 检查安装：

   ```bash
   heat3d-wows-replay --version
   ```

   你应该会看到：`heat3d-wows-replay 0.1.0`

## 如何理解本页的命令 {#how-to-read-the-commands-on-these-pages}

- 尖括号中的词，例如 `<replays>`，是占位符：把你自己的文件或文件夹填在那里，但不要保留尖括号。
- 路径中有空格时需要加引号：`"C:\Program Files (x86)\Steam"`。
- `#` 之后的文字是注释：不需要输入。
- `-o out` 会在你终端所在的文件夹中写入一个名为 `out` 的文件夹。如果它不存在，会自动创建。

## 成功是什么样子 {#what-success-looks-like}

命令会为每个录像输出一行，例如：

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

并以退出状态 `0` 结束。新文件位于 `out` 文件夹中。

## 常见错误 {#common-errors}

| 你看到的 | 该怎么做 |
|---|---|
| `'python' is not recognized ...` 或 `command not found` | Python 不在 PATH 中：重新安装，并勾选 **Add python.exe to PATH**；或在 Windows 上输入 `py` 代替 `python` |
| `'pip' is not recognized ...` | 改为输入 `python -m pip install -e .` |
| `'heat3d-wows-replay' is not recognized ...` | 改为输入 `python -m heat3d_ext_wows`，它的作用相同 |
| `No module named heat3d_ext_wows` | 你不在该工具的文件夹中，或它没有安装：用 `cd` 进入该文件夹并运行 `pip install -e .` |
| `the following arguments are required: -o/--out` | 在命令后面加上 `-o out` |

下一步：[转换录像](converting.md)。
