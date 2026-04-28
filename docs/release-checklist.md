# Engineering: release checklist

This file enumerates the checks that must pass before any chapter, volume, or full-book release. It formalises the "Suggested make check rules" from the project diagnostic into operational gates.

The checklist is enforced incrementally:

- `make check` enforces structural invariants (Phase 0.5 onwards). Currently passing.
- `make strict` enforces a halt-on-error LaTeX build (Phase 0.5 onwards).
- `make release` (planned, Phase 1) enforces the full set below; absent any single check, the release fails.

## Structural invariants

Every chapter file under `volumes/<NN>-<slug>/ch<MM>-<slug>/chapter.tex` must contain:

1. `\\chapter{...}` — chapter title.
2. `\\label{vol<NN>:ch<MM>}` — canonical label.
3. `\\chapmeta{...}` — half-life, archetypes, exercise target, project track.
4. At least one `\\section{...}` — sub-section structure.
5. A `Project` section.
6. An `Exercises` section.

Every volume directory `volumes/<NN>-<slug>/` must contain:

7. A `_volume.tex` opener.
8. The number of chapter files matching the volume's chapter count in its dossier.

Every chapter file must NOT contain:

9. Em dashes (`---` or `—`) outside primary-source quotation environments.
10. Unicode superscripts, subscripts, or math symbols not handled by the preamble's `newunicodechar` block.
11. The string `Half-life: TBD` (after Phase 0.5).
12. References to a chapter or volume number that does not exist.

`make check` enforces 1, 2, 3 currently. The remaining items are added as the prose work progresses and the failure modes appear.

## Build invariants

13. `make strict` exits 0. The PDF builds with `-halt-on-error`.
14. `latexmk` reports no undefined references and no unresolved citations (counted at non-zero failure threshold for a release).
15. `latexmk` reports no overfull `\\hbox` or `\\vbox` exceeding 5 pt (Phase 1 onwards).

## Citation and provenance

For every chapter at release-ready status:

16. Every empirical claim cites a source at the appropriate tier (`citation-policy.md`).
17. Every named accident has at least one `acc:` citation.
18. Every numerical table has a `Source:` line.
19. Every figure caption attributing reproduced content has a citation.
20. No tertiary explainer supports a load-bearing claim.
21. Every "current as of YYYY" tag has a year that matches the citation's publication date.

## Pedagogical invariants

22. Every chapter has at least one `\\begin{estimation}` block.
23. Every chapter has a failure section that connects to the chapter's main mechanism.
24. Every chapter has a project with required tools listed.
25. Every chapter project specifies a physical track and (where applicable) a simulation track.
26. Every chapter has at least the dossier-stated number of exercises.

## Voice invariants

27. No em-dashes anywhere in book prose.
28. No first-person "I" in body prose (frontmatter and preface excepted).
29. No banned AI-tic vocabulary (see `voice.md` ban-list).
30. Every chapter passes the voice reviewer's pass.

## Review invariants

31. Every chapter has a review log entry under `docs/reviews/` (or in its dossier).
32. The log shows technical, pedagogical, and voice reviewers with disclosed conflicts.
33. The log shows verdict and date for each role.

## Editorial-content invariants

34. Every chapter's `\\chapmeta` half-life matches the dossier's stated half-life or carries an explicit override note.
35. Every chapter project description in `\\chapmeta` matches the dossier's project text or carries an explicit override note.
36. Every fast-aging chapter has a companion-note pointer.
37. Every named accident referenced more than twice in the book lives in the named-cases registry under `docs/research/accidents/` (Q56).

## Bibliography invariants

38. No citation key references a non-existent BibLaTeX entry.
39. No BibLaTeX entry sits unused (warning, not block; cleanup at release).
40. Every entry uses the project's category-prefix convention (`std:`, `acc:`, `law:`, `hist:`, `text:`, `paper:`, `data:`, `web:`).
41. Every `acc:` entry includes the issuing investigation body and the report number.
42. Every `std:` entry includes the standard's edition and year.

## Front-matter and back-matter invariants

43. Frontmatter prose is in authorial "we" voice.
44. The notation table covers every symbol used in the book or directs to per-volume sub-tables.
45. The reading list (Appendix D) lists per-volume canonical references.
46. The index (`\\printindex`) generates without errors.
47. The bibliography section in the back matter prints without errors.

## License and metadata invariants

48. Text license file (`LICENSE-text.md` or equivalent) exists and is referenced from the README and the title page.
49. Code license file (`LICENSE-code.md` or equivalent) exists and is referenced from the README.
50. PDF metadata (Title, Author, Subject, Keywords) is set, not blank.
51. Cover page year matches the release year.

## Volume-release sub-checklists

A volume-release (releasing one of the twelve volumes as a standalone artifact) additionally requires:

V1. The volume's dossier is fully consistent with its chapter shells.

V2. The volume's reviewer roster is filled and all reviewers have signed off on every chapter.

V3. The volume's interlude (if it has one inside it; note that book-level interludes between volumes live in `main.tex`) is reviewed.

V4. The volume's bridges to prior volumes resolve cleanly (every cross-reference labels exist in the prior-volume sources).

V5. The volume is named in `frontmatter/notation.tex` for any volume-specific notation it contributes.

## Full-book-release additional checks

A full-book release (the canonical PDF / HTML of all twelve volumes) additionally requires:

F1. All 11 inter-volume interludes are reviewed and applied (not "queued").

F2. The decisions log (`editorial-decisions.md`) is sealed: no open settled-question revisions in flight.

F3. The open-questions log is empty or every remaining open question has an explicit "deferred to future edition" note.

F4. The accidents registry (`docs/research/accidents/`) has entries for every accident referenced more than twice.

F5. The companion website is live with errata, code, and dataset references.

F6. Every chapter's review log is complete.

F7. The project diagnostic has been re-run within 30 days and returns no critical findings.

## Failure modes for the release process

A release that fails any item above is held. Released artifacts that are later found to violate any item trigger:

- Errata entry on the companion website within 7 days.
- Source correction in the next minor release.
- Major release pause if the violation is structural (citation discipline collapse, voice drift, scale dishonesty).

## Operational note

This checklist is itself a moving target. Every diagnostic re-run can add items. Items that have proved redundant after a release pass can be retired with explicit rationale recorded in `editorial-decisions.md`.

The discipline of the release checklist is one of the project's core promises to its readers. A book that promises 17,000 pages of engineering must clear every check. A book that quietly drops a check has stopped being the book.
