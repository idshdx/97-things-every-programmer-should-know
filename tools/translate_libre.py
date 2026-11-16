#!/usr/bin/env python3
"""Translate the GitBook markdown tree from English to Romanian via LibreTranslate.

Only prose is sent to LibreTranslate. Markdown structure (URLs, inline code,
fences, link syntax, headings/list/quote markers, emphasis markers) is split
out locally and re-attached after translation. Prose segments are batched as
newline-joined lines because LibreTranslate preserves line boundaries; each
batch is validated by line count, with a per-segment fallback on mismatch.

Usage:
    python tools/translate_libre.py                 # translate en/ -> ro/
    python tools/translate_libre.py --limit 3       # dry run on first 3 files
    python tools/translate_libre.py --force         # overwrite existing ro/ files
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

API_URL = "http://localhost:5000/translate"
MAX_CHARS = 4000

FENCE_RE = re.compile(r"^[ \t]{0,3}(```+|~~~+)")

# Anything matching here is copied verbatim; the gaps between matches are prose.
PROTECT_RE = re.compile(
    r"(?P<inline>`+[^`\n]*`+)"
    r"|(?P<html><[^>\n]+>)"
    r"|(?P<linkopen>!?\[)"
    r"|(?P<linkclose>\](?=\())"
    r"|(?P<linkurl>(?<=\])\([^)\n]*\))"
    r"|(?P<url>https?://[^\s<>\)\]]+|www\.[^\s<>\)\]]+)"
    r"|(?P<marker>^[ \t]{0,3}(?:#{1,6}[ \t]+|>[ \t]?|[-*+][ \t]+|\d+\.[ \t]+))"
    r"|(?P<setext>^[ \t]*(?:=+|-+)[ \t]*$)"
    r"|(?P<emphasis>\*\*|__|~~|\*|_)"
)


@dataclass
class Part:
    prose: bool
    text: str
    translated: str = ""


def split_line(line: str) -> list[Part]:
    """Split a line into prose parts and verbatim structure parts."""
    parts: list[Part] = []
    position = 0
    for match in PROTECT_RE.finditer(line):
        if match.start() > position:
            parts.append(Part(True, line[position:match.start()]))
        parts.append(Part(False, match.group(0)))
        position = match.end()
    if position < len(line):
        parts.append(Part(True, line[position:]))
    return parts


def batch_segments(segments: list[tuple[int, int]], parts: list[list[Part]], max_chars: int) -> list[list[tuple[int, int]]]:
    """Group prose segments into API-sized batches, keeping source order."""
    batches: list[list[tuple[int, int]]] = []
    current: list[tuple[int, int]] = []
    size = 0
    for ref in segments:
        line_index, part_index = ref
        length = len(parts[line_index][part_index].text) + 1
        if current and size + length > max_chars:
            batches.append(current)
            current, size = [], 0
        current.append(ref)
        size += length
    if current:
        batches.append(current)
    return batches


def translate_chunk(query: str, api_url: str, retries: int = 3) -> str:
    payload = json.dumps({"q": query, "source": "en", "target": "ro"}).encode("utf-8")
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(
                api_url,
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(request, timeout=180) as response:
                return json.load(response)["translatedText"]
        except (urllib.error.URLError, KeyError, ValueError, TimeoutError) as exc:
            last_error = exc
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"LibreTranslate request failed: {last_error}") from last_error


def translate_batch(batch: list[tuple[int, int]], parts: list[list[Part]], api_url: str) -> None:
    """Translate one batch of prose segments, validating by line count."""
    texts = [parts[li][pi].text for li, pi in batch]
    query = "\n".join(texts)
    result = translate_chunk(query, api_url)
    output = result.split("\n")

    if len(output) != len(batch):
        result = translate_chunk(query, api_url)
        output = result.split("\n")

    if len(output) == len(batch):
        for (line_index, part_index), translated in zip(batch, output):
            parts[line_index][part_index].translated = translated
        return

    # Last resort: translate segments one by one so one bad batch cannot
    # shift the mapping for every other segment in the file.
    print("      batch: falling back to per-segment translation", flush=True)
    for (line_index, part_index), text in zip(batch, texts):
        if not text.strip():
            parts[line_index][part_index].translated = text
            continue
        parts[line_index][part_index].translated = translate_chunk(text, api_url)


def cleanup_markdown(text: str) -> str:
    """Undo spacing artifacts introduced by the MT model."""
    # "1.  [link]" -> "1. [link]"
    text = re.sub(r"(?m)^([ \t]*(?:[-*+]|\d+\.))[ \t]{2,}", r"\1 ", text)
    # "> * \"quote\"" -> "> *\"quote\"" (italic marker must touch the text)
    text = re.sub(r"(?m)^([ \t]*>[ \t]*)\*[ \t]+", r"\1*", text)
    # Stray standalone period on the final line
    text = re.sub(r"\n\.[ \t]*$", "", text)
    return text


def translate_file(source: Path, target: Path, api_url: str, force: bool) -> bool:
    if target.exists() and not force:
        print(f"SKIP  {source} -> {target} (exists; use --force to redo)", flush=True)
        return True

    text = source.read_text(encoding="utf-8")
    newline = "\r\n" if "\r\n" in text else "\n"
    had_final_newline = text.endswith(("\n", "\r\n"))
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = normalized.split("\n")

    parts: list[list[Part]] = []
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            parts.append([])  # fence line: verbatim
        elif in_fence:
            parts.append([])  # code content: verbatim
        else:
            parts.append(split_line(line))

    segments = [
        (line_index, part_index)
        for line_index, line_parts in enumerate(parts)
        for part_index, part in enumerate(line_parts)
        if part.prose and part.text.strip()
    ]

    for index, batch in enumerate(batch_segments(segments, parts, MAX_CHARS), start=1):
        translate_batch(batch, parts, api_url)
        print(f"      batch {index}/{len(batch)} segments", flush=True)

    output_lines: list[str] = []
    for line, line_parts in zip(lines, parts):
        if not line_parts:
            output_lines.append(line)
            continue
        for part in line_parts:
            # Verbatim parts keep their original text; empty prose stays empty.
            if not part.translated:
                part.translated = part.text
        output_lines.append("".join(part.translated for part in line_parts))

    # split() already preserves a final newline as an empty last element,
    # so no extra newline needs to be appended here.
    output = cleanup_markdown("\n".join(output_lines))
    output = output.replace("\n", newline)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(output, encoding="utf-8", newline="")
    print(f"OK    {source} -> {target}", flush=True)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("en"))
    parser.add_argument("--target", type=Path, default=Path("ro"))
    parser.add_argument("--api", default=API_URL)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--limit", type=int, default=0, help="Only translate first N files (0 = all)")
    args = parser.parse_args()

    if not args.source.is_dir():
        print(f"Source directory not found: {args.source}", file=sys.stderr)
        return 1

    files = sorted(args.source.rglob("*.md"))
    if args.limit:
        files = files[: args.limit]

    print(f"Translating {len(files)} markdown files: {args.source} -> {args.target}", flush=True)
    failures = 0
    for source in files:
        target = args.target / source.relative_to(args.source)
        try:
            translate_file(source, target, args.api, args.force)
        except Exception as exc:  # keep going; report at the end
            failures += 1
            print(f"FAIL  {source}: {exc}", file=sys.stderr, flush=True)

    print(f"Done: {len(files)} files, {failures} failures", flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
