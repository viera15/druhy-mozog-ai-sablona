# Automaticke kontroly projektu

Projekt pouziva dva hooky Codexu:

- `PreToolUse` chrani povodne subory v `01_zdroje` pred zmenou, prepisanim, vymazanim alebo presunutim a zakladne projektove subory pred vymazanim alebo presunutim. Kontroluje `apply_patch`, `Edit`, `Write` a bezne zapisove alebo destruktivne prikazy spustene cez `Bash`.
- Priamy `Move-Item` alebo `Copy-Item` jedneho existujuceho suboru z `00_inbox` do zatial neexistujuceho ciela v `01_zdroje` je povoleny. Prikaz musi pouzit literalne cesty, nemoze pouzit `-Force`, retazit dalsie prikazy ani prepisat existujuci zdroj.
- Jeden citaci prikaz `rg` sa neposudzuje podla hladaneho textu ako destruktivna operacia. Retazenie, presmerovanie, premenne a prikazova substitucia zostavaju blokovane.
- `PostToolUse` po `Bash`, `apply_patch`, `Edit` alebo `Write` skontroluje povinnu strukturu, mapu znalosti, identifikatory `ROZ-NNN` a `OPN-NNN`, povinne polia, poradie datumov v denniku a zakladne udaje o aktualnosti wiki clankov. Chyby aj upozornenia oznami v kontexte relacie; upozornenia su neblokujuce.

Hooky nic automaticky neopravujú. `PostToolUse` iba oznami zistene chyby a upozornenia.

## Prve spustenie

- Projekt mozes otvorit v koreni alebo pracovat v jeho podpriecinku. Prikaz hooku vyhlada najblizsi nadradeny priecinok s `.codex/hooks.json` a `AGENTS.md`.
- Skontroluj hooky v nastaveniach alebo pomocou `/hooks`.
- Oznac ich ako doveryhodne. Po kazdej zmene definicie hooku je potrebna nova kontrola doveryhodnosti.

## Rucna kontrola

Vo Windows spusti z korena projektu:

```powershell
python .codex\hooks\project_validator.py --root .
```

Na macOS alebo Linuxe spusti:

```bash
python3 .codex/hooks/project_validator.py --root .
```

Kontrola vracia kod `0`, ak nenasla chyby. Nevyplnene sablonove polia vypise ako upozornenia a neoznaci ich za technicku chybu.

## Docasne vypnutie

Jednotlivy hook vypni v prehliadaci hookov. Vsetky hooky mozno vypnut v `config.toml` nastavenim:

```toml
[features]
hooks = false
```

Ochrana hookom doplna pravidla v `AGENTS.md`; nenahradza ich a nie je uplnou bezpecnostnou hranicou. Shellova kontrola je zalozena na rozpoznani beznych zapisovych a destruktivnych prikazov, preto sa na nu nespoliehaj ako na uplnu analyzu lubovolneho skriptu.

## Schválené presuny od 2026-11-05

- Výnimka povoľuje presný samostatný `Move-Item` jedného súboru z `01_zdroje` do nového cieľa v `99_archiv` toho istého projektu. Dopĺňa vyššie uvedený všeobecný zákaz presunov zdrojov; mazanie a prepisovanie zdrojov zostáva blokované.
- Presné presuny jednotlivých bežných dokumentov medzi ostatnými pracovnými priečinkami sa nezamietajú iba pre výskyt názvu základného súboru v ich ceste.
- Výnimka odmieta kolízie, priečinky, presmerovania, vnorené projekty, nejednoznačné cesty, premenné, zástupné znaky a reťazenie. Ostatné ochrany a staršie schválené importné výnimky zostávajú zachované.
- Súhlas a porovnanie SHA-256 pred presunom a po ňom sú povinnosťou agenta podľa `03_postupy/schvalene_presuny_suborov.md`; hook ich sám nevyhodnocuje.
