# Engineering: research pipeline

This file describes how the project moves a topic from "named in a dossier" to "written, sourced, reviewed, released." The pipeline applies to chapter prose, named-case studies, and per-volume technical content. It does not cover frontmatter or appendix content, which follow a lighter process.

The pipeline has six stages. A topic at any stage can be sent back to the previous stage; promotions are uni-directional only after the gate passes.

## Stage 1: Outline (Phase 0, complete)

The chapter exists in its dossier (`docs/research/<NN>-<slug>/ch<MM>-<slug>.md`) with:

- Chapter title.
- Page budget.
- Sub-section list with sub-section page budgets.
- Archetype invocations.
- Project brief.
- Exercise count target.
- Bridges to adjacent chapters and volumes.
- Reading-list candidates.

A chapter at Stage 1 has a generated shell under `volumes/<NN>-<slug>/ch<MM>-<slug>/chapter.tex` with a `\\chapmeta` block, empty epigraph, and TODO markers throughout.

**Promotion criterion to Stage 2**: dossier metadata is consistent and the chapter shell rebuilds cleanly via `make scaffolding`.

Stage status, current as of 2026-05-15:

- **Stage 5**: 9 chapters (all of Volume I). All carried through Codex review with the resolution banner on the corresponding `docs/reviews/vol01-chNN-review.md`.
- **Stage 4**: 67 chapters awaiting Codex review (all 18 of Volume II, all 13 of Volume III, all 14 of Volume IV, all 12 of Volume V, Ch 1-10 of Volume VI).
- **Stage 1**: 98 chapters (Vol VI Ch 11-13 plus all of Volumes VII-XII). Shells exist with dossier-derived metadata; no prose yet.

Stage 6 (Released) is not yet reached; the project has produced no issued release. The Stage-5 chapters are integration-complete but await release packaging.

## Stage 2: Source acquisition

The chapter's lead writer assembles the primary and secondary sources required for the chapter's claims. This is research, not writing.

Activities:

- Read the chapter's dossier reading list.
- Read at least two primary investigation reports for any named accident.
- Read the canonical handbooks for any settled technical material.
- Identify peer-reviewed sources for any post-1980 technical claim.
- Identify standards documents for any standards-driven claim.
- Identify datasets for any quantitative claim.
- Take dated, sourced notes in the chapter's research notebook (under `docs/research/notebooks/`, structure to be settled).
- Add provisional BibLaTeX entries to `bibliography/references.bib` under the appropriate category prefix.

The chapter's BibLaTeX entries should be ready before any prose is written. A common failure mode is citing from memory or web search; this pipeline forbids it.

**Time budget**: 2-4 weeks of intermittent work for a typical chapter. 6-8 weeks for a chapter with substantial named-case content (most of Volume X).

**Promotion criterion to Stage 3**: every claim the writer intends to make has at least one cited source at the appropriate tier per `citation-policy.md`. The chapter's reading list in the dossier is updated to reflect what was actually read.

## Stage 3: Drafting

The writer produces chapter prose. The shell file under `volumes/<NN>-<slug>/` is filled in: epigraph, opener, sections (replacing each `\\TODO{Section prose.}` with actual prose), worked examples, estimation blocks, project description with concrete tools and tracks, exercises, failure section, and case studies (using `case-study-template.md` for any named accidents).

Discipline:

- The writer follows `voice.md` continuously.
- Every section's prose is tied to at least one cited source where empirical or historical claims appear.
- Worked examples are reproducible: numbers can be checked.
- Estimation blocks precede the corresponding calculation.
- Failure section connects to the chapter's main mechanism.
- Cross-references use canonical labels (`vol<NN>:ch<MM>`) and resolve.
- Half-life tag in `\\chapmeta` is reconfirmed against the prose.

**Time budget**: 4-12 weeks for a typical chapter (60-140 pages of dense prose plus exercises). Longer for case-study-heavy chapters.

**Promotion criterion to Stage 4**: the chapter compiles end-to-end via `make`; `make check` passes for the chapter; the writer self-reviews against the reviewer-guide checklist and produces a clean draft.

## Stage 4: Review

The chapter is reviewed by three roles per `reviewer-guide.md`: technical, pedagogical, voice.

Each reviewer returns:

- Verdict (approved / approved-with-corrections / blocked).
- Concrete written comments.
- Disclosed conflicts.

The writer addresses comments. If any role returns "blocked," the chapter returns to Stage 3 with a rewrite plan.

**Time budget**: 14 days per reviewer per pass; typically one corrections round per chapter.

**Promotion criterion to Stage 5**: all three roles return "approved" or "approved-with-corrections" with corrections completed.

## Stage 5: Integration

The reviewed chapter is integrated into the project at large.

Activities:

- BibLaTeX entries are checked for duplicates and consolidated.
- Cross-references from prior chapters that should now point into this chapter are added.
- The cross-volume `landscape.md` is updated if the chapter introduces or revisits an archetype.
- The accidents registry under `docs/research/accidents/` is updated with any new entries or revised cross-references.
- The companion website (when active) is updated with the chapter's code, datasets, simulations, and project templates.
- The chapter's review log is finalised in `docs/reviews/` and locked.

**Time budget**: 1-2 weeks per chapter.

**Promotion criterion to Stage 6**: integration tasks complete; `make release` for the volume that contains this chapter passes (or the residual failures are tracked).

## Stage 6: Released

The chapter is part of an issued release. From this point:

- Corrections flow through errata, not silent rewrites.
- Half-life-tagged sections are reviewed for re-derivation when their tag's interval lapses.
- Reader-reported errors are tracked in the errata system.
- A major-edition revision (5-year cycle per Q45) returns the chapter to Stage 2 if structural changes are needed, or directly to Stage 3 if only prose updates.

## Pipeline gates and tooling

Each stage has gates:

- Stage 1 → 2: dossier metadata consistent; `make scaffolding` runs cleanly.
- Stage 2 → 3: bibliography entries present for all intended claims.
- Stage 3 → 4: `make` builds; `make check` passes for the chapter.
- Stage 4 → 5: reviewer log shows three approvals.
- Stage 5 → 6: `make release` (or its volume-scoped variant) passes.

Tooling:

- `scripts/generate_scaffolding.py`: regenerates Stage 1 chapter shells from dossiers.
- `make stats`: reports counts at any stage.
- `make check`: enforces structural invariants (Stage 1 onwards).
- `make strict`: build with halt-on-error (Stage 3 onwards).
- `make release`: full-release validation (Stage 5 → 6).
- `make citations` (planned): scan TeX for orphan citation keys.
- `make accidents` (planned): verify named-accident sourcing.

## Capacity planning

A working assumption (revisable) is that one writer can carry one chapter through Stages 2-4 in 8-16 weeks of focused work. Domain reviewers can absorb 2-4 chapters per year per reviewer.

For 174 chapters across Volumes I-XII, this implies:

- Single-writer pace: 4-7 years to complete all 174 chapters at Stages 2-4.
- Multi-writer pace (general editor + named domain leads per Q50): 2-3 years if 6-10 leads work in parallel.
- Reviewer pool: 30-50 named reviewers across the domains, recruited per `reviewer-guide.md` "Reviewer recruitment."

These numbers are planning estimates only. The actual schedule emerges from the pilot chapter (Q52).

## What this pipeline forbids

- Writing from memory without source citations.
- Skipping the case-study template for named accidents.
- Releasing a chapter without three-role reviewer sign-off.
- Adding to the bibliography during drafting without category-prefix discipline.
- Accepting "I'll cite this later" as a stage gate.
- Promoting a chapter to Stage 6 with structural-check failures recorded in the issue log.

The pipeline is the discipline. The discipline is the project's promise that ~18,400 pages of engineering will compile into a credible book.
