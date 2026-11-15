---
title: Completitudinea
nav_order: 8
lang: "ro"
source: completeness.md
source_hash: "3e67ab80e664"
nav_exclude: true
search_exclude: true
---
# Completitudinea {#completeness}

Nimic dintr-un replay nu se aruncă. Ce citește convertorul intră în
tabel și în documentul meciului; fiecare alt element este păstrat întreg în fișierul auxiliar
`<match>.messages.parquet`; iar `selfCheck.completeness` din documentul meciului
numără ce s-a întâmplat cu fiecare fel de element. Aceasta este regula pe care o împart toate
convertoarele 3DHeat:
[Convertoarele păstrează tot](https://holdi601.github.io/3DHeat/converters.html).

![Autoverificarea unui replay sintetic: fiecare element văzut, citit, păstrat sau pierdut](../assets/img/completeness.svg)

## Numărătoarea {#the-count}

Pentru fiecare fel de element, `selfCheck.completeness.types` dă:

| Numărătoare | Înseamnă |
|---|---|
| `seen` | câte conține replay-ul |
| `decoded` | citite întregi |
| `partial` | citite parțial, și păstrate întregi în fișierul auxiliar |
| `raw` | doar păstrate întregi în fișierul auxiliar, necitite |
| `lost` | pierdute: mereu `0` |

Felurile sunt ale replay-ului însuși: `block <n>` (blocurile JSON), octeții proprii ai containerului,
`packet <type>`, iar pentru apelurile către entități
`method <entity type>.<number>` și `property <entity type>.<number>`.
`selfCheck.entities.roles` spune ce tip de entitate este avatarul jucătorului care înregistrează și care sunt navele. Un fel pe care nimeni nu îl cunoștea
apare cu numărătoarea sa.

## Fișierul auxiliar {#the-sidecar}

| Coloană | Ce este |
|---|---|
| `time` | ceasul replay-ului, ca în tabel |
| `type`, `name` | felul elementului; cum îl numește convertorul, acolo unde îl citește |
| `entity` | nava sau avatarul căruia îi aparține, ca `entity` din tabel |
| `decoded` | ce s-a citit din el, ca JSON |
| `payload`, `text` | octeții săi, întregi; blocurile JSON, întregi |
| `entityType`, `packet`, `method` | numerele |

Rândurile sunt sortate după pachet, metodă, entitate și timp. Ce entitate este ce
jucător: `entities` și `players` din documentul meciului.

## Ce se citește, și cum a fost verificat {#what-is-read-and-how-it-was-checked}

- **Rezultatele** (15.x, `results`): id-ul lor de bătălie este cel al fluxului, iar fiecare jucător din ele este în lista din antet.
- **Blocul de id-uri** (15.x, `blockIds`): contul și bătălia, citite ca text, ca să nu se piardă nicio cifră.
- **Înclinarea și rularea** fiecărei poziții: rularea merge cu viteza de viraj, cum se înclină o navă într-un viraj; înclinarea este aproape mereu 0.
- **Entitățile** (`entities`): când a intrat fiecare în vederea clientului și când a ieșit. Nicio navă nu are o poziție între ieșire și revenire.
- **Versiunea din flux** (`streamVersion`): aceeași cu cea din antet.

Orice altceva citit (scufundările, daunele, viața, proiectilele, torpilele, unde s-au oprit obuzele, chatul, apelurile pickle, înregistrările jucătorilor, pozițiile) este `partial`: în tabel sau în documentul meciului, și păstrat întreg în fișierul auxiliar.

**Păstrat, dar necitit** (`raw`), cele mai mari feluri: actualizările de poziție care nu sunt în tabel (după ce o navă s-a scufundat, entitățile fără jucător), proprietățile și metodele frecvente fără cititor, proprietățile creărilor de entități și orice alt pachet fără cititor.

## Ce nu este disponibil {#not-available}

- Ce nu a trimis niciodată serverul clientului care înregistrează: ținta, camera și comenzile altor jucători, inamicii nemarcați. Un replay este ce i s-a spus unui singur client.
- Numele tipurilor de entități, metodelor, proprietăților și cheilor statisticilor: sunt în fișierele de definiție ale jocului, nu în replay. Numerele sunt păstrate.
- Numele navelor după numerele navelor (folosiți `--ship-names`) și orice altceva care are nevoie de fișierele proprii ale jocului.
- Rezultatele clienților dinaintea versiunii 15.x: nu sunt în replay-urile lor.

---

Parte din [3DHeat](https://github.com/Holdi601/3DHeat) ([documentație](https://holdi601.github.io/3DHeat/)). Sursă: [3DHeat-Ext-WoWs](https://github.com/Holdi601/3DHeat-Ext-WoWs).
