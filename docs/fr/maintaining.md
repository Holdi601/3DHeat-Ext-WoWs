---
title: Maintenir la documentation
nav_order: 99
lang: "fr"
source: maintaining.md
source_hash: "1a502bc5713c"
nav_exclude: true
search_exclude: true
---
# Maintenir la documentation {#maintaining-the-documentation}

Pour celui qui publie une nouvelle version. Faites les étapes dans cet ordre.

1. **Régénérez les pages de référence** à partir du code :

   ```bash
   python tools/gen_docs_reference.py
   python tools/gen_docs_reference.py --check   # doit se terminer avec le code 0
   ```

   Cela réécrit la [Référence des commandes](../cli-reference.md) et la [Liste des colonnes](../columns.md).
   Ne modifiez jamais ces deux pages à la main.
2. **Listez ce qui a changé depuis la dernière version :**

   ```bash
   git log --oneline v<VERSION>..HEAD
   ```

   `<VERSION>` est la dernière version publiée (sans étiquette encore : tout le `git log --oneline`).
   Chaque nouvelle fonctionnalité, option ou colonne a besoin de sa page et d'une ligne dans la section
   **Docs** du [CHANGELOG.md](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/CHANGELOG.md).
3. **Relecture indépendante.** Quelqu'un qui n'a pas écrit les pages (une personne ou un agent) lit le
   README, chaque page et chaque image en trois lecteurs : un débutant qui n'a jamais utilisé de terminal,
   un enfant de 8 ans, et un professionnel qui vérifie chaque option, colonne et unité par rapport au code.
   Ils vérifient aussi les schémas par rapport au code, et qu'aucune page ne nomme une vraie carte, un vrai
   niveau, un vrai joueur ou un vrai match, ni ne donne de chiffres tirés de vrais replays.
4. **Corrigez ce que la relecture a trouvé.** Puis relancez l'étape 1 et redessinez les images dont la
   sortie a changé.
5. **Traductions.** Chaque page sous `docs/<langue>/` enregistre l'empreinte de la page anglaise à partir de
   laquelle elle a été traduite. Retraduisez chaque page dont la source anglaise a changé, étiquettes des
   schémas comprises. Puis relisez chaque langue : claire pour les trois lecteurs, étiquettes justes, et les
   mêmes mots que ceux qu'utilise la visionneuse 3DHeat dans cette langue.
6. **Publication :** augmentez `VERSION` et créez l'étiquette `v<VERSION>`. **Ne poussez qu'après le feu
   vert du propriétaire.**

## Traductions : les commandes {#translations-the-commands}

Le site est traduit dans les 40 langues de la visionneuse 3DHeat : l'anglais dans `docs/`, chaque autre langue
dans `docs/<lang>/` avec les mêmes noms de fichiers. `tools/docs_i18n.py` tient les comptes :

```bash
python tools/docs_i18n.py hashes             # après tout changement anglais : enregistrer l'empreinte de chaque page
python tools/docs_i18n.py svg-strings        # après tout changement d'image : les étiquettes à traduire
python tools/docs_i18n.py status             # par langue : pages à jour, périmées, manquantes
python tools/docs_i18n.py todo --lang de     # les pages allemandes à (re)traduire
python tools/docs_i18n.py svg-build --lang de    # les images allemandes à partir de docs/assets/i18n/svg/de.json
python tools/docs_i18n.py finish --lang de   # marquer les pages allemandes avec l'empreinte anglaise
python tools/docs_i18n.py check              # code 1 lorsque des empreintes ou des étiquettes sont périmées
```

Ne traduisez que ce que `todo` liste : gardez le Markdown, les liens, le code, les noms de fichiers et de
colonnes tels quels, traduisez les titres et les descriptions d'images, et utilisez les mots propres à la
visionneuse 3DHeat pour ses boutons et panneaux (dans son `src/i18n/locales/<lang>/`). Les pages de référence
générées et les images de terminal restent en anglais. Sur le site, une traduction périmée le dit et renvoie
vers la page anglaise ; une traduction manquante revient à l'anglais. Le menu de langue de l'en-tête et la
redirection de la page d'accueil selon la langue du navigateur viennent de `docs/_includes/`.
