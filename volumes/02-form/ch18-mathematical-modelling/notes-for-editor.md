# Vol II Ch 18 notes for editor

## Status
First-draft prose written 2026-04-29 against the dossier and the
Q55-vol02-ch18 settled project track. Structurally modelled on Vol I
Ch 9 (volume-closing chapter, archetype-codifying, project-bearing).

## Metrics
- Em-dash count: 0 (verified: `grep -c '\---\|—' chapter.tex`).
- Exercise count: 25 (matches chapmeta target).
- Source size: ~1500 lines, ~30 PDF pages (chapter starts ~p. 681,
  next part starts p. 711).
- Citations used: `gen:meadows2008`, `gen:mackay2009`, `gen:polya1945`
  (all already in `bibliography/references.bib`; no new keys needed).

## Sections and pathtags
- 18.1 What modelling is — `core`
- 18.2 Choosing what to keep and what to throw away — `core`
- 18.3 Identification and validation — `core`
- 18.4 Parameter estimation — `standard`
- 18.5 Model uncertainty and structural error — `core`
- 18.6 Worked example: cooling-cup notebook to model and back — `core`
- 18.7 Worked example: biological / financial / structural — `standard`
- 18.8 Failure: models that fooled their builders — `core`
- 18.9 Modelling as a moral discipline (closing) — `core`
- 18.10 Project — `core`
- 18.11 Exercises (calculation/derivation/estimation/simulation/
  design/judgement) — section per Q16 category, individually tagged.

## Archetype
Ethics (responsible modelling) introduced here as required by the
landscape index; volume opener flags Vol II as introducing three
archetypes (Optimisation, Stability, Control) plus developing the six
from Vol I. The dossier asks for Ethics here as the canonical first
introduction. Volume X is the formal home; this chapter treats the
archetype at the working level and points forward.

## Failure section
Treated at recognition level (no named-cases registry invocation in
prose). Four categories named: overfit calibration, regime extension,
missing-mechanism risk, the simulation that became the system. The
2007-09 financial-crisis modelling category is named without a
specific cited case (the registry has none for it, and the directive
asked for recognition-level treatment in that scenario). If the editor
wants any of these to escalate to named-case treatment, a registry
entry is required first per Q56.

## Project
Implements Q55-vol02-ch18 verbatim: 5-page write-up taking one Volume
I notebook quantity through identification, validation, and
sensitivity, plus 1500-word reflection. Seven-section structure spelled
out for the reader.

## Build verification
- `grep -c '\\---\|—'`: 0 PASS
- `make exercise-counts`: chapter target met (existing failure in
  ch12-pdes is pre-existing and unrelated).
- `make distclean && make strict`: chronic biblatex/biber convergence
  issue across the whole book; many pre-existing citations remain
  undefined after the latexmk run because the Makefile's `rm -f
  $(ARTIFACTS)` post-step strips `.bcf` and `.bbl` between runs.
  Workaround: run `latexmk -pdf` two or three times manually before
  the artifact cleanup. My chapter's three citations
  (`gen:meadows2008`, `gen:mackay2009`, `gen:polya1945`) all resolve
  correctly when biber gets to run; the cite locations appear in
  `main.aux`.

## Voice notes
- No em-dashes anywhere in the source.
- Authorial "we" used throughout.
- No self-announcing topic sentences (verified by grep).
- One earlier triple declarative ("The model is not the system. The
  pendulum equation is not the swing. The map is not the territory.")
  was rewritten to a single declarative when I noticed it on
  re-reading.
- "Robust" was caught and changed to "insensitive" in section 18.5.
- The MacKay citation was added late to satisfy the directive's
  requirement for `gen:mackay2009`; it sits naturally in the
  triangulation paragraph (he uses parallel routes to estimate the
  same energy quantity).

## Worked example
Section 18.6 uses the Vol I Ch 4 cooling-cup notebook as the bridge
back to Volume I. Numbers chosen to be reproducible by the reader's
own kitchen: 90 deg C start, 22 deg C ambient, k around 0.04 per
minute, drink-temperature time around 14.5 +/- 1.8 minutes. The
calculation exercises in section 18.11 use the same data set so the
exercise and the worked example reinforce each other.

## Three sketched systems (18.7)
- Biological: logistic growth in a flask. Engineering depth: the
  death phase as the structural error that biases r and K.
- Financial: discounted cash flow. Engineering depth: discount-rate
  choice and residual-value judgement as the dominant structural
  uncertainty; named without invoking 2007-09 specifically.
- Structural: Euler-Bernoulli beam. Engineering depth: the three
  failure regimes (shear, geometric nonlinearity, yielding) as the
  domain-of-validity statement.

## Open items the editor may want to revisit
- The financial-system worked example (18.7) could become a fuller
  treatment if the editor decides to escalate the 2007-09 case to a
  registry entry. Currently the section treats the category at
  recognition level only.
- Q57 (Vol I production-density pass) may rebalance the exercise
  count expectation; 25 is the dossier target but the volume's
  average is 35-40.
- Cross-references to specific Volume II chapters (Ch 7 ODEs, Ch 14
  inference) are by topic name rather than by `\cref{}` because
  some chapter labels have not yet been verified across recent
  drafts; the editor may want to convert these to `\cref{}` once
  the labels stabilise.
