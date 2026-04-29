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

### Q55. Per-chapter project track (165 chapters remaining)

Volume I is settled chapter-by-chapter (Q55-pilot, Q55-ch02 through Q55-ch09, all in `editorial-decisions.md`). The remaining 165 chapters across Volumes II-XII still carry `Project track: TBD (physical, simulation, household, or hybrid)` in their `\chapmeta`. The dossier projects strongly imply tracks; the editorial work is to confirm and record per chapter.

What we need to settle: who does this pass, and on what schedule. A reasonable cadence is one volume's worth of project tracks at a time, as that volume comes into prose drafting.

### Q56. Named-cases registry. Settled 2026-04-29

Registry exists with 15 entries and the supporting machinery: schema (`docs/research/accidents/SCHEMA.md`), citation-policy update with the closest-equivalent-to-primary clause, reviewer-guide registry-check requirement (items 24-27), `make accidents` target with both cite-resolution and prose-name scan, and registry index (`docs/research/accidents/README.md`). All nine Vol I chapter reviews exercised the registry without finding a missing case the chapter cited but the registry did not have. Future entries accumulate as later-volume chapters cite them; the discipline is the schema plus `make accidents`.

## Open after Phase 0.7

### Q57. Page density vs. target

Volume I currently runs ~220 pages of first-draft prose against a ~720-page target. Per-chapter spans (from `main.toc`): Ch 1 18pp, Ch 2 20pp, Ch 3 22pp, Ch 4 22pp, Ch 5 22pp, Ch 6 28pp, Ch 7 22pp, Ch 8 30pp, Ch 9 28pp. Average ~24pp/ch against ~80pp/ch target.

Two readings of the gap, neither obviously right:

1. **The chapters are dense; the target was loose.** `landscape.md` itself says page totals are "planning estimates, not commitments." A 22-30pp adult-engineer chapter is not thin if it has the right material; it just lacks decoration. Under this reading, Volume I is closer to done than the page count suggests, and Phase 1 should run forward into Volume II prose.

2. **Most of the missing 500 pages are artifacts that have not landed.** Figures, expanded worked examples, project-artifact templates, full solution sets, inline diagrams, code/data co-located with each chapter, case-study expansions. Under this reading, Volume I is at ~30% of the deliverable, and Phase 1 should run a Volume I production-density pass first.

What we need to settle: which reading governs. The two imply materially different Phase 1 sequences.

The decision interacts with Q54: if reading (2) wins, Q54 must be settled before the production-density pass starts.

## How to use this file

1. New questions get a level-3 heading with a short paragraph stating the question and the constraints around it.
2. Questions are numbered Q51 onward (Q1-Q50 are settled in `editorial-decisions.md`).
3. When answered, the settled block is added to `editorial-decisions.md` and the original question is marked settled here (kept for traceability rather than removed, so the file is a record of what was once open).
4. A question that sits open for more than two passes without movement is escalated as a structural risk in `status.md`.
