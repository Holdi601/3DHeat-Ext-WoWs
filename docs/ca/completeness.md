---
title: Completesa
nav_order: 8
lang: "ca"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Completesa {#completeness}

Res d'una repetició no es descarta. Allò que llegeix el convertidor va a la taula i al document de partida;
cada altre element es guarda sencer a l'annex `<partida>.messages.parquet`; i `selfCheck.completeness` del
document de partida compta què n'ha estat de cada tipus d'element. Aquesta és la regla que comparteixen tots
els convertidors de 3DHeat:
[Els convertidors ho guarden tot](https://holdi601.github.io/3DHeat/converters.html).

![L'autocomprovació d'una repetició sintètica: cada element vist, llegit, guardat o perdut](../assets/img/completeness.svg)

## El recompte {#the-count}

Per a cada tipus d'element, `selfCheck.completeness.types` dona:

| Recompte | Vol dir |
|---|---|
| `seen` | quants n'hi ha a la repetició |
| `decoded` | llegits sencers |
| `partial` | llegits en part, i guardats sencers a l'annex |
| `raw` | només guardats sencers a l'annex, no llegits |
| `lost` | perduts: sempre `0` |

Els tipus són els de la mateixa repetició: `block <n>` (els blocs JSON), els bytes propis del contenidor,
`packet <tipus>`, i, per a les crides a entitats, `method <tipus d'entitat>.<número>` i `property <tipus
d'entitat>.<número>`. `selfCheck.entities.roles` indica quin tipus d'entitat és l'avatar del jugador que grava
i quins són els vaixells. Un tipus que ningú no coneixia apareix amb el seu recompte.

## L'annex {#the-sidecar}

| Columna | Què és |
|---|---|
| `time` | el rellotge de la repetició, com a la taula |
| `type`, `name` | el tipus d'element; com li diu el convertidor, on el llegeix |
| `entity` | el vaixell o avatar al qual pertany, com el `entity` de la taula |
| `decoded` | el que se n'ha llegit, com a JSON |
| `payload`, `text` | els seus bytes, sencers; els blocs JSON, sencers |
| `entityType`, `packet`, `method` | els números |

Les files s'ordenen per paquet, mètode, entitat i temps. Quina entitat és quin jugador: `entities` i `players`
del document de partida.

## Què es llegeix, i com es va comprovar {#what-is-read-and-how-it-was-checked}

- **Els resultats** (15.x, `results`): el seu identificador de batalla és el del flux, i cada jugador que hi
  surt és a la llista de la capçalera.
- **El bloc d'identificadors** (15.x, `blockIds`): el compte i la batalla, llegits com a text perquè no es perdi
  cap dígit.
- **Inclinació i roll** de cada posició: el roll va amb la velocitat de gir, com un vaixell que s'inclina en un
  gir; la inclinació és gairebé sempre 0.
- **Entitats** (`entities`): quan cada una va entrar a la vista del client i quan en va sortir. Cap vaixell no
  té una posició entre que surt i torna.
- **La versió al flux** (`streamVersion`): la mateixa que la de la capçalera.

Tota la resta que es llegeix (enfonsaments, dany, salut, obusos, torpedes, on van acabar els obusos, xat,
crides en `pickle`, els registres dels jugadors, les posicions) és `partial`: a la taula o al document de
partida, i guardat sencer a l'annex.

**Guardat però no llegit** (`raw`), els tipus més grans: actualitzacions de posició que no són a la taula
(després que un vaixell s'enfonsés, entitats sense jugador), les propietats i mètodes freqüents sense lector, les
propietats de les creacions d'entitats, i qualsevol altre paquet sense lector.

## No disponible {#not-available}

- Allò que el servidor mai no va enviar al client que grava: la mira, la càmera i les entrades dels altres
  jugadors, els enemics mentre no són detectats. Una repetició és el que se li va dir a un client.
- Els noms dels tipus d'entitat, mètodes, propietats i de les claus de les estadístiques: són als fitxers de
  definició del joc, no a la repetició. Els números es guarden.
- Els noms dels vaixells pel número del vaixell (fes servir `--ship-names`), i qualsevol altra cosa que necessiti
  els fitxers propis del joc.
- Els resultats dels clients anteriors a la 15.x: no són a les seves repeticions.

---

Part de [3DHeat](https://github.com/Holdi601/3DHeat) ([documentació](https://holdi601.github.io/3DHeat/)). Font: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
