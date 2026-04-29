# Engineering: project status

Last updated: 2026-04-29.

## Phase

**Phase 0.7: registry foundation and pilot prose.** Complete on 2026-04-29. Delivered:

- Volume I prose: all nine chapters at Stage 5 (Ch 1 "Why we measure", Ch 2 "Units and dimensions", Ch 3 "Calibration and traceability", Ch 4 "Error and uncertainty", Ch 5 "Sensors and instruments", Ch 6 "Time, frequency, and signals", Ch 7 "Length, area, volume, mass", Ch 8 "Statistics for engineers", Ch 9 "The discipline of estimation"). Each chapter carries a Codex review at `docs/reviews/vol01-ch<NN>-review.md` resolved with all G fixes applied (~280 specific fixes across the volume). Volume I opener prose written; archetype list pins six Volume I archetypes (scaling, balance, failure, uncertainty, interface, transport).
- Named-cases registry: schema (`docs/research/accidents/SCHEMA.md`); fifteen entries on disk (every accident cited in any Volume I chapter plus the original twelve foundation entries); index (`docs/research/accidents/README.md`); citation-policy update with closest-equivalent clause; reviewer-guide registry-check requirement (items 24-27); `make accidents` target with both cite-resolution and prose-name scan.
- Citation policy expanded with a `method:` prefix for research-methods literature (replication studies, p-hacking, HARKing, forking paths). Five method entries added during Ch 8 review (Simmons/Nelson/Simonsohn 2011, Kerr 1998, Gelman/Loken, Open Science Collaboration 2015, Errington 2021).
- `\repopath{}` macro added to `preamble.tex` to render long repository paths in prose without margin overflow.
- Audit tooling: `make audit-docs` (stale references), `make accidents` (named-case discipline), `make exercise-counts` (per-chapter exercise count vs chapmeta target). All pass across the current state.

**Phase 1: production prose at scale.** In progress as of 2026-04-29. The forward-motion lane has begun: Volume II opener prose written, and Volume II Chapters 1-9 drafted on 2026-04-29 by nine parallel agents with editor-led pre-flight (opener prose, Q55-vol02-ch01 through Q55-vol02-ch09 settled in `editorial-decisions.md`, four math-text bib entries added, `\spn`/`\col`/`\rank`/`\nul`/`\sgn`/`\proj` operators promoted to `eng-macros.sty`) and integration. Vol II Ch 1-9 sit at ~238 pages of first-draft prose (TOC pp. 229-466) against an ~880-page target for the first nine chapters; same first-draft density Vol I landed at. All nine are at Stage 4 awaiting Codex review.

Two lanes remain open:

- Continue forward: Volume II Chapters 10-18 (eigenvalues, multivariable calculus, PDEs, probability, statistical inference, optimisation, numerical methods, discrete mathematics, mathematical modelling) or Volume III opener.
- Volume I production-density pass: figures, project artifacts, expanded solution sets, case-study expansions, code/data co-located with each chapter. Volume I currently runs ~220 pages of first-draft prose against a ~720-page target. Q57 (page density vs. target) is the open question that gates whether this lane runs at all.

Phase 0.6 (curriculum expansion). Complete on 2026-04-28. Closed eleven substantive curriculum gaps (acoustics, mass transfer, plasma physics, bioinformatics, quantum computing, power electronics, MEMS, project management, user research, defence systems, space infrastructure) plus four naming/register fixes and the explicit stigmergy hook in Vol IX.

Previous phase: **Phase 0.5** (structural hardening). Complete on 2026-04-28.
Earlier phase: **Phase 0** (scaffolding + outline). Complete on 2026-04-26.

## At a glance

| Metric | Count |
| --- | --- |
| Volumes | 12 |
| Chapter shells | 174 |
| Per-volume dossiers | 12 |
| `\chapmeta` blocks in chapter shells | 174 |
| Half-life: TBD remaining | 0 |
| TODO markers in TeX | ~1660 |
| Empty epigraphs in chapter shells | 156 (9 Vol I + 9 Vol II written) |
| Section headings in chapter shells | ~1640 |
| Bibliography entries | 90 |
| Named-case registry entries | 15 |
| Vol I chapters at Stage 5 | 9 of 9 |
| Vol II chapters at Stage 4 | 9 of 18 (Ch 1-9 awaiting review) |
| `main.pdf` page count (last build) | ~928 |
| Volume I current page span | ~220 (target ~720) |
| Volume II Ch 1-9 current page span | ~238 (target ~880) |

Run `make stats` for the live numbers.

## What is complete

- Twelve-volume LaTeX project skeleton (`main.tex`, `preamble.tex`, `eng-macros.sty`).
- Frontmatter prose: cover, title page, preface, how-to-use, notation. All in authorial "we" voice.
- 174 chapter shells, generated from `scripts/generate_scaffolding.py`, with dossier-derived metadata in a `\chapmeta` block (half-life, archetypes, exercise target).
- 12 per-volume research dossiers under `docs/research/`, each with chapter-level scope, archetype, project, exercise count.
- Cross-volume landscape document at `docs/research/landscape.md`. Per-volume header dossiers at `docs/research/<NN>-<slug>/_volume.md`. Per-chapter dossiers at `docs/research/<NN>-<slug>/ch<MM>-<slug>.md` (174 total, mirroring the `volumes/` tree).
- Editorial decisions log at `docs/editorial-decisions.md` (Q1-Q50 plus Q55-pilot through Q55-ch09 settled).
- Voice guide at `docs/voice.md`.
- Open questions log at `docs/open-questions.md` (Q54, Q55-remaining, Q57 active; Q51, Q52, Q53, Q56 settled).
- Project diagnostic at `docs/diagnostic.md` (Codex, 2026-04-28).
- Interludes catalogue at `docs/interludes.md` (queued III-IV and IV-V revisions).
- Citation policy at `docs/citation-policy.md` with prefixes `std:`, `acc:`, `law:`, `hist:`, `text:`, `paper:`, `method:`, `data:`, `web:`, `gen:`.
- Case-study template at `docs/case-study-template.md`.
- Reviewer guide at `docs/reviewer-guide.md`.
- Reviewer prompt at `docs/review-prompt.md` (used to commission all nine Vol I reviews).
- Release checklist at `docs/release-checklist.md`.
- Research pipeline at `docs/research-pipeline.md`.
- Build pipeline: `make`, `make watch`, `make scaffolding`, `make outline`, `make strict`, `make check`, `make stats`, `make clean`, `make distclean`, `make audit-docs`, `make accidents`, `make exercise-counts`.
- A working PDF build, currently around 928 pages. Volume I prose is complete and reviewed at first-draft density (~220 pages of 720 target). Volume II Chapters 1-9 are drafted at first-draft density (~238 pages of 880 target for that arc) and await Codex review.
- Named-cases registry with 15 entries, schema-conformant, audited by `make accidents`.
- Volume I review log: `docs/reviews/ch01-pilot-review.md` plus `docs/reviews/vol01-ch02-review.md` through `docs/reviews/vol01-ch09-review.md`. Each review carries a `Resolved: 2026-04-NN` banner and the integration record.
- Post-expansion drift cleanup (2026-04-28): all eight expanded volumes' arc paragraphs and editorial-question chapter numbers refreshed to match the 174-chapter sequence; status, research-pipeline, landscape, generator comments, Makefile `outline`, and appD-reading-list paths updated; README anchor numbering fixed; new `make audit-docs` target enforces the cleanup.

## What is queued

Active items from `open-questions.md`:

- **Q54 companion-note architecture**: spine vs companion-notes vs code repo vs data repo vs errata: not yet decided. Becomes load-bearing if the Vol I production-density lane runs (figures, code, datasets all need a home).
- **Q55 per-chapter project track (165 chapters remaining)**: Volume I is complete (Q55-pilot, Q55-ch02 through Q55-ch09 all settled). The remaining 165 chapters across Volumes II-XII still carry `Project track: TBD` in their `\chapmeta`. Editorial pass needed, ideally per volume.
- **Q57 page density vs target**: Volume I currently runs ~220 pages against a ~720-page target. Two readings: chapters are dense at first-draft density, target was loose; OR artifacts (figures, project deliverables, solutions, expanded case studies) are absent and the gap is real backlog. Settling this gates whether Phase 1 starts with Volume II prose or with a Volume I production-density pass.

Settled but kept on the wider planning radar:

- **Q51 reader-path model** (core / standard / mastery): settled 2026-04-28. Implemented through `\pathtag{}` macro on every section across the nine Vol I chapters.
- **Q52 pilot chapter** (Volume I Chapter 1): settled and surpassed; all nine Vol I chapters carried through Stage 5.
- **Q53 license confirmation** (CC BY-NC-SA + MIT/Apache 2.0): settled 2026-04-28.
- **Q56 named-cases registry**: settled 2026-04-29; registry exists with 15 entries, schema, README, citation-policy update, reviewer-guide checks, and `make accidents` audit.

Queued from `interludes.md`:

- III → IV revision (Force into Energy) acknowledging the Force/Energy/Matter unity. Status: queued, not applied.
- IV → V revision (Energy into Matter) closing the unity. Status: queued, not applied.

## Risks

The diagnostic identified three top risks (`docs/diagnostic.md`). Phase 0.5 mitigated the first; Phase 0.7 and the nine Vol I reviews mitigated the third in part. The second remains.

1. **Source-of-truth drift between generator and dossiers.** **Mitigated.** The generator now reads dossiers as the canonical source of per-chapter metadata; `make check` enforces that every chapter shell carries a `\chapmeta` block.
2. **Scale honesty for the reader.** **Open.** Q51 is settled at the section-tag level; the broader question of whether a 720-page Vol I is the actual deliverable (Q57) is now the live form of this risk.
3. **Verification (citation discipline, reproducible examples, table provenance).** **Substantially mitigated for Vol I.** Nine chapters carried through Codex review with every load-bearing claim either cited at the right tier or rewritten to remove the claim. Bibliography grew from 34 to 86 entries. The same discipline must scale to Volumes II-XII.

## Build state

The current build runs cleanly:

```
make distclean && make
```

Produces `main.pdf` at approximately 928 pages. `make check`, `make audit-docs`, `make accidents`, and `make exercise-counts` all report `PASS`. `make stats` reports the at-a-glance counts above.

## Operational notes

- `main.pdf` is gitignored; build locally.
- Scaffolding regeneration via `make scaffolding` (uses uv).
- The dossiers under `docs/research/` are the canonical per-volume editorial source. The generator reads them. Edit dossiers there; do not edit chapter shells directly until prose work begins.
- File slugs (`volumes/01-quantity/`, `_volume.tex`, `chNN-slug/chapter.tex`, `\label{vol01:ch01}`) are stable and not renamed.
- For repository paths in chapter prose, use the `\repopath{}` macro (a `\path{}` wrapper) rather than `\texttt{}`, which overflows the margin on long paths.
- Reviews live at `docs/reviews/`. The `Resolved: YYYY-MM-DD` banner at the top of a review file is the canonical signal that all G fixes have been applied; do not write that banner unless every G fix has actually been addressed.

## What good progress looks like

A serious-pace next pass would:

1. Settle Q57 (page density vs target). The two readings imply different Phase 1 sequences.
2. If Q57 favours production-density first: pick one Vol I chapter and carry it from ~22pp to ~80pp by adding figures, expanded worked examples, project artifacts, full solution sets, and inline diagrams. Treat it as the production-density pilot.
3. If Q57 favours forward motion first: write the Volume II opener and Volume II Chapter 1 prose, run Codex review on it, then make the same go/no-go on Vol II density.
4. Settle Q54 (companion-note architecture) before either lane runs. Both lanes need a clear home for code, datasets, and project artifacts.
5. Begin closing the 165 remaining Q55 project-track decisions, ideally one volume at a time as that volume comes into prose drafting.
6. Apply or formally defer the queued III-IV and IV-V interlude revisions.

The pilot has been carried, surpassed, and reviewed end-to-end nine times. The discipline scales. The next gating decision is page density, not whether the project can produce a defensible chapter.
