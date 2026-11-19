# Projektová wiki

Sem patria spracované, overené a aktuálne znalosti používané pri bežnej práci.

Odporúčané témy podľa typu projektu:

- požiadavky,
- terminológia,
- procesy,
- dátový model,
- architektúra,
- testovacie pravidlá,
- kontakty a zodpovednosti.

Pravidlá:

- Každý znalostný súbor má uvádzať stav, dátum poslednej kontroly, použité zdroje, súvisiace rozhodnutia a dôvod ďalšej kontroly.
- Neistú informáciu zreteľne označ.
- Pri zmene faktu aktualizuj wiki a podľa významu aj `MEMORY.md`.
- Starú verziu pri dôležitých zmenách archivuj.
- Pri vytvorení, premenovaní, nahradení alebo archivovaní znalostného súboru aktualizuj `index.md`.
- Rovnaký detail nekopíruj do viacerých článkov. V `index.md` uveď, kde sa nachádza jeho platné znenie.
- Neaktuálnu alebo protichodnú informáciu nevymazávaj bez vysvetlenia; označ jej stav a odkaz na platnú náhradu.

## Odporúčaná hlavička znalostného súboru

```markdown
# [Názov témy]

- Stav: [Potvrdené, Pracovné alebo Historické]
- Posledná kontrola: [RRRR-MM-DD]
- Zdroje: [Cesta alebo odkaz na pôvodný zdroj]
- Súvisiace rozhodnutia: [ROZ-NNN alebo Bez súvisiaceho rozhodnutia]
- Nahrádza: [Cesta k staršej znalosti alebo Bez predchodcu]
- Dôvod ďalšej kontroly: [Udalosť, zmena zdroja alebo Bez plánovanej kontroly]
```

Význam stavov:

- `Potvrdené`: informácia je overená a používa sa pri bežnej práci.
- `Pracovné`: informácia ešte nie je úplne overená alebo schválená.
- `Historické`: informácia už neplatí, ale zostáva zachovaná pre vysvetlenie vývoja.

Dátum sám neurčuje neaktuálnosť. Pri použití znalosti zohľadni aj jej stav, zdroj a dôvod ďalšej kontroly.
