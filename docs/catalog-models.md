---
title: Catalogue and models
nav_order: 6
---

# Catalogue and models: `catalog`, `models`

```
heat3d-wows-replay catalog    # every ship, shell and torpedo: $HEAT3D_LEVELS/wows/catalog.json
heat3d-wows-replay models     # each ship's armour model: $HEAT3D_LEVELS/model-packs/wows/
```

Without `HEAT3D_LEVELS` both write into the current folder; `-o` names another
place. The game is found in the Steam libraries and in `X:\Games`; `--game`
names its folder (the one holding `bin` and `res_packages`).

**`catalog`** lists every ship with its English name, class, nation, tier,
group, size, speed and health, and every shell, torpedo and bomb with its
calibre, kind, damage and penetration numbers. The viewer names, groups and
filters ships with it, and the converter uses it to name the other ships of a
replay (a replay stores only their numbers).

**`models`** writes each ship's armour model, the plates the game resolves
hits against, scaled to metres: the hull drawn in the viewer (three levels of
detail) and, beside it, the plates grouped by thickness in millimetres, so
hits can be coloured by the plate they struck. Turrets are not placed yet.
`--only Yamato` builds just the ships whose name contains it.

Both stay on your machine; nothing is uploaded or shared.
