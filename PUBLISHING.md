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
