# Engineering: project status

Last updated: 2026-05-16.

## Phase

**Phase 1: production prose at scale.** In progress. Volumes I through V are drafted in full at first-draft density; Volume VI is partially drafted (Ch 1 through Ch 10 of 13); Volumes VII, VIII, IX, X, XI, and XII are drafted in full (19 of 19, 14 of 14, 19 of 19, 16 of 16, 13 of 13, and 14 of 14 chapters respectively). All 171 drafted chapters compile cleanly in `main.pdf`. The discipline guards (`make check`, `make audit-docs`, `make accidents`, `make exercise-counts`) report PASS across the current state.

Per-volume state:

- **Volume I (Quantity)** — 9 of 9 chapters at **Stage 5**. All carry Codex reviews at `docs/reviews/vol01-chNN-review.md` resolved with G fixes applied.
- **Volume II (Form)** — 18 of 18 chapters at **Stage 4** awaiting Codex review. Drafted 2026-04-29 in two parallel-agent passes (Ch 1-9, then Ch 10-18).
- **Volume III (Force)** — 13 of 13 chapters at **Stage 4** awaiting Codex review. Drafted on the `dev: vol03` commit.
- **Volume IV (Energy)** — 14 of 14 chapters at **Stage 4** awaiting Codex review. Drafted on the `dev: vol04` commit.
- **Volume V (Matter)** — 12 of 12 chapters at **Stage 4** awaiting Codex review. Drafted on the `dev: vol05` commit.
- **Volume VI (Life)** — 10 of 13 chapters at **Stage 4** awaiting Codex review. Ch 11 (Bioinformatics), Ch 12 (Biocompatibility and medical devices), and Ch 13 (Living engineering, the anatomical compiler) remain at Stage 1.
- **Volume VII (Information)** — 19 of 19 chapters at **Stage 4** awaiting Codex review. Drafted on the `dev: vol07` commit.
- **Volume VIII (Machines)** — 14 of 14 chapters at **Stage 4** awaiting Codex review. Drafted on the `dev: vol08` commit.
- **Volume IX (Systems)** — 19 of 19 chapters at **Stage 4** awaiting Codex review. Drafted on the `dev: vol09` commit.
- **Volume X (Failure)** — 16 of 16 chapters at **Stage 4** awaiting Codex review. Drafted in the current session; volume opener plus Chapters 1-16 all carry first-draft prose.
- **Volume XI (Design)** — 13 of 13 chapters at **Stage 4** awaiting Codex review. Drafted in the current session; volume opener plus Chapters 1-13 (including the design-studios chapter and the capstone) all carry first-draft prose. Chapter 13 (the capstone) carries the integrative project for the volume rather than exercises.
- **Volume XII (Civilization)** — 14 of 14 chapters at **Stage 4** awaiting Codex review. Drafted in the current session; volume opener plus Chapters 1-14 (including the political-economy chapter and the closing future-of-the-artificial chapter that closes the entire book) all carry first-draft prose. Chapter 14 (the book closer) carries the integrative personal-manifesto project rather than exercises.

Two lanes remain open:

- Continue forward into Volume VI Ch 11-13 prose (the remaining $3$ chapters at Stage 1).
- Codex review for Volumes II through XII (162 chapters awaiting review on the same three-role protocol that carried Volume I from Stage 4 to Stage 5).
- Volume I-XII production-density pass: figures, project artifacts, expanded solution sets, case-study expansions, code/data co-located with each chapter. Q57 (page density vs target) is the open question that gates whether this lane runs at all; with eleven full volumes plus Vol VI partial drafted at consistent ~10-31% of target density, the empirical case is now strong.

Previous phases:

- **Phase 0.7** (registry foundation and pilot prose). Complete 2026-04-29.
- **Phase 0.6** (curriculum expansion: 11 new chapters, 4 renames). Complete 2026-04-28.
- **Phase 0.5** (structural hardening). Complete 2026-04-28.
- **Phase 0** (scaffolding + outline). Complete 2026-04-26.

## At a glance

| Metric | Count |
| --- | --- |
| Volumes | 12 |
| Chapter shells | 174 |
| Per-volume dossiers | 12 |
| Per-chapter dossiers | 174 |
| `\chapmeta` blocks in chapter shells | 174 |
| Half-life: TBD remaining | 0 |
| `Project track: TBD` remaining | 3 (Vol VI Ch 11-13) |
| TODO markers in TeX | ~65 |
| Empty epigraphs in chapter shells | 4 |
| Section headings | ~1629 |
| Bibliography entries | 324 |
| Named-case registry entries | 36 |
| `acc:` keys cited in chapter prose | 38 |
| Research seeds on disk | 1 |
| Chapters with prose (Stage 4 or 5) | 171 |
| Vol I chapters at Stage 5 | 9 of 9 |
| Vols II-XII chapters at Stage 4 | 162 awaiting review |
| Chapters at Stage 1 | 3 |
| `main.pdf` page count (last build) | 3289 |
| Volume I page span | pp 1-328 (~328pp; target ~720) |
| Volume II page span | pp 329-? (Tier 1+2 except Ch 2 at first-draft; target ~1800) |
| Volume II page span | pp 221-710 (~490pp; target ~1800) |
| Volume III page span | pp 711-984 (~274pp; target ~1300) |
| Volume IV page span | pp 985-1218 (~234pp; target ~1400) |
| Volume V page span | pp 1219-1456 (~238pp; target ~1200) |
| Volume VI page span (partial) | pp 1457-1634 (~178pp; target ~1300) |
| Volume VII page span | pp 1635-1898 (~264pp; target ~1980) |
| Volume VIII page span | pp 1899-2240 (~342pp; target ~1610) |
| Volume IX page span | pp 2241-2416 (~176pp; target ~1850) |
| Volume X page span | pp 2417-2705 (~289pp; target ~1450) |
| Volume XI page span | pp 2706-2863 (~158pp; target ~1080) |

Bibliography breakdown by category prefix:

| Prefix | Count | Use |
| --- | --- | --- |
| `text:` | ~138 | textbooks, monographs, working handbooks |
| `hist:` | ~32 | historical and biographical primary/secondary sources |
| `paper:` | ~33 | peer-reviewed papers |
| `acc:` | 30 | accident investigation reports and the registry's primary keys |
| `web:` | ~13 | tertiary explainers and reference web content (non-load-bearing) |
| `std:` | ~15 | standards documents |
| `gen:` | ~8 | general references |
| `method:` | 5 | research-methods literature (replication, p-hacking, HARKing) |
| `data:` | 2 | datasets with provenance |
| `law:` | 2 | laws and regulations (incl.\ Montreal Protocol 1987) |

Run `make stats` for the live numbers.

## What is complete

- Twelve-volume LaTeX project skeleton (`main.tex`, `preamble.tex`, `eng-macros.sty`).
- Frontmatter prose: cover, title page, preface, how-to-use, notation. All in authorial "we" voice.
- 174 chapter shells with dossier-derived `\chapmeta` (half-life, archetypes, exercise target).
- 157 chapters with first-draft prose across Volumes I-XI (Vol VI partial).
- 12 per-volume research dossiers and 174 per-chapter dossiers under `docs/research/`.
- Cross-volume landscape document at `docs/research/landscape.md`.
- Editorial decisions log at `docs/editorial-decisions.md`. Open questions log at `docs/open-questions.md`.
- Project diagnostic at `docs/diagnostic.md` (2026-04-28 snapshot, preserved as a snapshot).
- Operational docs: `voice.md`, `citation-policy.md` (prefixes `std:`, `acc:`, `law:`, `hist:`, `text:`, `paper:`, `method:`, `data:`, `web:`, `gen:`), `case-study-template.md`, `reviewer-guide.md`, `review-prompt.md`, `release-checklist.md`, `research-pipeline.md`, `interludes.md`.
- Build pipeline: `make`, `make watch`, `make scaffolding`, `make outline`, `make strict`, `make check`, `make stats`, `make clean`, `make distclean`, `make audit-docs`, `make accidents`, `make exercise-counts`.
- A working PDF build at 2863 pages. Volume I prose complete and reviewed at first-draft density; Volumes II-V prose complete at first-draft density awaiting review; Volume VI 10 of 13 chapters drafted at first-draft density awaiting review; Volumes VII, VIII, IX, X, and XI prose complete at first-draft density awaiting review.
- Named-cases registry with 30 entries, schema-conformant, audited by `make accidents`.
- Research seeds lane at `docs/research/seeds/` with SCHEMA, README, and one seed on disk.
- Volume I review log: `docs/reviews/ch01-pilot-review.md` plus `docs/reviews/vol01-ch02-review.md` through `docs/reviews/vol01-ch09-review.md`, each with a `Resolved:` banner and integration record.
- Math operators in `eng-macros.sty`: linear-algebra (`\spn`, `\col`, `\nul`, `\rank`, `\sgn`, `\proj`), trace and diagonal (`\tr`, `\diag`), optimisation (`\argmin`, `\argmax`).

## What is queued

Active items from `open-questions.md`:

- **Q54 companion-note architecture**: spine vs companion-notes vs code repo vs data repo vs errata. Not yet decided. Becomes load-bearing if a production-density lane runs (figures, code, datasets all need a home).
- **Q55 per-chapter project track (20 chapters remaining)**: Volumes I-V are complete; Volume VI is partially complete (Ch 1-10 settled, Ch 11-13 still TBD); Volumes VII, VIII, IX, X, and XI are complete; Volume XII still carries `Project track: TBD`. Editorial pass needed per volume as that volume comes into prose drafting.
- **Q57 page density vs target**: Ten full volumes plus partial Vol VI are now drafted at consistent first-draft density (~10-31\% of target across the eleven volumes). Volume I 220 of 720; Vol II 490 of 1800; Vol III 274 of 1300; Vol IV 234 of 1400; Vol V 238 of 1200; Vol VI (partial) 178 of 1300; Vol VII 264 of 1980; Vol VIII 342 of 1610; Vol IX 176 of 1850; Vol X 289 of 1450; Vol XI 158 of 1080 ($\approx$ 15\%). The pattern is consistent: first-draft prose lands at roughly one-tenth to one-third of the planned page budget. The two readings (chapters dense vs artifacts missing) are now testable against eleven volumes of evidence.

Settled but kept on the wider planning radar:

- **Q51 reader-path model** (core / standard / mastery): settled 2026-04-28. Implemented through `\pathtag{}` on every section across the Vol I chapters and propagated through subsequent volumes' drafting.
- **Q52 pilot chapter**: settled and surpassed; all nine Vol I chapters carried through Stage 5.
- **Q53 license confirmation**: settled 2026-04-28.
- **Q56 named-cases registry**: settled 2026-04-29; registry now holds 30 entries. Vol X drafting added 7 entries: Boeing 737 MAX MCAS (2018-2019), Tenerife airport disaster (1977), Eastern Air Lines Flight 401 (1972), American Eagle Flight 4184 (Roselawn ATR-72 icing, 1994), Comair Flight 5191 (2006), Genoa Morandi Bridge (2018), Flint water crisis (2014-2019). All `acc:` keys cited in prose resolve to a registry entry; every named accident in prose carries at least one of its registry's citation keys.

Queued from `interludes.md`:

- III → IV revision (Force into Energy) acknowledging the Force/Energy/Matter unity. Status: queued, not applied.
- IV → V revision (Energy into Matter) closing the unity. Status: queued, not applied.

## Risks

The diagnostic identified three top risks (`docs/diagnostic.md`). Phase 0.5 mitigated the first; Phase 0.7 and the nine Vol I reviews mitigated the third in part; Vols II-VI prose passes scaled the bibliography from 86 to 210 entries and the registry from 12 to 20 entries without breaking citation discipline. The second remains.

1. **Source-of-truth drift between generator and dossiers.** **Mitigated.** The generator reads dossiers as the canonical source; `make check` enforces `\chapmeta` presence on every chapter shell.
2. **Scale honesty for the reader.** **Open.** Q57 is the live form; nine volumes of evidence now sit under the question.
3. **Verification (citation discipline, reproducible examples, table provenance).** **Substantially mitigated for Volume I; carried forward into Vols II-IX as first-draft discipline awaiting Codex review.** Bibliography grew from 86 to 261 entries across Vols II-IX drafting. The Stage 4 review pass for Vols II-IX is the discipline carrier for the rest of the project.

## Build state

The current build runs cleanly:

```
make distclean && make
```

Produces `main.pdf` at 2519 pages. `make check`, `make audit-docs`, `make accidents`, and `make exercise-counts` all report `PASS`. `make stats` reports the at-a-glance counts above.

## Operational notes

- `main.pdf` is gitignored; build locally.
- Scaffolding regeneration via `make scaffolding` (uses uv).
- The dossiers under `docs/research/` are the canonical per-volume editorial source. The generator reads them. Edit dossiers there; do not edit chapter shells directly until prose work begins on that chapter.
- File slugs (`volumes/01-quantity/`, `_volume.tex`, `chNN-slug/chapter.tex`, `\label{vol01:ch01}`) are stable and not renamed.
- For repository paths in chapter prose, use the `\repopath{}` macro (a `\path{}` wrapper) rather than `\texttt{}`, which overflows the margin on long paths.
- Reviews live at `docs/reviews/`. The `Resolved: YYYY-MM-DD` banner at the top of a review file is the canonical signal that all G fixes have been applied; do not write that banner unless every G fix has actually been addressed.

## What good progress looks like

1. Commission Codex reviews for Volume II Ch 1 onward, one chapter at a time, applying the same three-role protocol that carried Vol I from Stage 4 to Stage 5.
2. Finish Vol VI prose (Ch 11 Bioinformatics, Ch 12 Biocompatibility and medical devices, Ch 13 Living engineering / anatomical compiler).
3. Start Volume X prose (Failure) once Vol VI is complete. The bridge from Vol IX (Systems) is direct: every chapter in Vol IX has a failure section; Vol X expands on the systematic engineering of failure.
4. Settle Q57 with nine volumes of evidence behind the decision. The two readings imply different forward sequences (forward to Vol X vs back to Vols I-IX production-density pass).
5. Settle Q54 (companion-note architecture) before any production-density lane runs.
6. Continue closing the 49 remaining Q55 project-track decisions, one volume at a time as that volume comes into prose drafting.
7. Apply or formally defer the queued III-IV and IV-V interlude revisions.

Eight-and-a-half volumes of first-draft prose are now on disk at consistent density. The pipeline has been exercised at scale (parallel-agent passes for Vol II ran cleanly; single-thread main-thread passes for Vols III through IX all ran cleanly). The next gating decisions are review throughput and page-density target, not whether the project can produce defensible chapters.
