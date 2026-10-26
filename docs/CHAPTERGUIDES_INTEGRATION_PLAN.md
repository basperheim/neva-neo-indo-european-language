# Future integration: Neva on ChapterGuides

**Planning document only — no feature, endpoint, menu link or deployment is being made now.**

Companion plan: https://github.com/basperheim/chapterguides/blob/master/notes/NEVA_INTEGRATION_PLAN.md

## Goal

Add a public **Neva (Artlang)** feature to https://chapterguides.com, with vocabulary lookup, case declension, verb conjugation, IPA pronunciation, and later carefully limited translation. Publish an article explaining its PIE inspiration, the invented innovations, and a link to the tool.

## Confirmed ChapterGuides deployment architecture (2026-10-26)

- UI: Astro 5 with Node standalone SSR, `astro/src/components/Header.astro` navigation, existing `/lexigraph` feature.
- Backend: Go/Gin in `go-server/main.go`, `go-server/internal/api`, native Alpine OpenRC service on loopback port 9292.
- Astro SSR is a **separate native Node process** on loopback port 4317.
- Nginx dispatches browser/site and API traffic. **Existing README notes potential `/api/` prefix proxy mismatch; verify before shipping new routes.**
- Production Docker Compose manages **PostgreSQL only**, not the Go and Astro apps. A Neva lookup feature should not need a new database or production Python process.

## Source-of-truth and versioning

This Neva repo owns language rules, etymological evidence, dictionary entries, and Python reference CLI (`scripts/neva.py`). ChapterGuides does **not** become a competing language-spec repo.

Recommended development workflow:
1. Obtain a **pinned Neva commit or tagged release**.
2. Validate/export a normalized CSV or JSON snapshot of headwords and grammatical tables. Record the Neva revision and SHA-256 in the generated metadata.
3. Vendor that snapshot in a Go package **inside the ChapterGuides go-server module**; use Go standard-library `encoding/csv` or `encoding/json` and (optionally) `//go:embed`. An embed directive cannot reach into the other checkout from a different Go module.
4. Parse once at startup into in-memory indexes; no request-time GitHub fetch, Python subprocess, Ollama, or external API.
5. Port only stable inflection and IPA rules to Go, with **cross-language test fixtures** generated from the Python reference CLI and reviewed for expected behavior. Do not infer irregular stems from headword spelling.
6. Script the export and use a single source of truth to prevent drift.

## Proposed API (future, not implemented)

Prefix in Go: `/neva` (unless the confirmed public Nginx route architecture requires another prefix). Public URL may be `/api/neva/...` once the existing proxy rules are verified.

- `GET /neva/words?q=water&lang=en&limit=20`: bounded dictionary search, returning gender and provenance.
- `GET /neva/words/:headword`: full entry, source anchor, historical status.
- `GET /neva/nouns/:headword/decline`: nominative/accusative/genitive/dative, both numbers, declared gender and any documented irregular stems.
- `GET /neva/verbs/:infinitive/conjugate`: six persons for present, past and future.
- `POST /neva/pronounce`: constrained Neva text → IPA, not generated audio.
- `POST /neva/translate`: **defer**; only build once the grammar and semantic lexicon support a clearly bounded translation subset. Return explicit unknown/ambiguous diagnostics, never hallucinated full-sentence translations.
- `GET /neva/version`: lexicon revision and rules version.

Bound query length, response size and requests per IP. Avoid PostgreSQL until there is a concrete need for user submissions or more sophisticated indexed search. Reuse the existing API response conventions and middleware where reasonable.

## Proposed ChapterGuides UI

- Add a responsive `Neva (Artlang)` menu item beside Lexigraph in `astro/src/components/Header.astro`, only at feature-launch time.
- New `astro/src/pages/neva.astro` with an interactive client component; reuse the site's existing responsive themes and accessible search conventions.
- Provide dictionary search by English/Neva, noun gender/case tables, verb tables, clear `PIE-inspired` vs `Neva coinage` provenance and confidence.
- Show IPA with predictable stress. Audio is **phase 2**: prefer pre-generated/hosted clips or client-side speech if quality suffices; no neural synthesizer process on the $5 server by default.
- Write an original article in the existing Astro blogs content collection, following `astro/src/content.config.ts` and the current publishing/sitemap workflow. Link both the tool and this source repo.

## Stages / acceptance

1. **Language stabilization first**: settle masculine plural, feminine dative and noun ablaut; decide vowel sequence constraints.
2. **Lexicon data contract**: schema checks, deterministic export, provenance and source confidence.
3. **Go library**: no DB or remote dependency, exact fixture parity for declensions, strong verbs and IPA.
4. **Gin API**: tests for bad inputs, rate limits, cacheability and deploy routing.
5. **Astro UI and navigation**: keyboard/mobile tests, meaningful error/empty states.
6. **Editorial article and rollout**: metadata, canonical link, page performance, staging checks and production deploy separately.

The feature should stay small, portable and cheap to operate. No new service or hosted AI API is necessary for the initial tools.
