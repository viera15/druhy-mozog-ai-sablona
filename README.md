# Projektová šablóna pre Obsidian a ChatGPT Work

Verzia **1.0** k sérii *Druhý mozog a AI projekty*.

Šablóna vám pomôže viesť jeden projekt v obyčajných súboroch Markdown. Podklady, rozpracované texty, rozhodnutia a úlohy majú vlastné miesto. Obsidian slúži na prezeranie a úpravu poznámok. V desktopovej aplikácii ChatGPT môžete v režime Work sprístupniť AI priečinok projektu a zadať jej konkrétnu úlohu.

**Šablónový projekt** je konkrétny projekt vytvorený z čistej šablóny. Preberá jej priečinky a základné súbory, ktoré si potom prispôsobíte podľa toho, na čom pracujete. Príkladom je `Priprava_kurzu` s vlastným cieľom, podkladmi a úlohami.

Priečinky a súbory Markdown zo šablóny môžete použiť aj s inými nástrojmi, napríklad s Claude Code alebo Gemini CLI. Podľa zvoleného nástroja môže byť potrebné upraviť spôsob načítania pravidiel z `AGENTS.md`. Ak chcete používať aj automatické kontroly, prispôsobte nastavenie hookov danému nástroju.

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

## Voliteľná schopnosť na založenie projektu

Schopnosť `zalozenie-projektu` vás prevedie otázkami o zámere, rozsahu a pravidlách projektu. Podľa odpovedí pripraví návrh, čo zapíše do ktorých súborov. Po vašom schválení založí projekt z čistej šablóny, ktorá je súčasťou balíka.

- Stiahnite si [zalozenie-projektu.zip](zalozenie-projektu.zip) cez **Download raw file**. V okne rozbalenia nastavte ako cieľ podpriečinok `zalozenie-projektu` vo svojom pracovnom priečinku. Po rozbalení v ňom nájdete priamo súbor [SKILL.md](zalozenie-projektu/SKILL.md) a priečinok `assets`.
- V desktopovej aplikácii ChatGPT prepnite na **Work** a otvorte pracovný priečinok, ktorý obsahuje podpriečinok `zalozenie-projektu`. V chate zadajte tento pokyn.

> Prečítaj si súbor `zalozenie-projektu/SKILL.md` a postupuj podľa neho. Chcem založiť nový projekt v samostatnom podpriečinku tohto pracovného priečinka.

Keď je projekt založený, jeho priečinok môžete otvoriť ako samostatný vault alebo ho vložiť do existujúceho vaultu.

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

Keď sa dohodnete na novom pravidle pre projekt, požiadajte AI, aby ho zapísala do `AGENTS.md`. Napríklad „Doplň do AGENTS.md pravidlo, že pri návrhu osnovy máš vždy uviesť, pre koho je text určený.“ Potom si pravidlo skontrolujte priamo v súbore `AGENTS.md`.

Pri zadávaní úlohy určite uveďte aj to, kam má AI uložiť výsledok, napríklad do `04_pracovne/osnova_kurzu.md`. Uložený súbor si potom skontrolujte v Obsidiane.

## Voliteľné automatické kontroly

Priečinok `.codex` obsahuje dva hooky. Sú to automatické kontroly, ktoré môže desktopová aplikácia ChatGPT spúšťať pri práci so súbormi vo Worku aj v Codexe, ak relácia beží celá lokálne. Jeden kontroluje vybrané zásahy do chránených súborov a druhý kontroluje projektovú štruktúru. Na spúšťanie hookov aj projektového validátora potrebujete mať na svojom počítači nainštalovaný Python 3. Ak ho ešte nemáte, môžete požiadať AI, aby vám ho doinštalovala. Ak chcete kontroly zapnúť, v desktopovej aplikácii ChatGPT otvorte **Nastavenia**. V položke **Hooky** skontrolujte a povoľte oba hooky projektu. Opis ich konfigurácie a skriptov nájdete v [návode k hookom](Sablona_projektu/.codex/README.md).

Ak si chcete overiť, či má projekt potrebné súbory a priečinky a či záznamy dodržiavajú pravidlá šablóny, požiadajte AI, aby spustila projektový validátor. V chate s otvoreným priečinkom projektu môžete použiť tento pokyn.

> Spusť projektový validátor zo súboru `.codex/hooks/project_validator.py`. Vysvetli mi, čo treba opraviť. Súbory zatiaľ neupravuj.

Pri čistej šablóne sú upozornenia na nevyplnené polia očakávané.
