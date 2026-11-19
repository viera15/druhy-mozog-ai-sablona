# Projektová šablóna pre Obsidian a Codex

Verzia **1.0** k sérii *Druhý mozog a AI projekty*.

Šablóna vám pomôže viesť jeden projekt v obyčajných súboroch Markdown. Podklady, rozpracované texty, rozhodnutia a úlohy majú vlastné miesto. Obsidian slúži na prezeranie a úpravu poznámok. Ak používate Codex s prístupom k miestnym súborom, môžete mu sprístupniť priečinok projektu a dať mu konkrétnu úlohu.

## Stiahnutie a otvorenie

- Stiahnite si [ZIP so šablónou 1.0](Sablona_projektu_v1.0.zip) cez tlačidlo **Download raw file** a rozbaľte ho. Priečinok `Sablona_projektu` si premenujte podľa svojho projektu, napríklad na `Priprava_kurzu`.
- **Ak už máte vault**, skopírujte celý premenovaný priečinok doň. V Obsidiane nájdete nový projekt medzi ostatnými priečinkami.
- **Ak začínate s novým vaultom**, v Obsidiane vyberte **Open folder as vault** a otvorte premenovaný priečinok projektu. Vault je priečinok na disku, v ktorom máte poznámky.
- V projekte otvorte `README.md` a doplňte názov, účel a očakávaný výsledok. Pri ďalšom projekte začnite z novej kópie ZIP súboru.

Na prvé použitie stačí Obsidian alebo textový editor. Git, Python ani doplnok pre Obsidian na prácu s poznámkami nepotrebujete. [Ako otvoriť priečinok ako vault v Obsidiane](https://obsidian.md/help/manage-vaults)

## Prvý projekt

Predstavte si, že pripravujete krátky kurz. Do `README.md` doplňte, pre koho kurz pripravujete a čo má vzniknúť. Nový podklad uložte do `00_inbox`, osnovu píšte v `04_pracovne` a schválený výsledok uložte do `05_vystupy`.

| Kam | Čo tam patrí |
| --- | --- |
| `00_inbox` | Nové podklady, ktoré ešte treba prejsť |
| `01_zdroje` | Pôvodné podklady, ktoré chcete zachovať |
| `02_wiki` | Spracované poznatky a ich mapa v `index.md` |
| `03_postupy` | Opakovateľné pracovné postupy |
| `04_pracovne` | Koncepty a rozpracované materiály |
| `05_vystupy` | Skontrolované a schválené výsledky |
| `06_dashboard` | Miesto pre prípadný projektový dashboard |
| `99_archiv` | Uzavreté alebo neaktuálne materiály |

Nápady si odkladajte do `backlog.md`. Keď sa rozhodnete na niečom pracovať, zaevidujte úlohu v `open_items.md`. Dohody zapisujte do `decisions.md`, stručný aktuálny stav do `MEMORY.md` a priebeh práce do `diary.md`. Každý súbor má vlastnú vzorovú štruktúru.

## Použitie s Codexom

Ako pracovný priečinok v Codexe otvorte priečinok projektu, v ktorom je `AGENTS.md`. Tak mu sprístupníte súbory jedného projektu. Vlastné pravidlá pre AI môžete doplniť do `AGENTS.md`. Prvú úlohu môžete zadať napríklad takto:

> Prečítaj AGENTS.md a README.md. Povedz mi, čo ešte chýba v zadaní projektu a aký prvý krok navrhuješ. Zatiaľ súbory neupravuj.

Ak chcete výsledok uložiť, určte miesto, napríklad `04_pracovne/osnova_kurzu.md`, a potom si uložený súbor skontrolujte v Obsidiane.

## Voliteľné automatické kontroly

Priečinok `.codex` obsahuje dva hooky. Sú to automatické kontroly, ktoré môže Codex spúšťať pri práci so súbormi. Jeden kontroluje vybrané zásahy do chránených súborov a druhý kontroluje projektovú štruktúru. Potrebujú Python 3. Pred povolením si pozrite konfiguráciu a skripty podľa návodu v `.codex/README.md`. Na ručné spustenie validátora použite z priečinka projektu tento príkaz:

```text
python .codex/hooks/project_validator.py --root .
```

Ak sa Python na vašom počítači spúšťa príkazom `python3`, použite ho namiesto `python`. Pri čistej šablóne sú upozornenia na nevyplnené polia očakávané.
