# Engineering: open editorial questions

This file holds genuinely open questions that have not yet been settled. Settled decisions live in `editorial-decisions.md`.

When a new question arises during writing, append it here under its appropriate cluster. When it gets answered, move it to `editorial-decisions.md` with a `### Settled YYYY-MM-DD` block and remove it from this file.

## Open after Phase 0.5

These questions arose from the project diagnostic (`diagnostic.md`, 2026-04-28) and the post-diagnostic hardening pass.

### Q51, Q52, Q53. Settled 2026-04-28

Reader-path model (three tiers: core/standard/mastery), pilot chapter (Vol I Ch 1), and license confirmation (CC BY-NC-SA prose, MIT code, CC0/CC BY data) all moved to `editorial-decisions.md`.

### Q54. Companion-note architecture

The diagnostic asks for an early decision about what belongs in the permanent PDF/HTML spine versus companion notes (current tools, software versions, product names, regulations, model snapshots, AI frontier details), versus the code repository (runnable examples and simulations), versus the data repository (datasets and provenance), versus errata (corrections).

What we need to settle: where each kind of content lives by default, what the spine-vs-companion test is, and how chapters cross-reference companion material.

This question becomes load-bearing if Phase 1 runs the Volume I production-density lane (figures, project artifacts, solutions, code, datasets all need a home). Without a settled answer, each chapter improvises and the answers diverge.

### Q55. Per-chapter project track (79 chapters remaining)

Volumes I-V are settled chapter-by-chapter, plus Vol VI Ch 1-10, plus all of Volume VII, with project tracks recorded in each chapter's `\chapmeta`. The remaining 79 chapters (Vol VI Ch 11-13 plus all of Volumes VIII-XII) still carry `Project track: TBD (physical, simulation, household, or hybrid)` in their `\chapmeta`. The dossier projects strongly imply tracks; the editorial work is to confirm and record per chapter.

What we need to settle: who does this pass, and on what schedule. The cadence followed so far is one volume's worth of project tracks at a time as that volume comes into prose drafting, settled by the drafting agent itself; that cadence has held cleanly across six-and-a-half volumes and can be carried forward.

### Q56. Named-cases registry. Settled 2026-04-29

Registry exists with 15 entries and the supporting machinery: schema (`docs/research/accidents/SCHEMA.md`), citation-policy update with the closest-equivalent-to-primary clause, reviewer-guide registry-check requirement (items 24-27), `make accidents` target with both cite-resolution and prose-name scan, and registry index (`docs/research/accidents/README.md`). All nine Vol I chapter reviews exercised the registry without finding a missing case the chapter cited but the registry did not have. Future entries accumulate as later-volume chapters cite them; the discipline is the schema plus `make accidents`.

## Open after Phase 0.7

### Q57. Page density vs. target

Six-and-a-half volumes are now drafted at first-draft density, against the page targets in `landscape.md`. Per-volume spans (from `main.toc`):

| Volume | Drafted (first-draft pp) | Target (pp) | Ratio | Chapters drafted |
| --- | --- | --- | --- | --- |
| I Quantity | 220 | ~720 | 31% | 9 of 9 |
| II Form | 490 | ~1800 | 27% | 18 of 18 |
| III Force | 274 | ~1300 | 21% | 13 of 13 |
| IV Energy | 234 | ~1400 | 17% | 14 of 14 |
| V Matter | 238 | ~1200 | 20% | 12 of 12 |
| VI Life (partial) | 178 | ~1300 | 14% (extrapolated full Vol VI ~230pp, 18%) | 10 of 13 |
| VII Information | 264 | ~1980 | 13% | 19 of 19 |

The first-draft ratio stabilises in the 13-31% band across seven volumes, with an average around 21%. Vol VII's lower ratio reflects the large chapter count (19) against ambitious per-chapter page budgets (80-120pp each).

Two readings of the gap, neither obviously right:

1. **The chapters are dense; the target was loose.** `landscape.md` itself says page totals are "planning estimates, not commitments." A 20-30pp adult-engineer chapter is not thin if it has the right material; it just lacks decoration. Under this reading, six volumes are closer to done than the page counts suggest, and Phase 1 should run forward into Volumes VII-XII prose, with a possible target-revision pass downward.

2. **Most of the missing pages are artifacts that have not landed.** Figures, expanded worked examples, project-artifact templates, full solution sets, inline diagrams, code/data co-located with each chapter, case-study expansions. Under this reading, the project is at ~22% of the artifact-complete deliverable, and Phase 1 should run a production-density pass per volume before moving forward.

What we need to settle: which reading governs. The two imply materially different forward sequences. With six volumes of consistent first-draft data behind the question, the decision is now defensible either way; the question is no longer "what density do we hit" but "which deliverable are we building."

The decision interacts with Q54: if reading (2) wins, Q54 must be settled before the production-density pass starts. The decision also interacts with the Codex-review lane: Vols II-VI are at Stage 4 awaiting review and the per-chapter feedback will surface artifact gaps that a production-density pass would have to close anyway.

## How to use this file

1. New questions get a level-3 heading with a short paragraph stating the question and the constraints around it.
2. Questions are numbered Q51 onward (Q1-Q50 are settled in `editorial-decisions.md`).
3. When answered, the settled block is added to `editorial-decisions.md` and the original question is marked settled here (kept for traceability rather than removed, so the file is a record of what was once open).
4. A question that sits open for more than two passes without movement is escalated as a structural risk in `status.md`.
