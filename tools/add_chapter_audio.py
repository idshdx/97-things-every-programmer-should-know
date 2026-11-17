#!/usr/bin/env python3
"""Embed the Romanian audiobook player into every translated chapter.

For each `ro/thing_XX/README.md` this inserts, right below the chapter title,
an HTML5 `<audio controls>` player plus a plain Markdown fallback link that
both point at `ro/audio/thing_XX_ro.mp3` (the published copy of the MP3 that
`tools/make_audiobook_all.py` renders into `audio/`).

Because `book.toml` sets `src = "ro"`, everything under `ro/audio/` is copied
verbatim by mdBook into `book/audio/`, so the relative path
`../audio/thing_XX_ro.mp3` resolves from the built page
`book/thing_XX/index.html` (and equally well from the Markdown source when
viewed on GitHub or legacy GitBook).

The script is idempotent: chapters that already contain the player are
skipped. `tools/verify_translation.py` strips this block back out before it
compares line/link parity against the English source, so the block does not
break translation verification.

Usage:
    python tools/add_chapter_audio.py
"""

from __future__ import annotations

import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RO_DIR = REPO_ROOT / "ro"
AUDIO_DIR = RO_DIR / "audio"
MANIFEST = REPO_ROOT / "audio" / "manifest.tsv"

MARKER = "<audio controls"


def load_durations() -> dict[str, float]:
    if not MANIFEST.exists():
        return {}
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        return {
            row["chapter"]: float(row["duration_s"])
            for row in csv.DictReader(handle, delimiter="\t")
            if row.get("duration_s")
        }


def format_duration(seconds: float) -> str:
    total = int(round(seconds))
    return f"{total // 60}:{total % 60:02d}"


def build_block(chapter: str, duration: float | None) -> str:
    mp3 = f"../audio/{chapter}_ro.mp3"
    duration_note = f", {format_duration(duration)}" if duration else ""
    return "\n".join(
        [
            f'<audio controls preload="metadata" style="width: 100%; max-width: 36rem;">',
            f'  <source src="{mp3}" type="audio/mpeg" />',
            f'  Browserul tău nu acceptă elementul audio — <a href="{mp3}">descarcă fișierul MP3</a>.',
            f"</audio>",
            "",
            f"🎧 **Audiobook:** [ascultă sau descarcă capitolul (MP3{duration_note})]({mp3})",
        ]
    )


def insert_block(text: str, block: str) -> str:
    lines = text.split("\n")
    heading_idx = next((i for i, line in enumerate(lines) if line.startswith("# ")), None)
    if heading_idx is None:
        heading_idx = -1  # no title: put the player at the very top

    rest = lines[heading_idx + 1 :]
    while rest and not rest[0].strip():
        rest.pop(0)

    new_lines = lines[: heading_idx + 1] + [""] + block.split("\n") + [""] + rest
    return "\n".join(new_lines)


def main() -> int:
    durations = load_durations()
    inserted: list[str] = []
    skipped: list[str] = []
    missing: list[str] = []

    for chapter_dir in sorted(RO_DIR.glob("thing_*")):
        chapter = chapter_dir.name
        readme = chapter_dir / "README.md"
        if not readme.exists():
            continue

        if not (AUDIO_DIR / f"{chapter}_ro.mp3").exists():
            missing.append(chapter)
            continue

        original = readme.read_text(encoding="utf-8")
        if MARKER in original:
            skipped.append(chapter)
            continue

        block = build_block(chapter, durations.get(chapter))
        readme.write_text(insert_block(original, block), encoding="utf-8", newline="\n")
        inserted.append(chapter)

    print(f"Inserted: {len(inserted)}")
    print(f"Already present: {len(skipped)}")
    print(f"Missing MP3 (skipped): {len(missing)} {missing}")
    if missing:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
