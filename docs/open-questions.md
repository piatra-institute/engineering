# Engineering: open editorial questions

This file holds genuinely open questions that have not yet been settled. Settled decisions live in `editorial-decisions.md`.

When a new question arises during writing, append it here under its appropriate cluster. When it gets answered, move it to `editorial-decisions.md` with a `### Settled YYYY-MM-DD` block and remove it from this file.

## Open after Phase 0.5

These questions arose from the project diagnostic (`diagnostic.md`, 2026-04-28) and the post-diagnostic hardening pass. They are deferred from Phase 0.5 to a later pass.

### Q51, Q52, Q53. Settled 2026-04-28

Reader-path model (three tiers: core/standard/mastery), pilot chapter (Vol I Ch 1), and license confirmation (CC BY-NC-SA prose, MIT code, CC0/CC BY data) all moved to `editorial-decisions.md`.

### Q54. Companion-note architecture

The diagnostic asks for an early decision about what belongs in the permanent PDF/HTML spine versus companion notes (current tools, software versions, product names, regulations, model snapshots, AI frontier details), versus the code repository (runnable examples and simulations), versus the data repository (datasets and provenance), versus errata (corrections).

What we need to settle: where each kind of content lives by default, what the spine-vs-companion test is, and how chapters cross-reference companion material.

### Q55. Per-chapter project track (173 chapters remaining)

Each chapter outside the pilot still has `Project track: TBD (physical, simulation, household, or hybrid)` in its `\chapmeta`. The dossier projects strongly imply tracks (e.g., "instrument the reader's home" is household; "simulate a Markov chain" is simulation; "build a fibreglass composite" is physical). The pilot's track was resolved on 2026-04-28; the remaining 173 are a Phase 0.7 editorial pass.

What we need to settle: who does this pass and on what schedule.

### Q56. Named-cases registry

The diagnostic recommends an accident/source registry under `docs/research/accidents/` before the failure-section prose starts, so the same accident can be referenced consistently across chapters with primary sources already cataloged. Currently named cases (Bhopal, Chernobyl, Boeing 737 MAX, Therac-25, Tacoma Narrows, Aloha 243, Air France 447, Genoa Morandi Bridge, Volkswagen diesel-defeat, ...) are mentioned in dossiers and section headings but have no canonical entries.

What we need to settle: the registry schema, the first ~30 entries, and the BibLaTeX entries for primary investigation reports.

## How to use this file

1. New questions get a level-3 heading with a short paragraph stating the question and the constraints around it.
2. Questions are numbered Q51 onward (Q1-Q50 are settled in `editorial-decisions.md`).
3. When answered, move the question and its settled block to `editorial-decisions.md` and remove from this file.
4. A question that sits open for more than two passes without movement is escalated as a structural risk in `status.md`.
