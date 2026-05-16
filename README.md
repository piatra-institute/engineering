# Engineering

A ~20,000-page sequential formation text for serious adult learners, structured as twelve volumes covering quantity, form, force, energy, matter, life, information, machines, systems, failure, design, and civilization. The thesis:

> Engineering is the discipline by which measured reality becomes reliable intervention under constraint, failure, scale, and responsibility.

Engineering is not applied science. Engineering is disciplined intervention.

A Piatra . Institute project. Phases 0 and 0.5 complete: scaffolding, full per-volume outlines, dossier-driven chapter metadata, structural-check tooling, and editorial policy docs are in place. Chapter prose has not started; the pilot chapter (Volume I Chapter 1) is the named next move.

## Structure

```
engineering/
├── main.tex                     Master document; \part{} per volume; \input{} per chapter
├── preamble.tex                 LaTeX preamble (memoir, biblatex, tikz, theorem environments)
├── eng-macros.sty               Cross-domain notation
├── Makefile                     Build (latexmk + uv)
├── pyproject.toml               Python tooling (uv)
├── frontmatter/                 Cover, title page, preface, how-to-use, notation
├── volumes/                     12 volumes × N chapters; each chapter is its own folder
│   ├── 01-quantity/             Volume I: Quantity (9 chapters)
│   │   ├── _volume.tex          volume opener
│   │   ├── ch01-why-we-measure/
│   │   │   └── chapter.tex      (figures/, code/, data/ accumulate here as prose lands)
│   │   └── ...
│   ├── 02-form/                 Volume II: Form (18 chapters)
│   ├── 03-force/                Volume III: Force (13 chapters)
│   ├── 04-energy/               Volume IV: Energy (14 chapters)
│   ├── 05-matter/               Volume V: Matter (12 chapters)
│   ├── 06-life/                 Volume VI: Life (13 chapters)
│   ├── 07-information/          Volume VII: Information (19 chapters)
│   ├── 08-machines/             Volume VIII: Machines (14 chapters)
│   ├── 09-systems/              Volume IX: Systems (19 chapters)
│   ├── 10-failure/              Volume X: Failure (16 chapters)
│   ├── 11-design/               Volume XI: Design (13 chapters)
│   └── 12-civilization/         Volume XII: Civilization (14 chapters)
├── appendices/                  Master appendices (glossary, units, prerequisites, reading list, archetypes)
├── bibliography/                BibLaTeX references
├── docs/                        Editorial planning (not part of the book)
│   ├── editorial-decisions.md   50 settled editorial decisions, anchored by the thesis
│   ├── open-questions.md        Active open questions (Q51 onward)
│   ├── status.md                Current phase, counts, what's complete, what's queued
│   ├── voice.md                 House voice rules and ban-list
│   ├── citation-policy.md       BibLaTeX category prefixes, citation tiers, accident rules
│   ├── case-study-template.md   Seven-section accident case-study standard
│   ├── reviewer-guide.md        Three-role reviewer protocol per chapter
│   ├── release-checklist.md     Structural / build / citation / voice gates for release
│   ├── research-pipeline.md     Six-stage outline-to-released pipeline
│   ├── interludes.md            Current and queued revisions of the volume-to-volume bridges
│   ├── diagnostic.md            Project diagnostic (2026-04-28; Codex)
│   └── research/                Per-volume + per-chapter dossiers and cross-volume landscape
│       ├── landscape.md         Cross-volume landscape, archetype index, page budget
│       └── 01-quantity/         Through 12-civilization/
│           ├── _volume.md       Volume header, scope, arc, project, bridges, reading list
│           └── chNN-slug.md     One per chapter (174 total): sub-sections, archetype, project, exercises
└── scripts/
    └── generate_scaffolding.py  uv-runnable scaffolding generator (reads dossiers)
```

`main.pdf` is built locally and not tracked by git (see `.gitignore`). `SCRATCH.md` is reserved for personal working notes that should not be tracked.

## Building the PDF

`main.pdf` is not committed; you build it from source. Requires a TeX Live distribution with `latexmk`, `xelatex`/`pdflatex`, `biber`, and `makeindex`.

```bash
make           # build main.pdf (the first build runs ~30-60 seconds)
make watch     # auto-rebuild on file change
make strict    # halt-on-error build (CI-style verification)
make check     # structural invariants (every chapter has chapter+label+chapmeta)
make stats     # counts of volumes, chapters, TODOs, sections, bibliography entries
make clean     # remove auxiliary files
make distclean # remove main.pdf and rebuild trackers (full fresh rebuild next time)
```

The build produces `main.pdf`, currently 491 pages of structural content (cover + frontmatter + 12 volumes × 174 chapters with sub-section TOC entries + appendices + bibliography stub).

## Regenerating chapter shells

The 174 chapter files under `volumes/*/*/chapter.tex` are generated from `scripts/generate_scaffolding.py`. The script is the source of truth for chapter slugs, titles, and sub-section structure; the per-chapter dossiers under `docs/research/<NN>-<slug>/ch<MM>-<slug>.md` are the source of truth for chapter metadata (half-life, archetypes, project, exercise count). The generator reads the dossiers at runtime.

```bash
make scaffolding         # invokes uv run scripts/generate_scaffolding.py
# or, equivalently:
uv run scripts/generate_scaffolding.py
```

`uv` is the project's standard Python runner. The generator script carries PEP 723 inline metadata; no virtual environment management is required.

Each chapter shell carries a `\chapmeta{...}` block at the top with: half-life category, archetypes invoked, exercise target, project track. Editing dossiers and re-running `make scaffolding` propagates the change to the chapter shells.

## The documents that anchor the project

When in doubt, read these in order:

1. `docs/editorial-decisions.md` — the fifty settled editorial decisions, with the thesis pinned at the top.
2. `docs/status.md` — current phase, counts, what's complete, what's queued.
3. `docs/research/landscape.md` — cross-volume landscape, archetype index, page-budget table.
4. `docs/research/<NN>-<slug>/_volume.md` — twelve per-volume header dossiers (scope, arc, bridges, reading list).
5. `docs/research/<NN>-<slug>/ch<MM>-<slug>.md` — 174 per-chapter dossiers, one per chapter, mirroring the `volumes/` tree.
6. `docs/diagnostic.md` — project diagnostic (2026-04-28).
7. `docs/voice.md`, `docs/citation-policy.md`, `docs/case-study-template.md`, `docs/reviewer-guide.md`, `docs/review-prompt.md`, `docs/research-pipeline.md`, `docs/release-checklist.md` — operational policy for the prose phase.
8. `docs/open-questions.md` — Q51 onwards: active open questions.
9. `docs/interludes.md` — current and queued revisions for the eleven volume-to-volume bridges in `main.tex`.

## House conventions

- **No em dashes** in prose (settled in editorial decisions, applied across all source files).
- **Authorial "we"** voice (settled question 21).
- **Working-engineer depth** for the science volumes (settled question 9).
- **Wide sense of engineering** (settled question 6).
- **Failure section in every chapter**, named accidents allowed and encouraged (settled questions 29-31).
- **Estimation environment in every chapter** (settled question 20).
- **Half-life tags** on chapters and sections (settled question 43); chapter-level tags now real, section-level still TBD.

See `docs/editorial-decisions.md` for the full settlement record and `docs/voice.md` for the operational voice rules.

## Status

- Phase 0: scaffolding + outline. **Complete** (2026-04-26). All 12 volumes, full TOC, compiles locally to a structural PDF (later expanded in Phase 0.6).
- Phase 0.5: structural hardening (post-diagnostic). **Complete** (2026-04-28). Chapter shells now carry `\chapmeta` blocks with dossier-derived half-life, archetypes, project, and exercise count; `make check`, `make stats`, `make strict` added; voice / citation / case-study / reviewer / release / pipeline policies written; bibliography reorganised by source category.
- Phase 0.6: curriculum expansion. **Complete** (2026-04-28). Eleven new chapters added to close substantive gaps (acoustics, mass transfer, plasma physics, bioinformatics, quantum computing, power electronics, MEMS, project management, user research, defence systems, space infrastructure). Four chapter renames for register and naming consistency. Vol IX Ch 12 sub-section expanded with stigmergy. Net: 163 → 174 chapters, ~17.2K → ~18.4K planned pages, ~491-page structural PDF.
- Phase 0.7: registry foundation and pilot prose. **Complete** (2026-04-29). Volume I prose drafted across all nine chapters and reviewed individually; named-cases registry stood up with schema, index, and `make accidents` audit; `method:` citation prefix introduced; `make audit-docs` and `make exercise-counts` added.
- Phase 1: production prose at scale. **In progress** (as of 2026-05-16). Volumes I through V are drafted in full at first-draft density; Volume VI is partially drafted (Ch 1-10 of 13); Volumes VII, VIII, and IX are drafted in full (19 of 19, 14 of 14, and 19 of 19). Volume I is at Stage 5 (reviewed and resolved); Volumes II-IX are at Stage 4 awaiting Codex review. Current build: 2519-page PDF, 128 chapters with prose, 261 bibliography entries, 23 named-case registry entries. All discipline guards (`make check`, `make audit-docs`, `make accidents`, `make exercise-counts`) report PASS.

For the live state, run `make stats` or read `docs/status.md`.
