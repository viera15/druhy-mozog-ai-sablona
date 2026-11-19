# Mapa znalostí

Tento súbor pomáha nájsť spracované znalosti bez načítania celej projektovej wiki. Neobsahuje úplné znenie poznatkov; odkazuje na miesto, kde sa nachádza ich platná verzia.

## Pravidlá údržby

- Záznam pridaj pri vytvorení prvého znalostného súboru k danej oblasti.
- Pri premenovaní, nahradení alebo archivovaní znalostného súboru uprav aj jeho záznam v tejto mape.
- Uvádzaj bežné názvy, skratky a synonymá, pod ktorými môže používateľ alebo agent tému hľadať.
- Ak sa téma opiera o rozhodnutie, uveď jeho identifikátor.
- Ak platná znalosť ešte neexistuje, nevytváraj ju iba kvôli mape; chýbajúcu potrebu eviduj v `open_items.md`.

## Oblasti a zdroje

| Oblasť alebo otázka | Platná znalosť | Zdroj pravdy | Súvisiace rozhodnutia | Kľúčové slová a synonymá |
|---|---|---|---|---|
| [Doplniť] | [Cesta v `02_wiki` alebo Zatiaľ nevytvorené] | [Cesta v `01_zdroje` alebo iný zdroj] | [ROZ-NNN alebo Bez rozhodnutia] | [Doplniť] |

## Známe medzery vo vedomostiach

- [OPN-NNN alebo Bez známej medzery]

## Externé vstupy a oprávnenia

- Pravidlá: `AGENTS.md`, časť Externý obsah a oprávnenia. Kontrolný a testovací postup: `03_postupy/overenie_externych_vstupov.md`. Kľúčové slová: dôveryhodnosť vstupov, externé dáta, prompt injection, RAG, prílohy, výstupy nástrojov, oprávnenia, schvaľovanie, pamäť. Scenáre pre AI aplikácie sú podmienené rozsahom konkrétneho projektu.

## Schválené presuny súborov

- Presun, archivácia, kolízia cieľa, kontrolný súčet, SHA-256, ochrana zdrojov: `03_postupy/schvalene_presuny_suborov.md` a časť Schválené presuny materiálov v `AGENTS.md`.

## Ukončenie pri limite

- Pokyny `limit5` a `limitT`, zostávajúci päťhodinový a týždenný limit, bezpečné prerušenie, uloženie stavu a pokračovanie: záväzné pravidlo v `AGENTS.md`, podrobné kroky v `03_postupy/bezpecny_cyklus_ai_agenta.md`. Stav konkrétnej úlohy patrí do `MEMORY.md` a podľa potreby do `open_items.md`; história do `diary.md`.

## Nápady, backlog a vybrané úlohy

- Prístup, NAP, výber do OPN, oddelený ročný archív a dátum spracovania: [Správa nápadov a úloh](../03_postupy/sprava_napadov_a_uloh.md). Backlog ani archívy sa nečítajú bez výslovného pokynu; táto mapa ich obsah nekopíruje.
