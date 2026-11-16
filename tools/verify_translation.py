#!/usr/bin/env python3
"""Verify the Romanian GitBook translation against the English source.

Checks file coverage, Markdown link integrity, line-count parity and that no
translation placeholders leaked into the output.

Usage:
    python tools/verify_translation.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\]\(([^)]*)\)")
TOKEN_RE = re.compile(r"XLTPX|LTPL|XQZ\d")


def main() -> int:
    source = Path("en")
    target = Path("ro")
    sources = sorted(source.rglob("*.md"))
    problems: list[str] = []

    for src in sources:
        dst = target / src.relative_to(source)
        if not dst.exists():
            problems.append(f"MISSING  {dst}")
            continue

        en_text = src.read_text(encoding="utf-8")
        ro_text = dst.read_text(encoding="utf-8")
        en_links = LINK_RE.findall(en_text)
        ro_links = LINK_RE.findall(ro_text)
        if en_links != ro_links:
            missing = [link for link in en_links if link not in ro_links]
            problems.append(f"LINKS    {dst}: {len(en_links)} -> {len(ro_links)}; missing {missing[:3]}")

        en_lines = len(en_text.replace("\r\n", "\n").split("\n"))
        ro_lines = len(ro_text.replace("\r\n", "\n").split("\n"))
        if en_lines != ro_lines:
            problems.append(f"LINES    {dst}: {en_lines} -> {ro_lines}")

        if TOKEN_RE.search(ro_text):
            problems.append(f"TOKEN    {dst}: placeholder leaked")

    extra = sorted(
        str(path.relative_to(target))
        for path in target.rglob("*.md")
        if not (source / path.relative_to(target)).exists()
    )
    if extra:
        problems.append(f"EXTRA    {extra}")

    summary = target / "SUMMARY.md"
    if summary.exists():
        for link in LINK_RE.findall(summary.read_text(encoding="utf-8")):
            if not (target / link).exists():
                problems.append(f"BROKEN   {summary}: {link}")

    print(f"English files: {len(sources)}")
    print(f"Romanian files: {len(list(target.rglob('*.md')))}")
    print(f"Problems: {len(problems)}")
    for problem in problems[:40]:
        print(problem)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
