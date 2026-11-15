---
title: Before you start
nav_order: 2
---

# Before you start

New to the command line? This page takes you from nothing to a working
`heat3d-wows-replay` in about ten minutes. If you already use Python, go straight to
[Installing](installing.md).

## 1. Install Python

1. Download Python **3.10 or later** from
   [python.org/downloads](https://www.python.org/downloads/).
2. On Windows, tick **Add python.exe to PATH** in the first window of the
   installer, then click **Install Now**.
3. On macOS and Linux, Python 3 is often there already. Type `python3`
   wherever these pages say `python`, and `pip3` for `pip`.

## 2. Open a terminal

A terminal is a window where you type commands.

- **Windows:** open the folder in File Explorer, click the address bar, type
  `cmd` and press Enter. A window opens, already in that folder.
- **macOS:** open the **Terminal** app. **Linux:** right-click in the folder
  and choose **Open in Terminal**.

To go to another folder, type `cd` and the folder:

```bash
cd "C:\Users\you\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Check that Python works

```bash
python --version
```

You should see `Python 3.` and a number of 10 or more, for example
`Python 3.12.4`.

## 4. Get the tool and install it

1. On [the tool's GitHub page](https://github.com/Holdi601/3DHeat-Ext-WoWs), click
   the green **Code** button, then **Download ZIP**, and unpack the zip.
2. Open a terminal in the unpacked folder (the one with `README.md` in it).
3. Type:

   ```bash
   pip install -e .
   ```

   You should see, at the end: `Successfully installed heat3d-ext-wows-0.1.0`
   (maybe with more names).
4. Check it:

   ```bash
   heat3d-wows-replay --version
   ```

   You should see: `heat3d-wows-replay 0.1.0`

## How to read the commands on these pages

- Words in angle brackets, like `<replays>`, are placeholders: type your own
  file or folder there, without the brackets.
- A path with spaces needs quotes: `"C:\Program Files (x86)\Steam"`.
- Text after `#` is a comment: you do not type it.
- `-o out` writes into a folder called `out` inside the folder your terminal
  is in. It is made if it is not there.

## What success looks like

The command prints one line per replay, for example:

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

and ends with exit status `0`. The new files are in the `out` folder.

## Common errors

| You see | What to do |
|---|---|
| `'python' is not recognized ...` or `command not found` | Python is not on the PATH: install it again with **Add python.exe to PATH** ticked, or type `py` instead of `python` (Windows) |
| `'pip' is not recognized ...` | type `python -m pip install -e .` instead |
| `'heat3d-wows-replay' is not recognized ...` | type `python -m heat3d_ext_wows` instead of `heat3d-wows-replay`; it does the same |
| `No module named heat3d_ext_wows` | you are not in the tool's folder, or it is not installed: `cd` there and run `pip install -e .` |
| `the following arguments are required: -o/--out` | add `-o out` to the command |

Next: [Converting replays](converting.md).
