---
title: The match document
nav_order: 5
---

# The match document

`<match>.match.json` holds everything the replay says that is not a row of
the table. The viewer's Match tab reads it.

![The start of a synthetic match document, and its keys](assets/img/match-document.svg)

- `<match>.match.json` - the map, the client version, who recorded it, every
  player's line (ally or enemy, ship, kills, whether they survived, what the
  client saw of them, their whole player record), every sinking with its
  time, place and cause, the chat, and everything else the file holds.

---

Part of [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
