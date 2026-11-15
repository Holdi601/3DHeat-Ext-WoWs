"""
Writes docs/cli-reference.md and docs/columns.md from the code itself - the commands' own `--help` and the
table's column list - so these pages cannot drift from the program.

    python tools/gen_docs_reference.py           # rewrite both pages
    python tools/gen_docs_reference.py --check   # exit 1 when a page differs from what the code says

Run it before every release (docs/maintaining.md). Do not edit the two pages by hand.
"""

from __future__ import annotations

import importlib
import os
import subprocess
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
#: (the command as users type it, the module that runs it)
COMMANDS = [("heat3d-wows-replay", "heat3d_ext_wows")]
#: (module, attribute) of the table's columns: a dict name -> type code, or a list of (name, type) pairs
COLUMNS = ("heat3d_ext_wows.replay", "COLUMNS")
TYPES = {"s": "text", "str": "text", "string": "text", "f": "decimal", "d": "decimal", "f32": "decimal",
         "f64": "decimal", "i": "whole number", "l": "whole number", "i8": "whole number", "i16": "whole number",
         "i32": "whole number", "i64": "whole number", "u8": "whole number", "u16": "whole number",
         "u32": "whole number", "u64": "whole number", "b": "true / false", "bool": "true / false"}
NOTE = ("This page is generated from the code by `tools/gen_docs_reference.py`; do not edit it by hand.")


def _help(module: str, args: list[str]) -> str:
    env = dict(os.environ, HEAT3D_NO_UPDATE="1", COLUMNS="88", PYTHONIOENCODING="utf-8", PYTHONPATH=ROOT)
    r = subprocess.run([sys.executable, "-m", module] + args, capture_output=True, text=True, env=env,
                       encoding="utf-8", cwd=ROOT)
    return (r.stdout or r.stderr).rstrip().replace("\r\n", "\n")


def _verbs(text: str) -> list[str]:
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("{") and s.endswith("}"):
            return s[1:-1].split(",")
    return []


def cli_page() -> str:
    out = ["---", "title: Command reference", "nav_order: 90", "---", "", "# Command reference", "", NOTE,
           "The other pages explain each command step by step.", ""]
    for shown, module in COMMANDS:
        top = _help(module, ["--help"])
        out += [f"## `{shown}`", "", "```text", top, "```", ""]
        for v in _verbs(top):
            out += [f"### `{shown} {v}`", "", "```text", _help(module, [v, "--help"]), "```", ""]
    return "\n".join(out)


def columns_page() -> str:
    sys.path.insert(0, ROOT)
    mod, attr = COLUMNS
    cols = getattr(importlib.import_module(mod), attr)
    pairs = list(cols.items()) if isinstance(cols, dict) else [tuple(c[:2]) for c in cols]
    out = ["---", "title: Column list", "nav_order: 91", "---", "", "# Column list", "", NOTE,
           f"What each column means is on [The table](table.md). The table has **{len(pairs)} columns**:", "",
           "| # | Column | Type |", "|---|---|---|"]
    out += [f"| {i} | `{n}` | {TYPES.get(str(t), str(t))} |" for i, (n, t) in enumerate(pairs, 1)]
    return "\n".join(out) + "\n"


def main() -> int:
    pages = {"cli-reference.md": cli_page(), "columns.md": columns_page()}
    stale = []
    for name, text in pages.items():
        path = os.path.join(ROOT, "docs", name)
        if "--check" in sys.argv:
            cur = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
            if cur != text:
                stale.append(name)
        else:
            open(path, "w", encoding="utf-8", newline="\n").write(text)
            print("wrote", os.path.relpath(path, ROOT))
    if stale:
        print("out of date:", ", ".join(stale), "- run python tools/gen_docs_reference.py")
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main())
