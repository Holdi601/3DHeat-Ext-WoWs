---
title: Exhaustivité
nav_order: 8
lang: fr
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Exhaustivité {#completeness}

Rien dans un replay n'est jeté. Ce que le convertisseur lit va dans la table et le document de match ;
chaque autre élément est conservé en entier dans le fichier annexe `<match>.messages.parquet` ; et
`selfCheck.completeness` du document de match compte ce qu'est devenu chaque type d'élément. C'est la
règle que partagent tous les convertisseurs de 3DHeat :
[Les convertisseurs gardent tout](https://holdi601.github.io/3DHeat/converters.html).

![Le contrôle interne d'un replay synthétique : chaque élément vu, lu, conservé ou perdu](../assets/img/completeness.svg)

## Le compte {#the-count}

Pour chaque type d'élément, `selfCheck.completeness.types` donne :

| Compte | Signification |
|---|---|
| `seen` | combien le replay en contient |
| `decoded` | lus en entier |
| `partial` | lus en partie, et conservés en entier dans le fichier annexe |
| `raw` | seulement conservés en entier dans le fichier annexe, non lus |
| `lost` | perdus : toujours `0` |

Les types sont ceux du replay lui-même : `block <n>` (les blocs JSON), les octets propres du conteneur,
`packet <type>`, et pour les appels sur des entités `method <entity type>.<number>` et
`property <entity type>.<number>`. `selfCheck.entities.roles` indique quel type d'entité est l'avatar du
joueur qui enregistre et lesquels sont les navires. Un type que personne ne connaissait apparaît avec son compte.

## Le fichier annexe {#the-sidecar}

| Colonne | Contenu |
|---|---|
| `time` | l'horloge du replay, comme dans la table |
| `type`, `name` | le type de l'élément ; le nom que lui donne le convertisseur, là où il le lit |
| `entity` | le navire ou l'avatar auquel il appartient, comme `entity` de la table |
| `decoded` | ce qui en a été lu, en JSON |
| `payload`, `text` | ses octets, en entier ; les blocs JSON, en entier |
| `entityType`, `packet`, `method` | les numéros |

Les lignes sont triées par paquet, méthode, entité et temps. Quelle entité correspond à quel joueur :
les `entities` et `players` du document de match.

## Ce qui est lu, et comment cela a été vérifié {#what-is-read-and-how-it-was-checked}

- **Les résultats** (15.x, `results`) : leur identifiant de bataille est celui du flux, et chaque joueur
  qui y figure est dans la liste de l'en-tête.
- **Le bloc des identifiants** (15.x, `blockIds`) : le compte et la bataille, lus comme du texte pour qu'aucun
  chiffre ne soit perdu.
- **Tangage et roulis** de chaque position : le roulis va avec la vitesse de virage, comme un navire qui
  gîte dans un virage ; le tangage vaut presque toujours 0.
- **Entités** (`entities`) : le moment où chacune est entrée dans la vue du client et en est sortie. Aucun
  navire n'a de position entre sa sortie et son retour.
- **La version dans le flux** (`streamVersion`) : la même que celle de l'en-tête.

Tout le reste lu (naufrages, dégâts, points de vie, obus, torpilles, lieux où les obus se sont arrêtés, chat,
appels pickle, fiches des joueurs, positions) est `partial` : dans la table ou le document de match, et conservé
en entier dans le fichier annexe.

**Conservé mais non lu** (`raw`), les plus gros types : les mises à jour de position qui ne sont pas dans la
table (après le naufrage d'un navire, les entités sans joueur), les propriétés et méthodes fréquentes sans
lecteur, les propriétés des créations d'entités, et tout autre paquet sans lecteur.

## Non disponible {#not-available}

- Ce que le serveur n'a jamais envoyé au client qui enregistre : la visée, la caméra et les commandes des
  autres joueurs, les ennemis tant qu'ils ne sont pas repérés. Un replay est ce qu'un client a été informé.
- Les noms des types d'entités, des méthodes, des propriétés et les clés des statistiques : ils se trouvent
  dans les fichiers de définition du jeu, non dans le replay. Les numéros sont conservés.
- Les noms des navires pour les numéros de navire (utiliser `--ship-names`), et tout ce qui demande les fichiers
  propres du jeu.
- Les résultats des clients antérieurs à 15.x : leurs replays n'en contiennent pas.

---

Une partie de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentation](https://holdi601.github.io/3DHeat/)). Source : [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
