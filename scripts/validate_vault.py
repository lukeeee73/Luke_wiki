#!/usr/bin/env python3
"""Validate the Obsidian vault structure for Luke Wiki.

This is intentionally lightweight: it catches structural drift without trying to
parse every markdown nuance. Run from the repository root.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_TOP_LEVEL = {
    ".gitignore",
    "CLAUDE.md",
    "README.md",
}
ALLOWED_TOP_LEVEL_DIRS = {
    ".git",
    ".obsidian",
    "_templates",
    "inbox",
    "scripts",
    "sources",
    "wiki",
}
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)


def markdown_files(base: Path) -> list[Path]:
    return sorted(p for p in base.rglob("*.md") if ".git" not in p.parts)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def frontmatter(path: Path) -> str:
    match = FRONTMATTER_RE.match(path.read_text(encoding="utf-8"))
    return match.group(1) if match else ""


def has_frontmatter(path: Path) -> bool:
    return bool(frontmatter(path))


def main() -> int:
    errors: list[str] = []

    for child in ROOT.iterdir():
        if child.name.startswith(".") and child.name not in {".git", ".gitignore", ".obsidian"}:
            continue
        if child.is_dir() and child.name not in ALLOWED_TOP_LEVEL_DIRS:
            errors.append(f"Unexpected top-level directory: {child.name}/")
        if child.is_file() and child.name not in ALLOWED_TOP_LEVEL:
            errors.append(f"Unexpected top-level file: {child.name}")

    news_dir = ROOT / "wiki" / "news"
    for path in markdown_files(ROOT):
        fm = frontmatter(path)
        relative = rel(path)
        if "routine-news" in fm and not relative.startswith("wiki/news/"):
            errors.append(f"routine-news frontmatter tag outside wiki/news: {relative}")

        if relative.startswith(("wiki/", "inbox/")) and path.name != ".gitkeep":
            if not has_frontmatter(path):
                errors.append(f"Missing YAML frontmatter: {relative}")

    if not news_dir.exists():
        errors.append("Missing routine news folder: wiki/news/")
    elif not (news_dir / "README.md").exists():
        errors.append("Missing news folder guide: wiki/news/README.md")

    if errors:
        print("Vault validation failed:\n")
        for item in errors:
            print(f"- {item}")
        return 1

    print("Vault validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
