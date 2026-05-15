# Engineering: project status

Last updated: 2026-05-15.

## Phase

**Phase 1: production prose at scale.** In progress. Volumes I through V are drafted in full at first-draft density; Volume VI is partially drafted (Ch 1 through Ch 10 of 13). All 76 drafted chapters compile cleanly in `main.pdf`. The discipline guards (`make check`, `make audit-docs`, `make accidents`, `make exercise-counts`) report PASS across the current state.

Per-volume state:

- **Volume I (Quantity)** — 9 of 9 chapters at **Stage 5**. All carry Codex reviews at `docs/reviews/vol01-chNN-review.md` resolved with G fixes applied.
- **Volume II (Form)** — 18 of 18 chapters at **Stage 4** awaiting Codex review. Drafted 2026-04-29 in two parallel-agent passes (Ch 1-9, then Ch 10-18).
- **Volume III (Force)** — 13 of 13 chapters at **Stage 4** awaiting Codex review. Drafted on the `dev: vol03` commit.
- **Volume IV (Energy)** — 14 of 14 chapters at **Stage 4** awaiting Codex review. Drafted on the `dev: vol04` commit.
- **Volume V (Matter)** — 12 of 12 chapters at **Stage 4** awaiting Codex review. Drafted on the `dev: vol05` commit.
- **Volume VI (Life)** — 10 of 13 chapters at **Stage 4** awaiting Codex review. Ch 11 (Bioinformatics), Ch 12 (Biocompatibility and medical devices), and Ch 13 (Living engineering, the anatomical compiler) remain at Stage 1.
- **Volumes VII through XII** — 95 chapters at **Stage 1** (scaffolding shells with dossier-derived metadata; no prose).

Two lanes remain open:

- Continue forward into Volume VI Ch 11-13 and Volume VII prose.
- Codex review for Volumes II through VI (67 chapters awaiting review on the same three-role protocol that carried Volume I from Stage 4 to Stage 5).
- Volume I-V production-density pass: figures, project artifacts, expanded solution sets, case-study expansions, code/data co-located with each chapter. Q57 (page density vs target) is the open question that gates whether this lane runs at all; with five full volumes drafted at the same ~22-30pp/chapter density, the empirical case is now strong.

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
| `Project track: TBD` remaining | 98 (Vol VI Ch 11-13 plus all of Vols VII-XII) |
| TODO markers in TeX | ~1055 |
| Empty epigraphs in chapter shells | 99 |
| Section headings | ~1653 |
| Bibliography entries | 210 |
| Named-case registry entries | 20 |
| `acc:` keys cited in chapter prose | 21 |
| Research seeds on disk | 1 |
| Chapters with prose (Stage 4 or 5) | 76 |
| Vol I chapters at Stage 5 | 9 of 9 |
| Vols II-VI chapters at Stage 4 | 67 awaiting review |
| Chapters at Stage 1 | 98 |
| `main.pdf` page count (last build) | 1972 |
| Volume I page span | pp 1-220 (~220pp; target ~720) |
| Volume II page span | pp 221-710 (~490pp; target ~1800) |
| Volume III page span | pp 711-984 (~274pp; target ~1300) |
| Volume IV page span | pp 985-1218 (~234pp; target ~1400) |
| Volume V page span | pp 1219-1456 (~238pp; target ~1200) |
| Volume VI page span (partial) | pp 1457-1634 (~178pp; target ~1300) |

Bibliography breakdown by category prefix:

| Prefix | Count | Use |
| --- | --- | --- |
| `text:` | 105 | textbooks, monographs, working handbooks |
| `hist:` | 27 | historical and biographical primary/secondary sources |
| `acc:` | 21 | accident investigation reports and the registry's primary keys |
| `paper:` | 18 | peer-reviewed papers |
| `web:` | 12 | tertiary explainers and reference web content (non-load-bearing) |
| `std:` | 11 | standards documents |
| `gen:` | 8 | general references |
| `method:` | 5 | research-methods literature (replication, p-hacking, HARKing) |
| `data:` | 2 | datasets with provenance |
| `law:` | 1 | laws and regulations |

Run `make stats` for the live numbers.

## What is complete

- Twelve-volume LaTeX project skeleton (`main.tex`, `preamble.tex`, `eng-macros.sty`).
- Frontmatter prose: cover, title page, preface, how-to-use, notation. All in authorial "we" voice.
- 174 chapter shells with dossier-derived `\chapmeta` (half-life, archetypes, exercise target).
- 76 chapters with first-draft prose across Volumes I-VI.
- 12 per-volume research dossiers and 174 per-chapter dossiers under `docs/research/`.
- Cross-volume landscape document at `docs/research/landscape.md`.
- Editorial decisions log at `docs/editorial-decisions.md`. Open questions log at `docs/open-questions.md`.
- Project diagnostic at `docs/diagnostic.md` (2026-04-28 snapshot, preserved as a snapshot).
- Operational docs: `voice.md`, `citation-policy.md` (prefixes `std:`, `acc:`, `law:`, `hist:`, `text:`, `paper:`, `method:`, `data:`, `web:`, `gen:`), `case-study-template.md`, `reviewer-guide.md`, `review-prompt.md`, `release-checklist.md`, `research-pipeline.md`, `interludes.md`.
- Build pipeline: `make`, `make watch`, `make scaffolding`, `make outline`, `make strict`, `make check`, `make stats`, `make clean`, `make distclean`, `make audit-docs`, `make accidents`, `make exercise-counts`.
- A working PDF build at 1972 pages. Volume I prose complete and reviewed at first-draft density; Volumes II-V prose complete at first-draft density awaiting review; Volume VI 10 of 13 chapters drafted at first-draft density awaiting review.
- Named-cases registry with 20 entries, schema-conformant, audited by `make accidents`.
- Research seeds lane at `docs/research/seeds/` with SCHEMA, README, and one seed on disk.
- Volume I review log: `docs/reviews/ch01-pilot-review.md` plus `docs/reviews/vol01-ch02-review.md` through `docs/reviews/vol01-ch09-review.md`, each with a `Resolved:` banner and integration record.
- Math operators in `eng-macros.sty`: linear-algebra (`\spn`, `\col`, `\nul`, `\rank`, `\sgn`, `\proj`), trace and diagonal (`\tr`, `\diag`), optimisation (`\argmin`, `\argmax`).

## What is queued

Active items from `open-questions.md`:

- **Q54 companion-note architecture**: spine vs companion-notes vs code repo vs data repo vs errata. Not yet decided. Becomes load-bearing if a production-density lane runs (figures, code, datasets all need a home).
- **Q55 per-chapter project track (98 chapters remaining)**: Volumes I-V are complete; Volume VI is partially complete (Ch 1-10 settled, Ch 11-13 still TBD); Volumes VII-XII still carry `Project track: TBD`. Editorial pass needed per volume as that volume comes into prose drafting.
- **Q57 page density vs target**: Five full volumes are now drafted at the same ~22-30pp/chapter density Volume I landed at. Volume I 220 of 720; Vol II 490 of 1800; Vol III 274 of 1300; Vol IV 234 of 1400; Vol V 238 of 1200; Vol VI (partial) 178 of 1300. The pattern across five-and-a-half volumes is consistent: first-draft prose lands at roughly one-third to one-fifth of the planned page budget. The two readings (chapters dense vs artifacts missing) are now testable against six volumes of evidence rather than one.

Settled but kept on the wider planning radar:

- **Q51 reader-path model** (core / standard / mastery): settled 2026-04-28. Implemented through `\pathtag{}` on every section across the Vol I chapters and propagated through subsequent volumes' drafting.
- **Q52 pilot chapter**: settled and surpassed; all nine Vol I chapters carried through Stage 5.
- **Q53 license confirmation**: settled 2026-04-28.
- **Q56 named-cases registry**: settled 2026-04-29; registry now holds 20 entries, all `acc:` keys cited in prose resolve to a registry entry, and every named accident in prose carries at least one of its registry's citation keys.

Queued from `interludes.md`:

- III → IV revision (Force into Energy) acknowledging the Force/Energy/Matter unity. Status: queued, not applied.
- IV → V revision (Energy into Matter) closing the unity. Status: queued, not applied.

## Risks

The diagnostic identified three top risks (`docs/diagnostic.md`). Phase 0.5 mitigated the first; Phase 0.7 and the nine Vol I reviews mitigated the third in part; Vols II-VI prose passes scaled the bibliography from 86 to 210 entries and the registry from 12 to 20 entries without breaking citation discipline. The second remains.

1. **Source-of-truth drift between generator and dossiers.** **Mitigated.** The generator reads dossiers as the canonical source; `make check` enforces `\chapmeta` presence on every chapter shell.
2. **Scale honesty for the reader.** **Open.** Q57 is the live form; six volumes of evidence now sit under the question.
3. **Verification (citation discipline, reproducible examples, table provenance).** **Substantially mitigated for Volume I; carried forward into Vols II-VI as first-draft discipline awaiting Codex review.** Bibliography grew from 86 to 210 entries across Vols II-VI drafting. The Stage 4 review pass for Vols II-VI is the discipline carrier for the rest of the project.

## Build state

The current build runs cleanly:

```
make distclean && make
```

Produces `main.pdf` at 1972 pages. `make check`, `make audit-docs`, `make accidents`, and `make exercise-counts` all report `PASS`. `make stats` reports the at-a-glance counts above.

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
3. Start Volume VII prose (Information) once Vol VI is complete. Vol VII is 19 chapters and is the largest single volume; pre-flight will likely add discrete-math, complexity, and ML operators to `eng-macros.sty` analogous to the Vol II expansion.
4. Settle Q57 with six volumes of evidence behind the decision. The two readings imply different forward sequences (forward to Vol VII vs back to Vol I production-density pass).
5. Settle Q54 (companion-note architecture) before any production-density lane runs.
6. Continue closing the 98 remaining Q55 project-track decisions, one volume at a time as that volume comes into prose drafting.
7. Apply or formally defer the queued III-IV and IV-V interlude revisions.

Five-and-a-half volumes of first-draft prose are now on disk at consistent density. The pipeline has been exercised at scale (parallel-agent passes for Vol II ran cleanly; single-agent passes for Vols III, IV, V, and the Vol VI partial ran cleanly). The next gating decisions are review throughput and page-density target, not whether the project can produce defensible chapters.
