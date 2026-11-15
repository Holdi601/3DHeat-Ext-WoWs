---
title: Com llegeix una repetició
nav_order: 7
lang: ca
source: how-it-reads.md
source_hash: "ec73820ae278"
nav_exclude: true
search_exclude: true
---
# Com llegeix una repetició {#how-it-reads-a-replay}

Una repetició és una capçalera de blocs JSON i el flux de paquets del joc (notes del format a
[`heat3d_ext_wows/bigworld.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/bigworld.py)):

- El primer bloc, sense xifrar: el mapa, la versió del client, el jugador que grava i el seu vaixell, i la
  llista de jugadors: el nom de cada jugador, aliat o enemic, i el número del vaixell. Els clients més nous
  (15.x) afegeixen dos blocs més: un de buit, i el compte del jugador que grava i l'identificador de la batalla
  com a text, llegits a `blockIds`. Els resultats no són al JSON; la 15.x els guarda al flux.
- El flux de paquets, comprimit amb zlib i xifrat amb Blowfish amb una clau que porta el joc, que les eines de
  la comunitat que llegeixen aquests fitxers han publicat. Desxifrat, conté:
  - les actualitzacions de posició del motor de cada vaixell que el client podia veure (el seu propi equip
    durant tota la partida, els enemics mentre són detectats o a prop), unes quantes vegades per segon mentre es
    mouen i menys sovint quan no;
  - el propi vaixell del jugador que grava, en un paquet propi, unes set vegades per segon;
  - una sola vegada, a l'inici, els registres dels jugadors com a llista de Python en `pickle`. Diuen quina
    entitat del flux és quin jugador. Les seves claus estan numerades, i els números canvien amb els pedaços,
    de manera que el lector troba les claus pels seus valors: la clau que té els noms de la llista, i la clau
    que té les entitats amb actualitzacions de posició;
  - la crida del servidor que diu al client que un vaixell s'ha enfonsat: víctima, assassí, causa. Es troba per
    la seva forma (dotze bytes; els dos primers són entitats de vaixell; cada víctima apareix una vegada), no pel
    seu número;
  - el dany de cada vaixell: una taula de (atacant, dany) per impacte, al vaixell impactat; i la seva salut, una
    propietat que es fixa un moment abans;
  - cada salba d'obusos i de torpedes de què el client va ser informat: el tipus d'obús, el tirador, la salba, i
    l'inici i la velocitat de cada obús o torpede;
  - on van acabar els obusos: el tirador, un tipus d'impacte, i el lloc de cada un (als clients 15.x amb més
    dades sobre l'obús on va impactar, que es deixen de banda);
  - el xat: remitent, canal, línia;
  - crides en `pickle` al jugador que grava: les seves estadístiques de dany, les actualitzacions dels registres
    dels jugadors, l'estat de la batalla;
  - als clients 15.x, els resultats de la batalla al final: un paquet propi, un objecte JSON amb l'identificador
    de la batalla, llegit sencer al `results` del document de partida (les llistes del joc, sense nom:
    `commonList`, `privateDataList`, `playersPublicInfo` per compte, ...).

Els números de paquet i de mètode que canvien entre les versions comprovades (el paquet del propi vaixell és el
43 o el 44, la crida d'enfonsament el 76 o el 83, els obusos el 101, 102, 126 o 127) es troben tots per la
forma: vegeu [`heat3d_ext_wows/stream.py`](https://github.com/Holdi601/3DHeat-Ext-WoWs/blob/main/heat3d_ext_wows/stream.py)
. Així un pedaç que els renumeri no buida la taula. Els números trobats són al `decoded` del document de partida.

**El `pickle` són dades no fiables.** Una repetició és un fitxer de qualsevol lloc, i un `pickle` pot nomenar
codi per executar. Es carrega amb un desserialitzador que dona a cada classe o funció que el `pickle` nomena un
substitut inert, de manera que construeix dades simples i res més. Una prova li dona un `pickle` que crida
`os.system`.

**Els enfonsaments** tenen l'hora exacta de la crida. El seu lloc és on la víctima es va veure per última vegada,
quan era dins de cinc segons. **L'inici de la batalla** és el primer moment en què es mou cap vaixell (els
vaixells estan quiets durant la compte enrere).

Tot allò que no és una fila de la taula és al [document de partida](match-document.md).

**El que se li va dir al client** és complet per al seu propi equip i parcial per als enemics: els seus trets,
impactes i salut hi són mentre són a l'abast.

**No llegit:**

- Els avions i les seves esquadres (les crides que els porten no es van desmuntar), les actualitzacions de visió
  del minimapa (empaquetades), la detecció, les cintes, els incendis i les inundacions com a esdeveniments propis
  (el seu dany és als impactes), els consumibles, els punts de captura i les puntuacions d'equip (propietats
  d'entitats sense definició, no distingides per la forma), la resta de propietats d'un vaixell (la punteria, el
  timó, la configuració de velocitat...).
- Els números de clau dels registres dels jugadors i de les estadístiques de dany com a noms: el joc els numera,
  i els números canvien; es guarden com a números.
- Les dades addicionals d'un obús on va impactar (15.x) i els bytes després de l'inici i la velocitat d'un obús o
  torpede.
- Els resultats dels clients anteriors a la 15.x: les seves repeticions no en porten.
- El número del vaixell com a nom: els noms són als fitxers de paràmetres propis del joc, no a la repetició.

## Com es va comprovar la lectura {#how-the-reading-was-checked}

La lectura es va comprovar amb repeticions públiques de clients de la 0.9 a la 15.x, cada valor amb una altra
cosa que la repetició dona una segona vegada:

- **Posicions:** l'entitat de cada vaixell coincidia amb un nom de la llista de jugadors; els headings coincideixen
  amb la direcció del moviment dins de 0,1 rad; després del seu enfonsament, un vaixell es mou menys de 0,1
  unitats. Un vaixell quiet s'actualitza amb menys freqüència.
- **Salut:** cada vaixell enfonsat dins de la vista del client acaba amb salut 0. Unes la meitat de tots els
  impactes coincideixen amb una caiguda de salut el segon anterior; la resta cauen juntament amb reparacions o
  altres impactes.
- **Dany contra les pròpies estadístiques del joc:** al client més nou, el dany llegit del jugador que grava és
  dins del 0,1 % de les estadístiques. Als clients més antics les estadístiques són més altes: no se n'envia cada
  impacte al client, o les estadístiques compten més que impactes (no resolt).
- **Obusos:** un obús comença a pocs unitats de l'última posició coneguda del seu vaixell (els canons estan
  repartits pel casc); gairebé el final de cada obús segueix, dins d'un minut, un tret que el client va veure.

Els tests construeixen repeticions amb la mateixa disposició, de manera que cap repetició real no es guarda en
aquest repositori.

**No comprovat:** clients anteriors a la 0.9.6, el client de Lesta (Mir Korabley), les operacions i els escenaris
més enllà d'un, les batalles de clan i les classificatòries, i quin número de vaixell és quin vaixell.

---

Part de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentació](https://holdi601.github.io/3DHeat/)). Font: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
