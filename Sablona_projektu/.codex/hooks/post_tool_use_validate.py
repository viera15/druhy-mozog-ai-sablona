#!/usr/bin/env python3
"""PostToolUse kontrola zakladnej struktury projektu po uprave suboru."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from project_validator import validate_project


def _find_project_root(start: Path) -> Path | None:
    start = start.resolve()
    for candidate in (start, *start.parents):
        if (candidate / ".codex" / "hooks.json").is_file() and (candidate / "AGENTS.md").is_file():
            return candidate
    return None


def _message_for_findings(findings: list[object]) -> tuple[str, str] | None:
    errors = [item for item in findings if getattr(item, "severity", None) == "error"]
    warnings = [item for item in findings if getattr(item, "severity", None) == "warning"]
    if not errors and not warnings:
        return None

    if errors:
        system_message = "Projektova kontrola nasla chyby alebo upozornenia."
        lines = ["Projektova kontrola nasla chyby, ktore treba preverit:"]
    else:
        system_message = "Projektova kontrola nasla upozornenia."
        lines = ["Projektova kontrola nasla neblokujuce upozornenia:"]

    selected = [*errors, *warnings]
    lines.extend(
        f"- {getattr(item, 'path', '?')}: {getattr(item, 'message', '')}"
        for item in selected[:12]
    )
    if len(selected) > 12:
        lines.append(f"- Dalsich zisteni: {len(selected) - 12}")
    return system_message, "\n".join(lines)


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return 0

    raw_cwd = event.get("cwd")
    start = Path(raw_cwd) if isinstance(raw_cwd, str) and raw_cwd else Path.cwd()
    root = _find_project_root(start)
    if root is None:
        return 0

    findings = validate_project(root)
    rendered = _message_for_findings(findings)
    if rendered is None:
        return 0
    system_message, message = rendered

    print(
        json.dumps(
            {
                "systemMessage": system_message,
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": message,
                },
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
