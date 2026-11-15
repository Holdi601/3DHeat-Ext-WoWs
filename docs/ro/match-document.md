---
title: Documentul meciului
nav_order: 6
lang: ro
source: match-document.md
source_hash: "6e925c5effd7"
nav_exclude: true
search_exclude: true
---
`<match>.match.json` ține tot ce spune replay-ul și care nu este un rând al tabelului. Fila Meci a
vizualizatorului îl citește. (Codul îl numește rezumat.)

![Începutul unui document de meci sintetic și cheile sale](../assets/img/match-document.svg)

## Bătălia

| Cheie | Ce este |
|---|---|
| `format`, `version` | `heat3d-wows-match`, `2` |
| `game`, `match`, `map`, `mapName` | `World of Warships`; id-ul bătăliei; harta așa cum o numește jocul (`spaces/<map>`) și numele său afișat |
| `clientVersion`, `streamVersion` | versiunea jocului din antet, și cum o spune fluxul de pachete |
| `recorded` | când a fost înregistrat replay-ul, așa cum îl scrie jocul |
| `player`, `vehicle` | jucătorul care înregistrează și nava sa |
| `gameType`, `scenario` | tipul bătăliei (`RandomBattle`, ...) și scenariul, din antet |
| `duration` | limita de timp a bătăliei în secunde, din antet |
| `truncated` | înregistrarea s-a oprit devreme |
| `battleStart`, `recordingSeconds` | începutul bătăliei (primul moment în care se mișcă vreo navă) și lungimea înregistrării, în secunde |
| `positionPacket`, `ownPositionPacket` | numerele pachetelor în care au venit pozițiile: ale celorlalte nave, ale jucătorului care înregistrează |
| `deathMethod` | numărul metodei în care au fost găsite scufundările |
| `hz`, `ownHz`, `positions` | eșantioane pe secundă ale celorlalte nave și ale navei proprii; rândurile de poziție |
| `units` | unități ale lumii (15 m după corpurile navelor, 30 m după razele jocului); x est, y sus, z nord |
| `events` | numărul de rânduri din tabel pentru fiecare eveniment |
| `decoded` | numărul metodei și al pachetelor găsite pentru fiecare fel de mesaj |

## Jucători și evenimente

| Cheie | Ce este |
|---|---|
| `players` | o intrare pe navă: nume, `ally` sau `enemy`, numărul și numele navei, entitatea, eșantioane, uciderile, supraviețuit; `seen` (daunele date și primite, obuzele, torpilele și ultima viață pe care le-a văzut clientul); `header` (intrarea din listă) și `record` (înregistrarea jucătorului din flux, după numărul cheii) |
| `kills` | fiecare scufundare: ora, victima, ucigașul, numărul cauzei, locul |
| `chat` | fiecare linie de chat, cu canalul și expeditorul |
| `damageStats` | statisticile proprii ale jucătorului care înregistrează, cum le ține jocul: pe armă și fel, un număr și o sumă (felul 0 sunt daunele date) |
| `avatarPickles` | fiecare apel pickle către jucătorul care înregistrează, decodat, după numărul metodei |

## Antetul, rezultatele și verificările

| Cheie | Ce este |
|---|---|
| `header` | primul bloc JSON, tot în afară de listă: modul de joc, vremea, marginea hărții, mărimea echipelor și altele |
| `moreBlocks` | blocurile JSON de după primul, așa cum sunt |
| `blockIds` | 15.x: contul jucătorului care înregistrează și id-ul bătăliei, citite ca text |
| `results` | 15.x: rezultatele, pe care aceste clienți le țin în flux |
| `entities` | fiecare entitate pe care o creează fluxul: numărul tipului său și rolul, când a intrat în vederea clientului și când a ieșit |
| `selfCheck` | numărătoarea de completitudine ([Completitudinea](completeness.md)) și verificările entităților, rezultatelor, id-urilor și versiunii |

---

Parte din [3DHeat](https://github.com/Holdi601/3DHeat) ([documentație](https://holdi601.github.io/3DHeat/)). Sursă: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
