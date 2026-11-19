# Projektová šablóna pre Obsidian a ChatGPT Work

Verzia **1.0** k sérii *Druhý mozog a AI projekty*.

Šablóna vám pomôže viesť jeden projekt v obyčajných súboroch Markdown. Podklady, rozpracované texty, rozhodnutia a úlohy majú vlastné miesto. Obsidian slúži na prezeranie a úpravu poznámok. V desktopovej aplikácii ChatGPT môžete v režime Work sprístupniť AI priečinok projektu a zadať jej konkrétnu úlohu.

Obsah si môžete prezrieť priamo na GitHube v [rozbalenej šablóne](Sablona_projektu). Začnite jej [projektovým README](Sablona_projektu/README.md), kde nájdete vzor zadania a prehľad priečinkov.

## Stiahnutie a otvorenie

- Stiahnite si [ZIP so šablónou 1.0](Sablona_projektu_v1.0.zip) cez tlačidlo **Download raw file** a rozbaľte ho. Priečinok `Sablona_projektu` si premenujte podľa svojho projektu, napríklad na `Priprava_kurzu`.
- **Ak už máte vault**, skopírujte celý premenovaný priečinok doň. V Obsidiane nájdete nový projekt medzi ostatnými priečinkami.
- **Ak začínate s novým vaultom**, v Obsidiane vyberte **Open folder as vault** a otvorte premenovaný priečinok projektu. Vault je priečinok na disku, v ktorom máte poznámky.
- Pri každom ďalšom projekte začnite z novej kópie ZIP súboru.

Na prvé použitie stačí Obsidian alebo textový editor. Git, Python ani doplnok pre Obsidian na prácu s poznámkami nepotrebujete. [Ako otvoriť priečinok ako vault v Obsidiane](https://obsidian.md/help/manage-vaults) (v angličtine).

## Založenie projektu s AI

Otvorte desktopovú aplikáciu ChatGPT. V hornej časti nového chatu prepnite na **Work** a otvorte priečinok nového projektu, v ktorom je súbor `AGENTS.md`. Potom do chatu skopírujte nasledujúci pokyn.

> Prečítaj si projektové súbory AGENTS.md a README.md. Spýtaj sa ma na názov projektu, čo ním chcem dosiahnuť a podľa čoho spoznáme, že je hotový. Počkaj na moje odpovede a podľa nich doplň príslušné časti v README.md. Zachovaj jeho nadpisy a poradie. Uprav iba README.md a použi len údaje, ktoré ti potvrdím. Na záver mi stručne povedz, čo si doplnil a ktoré polia ešte treba vyplniť.

Po doplnení si projektové `README.md` otvorte v Obsidiane a skontrolujte, či vystihuje váš zámer. Ak šablónu používate bez AI, názov, účel a očakávaný výsledok doplňte do tohto súboru ručne.

## Kam ukladať súbory

Ak napríklad pripravujete krátky kurz, nový podklad uložte do `00_inbox`, osnovu píšte v `04_pracovne` a schválený výsledok uložte do `05_vystupy`.

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

## Nápady, úlohy a záznamy

**Bez AI** si nápady zapisujte do `backlog.md` a úlohy, ktorým ste sa rozhodli venovať, do `open_items.md`. Dohody patria do `decisions.md`, stručný aktuálny stav do `MEMORY.md` a priebeh práce do `diary.md`. Pri zápise sa riaďte vzorom v príslušnom súbore.

**S AI** zadajte pokyn v režime Work a nechajte AI zapísať informáciu podľa vzoru. Môžete jej napríklad napísať „Zapíš do backlogu nápad pridať ku kurzu pracovný list“ alebo „Zapíš do rozhodnutí, že kurz bude trvať 60 minút“. Uložený záznam si potom skontrolujte.

Z nápadu v `backlog.md` vytvorí AI úlohu v `open_items.md` iba na váš výslovný pokyn. Uveďte, ktorý nápad vyberáte, napríklad „Z nápadu NAP-003 vytvor otvorenú úlohu“. AI úlohu prepojí s pôvodným nápadom a ten zaeviduje v archíve ako vybraný. [Postup správy nápadov a úloh](Sablona_projektu/03_postupy/sprava_napadov_a_uloh.md)

## Ďalšia práca v režime Work

Vlastné pravidlá pre AI môžete doplniť do `AGENTS.md`. Keď zadávate úlohu, určte aj miesto na uloženie výsledku, napríklad `04_pracovne/osnova_kurzu.md`. Uložený súbor si potom skontrolujte v Obsidiane.

## Voliteľné automatické kontroly

Priečinok `.codex` obsahuje dva hooky. Sú to automatické kontroly, ktoré môže Codex spúšťať pri práci so súbormi. Jeden kontroluje vybrané zásahy do chránených súborov a druhý kontroluje projektovú štruktúru. Potrebujú Python 3. Pred povolením si pozrite konfiguráciu a skripty podľa návodu v `.codex/README.md`. Na ručné spustenie validátora použite z priečinka projektu tento príkaz:

```text
python .codex/hooks/project_validator.py --root .
```

Ak sa Python na vašom počítači spúšťa príkazom `python3`, použite ho namiesto `python`. Pri čistej šablóne sú upozornenia na nevyplnené polia očakávané.
