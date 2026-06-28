# Engineering: project status

Last updated: 2026-06-05.

## Phase

**Phase 1: production prose at scale.** In progress. **All 174 chapters are at Stage 4 or later** as of 2026-06-03. Volume I is at Stage 5 (reviewed and resolved) and has been carried through a Tier 3 second pass to roughly full target density; Volumes II through XII are at Stage 4 (first-draft to Tier-1+2 density) awaiting Codex review. All drafted chapters compile in `main.pdf`. The discipline guards (`make check`, `make audit-docs`, `make accidents`, `make exercise-counts`) report PASS across the current state.

Per-volume state:

- **Volume I (Quantity)** — 9 of 9 chapters at **Stage 5**, carried to a **Tier 3 second pass** (2026-05-31 / 06-02). All carry Codex reviews at `docs/reviews/vol01-chNN-review.md` resolved with G fixes applied. The most advanced volume in the book; ~674 pp against a ~720 pp target.
- **Volume II (Form)** — 18 of 18 chapters at **Stage 4** awaiting Codex review. **Tier 3 first AND second pass complete across ALL 18 chapters** (2026-06-05/06). First pass (Waves 1-5) deepened every chapter to ~55-65% of target; the second pass (Waves A-E, gap-prioritized) added a multi-page end-to-end CASE STUDY to most chapters plus more worked examples, figures, and mastery boxes. Representative case studies: geodetic levelling-network adjustment (Ch 9), machine-availability Markov chain (Ch 10), steel-plate quench (Ch 12), battery Coulomb-counting (Ch 6), Markowitz portfolio + truss sizing (Ch 15), error-budget cantilever (Ch 16), fatigue S-N inference (Ch 14), RLC + van der Pol + shooting method (Ch 7), load-strength reliability (Ch 13), M/M/c staffing under random demand (Ch 18), Hamming(7,4) codes (Ch 17), Machin's-formula pi to 10 digits (Ch 4), Welford running variance (Ch 1), machined-plate inertia (Ch 11), coaxial-cable field/capacitance (Ch 8), single-phase AC power-factor network (Ch 3), load-cell characterisation (Ch 2). A **third pass** (Waves F-I, 2026-06-06) then added a SECOND distinct multi-page case study to most chapters plus advanced worked examples and mastery boxes (e.g. Reed-Solomon over GF(16), symmetrical-components fault analysis, repairable-system CTMC availability, Peng-Robinson globalized Newton, FFT/spectral methods + convection-diffusion MMS, SIR + Robertson stiff kinetics, bridge structural-health PCA, FEM direct-stiffness truss + Leontief, network-contagion + feedback-control modelling, control-volume drag/lift). Ch 1 (~92%) and Ch 11 (~87%) were left after the second pass; the other 16 chapters got the third pass. Vol II now **~82% of dossier target (~1506 of ~1830 pp)** and compiles with **zero errors in the build**. Exercise counts held exactly throughout all three passes; no new bibliography entries required (all citations reuse existing keys); Ch 16 wired in the Vancouver Stock Exchange case using the existing registry entry. One more focused pass on the largest chapters (Ch 9, 10, 12) would reach Vol I's ~94% density.
- **Volume III (Force)** — 13 of 13 chapters at **Stage 4** awaiting Codex review. **Tier 1+2 baseline pass complete across ALL 13 chapters** (2026-06-24, three parallel-agent waves). Each chapter started as text-plus-exercises only (no figures, code, data, or solutions) and gained: a full `\paragraph{Solution sketch.}` inside every exercise (446 solutions across the volume), 6-10 TikZ/pgfplots figures (113 new figure files), 3-6 code files, 2-4 datasets, expanded worked-examples sections, estimation blocks where missing, and 1-2 mastery boxes per chapter. Then a **Tier 3 deepening pass across ALL 13 chapters** (2026-06-24, three more parallel-agent waves of 4-5) added to every chapter a substantial multi-page END-TO-END CASE STUDY (numbers carried through), 3-4 more multi-step worked examples, 2-4 more figures, and another mastery box. Representative case studies: lifting-padeye stress + Goodman fatigue check (Ch 3), rotating-machinery FFT diagnosis + isolation-mount design (Ch 6), steel floor-beam design to deflection/LTB checks (Ch 8), air-receiver pressure-vessel sizing (Ch 9), two-vehicle accident reconstruction (Ch 4), industrial noise-control enclosure to OSHA dose (Ch 7), penstock water-hammer surge + surge-tank sizing (Ch 11), pipeline pump sizing with NPSH margin (Ch 12), supersonic rocket-nozzle design chamber-to-plume (Ch 13), jib-crane load-path FBD (Ch 1), Howe roof-truss full analysis (Ch 2), Castigliano frame deflection + drop-impact factor (Ch 5), gravity-dam stability (Ch 10). A **second Tier 3 pass across ALL 13 chapters** (2026-06-24, three more parallel-agent waves) then added a SECOND, distinct multi-page case study to every chapter plus 2-3 more worked examples, 2-3 more figures, and another mastery box each. Representative second case studies: rotating-flywheel disk stress + Lame thick-cylinder shrink-fit (Ch 3), centrally-loaded strut Euler/Johnson design (Ch 8), ring-stiffened external-pressure vacuum vessel (Ch 9), Venturi flow-metering station (Ch 11), quarter-car suspension tuning (Ch 6), auditorium reverberation design (Ch 7), hydrodynamic journal bearing (Ch 12), Mach-3 supersonic inlet (Ch 13), multi-leg sling lifting plan (Ch 1), parabolic suspension cable + retaining-wall stability (Ch 2), two-stage launch Delta-v budget (Ch 4), Rayleigh-Ritz column buckling + von Mises-truss snap-through (Ch 5), loaded-pontoon metacentric stability (Ch 10). A **third Tier 3 pass across ALL 13 chapters** (2026-06-27/28, three more parallel-agent waves) then added a third (or fourth) distinct multi-page case study to every chapter plus 3-4 more worked examples / long-form derivations, 2-4 more figures, and another mastery box each. Representative third case studies: fatigue-crack-growth Paris-law life + leak-before-break (Ch 3), welded plate-girder design (Ch 8), flat-bottom storage-tank shell courses (Ch 9), finite-wing lifting-line lift + induced drag (Ch 11), seismic base-isolation / TMD (Ch 6), reactive muffler / sonar (Ch 7), vehicle aero drag + journal-bearing companion (Ch 12), re-entry blunt-body aerothermodynamics (Ch 13), tower-crane tipping stability (Ch 1), 3D signpost-mast wind reactions (Ch 2), Hohmann orbital transfer (Ch 4), crashworthiness crumple-zone energy absorption (Ch 5), canal lock mitre-gate (Ch 10). Vol III went from ~274 pp to **~834 pp (~64% of the ~1300 pp dossier target)** and now carries **250 figures** (zero at session start). Exercise counts held exactly throughout; no new bibliography entries required (all citations reuse existing keys); the de Havilland Comet (1954) failure case was wired into Ch 9 using the existing registry entry. Across the three passes, several agent-authored figures shipped with a missing `\end{axis}` or a referenced-but-not-`\input` figure and were repaired; per-wave verification now includes an axis/tikz balance scan AND an orphan-figure scan. The third pass ran during a period of API instability (classifier-unavailable / connection-closed errors); affected chapters were re-run cleanly, and partial broken/orphan figures from killed agents were deleted or rebuilt. Next: a fourth Tier 3 pass to close from ~64% toward Vol I/II density (~80-94%), or commission Codex reviews (Stage 4 -> 5).
- **Volume IV (Energy)** — 14 of 14 chapters at **Stage 4** awaiting Codex review.
- **Volume V (Matter)** — 12 of 12 chapters at **Stage 4** awaiting Codex review.
- **Volume VI (Life)** — 13 of 13 chapters at **Stage 4** awaiting Codex review. Ch 11-13 drafted from Stage 1 in Wave 1 (2026-06-03); Ch 1-5 expanded to a Tier 3 baseline in Wave 2 (2026-06-03).
- **Volume VII (Information)** — 19 of 19 chapters at **Stage 4** awaiting Codex review.
- **Volume VIII (Machines)** — 14 of 14 chapters at **Stage 4** awaiting Codex review.
- **Volume IX (Systems)** — 19 of 19 chapters at **Stage 4** awaiting Codex review.
- **Volume X (Failure)** — 16 of 16 chapters at **Stage 4** awaiting Codex review.
- **Volume XI (Design)** — 13 of 13 chapters at **Stage 4** awaiting Codex review. Ch 13 (the capstone) carries the integrative project for the volume rather than exercises.
- **Volume XII (Civilization)** — 14 of 14 chapters at **Stage 4** awaiting Codex review. Ch 14 (the book closer) carries the integrative personal-manifesto project rather than exercises.

Open lanes:

- **Codex review for Volumes II through XII** (165 chapters awaiting review on the same three-role protocol that carried Volume I from Stage 4 to Stage 5).
- **Tier 3 production-density pass** per volume: figures, project artifacts, expanded solution sets, case-study expansions, code/data co-located with each chapter. Vol I is the worked example; Vol II Wave 1 has begun the same pass. Q57 (page density vs target) is settled in practice: first-draft prose lands at ~10-44% of the planned page budget and the density pass closes the gap.

Previous phases:

- **Phase 0.7** (registry foundation and pilot prose). Complete 2026-04-29.
- **Phase 0.6** (curriculum expansion: 11 new chapters, 4 renames). Complete 2026-04-28.
- **Phase 0.5** (structural hardening). Complete 2026-04-28.
- **Phase 0** (scaffolding + outline). Complete 2026-04-26.

## At a glance

Run `make stats` for live numbers. Snapshot (2026-06-05):

| Metric | Count |
| --- | --- |
| Volumes | 12 |
| Chapter shells | 174 |
| Per-volume dossiers | 12 |
| Per-chapter dossiers | 176 |
| `\chapmeta` blocks in chapter shells | 174+ |
| Half-life: TBD remaining | 0 |
| `Project track: TBD` remaining | 0 |
| TODO markers in TeX | 34 |
| Empty epigraphs in chapter shells | 0 |
| Section headings | ~1637 |
| Bibliography entries | 1286 |
| Named-case registry entries | 47 |
| `acc:` keys cited in chapter prose | 49 |
| Research seeds on disk | 1 |
| Chapters at Stage 4 or later | 174 of 174 |
| Vol I chapters at Stage 5 | 9 of 9 |
| Vols II-XII chapters at Stage 4 | 165 awaiting review |
| Chapters at Stage 1 | 0 |
| `main.pdf` page count (last build) | 5287 |

Per-volume page spans against target (figures approximate; from the per-chapter ledger in `CLAUDE.md`):

| Volume | Approx. pp | Target | % | Stage |
| --- | --- | --- | --- | --- |
| I Quantity | ~674 | ~720 | ~94% | 5 (Tier 3 2nd pass) |
| II Form | ~1506 | ~1830 | ~82% | 4 (Tier 3 third pass: 16 of 18 ch) |
| III Force | ~834 | ~1300 | ~64% | 4 (Tier 1+2 baseline + three Tier 3 passes: all 13 ch) |
| IV Energy | ~234 | ~1400 | ~17% | 4 |
| V Matter | ~238 | ~1200 | ~20% | 4 |
| VI Life | ~370 | ~1200 | ~31% | 4 |
| VII Information | ~264 | ~1980 | ~13% | 4 |
| VIII Machines | ~342 | ~1610 | ~21% | 4 |
| IX Systems | ~176 | ~1850 | ~10% | 4 |
| X Failure | ~289 | ~1450 | ~20% | 4 |
| XI Design | ~158 | ~1080 | ~15% | 4 |
| XII Civilization | ~123 | ~1320 | ~9% | 4 |

Bibliography breakdown by category prefix (live):

| Prefix | Count | Use |
| --- | --- | --- |
| `paper:` | 506 | peer-reviewed papers |
| `text:` | 323 | textbooks, monographs, working handbooks |
| `web:` | 164 | tertiary explainers and reference web content (non-load-bearing) |
| `hist:` | 71 | historical and biographical primary/secondary sources |
| `std:` | 70 | standards documents |
| `acc:` | 47 | accident investigation reports and the registry's primary keys |
| `data:` | 28 | datasets with provenance |
| `method:` | 16 | research-methods literature (replication, p-hacking, HARKing) |
| `law:` | 13 | laws and regulations |
| `gen:` | 8 | general references |

## What is complete

- Twelve-volume LaTeX project skeleton (`main.tex`, `preamble.tex`, `eng-macros.sty`).
- Frontmatter prose: cover, title page, preface, how-to-use, notation. All in authorial "we" voice.
- 174 chapter shells with dossier-derived `\chapmeta` (half-life, archetypes, project track, exercise target).
- First-draft (or denser) prose for all 174 chapters across all twelve volumes.
- 12 per-volume research dossiers and 176 per-chapter dossiers under `docs/research/`.
- Cross-volume landscape document at `docs/research/landscape.md`.
- Editorial decisions log at `docs/editorial-decisions.md`. Open questions log at `docs/open-questions.md`.
- Project diagnostic at `docs/diagnostic.md` (2026-04-28 snapshot, preserved as a snapshot).
- Operational docs: `voice.md`, `citation-policy.md` (prefixes `std:`, `acc:`, `law:`, `hist:`, `text:`, `paper:`, `method:`, `data:`, `web:`, `gen:`), `case-study-template.md`, `reviewer-guide.md`, `review-prompt.md`, `release-checklist.md`, `research-pipeline.md`, `interludes.md`.
- Build pipeline: `make`, `make watch`, `make scaffolding`, `make outline`, `make strict`, `make check`, `make stats`, `make clean`, `make distclean`, `make audit-docs`, `make accidents`, `make exercise-counts`.
- A working PDF build at 4019 pages. Volume I prose complete, reviewed, and carried to Tier 3 density; Volumes II-XII complete at first-draft to Tier-1+2 density awaiting review.
- Named-cases registry with 47 entries, schema-conformant, audited by `make accidents`.
- Research seeds lane at `docs/research/seeds/` with SCHEMA, README, and one seed on disk.
- Volume I review log: `docs/reviews/ch01-pilot-review.md` plus `docs/reviews/vol01-ch02-review.md` through `docs/reviews/vol01-ch09-review.md`, each with a `Resolved:` banner and integration record.
- `docs/vol01-tier3-plan.md` records the Tier 3 plan that drove the Vol I second pass.
- Math operators in `eng-macros.sty`: linear-algebra (`\spn`, `\col`, `\nul`, `\rank`, `\sgn`, `\proj`), trace and diagonal (`\tr`, `\diag`), optimisation (`\argmin`, `\argmax`).

## What is queued

Active items from `open-questions.md`:

- **Q54 companion-note architecture**: spine vs companion-notes vs code repo vs data repo vs errata. Not yet decided. Load-bearing now that a production-density lane is running (figures, code, datasets all need a home).
- **Q57 page density vs target**: settled in practice. Twelve volumes of evidence show first-draft prose landing at ~10-44% of the planned page budget; the Tier 3 density pass (worked first on Vol I, now begun on Vol II) closes the gap.

Settled but kept on the wider planning radar:

- **Q51 reader-path model** (core / standard / mastery): settled 2026-04-28. Implemented through `\pathtag{}` on every section.
- **Q52 pilot chapter**: settled and surpassed; all nine Vol I chapters carried through Stage 5 and a Tier 3 second pass.
- **Q53 license confirmation**: settled 2026-04-28.
- **Q55 per-chapter project track**: fully settled across all 174 chapters as of 2026-06-03.
- **Q56 named-cases registry**: settled 2026-04-29; registry now holds 47 entries. All `acc:` keys cited in prose resolve to a registry entry; every named accident in prose carries at least one of its registry's citation keys.

Queued from `interludes.md`:

- III → IV revision (Force into Energy) acknowledging the Force/Energy/Matter unity. Status: queued, not applied.
- IV → V revision (Energy into Matter) closing the unity. Status: queued, not applied.

## Risks

The diagnostic identified three top risks (`docs/diagnostic.md`).

1. **Source-of-truth drift between generator and dossiers.** **Mitigated.** The generator reads dossiers as the canonical source; `make check` enforces `\chapmeta` presence on every chapter shell.
2. **Scale honesty for the reader.** **Substantially addressed.** Q57 has twelve volumes of evidence; the Tier 3 density pass is the mechanism that takes first-draft density to target.
3. **Verification (citation discipline, reproducible examples, table provenance).** **Substantially mitigated for Volume I; carried forward into Vols II-XII as first-draft discipline awaiting Codex review.** Bibliography grew to 1286 entries across the twelve-volume drafting. The Stage 4 review pass for Vols II-XII is the discipline carrier for the rest of the project.

## Build state

```
make distclean && make
```

Produces `main.pdf` at 5287 pages (latexmk exit 2: 66 recoverable Vol VI Ch 10-13 errors remain, see below; PDF builds despite them). `make check`, `make audit-docs`, `make accidents`, and `make exercise-counts` all report `PASS`. `make stats` reports the at-a-glance counts above. The build requires the enlarged TeX `main_memory` described below; without it the run aborts in Vol IV with `TeX capacity exceeded`.

Always build with `make distclean && make` (a fresh build). Incremental `latexmk` runs intermittently corrupt `main.bbl` (biber emits a runaway-argument bbl, symptom: "Paragraph ended before \name was complete" / "Loading a class or package in a group" at `\begin{document}`, no PDF). A `make distclean` clears the bad `.bbl`/`.bcf` (and any `*-SAVE-ERROR` files) and regenerates the bibliography cleanly.

Resolved build issues (2026-06-05): the Vol II Ch 11 PGF negative-sqrt figure error is fixed (`max(0,...)` clamp); the Vol VI Ch 6 cardiovascular figure path syntax is fixed; Vol VI Ch 9 was truncated (unclosed `exercise`, seven never-created figure `\input`s) and is now structurally valid (figures commented with a TODO for the Vol VI pass); Vol VI Ch 10 `engorange` color added to the preamble and the reserved `cells` TikZ key renamed.

TeX main-memory ceiling (2026-06-24): once Vol III gained 113 TikZ/pgfplots figures the whole-book build began failing with `! TeX capacity exceeded, sorry [main memory size=5000000]` partway through (Vol IV Ch 10), because pdftex's default arena is fixed at format-dump time and the accumulating per-document tables (labels, hyperref destinations, biblatex data) crossed it. Fix is **machine-local, no sudo, no repo change**: a user-level `texmf.cnf` at `$TEXMFCONFIG/web2c/texmf.cnf` (`~/Library/texlive/2025/texmf-config/web2c/texmf.cnf` on this machine) sets `main_memory = 12000000`, then a user-local `pdflatex` format is rebuilt so the larger arena is baked in:

```
# write ~/Library/texlive/2025/texmf-config/web2c/texmf.cnf containing: main_memory = 12000000
TEXMFCNF="$(kpsewhich -var-value TEXMFCONFIG)/web2c:" fmtutil-user --byfmt pdflatex
```

`main_memory` is read only at format-dump time, so the `TEXMFCNF` override is needed for that one command; afterwards normal `make` runs use the baked-in 12M format automatically (the user `pdflatex.fmt` in TEXMFVAR precedes the system tree). Do not also raise `pool_size`/`save_size` in the same file: the combination tripped `Ouch---my internal constants have been clobbered!---case 14` and the dump failed; `main_memory` alone dumps cleanly. To revert, delete the line and rerun the `fmtutil-user` command. 12M clears the current ~4955 pp book with headroom; raise further (re-dump) if a future volume overflows again.

Known residual (deferred to the Vol VI production pass): ~66 recoverable "Missing $" / "Undefined control sequence" errors in Vol VI Ch 10-13 prose, caused by markdown-style backtick code spans with raw underscores (e.g. a bare `monod_growth_fit.py`). They do not stop the build (the PDF reaches 4205 pp) and are confined to Vol VI; the fix is to convert those spans to `\texttt{...}` / `\repopath{}` with escaped underscores when Vol VI is drafted to Tier 3.

## Operational notes

- `main.pdf` is gitignored; build locally.
- Scaffolding regeneration via `make scaffolding` (uses uv).
- The dossiers under `docs/research/` are the canonical per-volume editorial source. The generator reads them. Edit dossiers there; do not edit chapter shells directly for metadata changes.
- File slugs (`volumes/01-quantity/`, `_volume.tex`, `chNN-slug/chapter.tex`, `\label{vol01:ch01}`) are stable and not renamed.
- For repository paths in chapter prose, use the `\repopath{}` macro (a `\path{}` wrapper) rather than `\texttt{}`, which overflows the margin on long paths.
- Reviews live at `docs/reviews/`. The `Resolved: YYYY-MM-DD` banner at the top of a review file is the canonical signal that all G fixes have been applied; do not write that banner unless every G fix has actually been addressed.

## What good progress looks like

1. Bring Volume II to the Vol I standard: Tier 3 density pass across the remaining 15 chapters, and/or commission Codex reviews chapter by chapter (Stage 4 → Stage 5).
2. Fix the Vol II Ch 11 PGF figure error so full builds return a clean exit code.
3. Continue the Tier 3 density pass volume by volume (III onward), one chapter at a time in the main thread.
4. Settle Q54 (companion-note architecture) before the production-density lane scales further.
5. Apply or formally defer the queued III-IV and IV-V interlude revisions.

All twelve volumes of first-draft prose are on disk. The pipeline has been exercised at scale through Stage 4, and Volume I demonstrates the full Stage 4 → Stage 5 → Tier 3 path. The gating decisions now are review throughput and how aggressively the density pass runs, not whether the project can produce defensible chapters.
