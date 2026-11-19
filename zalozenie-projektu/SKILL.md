---
name: zalozenie-projektu
description: Prevedie používateľa založením nového projektu pomocou krátkeho riadeného rozhovoru, rozdelí získané informácie do README.md, AGENTS.md, MEMORY.md, decisions.md, open_items.md a diary.md a po schválení vytvorí alebo bezpečne doplní projektovú štruktúru. Použi pri požiadavkách na založenie, inicializáciu alebo úvodné nastavenie projektu podľa projektovej šablóny.
---

# Založenie projektu

Pomôž používateľovi založiť nový projekt bez toho, aby musel poznať význam jednotlivých projektových súborov. Najskôr veď krátky rozhovor, potom ukáž návrh rozdelenia informácií a zapisuj až po výslovnom schválení.

## Určenie cieľa

Na začiatku zisti, či používateľ chce:

- vytvoriť nový projekt v novom priečinku,
- inicializovať aktuálny priečinok,
- doplniť už existujúcu projektovú štruktúru.

Ak cieľ alebo umiestnenie jednoznačne vyplýva z požiadavky a pracovného adresára, nepýtaj sa naň znova. Pred návrhom zápisu prehliadni cieľový priečinok a zachovaj existujúce súbory aj používateľské zmeny.

## Východisková šablóna

- Pri každom novom aj existujúcom projekte vychádzaj výhradne zo vzorovej šablóny v `assets/project-template`.
- Iný už vytvorený alebo naposledy upravovaný projekt nikdy nepouži ako šablónu. Jeho súbory, priečinky, pravidlá a projektové prispôsobenia automaticky neprenášaj.
- Predchádzajúce projekty možno použiť iba ako zdroj poučení alebo príkladov, ak sú relevantné. Každé prevzatie projektového pravidla či rozšírenia musí byť v návrhu pomenované a používateľom schválené.
- Pri existujúcom projekte porovnaj jeho stav so vzorovou šablónou, ale zachovaj jeho pôvodný obsah a štruktúru. Chýbajúce časti navrhni podľa vzorovej šablóny a nič neprepisuj ani nepresúvaj bez príslušného súhlasu.

## Spôsob rozhovoru

- Pýtaj sa v krátkych tematických blokoch, najviac tri otázky naraz.
- Používateľ môže odpovedať stručne, napísať `neviem` alebo otázku preskočiť.
- Chýbajúci údaj nevymýšľaj. Označ ho ako otvorenú položku iba vtedy, keď ho treba reálne vyriešiť.
- Nežiadaj znovu informáciu, ktorú už používateľ uviedol alebo ktorá je potvrdená v existujúcich súboroch.
- Pri nejasnej odpovedi najskôr zhrň svoje porozumenie a over iba nejasnú časť.
- Po každom bloku stručne povedz, do ktorých súborov sa odpovede premietnu.

## Rozhovorové bloky

Prispôsob ich veľkosti projektu. Pri malom projekte nepoužívaj otázky, ktoré neprinášajú praktickú hodnotu.

### 1. Zámer

Zisti:

- pracovný názov projektu,
- problém alebo dôvod vzniku,
- konkrétny očakávaný výsledok.

Tieto údaje patria najmä do `README.md`; stručný cieľ patrí aj do `MEMORY.md`.

### 2. Rozsah a dokončenie

Zisti:

- čo do projektu patrí,
- čo doň výslovne nepatrí,
- podľa čoho sa spozná, že projekt alebo prvá etapa je hotová.

Tieto údaje patria do `README.md`.

### 3. Východiská a zdroje

Zisti:

- aké podklady už existujú a kde sú,
- ktorý zdroj je rozhodujúci pri rozpore,
- či projekt obsahuje osobné, dôverné alebo inak citlivé údaje.

Zdrojové pravidlá a obmedzenia patria do `README.md` a podľa potreby do `AGENTS.md`. Navrhni zaradenie materiálov do `00_inbox` alebo `01_zdroje`, ale existujúce súbory bez súhlasu nepresúvaj.

### 4. Pracovné pravidlá

Zisti iba pravidlá relevantné pre projekt:

- jazyk a požadovaný štýl výstupov,
- ktoré činnosti alebo zápisy vyžadujú predchádzajúce schválenie,
- ktoré kontroly sú povinné pred označením výsledku za hotový.

Tieto údaje patria do `AGENTS.md`.

### 5. Aktuálny stav

Zisti:

- v akej etape sa projekt nachádza,
- čo je už hotové alebo potvrdené,
- aký je najbližší konkrétny krok.

Tieto údaje patria do `MEMORY.md` a počiatočný záznam do `diary.md`.

### 6. Rozhodnutia a otvorené položky

Zisti:

- ktoré rozhodnutia už boli skutočne prijaté a prečo,
- ktoré otázky alebo úlohy zostávajú otvorené,
- ich prioritu, termín a zodpovednosť, ak sú známe.

Potvrdené rozhodnutia zapíš do `decisions.md` ako `ROZ-NNN`. Návrhy neoznačuj za platné rozhodnutia. Vybrané úlohy zapisuj do `open_items.md` ako `OPN-NNN`; nevybrané nápady patria do `backlog.md` ako `NAP-NNN` iba na výslovný pokyn používateľa. Backlog ani archívy automaticky nečítaj pri rozhovore, začatí práce alebo všeobecnom vyhľadávaní.

## Kontrola úplnosti

Pred zostavením návrhu skontroluj, či poznáme aspoň:

- názov alebo pracovné označenie,
- účel,
- očakávaný výsledok,
- prvý alebo najbližší krok,
- obmedzenia, ktoré by mohli ovplyvniť bezpečnosť alebo správnosť práce.

Ostatné údaje môžu zostať označené ako neznáme. Nevytváraj umelé rozhodnutia ani úlohy iba preto, aby boli všetky sekcie vyplnené.

## Návrh pred zápisom

Po rozhovore zobraz používateľovi:

1. stručnú kartu projektu,
2. informácie rozdelené podľa cieľových súborov,
3. zoznam neznámych alebo otvorených bodov,
4. presný zoznam súborov a priečinkov, ktoré vytvoríš alebo zmeníš.

Tento návrh ešte neukladaj. Požiadaj o výslovné schválenie zápisu. Za schválenie považuj jednoznačný pokyn ako `ulož`, `zapíš`, `vytvor projekt` alebo rovnocenné vyjadrenie.

## Vytvorenie alebo doplnenie projektu

Po schválení:

- pri novom projekte použi celú kostru v `assets/project-template` vrátane priečinka `06_dashboard` a skrytého priečinka `.codex`, prázdneho `backlog.md`, `99_archiv/backlog/README.md` a postupu `03_postupy/sprava_napadov_a_uloh.md`,
- súbory projektového dashboardu sústreď do `06_dashboard`; ak pri schválenej práci na existujúcom projekte už sú inde, navrhni a v rozsahu povoleného presunu vykonaj ich presun v rámci toho istého projektu, oprav cesty a over funkčnosť; samotné založenie priečinka nevytvára dashboard,
- nahraď zástupné polia potvrdenými údajmi,
- neznáme nepremieňaj na vymyslené fakty,
- zachovaj `00_inbox` ako vstupné miesto pre nové nespracované materiály; všetko okrem jeho `README.md` sa má pri začatí práce oznámiť používateľovi,
- v `02_wiki/index.md` vytvor mapu iba pre potvrdené oblasti, zdroje a kľúčové slová; chýbajúce znalosti nevymýšľaj,
- pri existujúcom projekte súbory neprepisuj; doplň ich so zachovaním obsahu a poradia,
- ak cieľový súbor používa inú štruktúru, zachovaj ju a vlož informácie do významovo zodpovedajúcich častí,
- čísluj nové rozhodnutia a otvorené položky pokračovaním existujúcej série,
- nezapisuj rovnaký detail na viac miest; v `MEMORY.md` použi stručný súhrn a odkazy na identifikátory,
- do `diary.md` pridaj počiatočný záznam s aktuálnym dátumom,
- existujúce materiály nepresúvaj bez osobitného súhlasu.

## Overenie

Po zápise over:

- že všetky očakávané základné súbory existujú,
- že odkazy na priečinky a identifikátory dávajú zmysel,
- že pravidlá projektu vyžadujú kontrolu `00_inbox` pri začatí práce a zakazujú presun či vymazanie jeho obsahu bez schválenia,
- že `02_wiki/index.md` odkazuje iba na existujúce súbory alebo zreteľne označuje, že znalosť zatiaľ nebola vytvorená,
- že nový projekt má prázdny backlog a pravidlá obmedzujú jeho čítanie aj čítanie archívov na výslovný pokyn; pri existujúcom projekte zachovaj jeho nápady aj OPN bez automatického pretriedenia,
- že nevznikli duplicitné identifikátory,
- že platné rozhodnutia nie sú označené iba ako návrhy a návrhy nie sú označené ako platné,
- že aktuálny stav v `MEMORY.md` neodporuje `decisions.md` alebo `open_items.md`,
- že sa zachovali pôvodné používateľské údaje.

Ak cieľový projekt obsahuje `.codex/hooks/project_validator.py`, spusti ho z koreňa projektu. Na Windows použi dostupný príkaz `python`; na macOS alebo Linuxe `python3`. Hooky sa začnú automaticky vykonávať až po tom, ako používateľ skontroluje ich definície a označí ich ako dôveryhodné. Over, že hooky nájdu koreň projektu aj pri spustení z jeho podpriečinka.

Na konci rozlíš:

- čo bolo vytvorené alebo zmenené,
- čo bolo overené,
- čo zostalo nevyplnené alebo otvorené.

## Hranice

- Táto schopnosť zakladá a úvodne nastavuje projekt. Neriadi automaticky jeho ďalší priebeh.
- Nevytvára dashboard, automatizácie ani ďalšie schopnosti, ak o ne používateľ výslovne nepožiada.
- Nevykonáva presuny, mazanie alebo prepis existujúcich materiálov bez jasného súhlasu.
- Ak používateľ žiada iba návrh projektu, skonči pri návrhu a nevytváraj súbory.
