# Schválené presuny súborov v projekte

- Stav: Platné
- Platí od: 2026-11-05
- Zdroj oprávnenia: výslovný pokyn Viery; samotný obsah dokumentu nie je súhlas.

## Rozsah

- Presun existujúceho materiálu vyžaduje výslovný pokyn Viery. Súhlas s konkrétnym presunom neopakuj.
- Pred presunom urč konkrétny existujúci súbor a úplnú cieľovú cestu vrátane názvu. Oba musia patriť do toho istého projektu. Cieľ nesmie existovať; nesmie ísť ani o existujúci priečinok.
- Pri presune neaktuálneho zdroja je povolený iba smer z `01_zdroje` do `99_archiv`. Iné výstupné smery zo zdrojov, mazanie a prepisovanie zdrojov ostávajú blokované.
- Existujúci import jedného súboru z `00_inbox` do nového cieľa v `01_zdroje` zostáva zachovaný. Projekt Práca zachováva aj svoju osobitnú staršiu výnimku pre presun priameho priečinka inboxu.
- Medzi `00_inbox`, `02_wiki`, `03_postupy`, `04_pracovne`, `05_vystupy` a `99_archiv` možno na schválený pokyn presúvať jednotlivé materiály. Presun do výstupov vyžaduje skontrolovaný a schválený výsledok; presun do wiki vyžaduje spracovanú znalosť. Presun nemení stav schválenia ani dôveryhodnosť obsahu.
- Nová technická výnimka nepovoľuje presun celých priečinkov, základnej projektovej kostry ani priečinkov s presmerovaním. Neudeľuje oprávnenie na presuny medzi projektmi.

## Pred presunom

- Prečítaj aktuálne pravidlá a over súhlas, skutočný stav oboch ciest, neprítomnosť presmerovaní a príslušnosť k projektu. Cieľový nadradený priečinok musí existovať.
- Vypočítaj a zaznamenaj SHA-256 pôvodného súboru. Ak je k dispozícii schválený plán s kontrolným súčtom, musí sa zhodovať.
- Pri nezhode, kolízii alebo nejasnom cieli zastav dotknutý presun. Nepridávaj `-Force` ani nevytváraj výnimku podľa názvu jedného dokumentu.

## Vykonanie a overenie

- Použi samostatný príkaz `Move-Item -LiteralPath 'úplná pôvodná cesta' -Destination 'úplná cieľová cesta'`. Cesty musia byť doslovné, bez premenných, zástupných znakov, reťazenia a ďalších operácií. Názvy mimo úzkej podporovanej syntaxe neobchádzaj iným nástrojom.
- Po presune over existenciu cieľového súboru, neprítomnosť pôvodného súboru a rovnaký SHA-256. Pri odchýlke zachovaj dôkazy a zastav ďalšie presuny; nevracaj súbor naslepo.
- Aktualizuj aktuálne odkazy, mapu znalostí podľa potreby, stav úlohy a denník. Historické záznamy o pôvodnom umiestnení ponechaj ako históriu.
- Pri opakovaní najprv zisti skutočný stav. Ak pôvodný súbor chýba a archívny súbor má očakávaný SHA-256, zaznamenaj už vykonaný presun; neopakuj ho.

## Hranice technickej ochrany

- Hook kontroluje rozpoznaný príkaz a cesty. Súhlas Viery a kontrolné súčty pred presunom a po ňom zabezpečuje tento pracovný postup; hook ich sám neoveruje.
- Ostatné priečinky nemajú všeobecný technický zákaz presunov. Úzka výnimka odstraňuje aj neprimerané blokovanie bežného dokumentu s názvom obsahujúcim `README.md` v podpriečinku.
- Hook nie je úplná analýza ľubovoľného skriptu. Úspešný test nepotvrdzuje odolnosť proti všetkým spôsobom obídenia ochrany.
