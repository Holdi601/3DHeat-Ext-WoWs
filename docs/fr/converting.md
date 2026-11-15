---
title: Convertir les replays
nav_order: 4
lang: fr
source: converting.md
source_hash: "6434f8e61c9c"
nav_exclude: true
search_exclude: true
---
# Convertir les replays {#converting-replays}

## Étape par étape {#step-by-step}

1. **Activer l'enregistrement** : `isReplayEnabled` dans le `preferences.xml` du jeu, ou le réglage propre du
   jeu lorsqu'il en a un. Dès lors, le jeu enregistre chaque bataille dans le dossier `replays` de votre
   installation de World of Warships, par exemple `C:\Games\World_of_Warships_EU\replays`.
2. **Ouvrir un terminal** dans un dossier où les résultats peuvent être écrits
   ([Avant de commencer](before-you-start.md)).
3. **Lancer le convertisseur** sur des fichiers de replay, ou sur des dossiers qui en contiennent :

   ```bash
   heat3d-wows-replay "C:\Games\World_of_Warships_EU\replays" -o out
   heat3d-wows-replay a.wowsreplay b.wowsreplay -o out
   ```

   `out` est créé dans le dossier où se trouve votre terminal.
4. **Lire ce que la commande affiche.** Vous devez voir une ligne par replay, qui se termine par la
   table écrite.
5. **Ouvrir le résultat** dans la visionneuse 3DHeat : `out/<map>/<match>.parquet` dans l'onglet Carte de
   chaleur, `<match>.match.json` dans l'onglet Match. Ou lisez-les avec n'importe quel lecteur Parquet ou JSON.

![Un essai sur un replay synthétique : conversion, nouvelle exécution, un fichier cassé, un dossier vide](../assets/img/convert.svg)

L'image montre un essai sur un replay que les tests construisent dans le code (aucun vrai replay) :

- un replay converti : `<file>: <n> positions of <n> ships at <rate> Hz (own <rate> Hz), <n> sunk, <map> (<client version>) -> <table>` ;
- relancé, le match déjà écrit est sauté : `<file>: already written, <table>` ;
- un fichier qui n'est pas un replay : `<file>: not converted: <why>` (dans la sortie d'erreur ; code de
  sortie 1, les autres replays sont tout de même convertis) ;
- aucun replay trouvé : `no .wowsreplay files in <folders>` (code de sortie 2).

## Options {#options}

| Option | Par défaut | Rôle |
|---|---|---|
| `replays` (un ou plusieurs) | - | fichiers `.wowsreplay`, ou dossiers où les chercher (sous-dossiers compris) |
| `-o`, `--out` | obligatoire | le dossier où écrire : un dossier par carte, à l'intérieur |
| `--force` | désactivé | convertir à nouveau ce qui est déjà écrit |
| `--ship-names JSON` | - | un fichier JSON `{"<shipId>": "<name>", ...}` : les replays ne nomment que le navire du joueur qui enregistre, les autres par leur numéro |
| `--version` | - | afficher `heat3d-wows-replay <version>` et s'arrêter |
| `-h`, `--help` | - | afficher les options et s'arrêter |

Les options telles que le programme les affiche : [Référence des commandes](../cli-reference.md).

## Ce qui est écrit {#what-is-written}

Uniquement des fichiers séparés : ce convertisseur n'écrit aucun fichier `.3dheat` (la visionneuse peut les
regrouper en un seul : [Un fichier par match](https://holdi601.github.io/3DHeat/container.html)).
Par replay, dans `out/<map>/` (le nom de la carte sans son `spaces/`) :

| Fichier | Contenu |
|---|---|
| `<match>.parquet` | la table : la position de chaque navire au fil du temps et chaque événement à son endroit ([La table](table.md)) |
| `<match>.match.json` | le document de match : carte, version du client, joueurs, naufrages, chat et tout le reste ([Le document de match](match-document.md)) |
| `<match>.messages.parquet` | le fichier annexe : chaque élément du replay que les deux fichiers ci-dessus ne contiennent pas en entier ([Exhaustivité](completeness.md)) |

`<match>` est l'identifiant propre de la bataille, ou le nom du fichier lorsque l'enregistrement s'est
arrêté avant les résultats.

## Code de sortie {#exit-status}

`0` lorsque chaque replay a été converti ou sauté, `1` lorsque l'un d'eux a échoué (les autres sont tout de
même convertis), `2` lorsqu'aucun fichier de replay n'a été trouvé.

---

Une partie de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source : [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
