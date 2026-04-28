# Engineering: reviewer guide

This file describes what domain reviewers should check when reading a chapter draft. It exists because Q25 (technical correctness across 20K pages) is impossible without explicit reviewer protocols.

The guide assumes a reviewer who is a working specialist in the chapter's domain (a practising mechanical engineer for Volume III chapters, a working ML engineer for Volume VII chapter 17, etc.) and who reads at production-review intensity, not at skim depth.

## Reviewer roles

A chapter clears review only after passing through three roles. The same person may play more than one role across a chapter, but never all three on the same chapter.

### 1. Technical reviewer

A working specialist in the chapter's primary domain. Reads for correctness of the technical claims, derivations, worked examples, and exercise solutions.

### 2. Pedagogical reviewer

A teacher or experienced mentor who has taught adjacent material. Reads for whether the chapter actually teaches: prerequisite assumptions, definition order, derivation clarity, exercise scaffolding, project tractability.

### 3. Voice reviewer

The general editor or a designated voice-keeper. Reads for adherence to the rules in `voice.md`: authorial "we", no em-dashes, no AI-tic vocabulary, derivation-first, dimensions-first, failure-visible, half-life-honest, named-case discipline.

A chapter passes if all three roles return "approved." A chapter fails if any role returns "blocked." A chapter receives "approved with minor corrections" only if the corrections are mechanical and the next pass needs no re-review.

## Per-chapter reviewer checklist

The technical reviewer works through this checklist sequentially. Each item is either pass, fail, or non-applicable. A "fail" blocks the chapter.

### Identity

1. Chapter title matches the dossier title.
2. Chapter number matches the volume's chapter list.
3. Chapter half-life matches the dossier (or the chapter prose explicitly justifies a different tag).
4. Chapter archetypes match the dossier (or are explicitly extended with rationale).

### Foundations

5. The chapter's prerequisites (volumes and chapters cited as required reading) are accurate.
6. The chapter does not assume content from a later chapter.
7. The chapter's claimed scope (in the opener) is what the chapter actually covers.

### Technical correctness

8. Every formal claim (theorem, principle, model, archetype) is correct as stated.
9. Every derivation is reproducible and free of leap-of-faith steps.
10. Every numerical value cited is correct and traceable to a source.
11. Every dimensional analysis checks.
12. Every diagram is correctly labelled and matches the prose.
13. Every worked example produces the stated answer when the reviewer redoes it.
14. Every exercise has a defensible solution and is solvable from the chapter's content.

### Citation

15. Every empirical claim has a citation at the appropriate tier (`citation-policy.md`).
16. Every named accident has primary-source citations.
17. Every table has a `Source:` line.
18. Every figure caption has attribution if reproduced from another source.
19. No tertiary explainer supports a load-bearing claim.

### Failure section

20. Every chapter has a failure section.
21. The failure section connects to the chapter's main mechanism.
22. Named accidents in the failure section follow the seven-section template (or reference the registry entry).
23. Counterfactuals are evidence-based, not invented.

### Named-cases registry (Q56)

For every named accident appearing in the chapter (in prose, exercises, or chapmeta `Named cases` list):

24. The accident has a registry entry at `docs/research/accidents/<slug>-<year>.md`.
25. The chapter's mechanism description aligns with the registry's `## Technical mechanism` section, or quotes one of the registry's `## Short-form summaries` verbatim. The chapter does not re-narrate the accident from a different framing.
26. The chapter's `\\cite{...}` key for the accident matches the registry's primary or closest-equivalent key.
27. If the registry entry is at status `placeholder` or `provisional`, the chapter's draft is acceptable but the chapter cannot ship until the registry entry is `verified`.

A chapter that names an accident with no registry entry is blocked. The author either writes the registry entry (the easier path; ~30 min using the schema at `docs/research/accidents/SCHEMA.md`) or removes the accident from the chapter.

The `make accidents` target runs the same check mechanically; reviewers should run it before reading.

### Estimation environment

28. Every chapter has at least one `\\begin{estimation}` block.
29. Estimation blocks precede the corresponding calculation.
30. Estimation answers are correct to within the stated tolerance.

### Project

31. The chapter project is tractable in the stated time budget.
32. The project's required tools are listed.
33. The project specifies a physical track and (where applicable) a simulation track.
34. The project's expected outcome is stated.
35. The project's failure modes are described.

### Aging

36. Every fast-aging or medium-life claim carries a "current as of YYYY" tag.
37. Software / commercial / regulatory specifics live in companion notes when appropriate.
38. The reader returning in 2046 can tell which parts to re-derive and which to trust.

### Cross-references

39. Every `\\cref{...}` and `\\autoref{...}` resolves to the intended target.
40. Forward references are minimised; backward references are precise.
41. Bridges to adjacent chapters and volumes are accurate.

### Voice (handled by voice reviewer; technical reviewer flags only the egregious)

42. No em-dashes.
43. No first-person "I" in body prose.
44. No "let us pause to note" / "in essence" / "fundamentally" / similar AI-tic.

A chapter that fails three or more items in any cluster (foundations, correctness, citation, registry, etc.) is returned with a structural rewrite required, not a corrections list.

## Reviewer turnaround

The pace assumption is 3-6 hours of attentive review per 80-page chapter for the technical reviewer, 2-4 hours for the pedagogical reviewer, 1-2 hours for the voice reviewer. A chapter typically goes through one round of corrections before final approval.

A reviewer who cannot deliver inside 14 calendar days for a normal chapter declines the chapter. Time-bound editorial work is one of the project's core disciplines.

## Conflict of interest

Reviewers disclose:

- Authorship of cited primary work (if any).
- Commercial relationships with named tools, products, or organisations.
- Membership in standards bodies relevant to the chapter.
- Prior employment by organisations named in the chapter's failure section.

A disclosed conflict does not disqualify; an undisclosed one does. The disclosure is recorded in the chapter's review-log entry.

## Reviewer-log

Each chapter carries a review log in its dossier (or in a `docs/reviews/` extension; structure to be settled before the first pilot review). The log captures:

- Reviewer name and role per pass.
- Date received, date returned.
- Verdict (approved / approved-with-corrections / blocked).
- Disclosed conflicts.
- Substantive comments (preserved verbatim in the dossier).

The review log is part of the project's accountability record. Volumes that ship without a complete review log per chapter are not released.

## What reviewers do not do

A reviewer is not a co-author. A reviewer does not rewrite the chapter. A reviewer flags problems and suggests directions. The author resolves.

A reviewer does not litigate the chapter's editorial decisions. The chapter scope, voice, and depth standard are settled in `editorial-decisions.md`. A reviewer who disagrees with a settled decision raises it as an open question for the next decisions-log pass, not as a block on the current chapter.

A reviewer does not substitute their preferred sources. The author chooses sources within the citation policy; the reviewer flags inadequate sourcing.

## What reviewers must do

Reviewers must return concrete written comments. "I have concerns about chapter 4" is not a review. "Equation 4.12 has a sign error in the second term; the standard derivation in Timoshenko §3.5 gives the opposite sign" is.

Reviewers must read primary sources for any flagged claim, not rely on memory.

Reviewers must say "I do not know" where they do not know. The discipline of admitted ignorance is more valuable than the appearance of completeness.

## Reviewer recruitment

Each volume names its target reviewer pool in its dossier (under "Source-text reading list" or a future "Reviewer roster" section). Recruitment is a Phase 1 activity, started no later than the pilot chapter.

Initial-pass review is single-reviewer-per-role; mature chapters move to two-reviewer technical (for high-stakes chapters in Volumes IX, X, and XII especially).

## When this guide changes

This guide is itself reviewed annually. Edits go through the same kind of review cycle the chapters do, with the general editor as the technical and voice reviewer and an experienced contributor as the pedagogical reviewer.
