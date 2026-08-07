#!/usr/bin/env python3
"""Validate the Obsidian vault structure for Luke Wiki.

The single rule this script exists to protect: **사람이 쓴 것과 루틴이 수집한 것은 섞이지
않는다.** `wiki/` 는 사람-작성 전용이고, 자동 뉴스 수집 산출물은 최상위 `routine-news/`
안에서만 산다 (2026-08-07 분리).

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
    ".github",
    ".obsidian",
    "_templates",
    "inbox",
    "routine-news",
    "scripts",
    "sources",
    "wiki",
}
# 사람-작성 영역 — 루틴 산출물이 한 글자도 들어오면 안 되는 곳.
HUMAN_PREFIXES = ("wiki/", "inbox/", "sources/", "_templates/")
ROUTINE_ROOT = "routine-news"
# 루틴이 예전에 쓰던, 또는 실수로 되살릴 수 있는 경로들.
FORBIDDEN_ROUTINE_DIRS = ("wiki/news", "news")

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
SIGNAL_NAME_RE = re.compile(r"\d{4}-\d{2}-\d{2}\.md")
# 마크다운 링크 중 routine-news 로 들어가는 것 (사람-작성 영역에서 금지).
ROUTINE_LINK_RE = re.compile(r"\]\((?:\.\./)*routine-news/[^)]*\)")
ROUTINE_TOP_LEVEL_FILES = {"README.md", "_dashboard.md", "FORMAT.md", "glossary.md"}


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
        if tag not in {"routine-news", "watchlist", "dashboard", "meta", "market-summary", "signals"}:
            return tag
    return None


def has_company_intro(path: Path) -> bool:
    """신규 편입 스켈레톤 허용 조건 — 회사 소개 섹션에 본문이 있으면 유효."""
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## 회사 소개\n+(.+?)(?=\n>|\n##|\Z)", text, re.DOTALL | re.MULTILINE)
    return bool(match and match.group(1).strip())


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


def check_top_level(errors: list[str]) -> None:
    for child in ROOT.iterdir():
        if child.name.startswith(".") and child.name not in {".git", ".github", ".gitignore", ".obsidian"}:
            continue
        if child.is_dir() and child.name not in ALLOWED_TOP_LEVEL_DIRS:
            errors.append(f"Unexpected top-level directory: {child.name}/")
        if child.is_file() and child.name not in ALLOWED_TOP_LEVEL:
            errors.append(f"Unexpected top-level file: {child.name}")


def check_separation(errors: list[str]) -> None:
    """루틴 산출물이 사람-작성 영역으로 새지 않았는지 — 이 스크립트의 핵심 검사."""
    for forbidden in FORBIDDEN_ROUTINE_DIRS:
        if (ROOT / forbidden).exists():
            errors.append(
                f"Routine news reappeared at the old path: {forbidden}/ "
                f"— 루틴 산출물은 {ROUTINE_ROOT}/ 안에만 둔다 (2026-08-07 분리)."
            )


def check_routine_layout(path: Path, relative: str, fm: str, ticker_paths: dict[str, str],
                         errors: list[str]) -> None:
    """routine-news/ 내부 구조 — tickers/ · markets/{map_id}/ · signals/ 세 갈래만 허용."""
    if path.name in ROUTINE_TOP_LEVEL_FILES and Path(relative).parent.as_posix() == ROUTINE_ROOT:
        return

    if relative.startswith(f"{ROUTINE_ROOT}/markets/"):
        if path.name == "README.md":
            return
        # 시장 노드 종합: routine-news/markets/{map_id}/{market_id}.md
        if len(Path(relative).parts) != 4:
            errors.append(
                f"Market summary must live at {ROUTINE_ROOT}/markets/{{map_id}}/{{market_id}}.md: {relative}"
            )
        if "market-summary" not in frontmatter_tags(fm):
            errors.append(f"Market summary missing 'market-summary' tag: {relative}")
        return

    if relative.startswith(f"{ROUTINE_ROOT}/signals/"):
        # 날짜별 시그널: signals/YYYY-MM-DD.md — 하루 한 파일이라 루틴과 사람이
        # 같은 파일을 동시에 고칠 일이 없다 (머지 충돌 방지).
        if not SIGNAL_NAME_RE.fullmatch(path.name):
            errors.append(f"Signal note must be named YYYY-MM-DD.md: {relative}")
        if "signals" not in frontmatter_tags(fm):
            errors.append(f"Signal note missing 'signals' tag: {relative}")
        return

    if not relative.startswith(f"{ROUTINE_ROOT}/tickers/"):
        errors.append(f"Ticker news log must live under {ROUTINE_ROOT}/tickers/: {relative}")
    if "routine-news" in fm and is_empty_routine_scaffold(path) and not has_company_intro(path):
        errors.append(f"Empty routine-news scaffold should be deleted: {relative}")

    ticker = ticker_tag(fm)
    if ticker:
        if ticker in ticker_paths:
            errors.append(
                f"Duplicate routine-news ticker tag {ticker}: {ticker_paths[ticker]} and {relative}"
            )
        ticker_paths[ticker] = relative


def main() -> int:
    errors: list[str] = []

    check_top_level(errors)
    check_separation(errors)

    ticker_paths: dict[str, str] = {}
    for path in markdown_files(ROOT):
        fm = frontmatter(path)
        relative = rel(path)

        if path.name == ".gitkeep":
            errors.append(f"Unnecessary empty Obsidian-visible placeholder: {relative}")
            continue

        is_human = relative.startswith(HUMAN_PREFIXES)

        if is_human:
            if "routine-news" in frontmatter_tags(fm):
                errors.append(
                    f"routine-news tag inside the human-authored area: {relative} "
                    f"— 루틴 산출물이면 {ROUTINE_ROOT}/ 로 옮긴다."
                )
            # 사람-작성 페이지는 루틴 산출물을 링크하지 않는다 (링크는 routine-news → wiki 한 방향).
            for link in ROUTINE_LINK_RE.findall(path.read_text(encoding="utf-8")):
                errors.append(
                    f"Human page links into routine output: {relative} → {link[2:-1]} "
                    f"— promote 후 원 출처 URL 을 sources: 에 박는다."
                )
            if not relative.startswith("sources/") and not has_frontmatter(path):
                errors.append(f"Missing YAML frontmatter: {relative}")

        if relative.startswith(f"{ROUTINE_ROOT}/"):
            check_routine_layout(path, relative, fm, ticker_paths, errors)
            if not has_frontmatter(path):
                errors.append(f"Missing YAML frontmatter: {relative}")

    routine_dir = ROOT / ROUTINE_ROOT
    if not routine_dir.exists():
        errors.append(f"Missing routine news folder: {ROUTINE_ROOT}/")
    else:
        if not (routine_dir / "README.md").exists():
            errors.append(f"Missing routine news guide: {ROUTINE_ROOT}/README.md")
        if not (routine_dir / "tickers").is_dir():
            errors.append(f"Missing ticker news folder: {ROUTINE_ROOT}/tickers/")

    ignore_filters = (ROOT / ".obsidian" / "app.json").read_text(encoding="utf-8")
    if f"{ROUTINE_ROOT}/" not in ignore_filters:
        errors.append(
            f".obsidian/app.json 의 userIgnoreFilters 에 '{ROUTINE_ROOT}/' 가 없다 "
            "— 옵시디언 검색·그래프에서 루틴 뉴스가 다시 노출된다."
        )

    if errors:
        print("Vault validation failed:\n")
        for item in errors:
            print(f"- {item}")
        return 1

    print("Vault validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
