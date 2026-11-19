# Správa nápadov a úloh

- Stav: Spoločný postup správy nápadov a vybraných úloh; konkrétne operácie vyžadujú pokyn používateľa.
- Platnosť: projekt, ktorého AGENTS.md na tento postup odkazuje.
- Dátum: 2026-11-13.

## Účel a rozsah

Oddeliť nápady na zváženie od vybraných úloh. `backlog.md` obsahuje aktívne nápady, `open_items.md` vybrané úlohy a `99_archiv/backlog/backlog_RRRR.md` uzavreté nápady podľa roku uzavretia. Platné projektové rozhodnutia zostávajú v `decisions.md`.

Zavedenie tohto postupu nezahŕňa hromadné pretriedenie existujúcich OPN ani zmenu hookov či dashboardu. Odborné plány a registre zostávajú zdrojmi pravdy svojho obsahu. Prepojenie s Google Tasks je požiadavkou na budúci workflow; jeho vytvorenie a overenie sa teraz nevykonáva.

## Vstupy a oprávnenie

- Výslovný pokyn používateľa určuje, či sa má nápad zapísať, backlog čítať alebo z neho vybrať nápad a vytvoriť OPN. Pokyn na dohodnutý zber platí iba vo svojom určenom rozsahu.
- Backlog ani archívy sa nečítajú pri bežnom začatí práce, údržbe alebo iba preto, že by mohli súvisieť s úlohou. Pri všeobecnom vyhľadávaní ich vynechaj.
- Pri zadanom kroku možno vykonať nevyhnutné súvisiace čítanie, kontrolu duplicít a identifikátorov, zápis odkazov a archiváciu dotknutého záznamu. Rovnaký súhlas sa nevyžaduje opakovane.
- Pokyn na výber konkrétneho nápadu zahŕňa vytvorenie OPN a archiváciu pôvodného nápadu. Neznamená schválenie realizácie zmeny, ktorá má vlastnú schvaľovaciu hranicu.
- Materiály v inboxe ani pôvodné zdroje sa zápisom nápadu nepovažujú za spracované alebo schválené na presun.

## Zápis nového nápadu

- Over aktuálny backlog a v potrebnom rozsahu archívy, aby nevznikla duplicita a neopakoval sa identifikátor. Zvoľ nasledujúce voľné číslo po najvyššom použitom NAP v tomto projekte.
- Použi nadpis `### NAP-NNN: Názov nápadu`.
- Uveď polia `Dátum zachytenia`, `Stav`, `Podstata`, `Prínos alebo problém` a `Pôvod alebo podklad`.
- Aktívne stavy sú `Na zváženie` a `Odložený`. Pri odložení uveď dôvod alebo podmienku návratu, ak sú známe.
- Neznámy prínos, pôvod alebo dôvod označ ako neznámy; nevymýšľaj ho. Priorita, termín a najbližší krok nie sú povinnými poľami nápadu.
- Ak používateľ prikáže doplniť existujúci nápad, zachovaj jeho identifikátor a pôvodný význam. Rozlíš nové doplnenie od predošlého znenia, ak by sa menil význam.
- Zápis spätne načítaj a skontroluj. Nevytváraj automaticky OPN, termín ani Google Tasks.

## Čítanie a výber

- Na pokyn používateľa čítaj iba požadovanú časť. Pri výbere posúď prínos, súlad s projektom, náročnosť, podklady a závislosti; neistoty označ. Posúdenie nie je automatický súhlas s realizáciou.
- Pri výbere na spracovanie vytvor konkrétnu OPN s očakávaným výsledkom, stavom, prioritou, najbližším krokom a ostatnými povinnými poľami existujúcej evidencie.
- Do OPN zapíš pôvodné NAP a odkaz na jeho výsledné umiestnenie v archíve. Do záznamu NAP doplň stav `Vybraný`, dátum uzavretia a odkazy na vytvorené OPN. Jeden nápad môže vytvoriť viac úloh.
- NAP archivuj podľa postupu nižšie. Aktuálny postup a výsledok práce ďalej zapisuj iba pri OPN.
- Pri odložení zachovaj nápad v aktívnom backlogu. Nápady sa automaticky nezamietajú pre vek, nízku prioritu ani neznámu náročnosť.

## Vyradenie, zlúčenie a archivácia

- Na pokyn na zamietnutie konkrétneho nápadu doplň stav `Zamietnutý`, dátum uzavretia a potvrdený dôvod. Ak dôvod nebol uvedený, uveď to.
- Na pokyn na zlúčenie označ pôvodný záznam stavom `Zlúčený` a odkáž na zachovaný nápad; zachovaj jedinečné informácie.
- Skontroluj cieľový ročný archív a neprítomnosť rovnakého NAP. Nový ročný súbor vytvor iba vtedy, ak ešte neexistuje; existujúci obsah neprepisuj.
- Skopíruj úplný uzavretý záznam do archívu. Porovnaj pôvodný obsah a doplnené polia, over odkazy a až potom odstráň aktívny záznam. Skontroluj, že existuje jediný úplný aktuálny záznam daného NAP.
- V `99_archiv/backlog/README.md` pridaj odkaz na nový ročný súbor, ak vznikol. Pri OPN a zlúčenom nápade skontroluj výsledné odkazy.
- Zaznamenaj uskutočnený krok do denníka. Nejde o presun zdrojového súboru; pravidlá ochrany `01_zdroje` sa nemenia.
- Pri prerušení najprv zisti skutočný stav oboch súborov. Odstránenie aktívneho záznamu nesmie predbehnúť overenie archívu a opakovanie nesmie vytvoriť duplicitu.
- Vymazanie nápadu namiesto archivácie a presuny iných materiálov vyžadujú osobitný pokyn.

## Opätovné otvorenie a staršie OPN

- Na výslovný pokyn na opätovné otvorenie nápadu zachovaj NAP aj históriu uzavretia. Vráť celý záznam do aktívneho backlogu a v archíve ponechaj iba historický odkaz na aktuálne umiestnenie. Referenčný odkaz nie je druhým úplným záznamom.
- Výber iného ďalšieho kroku pri už existujúcej OPN nemusí znamenať opätovné otvorenie NAP. Zamedz vzniku druhej rovnakej úlohy.
- Staršie OPN zostávajú na mieste. Prípadné preradenie priprav ako konkrétny návrh a vykonaj až na pokyn používateľa. Zachovaj pôvodné ID a vysvetlenie; administratívne preradenie neoznačuj za vecné zamietnutie alebo dokončenie práce.

## Dátum spracovania a budúci workflow

- `Dátum spracovania` je nepovinný plánovaný deň práce. `Termín` je najneskorší dátum dokončenia alebo iná termínová podmienka. Nezamieňaj ich a dátum nevymýšľaj.
- Kým nebude vytvorený workflow, pri OPN sa nevytvára ani netestuje prepojenie Google Tasks. Nevytvára sa náhradná kalendárová udalosť.
- Po vytvorení workflow sa má na konkrétnej autorizovanej OPN overiť vytvorenie Google Tasks podľa dátumu spracovania, uloženie identifikátora zoznamu a úlohy, zmena dátumu bez duplicity a prenesenie dokončenia. Konkrétne pripojenie a pravidlá workflow sa určia v samostatnom zadaní.
- Spôsob pripojenia, spúšťania a riešenia konfliktov sa dorieši pri samostatnom zadaní workflow. Samotné založenie backlogu tieto činnosti nespúšťa.

## Kontrola a očakávaný výsledok

- Over oprávnenie na prístup, zachovanie obsahu, jedinečnosť ID naprieč aktívnym súborom a archívmi, správne stavy a odkazy. Kontrola obsahu backlogu sa robí len v rozsahu zadaného kroku.
- Spätne načítaj zápisy, aktualizuj dotknutú evidenciu a spusti projektový validátor podľa bezpečného cyklu. Pri zmene pravidiel použi relevantné existujúce testy.
- Aktuálny validátor nekontroluje polia NAP ani ich jedinečnosť. Tieto kontroly vykonáva agent pri konkrétnom pokyne; ich automatizácia a zmena hookov neboli zavedené.
- Výsledkom je dohľadateľný nápad alebo vybraná úloha bez straty údajov, dvojitého vedenia postupu práce či neschváleného rozšírenia rozsahu.
