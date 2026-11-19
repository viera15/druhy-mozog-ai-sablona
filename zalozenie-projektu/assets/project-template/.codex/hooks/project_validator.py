#!/usr/bin/env python3
"""Rychla strukturalna kontrola projektu vytvoreneho zo vzorovej sablony."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "MEMORY.md",
    "decisions.md",
    "open_items.md",
    "diary.md",
    "02_wiki/index.md",
)

REQUIRED_DIRECTORIES = (
    "00_inbox",
    "01_zdroje",
    "02_wiki",
    "03_postupy",
    "04_pracovne",
    "05_vystupy",
    "99_archiv",
)

DECISION_REQUIRED_FIELDS = (
    "- Datum:",
    "- Stav:",
    "- Nahradza:",
    "- Suvisi s:",
    "### Rozhodnutie",
    "### Dovod",
)

DECISION_RECOMMENDED_FIELDS = (
    "### Posudzovane moznosti",
    "### Dosledky",
    "### Overenie",
)

OPEN_ITEM_FIELDS = (
    "- Stav:",
    "- Priorita:",
    "- Vznikla:",
    "- Termin:",
    "- Zodpovednost:",
    "- Suvisi s:",
    "#### Potrebny vysledok",
    "#### Najblizsi krok",
    "#### Poznamka alebo blokator",
)

DECISION_STATES = {"Navrhnute", "Platne", "Nahradene", "Zrusene"}
OPEN_ITEM_STATES = {"Otvorena", "Rozpracovana", "Caka", "Blokovana", "Hotova", "Zrusena"}
PRIORITIES = {"Vysoka", "Stredna", "Nizka"}

WIKI_METADATA_FIELDS = (
    "- Stav:",
    "- Posledna kontrola:",
    "- Zdroje:",
    "- Suvisiace rozhodnutia:",
    "- Dovod dalsej kontroly:",
)

PLACEHOLDER_RE = re.compile(
    r"\[(?:Doplnit|RRRR-MM-DD|Nazov projektu|Nazov polozky|Nazov rozhodnutia|"
    r"Strucne opisat|Opisat|Co musi|Ako sa|Uviest|Meno alebo rola|"
    r"Identifikator alebo|Vysoka,|Navrhnute alebo)",
    re.IGNORECASE,
)


def _plain(value: str) -> str:
    """Porovnava slovenske sablonove texty bez zavislosti od diakritiky."""
    table = str.maketrans(
        "áäčďéíĺľňóôŕšťúýžÁÄČĎÉÍĹĽŇÓÔŔŠŤÚÝŽ",
        "aacdeillnoorstuyzAACDEILLNOORSTUYZ",
    )
    return value.translate(table)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str


def _finding(severity: str, code: str, path: str, message: str) -> Finding:
    return Finding(severity=severity, code=code, path=path, message=message)


def _read_utf8(path: Path, relative: str, findings: list[Finding]) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        findings.append(
            _finding("error", "encoding", relative, "Subor nie je citatelny ako UTF-8.")
        )
        return None
    except OSError as exc:
        findings.append(
            _finding("error", "read", relative, f"Subor sa nepodarilo precitat: {exc}")
        )
        return None

    if not text.strip():
        findings.append(_finding("error", "empty", relative, "Povinny subor je prazdny."))
    return text


def _record_blocks(text: str, prefix: str) -> list[tuple[str, str]]:
    pattern = re.compile(rf"^(?:##|###)\s+({prefix}-[^:\s]+):.*$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((match.group(1), text[match.start():end]))
    return blocks


def _check_identifiers(
    text: str,
    relative: str,
    prefix: str,
    required_fields: Iterable[str],
    findings: list[Finding],
    recommended_fields: Iterable[str] = (),
) -> None:
    blocks = _record_blocks(text, prefix)
    seen: set[str] = set()
    valid_re = re.compile(rf"^{prefix}-\d{{3}}$")

    for identifier, block in blocks:
        if not valid_re.fullmatch(identifier):
            findings.append(
                _finding(
                    "error",
                    "identifier-format",
                    relative,
                    f"Identifikator {identifier} nema format {prefix}-NNN.",
                )
            )
        elif identifier in seen:
            findings.append(
                _finding(
                    "error",
                    "identifier-duplicate",
                    relative,
                    f"Identifikator {identifier} je pouzity viac ako raz.",
                )
            )
        seen.add(identifier)

        normalized = _plain(block)
        for field in required_fields:
            if _plain(field) not in normalized:
                findings.append(
                    _finding(
                        "error",
                        "missing-field",
                        relative,
                        f"Zaznam {identifier} nema povinnu cast: {field}",
                    )
                )

        for field in recommended_fields:
            if _plain(field) not in normalized:
                findings.append(
                    _finding(
                        "warning",
                        "recommended-field",
                        relative,
                        f"Starsiemu zaznamu {identifier} chyba odporucana cast: {field}",
                    )
                )


def _field_values(block: str, label: str) -> list[str]:
    pattern = re.compile(rf"^-\s+{re.escape(label)}:\s*(.+?)\s*$", re.MULTILINE)
    return [value.strip() for value in pattern.findall(_plain(block))]


def _check_allowed_values(text: str, relative: str, findings: list[Finding]) -> None:
    if relative == "decisions.md":
        for identifier, block in _record_blocks(text, "ROZ"):
            for value in _field_values(block, "Stav"):
                if value.startswith("["):
                    continue
                if value not in DECISION_STATES:
                    findings.append(
                        _finding(
                            "error",
                            "decision-state",
                            relative,
                            f"Zaznam {identifier} ma nepovoleny stav: {value}",
                        )
                    )

    if relative == "open_items.md":
        for identifier, block in _record_blocks(text, "OPN"):
            for value in _field_values(block, "Stav"):
                if value.startswith("["):
                    continue
                if value not in OPEN_ITEM_STATES:
                    findings.append(
                        _finding(
                            "error",
                            "open-item-state",
                            relative,
                            f"Zaznam {identifier} ma nepovoleny stav: {value}",
                        )
                    )
            for value in _field_values(block, "Priorita"):
                if value.startswith("["):
                    continue
                if value not in PRIORITIES:
                    findings.append(
                        _finding(
                            "error",
                            "priority",
                            relative,
                            f"Zaznam {identifier} ma nepovolenu prioritu: {value}",
                        )
                    )


def _check_diary_order(text: str, findings: list[Finding]) -> None:
    date_values: list[date] = []
    for raw in re.findall(r"^##\s+(\d{4}-\d{2}-\d{2})\s*$", text, re.MULTILINE):
        try:
            date_values.append(date.fromisoformat(raw))
        except ValueError:
            findings.append(
                _finding("error", "diary-date", "diary.md", f"Neplatny datum zaznamu: {raw}")
            )

    if any(earlier < later for earlier, later in zip(date_values, date_values[1:])):
        findings.append(
            _finding(
                "error",
                "diary-order",
                "diary.md",
                "Dennik nema najnovsie datumy navrchu.",
            )
        )


def _check_wiki_metadata(root: Path, findings: list[Finding]) -> None:
    wiki_root = root / "02_wiki"
    if not wiki_root.is_dir():
        return

    excluded = {"readme.md", "index.md"}
    for path in sorted(wiki_root.rglob("*.md")):
        if path.name.lower() in excluded:
            continue
        relative = path.relative_to(root).as_posix()
        text = _read_utf8(path, relative, findings)
        if text is None:
            continue
        normalized = _plain(text)
        for field in WIKI_METADATA_FIELDS:
            if _plain(field) not in normalized:
                findings.append(
                    _finding(
                        "warning",
                        "wiki-metadata",
                        relative,
                        f"Znalostnemu suboru chyba odporucany udaj: {field}",
                    )
                )


def _check_inbox(root: Path, findings: list[Finding]) -> None:
    inbox = root / "00_inbox"
    if not inbox.is_dir():
        return

    pending = sorted(
        item.relative_to(inbox).as_posix()
        for item in inbox.rglob("*")
        if item.is_file() and item.name.lower() != "readme.md"
    )
    if not pending:
        return

    preview = ", ".join(pending[:5])
    if len(pending) > 5:
        preview += f", a dalsich {len(pending) - 5}"
    findings.append(
        _finding(
            "warning",
            "inbox-pending",
            "00_inbox",
            f"Inbox obsahuje {len(pending)} nespracovanych suborov: {preview}",
        )
    )


def validate_project(root: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    contents: dict[str, str] = {}

    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            findings.append(
                _finding("error", "missing-file", relative, "Chyba povinny projektovy subor.")
            )
            continue
        text = _read_utf8(path, relative, findings)
        if text is not None:
            contents[relative] = text
            placeholder_count = len(PLACEHOLDER_RE.findall(_plain(text)))
            if placeholder_count:
                findings.append(
                    _finding(
                        "warning",
                        "placeholder",
                        relative,
                        f"Subor obsahuje {placeholder_count} nevyplnenych sablonovych poli.",
                    )
                )

    for relative in REQUIRED_DIRECTORIES:
        if not (root / relative).is_dir():
            findings.append(
                _finding("error", "missing-directory", relative, "Chyba povinny projektovy priecinok.")
            )

    decisions = contents.get("decisions.md")
    if decisions is not None:
        _check_identifiers(
            decisions,
            "decisions.md",
            "ROZ",
            DECISION_REQUIRED_FIELDS,
            findings,
            DECISION_RECOMMENDED_FIELDS,
        )
        _check_allowed_values(decisions, "decisions.md", findings)

    open_items = contents.get("open_items.md")
    if open_items is not None:
        _check_identifiers(open_items, "open_items.md", "OPN", OPEN_ITEM_FIELDS, findings)
        _check_allowed_values(open_items, "open_items.md", findings)

    diary = contents.get("diary.md")
    if diary is not None:
        _check_diary_order(diary, findings)

    _check_wiki_metadata(root, findings)
    _check_inbox(root, findings)

    return findings


def _print_human(root: Path, findings: list[Finding]) -> None:
    errors = [item for item in findings if item.severity == "error"]
    warnings = [item for item in findings if item.severity == "warning"]
    print(f"Kontrola projektu: {root.resolve()}")
    print(f"Chyby: {len(errors)}")
    print(f"Upozornenia: {len(warnings)}")
    for item in findings:
        print(f"- {item.severity.upper()} [{item.code}] {item.path}: {item.message}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Koren kontrolovaneho projektu")
    parser.add_argument("--json", action="store_true", help="Vypise strojovo citatelny JSON")
    args = parser.parse_args()

    root = Path(args.root)
    findings = validate_project(root)
    errors = [item for item in findings if item.severity == "error"]

    if args.json:
        print(
            json.dumps(
                {
                    "root": str(root.resolve()),
                    "ok": not errors,
                    "findings": [asdict(item) for item in findings],
                },
                ensure_ascii=False,
            )
        )
    else:
        _print_human(root, findings)
    return 1 if errors else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
