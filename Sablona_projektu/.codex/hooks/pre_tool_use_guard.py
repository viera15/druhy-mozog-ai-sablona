#!/usr/bin/env python3
"""PreToolUse ochrana povodnych zdrojov a zakladnej kostry projektu."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any


CORE_FILES = {
    "readme.md",
    "agents.md",
    "memory.md",
    "decisions.md",
    "open_items.md",
    "diary.md",
    ".codex/hooks.json",
}

DESTRUCTIVE_WORDS = re.compile(
    r"\b(remove-item|rename-item|move-item|set-content|add-content|clear-content|"
    r"out-file|copy-item|rm|del|erase|rmdir|rd|move|ren|mv|cp|tee)\b|>{1,2}",
    re.IGNORECASE,
)

SOURCE_IMPORT_COMMAND = re.compile(
    r"^\s*(?P<operation>move-item|copy-item)\s+"
    r"-literalpath\s+(?P<source_quote>[\"'])(?P<source>.+?)(?P=source_quote)\s+"
    r"-destination\s+(?P<target_quote>[\"'])(?P<target>.+?)(?P=target_quote)\s*$",
    re.IGNORECASE,
)

READ_ONLY_SEARCH_COMMAND = re.compile(r"^\s*rg(?:\.exe)?\b", re.IGNORECASE)


def _find_project_root(start: Path) -> Path | None:
    start = start.resolve()
    for candidate in (start, *start.parents):
        if (candidate / ".codex" / "hooks.json").is_file() and (candidate / "AGENTS.md").is_file():
            return candidate
    return None


def _normalize(raw: str, root: Path | None = None, cwd: Path | None = None) -> str:
    value = raw.strip().strip('"\'').replace("\\", "/")
    while value.startswith("./"):
        value = value[2:]
    if root is not None:
        candidate = Path(value)
        if not candidate.is_absolute():
            candidate = (cwd or root) / candidate
        try:
            value = candidate.resolve().relative_to(root.resolve()).as_posix()
        except (OSError, ValueError):
            pass
    return str(PurePosixPath(value)).lower()


def _is_source_path(path: str) -> bool:
    return "01_zdroje" in PurePosixPath(path).parts


def _is_core_file(path: str, root: Path | None = None, cwd: Path | None = None) -> bool:
    normalized = _normalize(path, root, cwd)
    return normalized in CORE_FILES


def _resolve_path(raw: str, cwd: Path) -> Path:
    candidate = Path(raw)
    if not candidate.is_absolute():
        candidate = cwd / candidate
    return candidate.resolve()


def _is_safe_source_import(command: str, root: Path | None, cwd: Path) -> bool:
    """Allow one new file from 00_inbox into 01_zdroje without overwriting."""
    if root is None:
        return False
    match = SOURCE_IMPORT_COMMAND.fullmatch(command)
    if not match:
        return False

    source = _resolve_path(match.group("source"), cwd)
    target = _resolve_path(match.group("target"), cwd)
    resolved_root = root.resolve()
    try:
        source_relative = source.relative_to(resolved_root)
        target_relative = target.relative_to(resolved_root)
    except ValueError:
        return False

    source_parts = tuple(part.lower() for part in source_relative.parts)
    target_parts = tuple(part.lower() for part in target_relative.parts)
    return (
        len(source_parts) >= 2
        and source_parts[0] == "00_inbox"
        and len(target_parts) >= 2
        and target_parts[0] == "01_zdroje"
        and source.is_file()
        and not target.exists()
    )


def _is_read_only_search(command: str) -> bool:
    """Recognize one plain rg invocation without executable shell syntax."""
    if not READ_ONLY_SEARCH_COMMAND.match(command) or any(
        token in command for token in ("$", "`", "\r", "\n")
    ):
        return False

    quote: str | None = None
    for character in command:
        if character in {"'", '"'}:
            if quote is None:
                quote = character
            elif quote == character:
                quote = None
            continue
        if quote is None and character in ";|&><":
            return False
    return quote is None


def _is_safe_project_move(command: str, root: Path | None, cwd: Path) -> bool:
    """Povolí presun jedného súboru; súhlas a SHA-256 overuje pracovný postup."""
    if root is None:
        return False
    match = SOURCE_IMPORT_COMMAND.fullmatch(command)
    if not match or match.group("operation").lower() != "move-item":
        return False
    # Úzka výnimka nepripúšťa shellové výrazy ani nejednoznačné cesty.
    for name in ("source", "target"):
        raw = match.group(name)
        if any(character in raw for character in "\"'$`;|&><*?[]\r\n"):
            return False
        lexical = Path(raw)
        if not lexical.is_absolute():
            lexical = cwd / lexical
        if ".." in lexical.parts or any(":" in part for part in lexical.parts[1:]):
            return False
        for part in (lexical, *lexical.parents):
            if part.is_symlink() or part.is_junction():
                return False
    try:
        source = _resolve_path(match.group("source"), cwd)
        target = _resolve_path(match.group("target"), cwd)
        source_relative = source.relative_to(root.resolve())
        target_relative = target.relative_to(root.resolve())
    except (OSError, ValueError):
        return False
    if (not source.is_file() or target.exists() or not target.parent.is_dir()
            or _find_project_root(source.parent) != root.resolve()
            or _find_project_root(target.parent) != root.resolve()):
        return False
    source_parts = tuple(part.lower() for part in source_relative.parts)
    target_parts = tuple(part.lower() for part in target_relative.parts)
    folders = {"00_inbox", "01_zdroje", "02_wiki", "03_postupy",
               "04_pracovne", "05_vystupy", "99_archiv"}
    protected = {f"{folder}/readme.md" for folder in folders} | {"02_wiki/index.md"}
    if (len(source_parts) < 2 or len(target_parts) < 2
            or source_relative.as_posix().lower() in protected
            or target_relative.as_posix().lower() in protected):
        return False
    if source_parts[0] == "01_zdroje":
        return target_parts[0] == "99_archiv"
    ordinary = folders - {"01_zdroje"}
    return source_parts[0] in ordinary and target_parts[0] in ordinary


def _patch_operations(
    command: str, root: Path | None = None, cwd: Path | None = None
) -> list[tuple[str, str]]:
    operations: list[tuple[str, str]] = []
    current_path: str | None = None
    for line in command.splitlines():
        match = re.match(r"^\*\*\* (Add|Update|Delete) File:\s*(.+?)\s*$", line)
        if match:
            operation = match.group(1).lower()
            current_path = _normalize(match.group(2), root, cwd)
            operations.append((operation, current_path))
            continue
        move_match = re.match(r"^\*\*\* Move to:\s*(.+?)\s*$", line)
        if move_match:
            if current_path:
                operations.append(("move", current_path))
            operations.append(("move", _normalize(move_match.group(1), root, cwd)))
    return operations


def _patch_reason(command: str, root: Path | None = None, cwd: Path | None = None) -> str | None:
    for operation, path in _patch_operations(command, root, cwd):
        if _is_source_path(path) and operation != "add":
            return (
                f"Operacia {operation} nad {path} je zablokovana. "
                "Povodne subory v 01_zdroje sa nesmu menit, mazat ani presuvat."
            )
        if _is_core_file(path) and operation in {"delete", "move"}:
            return f"Operacia {operation} nad povinnym projektovym suborom {path} je zablokovana."
    return None


def _bash_reason(command: str, root: Path | None, cwd: Path) -> str | None:
    if _is_read_only_search(command):
        return None

    normalized = command.replace("\\", "/").lower()
    if not DESTRUCTIVE_WORDS.search(normalized):
        return None

    if _is_safe_project_move(command, root, cwd):
        return None

    if "01_zdroje" in normalized and _is_safe_source_import(command, root, cwd):
        return None

    if "01_zdroje" in normalized:
        return "Prikaz by mohol zmenit, vymazat alebo presunut obsah 01_zdroje."

    for core in CORE_FILES:
        if core in normalized:
            return f"Prikaz by mohol vymazat, prepisat alebo presunut povinny subor {core}."

    broad_delete = re.search(
        r"\b(remove-item|rm|rmdir|rd)\b[^\r\n]*(?:\s\.\s*$|\s\.\\|\s\./|\s\*\s*$)",
        normalized,
    )
    if broad_delete:
        return "Hromadne mazanie v koreni projektu je zablokovane."
    return None


def _direct_file_reason(
    tool_name: str, tool_input: dict[str, Any], root: Path | None, cwd: Path
) -> str | None:
    raw_path = tool_input.get("file_path") or tool_input.get("path")
    if not isinstance(raw_path, str):
        return None
    path = _normalize(raw_path, root, cwd)
    if not _is_source_path(path):
        return None

    candidate = Path(raw_path)
    if not candidate.is_absolute():
        candidate = cwd / candidate
    if tool_name == "Edit" or candidate.exists():
        return (
            f"Nastroj {tool_name} by zmenil povodny subor {path}. "
            "Povodne subory v 01_zdroje sa nesmu menit ani prepisovat."
        )
    return None


def evaluate_event(event: dict[str, Any]) -> str | None:
    tool_name = str(event.get("tool_name", ""))
    tool_input = event.get("tool_input")
    if not isinstance(tool_input, dict):
        return None
    raw_cwd = event.get("cwd")
    cwd = Path(raw_cwd) if isinstance(raw_cwd, str) and raw_cwd else Path.cwd()
    root = _find_project_root(cwd)

    if tool_name in {"Edit", "Write"}:
        return _direct_file_reason(tool_name, tool_input, root, cwd)

    command = tool_input.get("command")
    if not isinstance(command, str):
        return None

    if tool_name == "apply_patch":
        return _patch_reason(command, root, cwd)
    if tool_name == "Bash":
        return _bash_reason(command, root, cwd)
    return None


def main() -> int:
    if hasattr(sys.stdin, "reconfigure"):
        sys.stdin.reconfigure(encoding="utf-8")
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return 0

    reason = evaluate_event(event)
    if reason:
        print(
            json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "PreToolUse",
                        "permissionDecision": "deny",
                        "permissionDecisionReason": reason,
                    }
                },
                ensure_ascii=False,
            )
        )
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
