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


def frontmatter_field(fm: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}:\s*(.*)$", fm, re.MULTILINE)
    return match.group(1).strip() if match else ""


def frontmatter_tags(fm: str) -> list[str]:
    raw = frontmatter_field(fm, "tags")
    if raw.startswith("[") and raw.endswith("]"):
        return [tag.strip().strip('"\'') for tag in raw[1:-1].split(",") if tag.strip()]
    return []


def ticker_tag(fm: str) -> str | None:
    for tag in frontmatter_tags(fm):
        if tag not in {"routine-news", "watchlist", "dashboard", "meta"}:
            return tag
    return None


def marked_section(text: str, start: str, end: str) -> str:
    if start not in text or end not in text:
        return ""
    return text.split(start, 1)[1].split(end, 1)[0].strip()


def is_empty_routine_scaffold(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    sections = [
        marked_section(text, "<!-- OPEN_CLAIMS_START -->", "<!-- OPEN_CLAIMS_END -->"),
        marked_section(text, "<!-- FACTS_START -->", "<!-- FACTS_END -->"),
        marked_section(text, "<!-- DAILY_START -->", "<!-- DAILY_END -->"),
    ]
    meaningful = [
        re.sub(r"_\([^)]*비어 있음[^)]*\)_", "", section).strip()
        for section in sections
    ]
    return not any(meaningful)


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
    ticker_paths: dict[str, str] = {}
    for path in markdown_files(ROOT):
        fm = frontmatter(path)
        relative = rel(path)

        if path.name == ".gitkeep":
            errors.append(f"Unnecessary empty Obsidian-visible placeholder: {relative}")
            continue

        if "routine-news" in fm and not relative.startswith("wiki/news/"):
            errors.append(f"routine-news frontmatter tag outside wiki/news: {relative}")

        if relative.startswith("wiki/news/") and path.name not in {"README.md", "_dashboard.md"}:
            if not relative.startswith("wiki/news/tickers/"):
                errors.append(f"Ticker news log must live under wiki/news/tickers/: {relative}")
            if "routine-news" in fm and is_empty_routine_scaffold(path):
                errors.append(f"Empty routine-news scaffold should be deleted: {relative}")
            ticker = ticker_tag(fm)
            if ticker:
                if ticker in ticker_paths:
                    errors.append(
                        f"Duplicate routine-news ticker tag {ticker}: {ticker_paths[ticker]} and {relative}"
                    )
                ticker_paths[ticker] = relative

        if relative.startswith(("wiki/", "inbox/")):
            if not has_frontmatter(path):
                errors.append(f"Missing YAML frontmatter: {relative}")

    if not news_dir.exists():
        errors.append("Missing routine news folder: wiki/news/")
    elif not (news_dir / "README.md").exists():
        errors.append("Missing news folder guide: wiki/news/README.md")
    elif not (news_dir / "tickers").is_dir():
        errors.append("Missing ticker news folder: wiki/news/tickers/")

    if errors:
        print("Vault validation failed:\n")
        for item in errors:
            print(f"- {item}")
        return 1

    print("Vault validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
