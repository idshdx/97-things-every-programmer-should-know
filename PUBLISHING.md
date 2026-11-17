# Publishing the Romanian edition

The public site is the **Romanian-only** edition of *97 Things Every Programmer Should Know*,
built with mdBook and deployed to GitHub Pages with GitHub Actions.

## Architecture

| Layer | Choice | Why |
|---|---|---|
| Source | `en/`, `ro/` Markdown | Existing GitBook-style source, unchanged content |
| Renderer | mdBook (pinned `v0.5.4`) | Reads `SUMMARY.md` natively; search + responsive theme; static HTML |
| Build config | `book.toml` (`src = "ro"`) | Keeps the English tree out of the published site |
| CI | `.github/workflows/deploy-pages.yml` | Deterministic build, atomic deploy, one-click rollback |
| Hosting | GitHub Pages, source = **GitHub Actions** | Free, no separate account or DNS needed |

`ro/SUMMARY.md` uses mdBook list markers (`-`) instead of the original numbered GitBook
markers (`1.`); all link destinations are byte-identical to `en/SUMMARY.md`.

## Audiobook

Every Romanian chapter page embeds an HTML5 audio player directly below its title,
plus a plain Markdown fallback link, both pointing at that chapter's MP3:

| Piece | Location | Notes |
|---|---|---|
| Player markup | `ro/thing_XX/README.md` (below the `#` title) | inserted by `python tools/add_chapter_audio.py` (idempotent) |
| Published MP3s | `ro/audio/thing_XX_ro.mp3` (tracked, 97 files, ~151 MB) | inside the mdBook source tree, so `mdbook build` copies them verbatim to `book/audio/` |
| Generation output | `audio/` (git-ignored, ~1 GB WAV/TXT/staging MP3s) | written by `tools/make_audiobook_all.py` |

Markdown itself cannot play audio, so the block uses raw HTML
(`<audio controls preload="metadata">…</audio>`), which mdBook passes through
untouched; the relative path `../audio/thing_XX_ro.mp3` resolves from the built
page `book/thing_XX/index.html` (and equally from the Markdown source on GitHub
or legacy GitBook).

Regenerate and republish audio:

```bash
python tools/make_audiobook_all.py   # renders audio/thing_XX_ro.{wav,mp3}
cp audio/*.mp3 ro/audio/             # refresh the published copies
python tools/add_chapter_audio.py    # no-op if the players already exist
python tools/verify_translation.py   # also checks player + MP3 presence
```

The player block is stripped from the text before `verify_translation.py`
compares line/link parity against `en/`, so embedded players never count as
translation problems — while a missing player or MP3 fails the check.

## One-time GitHub setup

The Pages site is created with `build_type: workflow` (via the REST API or
**Settings → Pages → Build and deployment → Source: GitHub Actions**). No branch
selection is needed: the workflow deploys the built artifact.

```bash
gh api repos/idshdx/97-things-every-programmer-should-know/pages \
  -f build_type=workflow
```

## Local build and preview

mdBook must be on `PATH`:

```bash
# Download the pinned Linux/Windows binary from the release assets, then:
mdbook build          # writes book/
mdbook serve --open   # http://localhost:3000
```

Validate the translated tree before building:

```bash
python tools/verify_translation.py
```

Expected: `English files: 99`, `Romanian files: 99`, `Problems: 0`.

## Deploy

Every push to `master` runs the workflow: verify → build mdBook → upload artifact →
deploy to Pages. Manual deploy:

```bash
gh workflow run "Deploy Romanian book to GitHub Pages" --ref master
gh run watch
```

The public URL is reported by the `deploy` job as `steps.deployment.outputs.page_url`,
normally `https://idshdx.github.io/97-things-every-programmer-should-know/`.

## Rollback

GitHub Pages keeps prior deployments in the environment's deployment list. To roll back:

```bash
gh api repos/idshdx/97-things-every-programmer-should-know/deployments \
  --jq '.[0:5][] | [.id, .ref, .created_at] | @tsv'
# Redeploy a known-good commit:
git push origin <known-good-sha>:master
```

For a code-level rollback, revert the deploy commit and push:

```bash
git revert <sha> && git push origin HEAD:master
```

## Regenerating the translation

```bash
libretranslate --load-only en,ro --update-models   # terminal 1
python tools/translate_libre.py --force           # terminal 2
python tools/verify_translation.py
```

Re-run `mdbook build` afterwards to refresh `book/`.
