---
title: Maintaining
nav_order: 99
---

# Maintaining the documentation

For whoever releases a new version. Do the steps in this order.

1. **Regenerate the reference pages** from the code:

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # must exit 0
   ```

   This rewrites [Command reference](cli-reference.md) and
   [Column list](columns.md). Never edit those two by hand.
2. **List what changed since the last release:**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` is the last released version (no tag yet: the whole
   `git log --oneline`). Every new feature, option or column needs its page
   and a row in the **Docs** section of
   [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Independent review.** Someone who did not write the pages (a person or
   an agent) reads the README, every page and every picture as three
   readers: a beginner who has never used a terminal, an 8-year-old, and a
   professional who checks every option, column and unit against the code.
   They also check the diagrams against the code, and that no page names a
   real map, level, player or match, or gives figures from real replays.
4. **Fix what the review found.** Then run step 1 again and redraw the
   pictures whose output changed.
5. **Translations.** Every page under `docs/<language>/` records the hash of
   the English page it was translated from. Translate again every page whose
   English source changed, diagram labels included. Then review each
   language: clear for all three readers, labels right, and the same words
   as the 3DHeat viewer uses in that language.
6. **Release:** raise `VERSION` and tag `v<VERSION>`. **Push only after the
   owner's go-ahead.**
