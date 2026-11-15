---
title: Avant de commencer
nav_order: 2
lang: fr
source: before-you-start.md
source_hash: "310d596b3b1f"
nav_exclude: true
search_exclude: true
---
# Avant de commencer {#before-you-start}

Vous ne connaissez pas la ligne de commande ? Cette page vous mène de zéro à un
`heat3d-wows-replay` qui fonctionne, en une dizaine de minutes. Si vous utilisez déjà
Python, allez directement à [Installation](installing.md).

## 1. Installer Python {#install-python}

1. Téléchargez Python **3.10 ou plus récent** sur
   [python.org/downloads](https://www.python.org/downloads/).
2. Sous Windows, cochez **Add python.exe to PATH** dans la première fenêtre de
   l'installateur, puis cliquez sur **Install Now**.
3. Sous macOS et Linux, Python 3 est souvent déjà là. Tapez `python3` partout où ces
   pages disent `python`, et `pip3` à la place de `pip`.

## 2. Ouvrir un terminal {#open-a-terminal}

Un terminal est une fenêtre dans laquelle vous tapez des commandes.

- **Windows :** ouvrez le dossier dans l'Explorateur de fichiers, cliquez dans la barre
  d'adresse, tapez `cmd` et appuyez sur Entrée. Une fenêtre s'ouvre, déjà dans ce dossier.
- **macOS :** ouvrez l'application **Terminal**. **Linux :** faites un clic droit dans le
  dossier et choisissez **Ouvrir dans un terminal**.

Pour aller dans un autre dossier, tapez `cd` suivi du dossier :

```bash
cd "C:\Users\vous\Downloads\3DHeat-Ext-WoWs-main"
```

## 3. Vérifier que Python fonctionne {#check-that-python-works}

```bash
python --version
```

Vous devez voir `Python 3.` suivi d'un numéro égal ou supérieur à 10, par exemple
`Python 3.12.4`.

## 4. Récupérer l'outil et l'installer {#get-the-tool-and-install-it}

1. Sur [la page GitHub de l'outil](https://github.com/Holdi601/3DHeat-Ext-WoWs), cliquez
   sur le bouton vert **Code**, puis sur **Download ZIP**, et décompressez le zip.
2. Ouvrez un terminal dans le dossier décompressé (celui qui contient `README.md`).
3. Tapez :

   ```bash
   pip install -e .
   ```

   À la fin, vous devez voir : `Successfully installed heat3d-ext-wows-0.1.0`
   (peut-être avec d'autres noms).
4. Vérifiez :

   ```bash
   heat3d-wows-replay --version
   ```

   Vous devez voir : `heat3d-wows-replay 0.1.0`

## Comment lire les commandes de ces pages {#how-to-read-the-commands-on-these-pages}

- Les mots entre chevrons, comme `<replays>`, sont des emplacements : tapez à cet endroit
  votre propre fichier ou dossier, sans les chevrons.
- Un chemin qui contient des espaces a besoin de guillemets : `"C:\Program Files (x86)\Steam"`.
- Le texte qui suit `#` est un commentaire : vous ne le tapez pas.
- `-o out` écrit dans un dossier nommé `out`, à l'intérieur du dossier où se trouve votre
  terminal. Il est créé s'il n'existe pas.

## À quoi ressemble la réussite {#what-success-looks-like}

La commande affiche une ligne par replay, par exemple :

```text
example.wowsreplay: 904 positions of 3 ships at 6.99 Hz, ... -> out/<map>/<match>.parquet
```

et se termine avec le code de sortie `0`. Les nouveaux fichiers se trouvent dans le
dossier `out`.

## Erreurs courantes {#common-errors}

| Vous voyez | Que faire |
|---|---|
| `'python' is not recognized ...` ou `command not found` | Python n'est pas dans le PATH : installez-le à nouveau en cochant **Add python.exe to PATH**, ou tapez `py` au lieu de `python` (Windows) |
| `'pip' is not recognized ...` | tapez `python -m pip install -e .` à la place |
| `'heat3d-wows-replay' is not recognized ...` | tapez `python -m heat3d_ext_wows` au lieu de `heat3d-wows-replay` ; cela fait la même chose |
| `No module named heat3d_ext_wows` | vous n'êtes pas dans le dossier de l'outil, ou il n'est pas installé : faites `cd` vers ce dossier et lancez `pip install -e .` |
| `the following arguments are required: -o/--out` | ajoutez `-o out` à la commande |

Suite : [Convertir des replays](converting.md).
