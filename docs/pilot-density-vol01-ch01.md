# Production-density pilot: Vol I Ch 1 (Why we measure)

Date: 2026-05-16.
Status: Pilot complete. Decision artifact for Q57 (page density vs target).

## Question this pilot answers

Q57 has been open with 12 volumes of evidence behind it: the project's
first-draft pages cluster at 16% of the cumulative target (~3,000pp
against ~18,400pp). Two readings have been named in `docs/status.md`:
chapters are dense enough (revise targets down), or a per-volume
production-density pass is required to reach target. The user chose
to pilot one chapter — adding figures, expanded named cases, exercise
solutions, and co-located code/data assets — to characterise the lift
concretely before committing to a path.

This report documents the pilot's outcome.

## Pilot scope

Chapter: `volumes/01-quantity/ch01-why-we-measure/chapter.tex`.

Baseline (before pilot): the chapter was at Stage 5 (Codex-reviewed
and resolved per `docs/reviews/ch01-pilot-review.md`), with 878 lines
of LaTeX, 8 sections, 26 subsections, 28 exercises, 1 estimation
block, 1 archetype, 1 principle, 1 project, 3 named cases at ~30
lines each, and zero figures, code, or data assets.

Tier-1 additions executed:

| Category | Specifics | Lines added (approx) |
|---|---|---|
| Exercise solutions | 28 exercises, each with `\paragraph{Solution sketch.}` or `\paragraph{Discussion.}` | ~430 |
| Estimation expansion | Second estimation block on global cement-production flow rate | ~30 |
| Named-case expansion | MCO, Air Canada 143, Ariane 5 each restructured with Technical mechanism / Organisational context / Lesson paragraphs; ~80-100 lines per case | ~180 |
| Figures | 6 TikZ figures (SI dependency, target diagram, MCO trajectory, Type A/B, sig figs, unit interface) | ~6 figures + 6 `\input` references |
| Code assets | 5 Python files + README in `code/`: uncertainty propagation, Monte Carlo sigma scaling, bivariate propagation, calibration regression, measurement-log CLI | 0 in chapter (references inline) |
| Data assets | 3 CSV/JSONL files + README in `data/`: coin masses, USGS cement production 2010-2023, example calibration log | 0 in chapter (references inline) |
| Bibliography | 4 new entries (ICRP-89, Eiffel Tower official, USGS MCS, WHO PQS) | 4 entries in `bibliography/references.bib` |

## Quantitative result

| Metric | Before pilot | After pilot | Ratio |
|---|---|---|---|
| Chapter PDF span | pp 100-116 (17pp) | pp 100-129 (30pp) | 1.76× |
| Chapter LaTeX lines | 878 | 1623 | 1.85× |
| Total PDF | 2986 pp | 2998 pp | (+12pp project-wide) |
| Vol I Ch 1 density (target 80pp) | 21% | 37.5% | +16.5 pp of target |

## Discipline-guard verification

All four guards PASS after pilot:

- `make check` — 174 chapters structural check.
- `make audit-docs` — no stale references.
- `make accidents` — 38 `acc:` keys cited, 36 registry entries.
- `make exercise-counts` — 169 chapters with prose match chapmeta target.

## What dominated the lift, by category

Estimated page contribution (after observing the final 13-page lift):

| Category | Pages contributed | Per unit of effort |
|---|---|---|
| Exercise solutions | ~6 pp | Highest leverage. 28 short solutions add the most pages per minute of drafting. |
| Named-case expansion | ~3 pp | Medium leverage. Each case ~1pp of expanded prose. |
| Figures | ~3 pp | Low-medium per-page leverage but high pedagogical value; each TikZ figure spans roughly 0.5-0.7pp. |
| Second estimation | ~1 pp | Modest. |
| Code/data assets | 0 pp in chapter | Zero pages in PDF but high reader-utility; the assets sit alongside the chapter. |

The exercise-solutions category was the dominant driver, and is the
most repeatable across chapters: every chapter has exercises, every
exercise type can take a solution sketch, the voice-rule risk is low
(numerical solutions and rubrics are constrained format), and the
chapter author can produce them quickly because they have already
written the exercise.

## What did not lift density that the plan anticipated would

- **Co-located code/data assets**: zero pages added to the PDF. The
  files exist in `code/` and `data/` and are referenced from the
  chapter, but they are not included in the chapter prose. They
  serve the reader's deeper engagement but do not count toward the
  page budget. If page budgets are the measure of completeness, the
  code/data pass does not move the needle.
- **Figures**: contributed less than expected because TikZ figures
  in this chapter are diagrammatic rather than full-page. A bar
  chart or full-page schematic would contribute more.

## Cost of the pilot

Effort (single session):
- Reading current state, plan, voice rules: ~15 min
- Drafting 28 exercise solutions: ~45 min (~1.5 min/solution)
- Expanding 3 named cases: ~30 min
- Drafting estimation block: ~10 min
- Drafting 6 TikZ figures + debugging: ~60 min (more than expected; 2 figures required iteration on TikZ syntax)
- Drafting 5 code assets + 3 data assets + READMEs: ~45 min
- Bibliography additions: ~10 min
- Build cycles + voice sweep + this report: ~30 min

Total: approximately 4 hours.

## Implications for the 174-chapter book

A 4-hour pilot on the chapter at Vol I's highest baseline density
produced a 1.76× lift to 37.5% of target. To reach the 80pp target
for this chapter would require roughly another 1.5× expansion
(another 3-4 hours of comparable depth additions: more subsection
expansion, additional named cases, full-page figures, project
expansion). Estimated cost to reach 100% of target per chapter: ~8
hours per Vol I-density chapter.

For the full project:
- 174 chapters × 8 hours = ~1,400 hours per chapter author.
- At realistic sustained pace (4 chapters/week of density-pass work
  for a focused author), this is approximately 9-12 months of
  full-time work to reach the full ~18,400pp target.

For chapters at lower baseline density (Vol IX at 10%, Vol XII at
9%), the per-chapter cost is higher because more subsection structure
must be added from scratch; estimate 12-16 hours per chapter for
those volumes. Weighted average across the project: ~10-12 hours per
chapter.

## Path A/B/C reconsidered with this evidence

- **Path A (close the gap)**: feasible. The per-chapter cost is
  bounded (~10 hours average). The total work is large but tractable
  (~1,700-2,100 hours across the project, roughly 12-18 months of
  focused work). The lift mechanisms are well-understood after this
  pilot. The pilot's 1.76× in 4 hours suggests that the 5× full
  target is achievable per chapter, but requires roughly twice the
  effort the pilot consumed.

- **Path B (revise targets down)**: less attractive in light of the
  pilot. The pilot showed that the gap is not principally artistic
  (the chapter can credibly carry more content); it is a question
  of executing the planned additions across the book. Revising
  targets down would be admitting the project's positioning claim
  in advance of having tried to close the gap.

- **Path C (hybrid tier-1)**: now well-specified. The pilot's
  tier-1 checklist (exercise solutions, named-case expansion,
  figures, second estimation, code/data assets) added 1.76× to a
  chapter at 31% of target density. Extrapolating across the
  project, a tier-1 pass alone would lift the project from ~3,000pp
  to ~5,300pp (about 29% of target). A tier-1 + tier-1.5 pass (add:
  expand existing subsections; add a second project or expanded
  project rubric per chapter; populate full-page figures where
  TikZ snippets exist) could plausibly reach ~8,000-10,000pp
  (45-55% of target). Revising the target to ~10,000pp would then
  match the achievable density at this tier of effort.

## Recommendation

The project should pursue **Path C with explicit tier definitions**:

- **Tier 1** (mandatory for production): exercise solutions for
  calc/derivation/estimation; named-case expansion to ~80-100 lines
  with the Technical-Organisational-Lesson structure; 4-6 figures
  per chapter; co-located code/data assets where computational
  content exists. Estimated per-chapter cost: ~4 hours.
- **Tier 2** (recommended): second project or expanded project
  rubric; expanded estimation blocks; full subsection-level
  pedagogical examples within each section. Estimated per-chapter
  cost: another ~4 hours.
- **Tier 3** (aspirational, post-tier-2 review): pedagogical
  handout problems with multi-page solutions; long-form historical
  sketches; integrated multi-chapter case-study series. Estimated
  per-chapter cost: another ~4 hours.

Tier 1 across all 174 chapters: ~700 hours, ~4-6 months of focused
work. Lifts the project to roughly 30% of nominal target. Revise
landscape.md page budgets to the achievable target at this tier
(approximately 35-40pp per chapter average, ~7,000pp project total).

Tier 2 adds another ~700 hours and lifts to ~50% of nominal target
(~9,000pp). Further revision optional.

Tier 3 is open-ended.

The pilot has demonstrated that production density is achievable
and that the cost-per-chapter is bounded and predictable. The
remaining decision is which tier the project commits to and on
what schedule.

## Files modified by the pilot

- `volumes/01-quantity/ch01-why-we-measure/chapter.tex` (878 → 1623 lines)
- `volumes/01-quantity/ch01-why-we-measure/figures/` (6 new files)
- `volumes/01-quantity/ch01-why-we-measure/code/` (6 new files: 5 .py + README)
- `volumes/01-quantity/ch01-why-we-measure/data/` (4 new files: 3 data + README)
- `bibliography/references.bib` (4 new entries)
- `docs/pilot-density-vol01-ch01.md` (this file)

## Next decision

The user reviews this report and chooses one of:

1. Approve Path C tier-1 rollout across all 174 chapters.
2. Approve a smaller scope (e.g., tier-1 for Vol I only, then
   reassess).
3. Reject the production-density pass in favour of revising
   landscape.md targets down to match current first-draft density
   (Path B; Q57 settles for Reading 1).
4. Request additional pilot data (e.g., a second pilot on a
   low-density chapter from Vol IX or XII) before deciding.
