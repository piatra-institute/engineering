# Notes for editor: Vol II Ch 13 (Probability theory)

Drafted 2026-04-29. First-draft prose. Targets ~25-35pp at first-draft
density; isolated standalone compile produces 27 pp PDF (412 kB) using
the standard preamble.

## Verification snapshot

- `grep -c '\---\|—' volumes/02-form/ch13-probability/chapter.tex` -> 0.
- `\begin{exercise}` count: 40 (matches `Exercise target: 40` in
  `\chapmeta`); 40 matching `\end{exercise}`.
- Brace balance: 790 / 790 (unescaped).
- Environment balance: exercise 40/40, itemize 6/6, estimation 2/2,
  pmatrix 2/2, archetype 1/1, principle 1/1, project 1/1.
- Standalone compile via a minimal `\documentclass{memoir}` wrapper that
  inputs `preamble.tex` and `volumes/02-form/ch13-probability/chapter`
  produces a clean 27-page PDF with no LaTeX errors.

## Build-blocking issue outside this chapter

`make distclean && make strict` does not complete because of a
pre-existing typo in
`volumes/02-form/ch17-discrete-mathematics/chapter.tex` line 249:

```
declare those to be the operational topology.}
```

The closing brace at end of line 249 has no matching opener; the
intended sentence appears to end with a period and no brace. The
`estimation` environment opens on line 242 with `\textbf{Question.}`
correctly closed inline. Removing the stray `}` on line 249 should
clear the error. This is unrelated to Ch 13 and is flagged here so
the next editor pass on Ch 17 can fix it.

I confirmed Ch 13 in isolation by compiling it through the preamble
into a standalone test document; the resulting 27-page PDF is clean.
The `make strict` failure halts before Ch 13 is even reached
(error first surfaces on page ~574 of the would-be PDF, which is in
Ch 17).

## Editorial flags

### 2008 financial-crisis treatment in section 13.8

The brief asked to treat the 2008 mortgage-backed-securities
correlation-collapse pattern at recognition level without a
named-case registry entry, OR to flag it. I chose the
recognition-level treatment without a registry entry, and noted this
choice in the chapter's `\chapmeta{... Named cases: ...}` block
explicitly. The section names the pattern (independence assumed
across events that share a hidden common driver) and gives four
modern instances (redundant systems, ML ensembles, sensor fusion,
multiple-hypothesis testing) without making any cite-able claim
about specific actors, ratings, or dates that would require a
primary source. If the editorial decision is to register the 2008
crisis as a named case for cross-chapter reuse (the pattern recurs
in Vol VII Ch 17 ML, Vol IX systems, Vol X reliability, Vol XI
finance), the registry entry would document AIG, the rating
agencies, the Gaussian copula model, and a closest-equivalent
primary key (the FCIC final report would be the canonical primary).
Until that registry entry exists, the chapter prose stays at the
generic-pattern level and avoids cite-bearing specifics.

### Cross-references

The chapter references Volume I Ch 4 (uncertainty), Volume I Ch 8
(engineering statistics, especially §8.2 distributions and §8.5
Bayes worked example), Volume II Ch 9 (linear algebra; covariance
matrix spectrum), Volume II Ch 10 (eigenvalues; left eigenvector
machinery for stationary distributions), Volume II Ch 14 (statistical
inference; explicitly framed as the next step), Volume IX (queueing,
control), and Volume X (reliability, Bayesian updating). All
cross-references use the named-volume-and-chapter form rather than
`\cref{}` because the destination chapter labels in some target
volumes are still scaffolds; the editor may wish to upgrade these
to `\cref{vol01:ch08}` etc. on a later integration pass.

### Citations used

- `text:ross-probability` (Ross, A First Course in Probability, 10th
  ed., 2018). Cited at chapter recognition and in sections 13.1,
  13.2, 13.4, 13.6.
- `text:wasserman2004` (Wasserman, All of Statistics, 2004). Cited
  in sections 13.1 (Borel sigma-algebra remark, appendix), 13.2
  (Bayesian network preview), 13.3 (random-variable definitions),
  13.6 (modes of convergence, Berry-Esseen), and 13.7 (stochastic
  processes).

Both keys exist in `bibliography/references.bib` (lines 380, 573).
No new citations were added.

### Path tags

- §13.1 Sample spaces and events: core
- §13.2 Conditional probability and Bayes' rule: core
- §13.3 Random variables, expectation, variance: core
- §13.4 Common distributions: core
- §13.5 Joint distributions, independence, correlation: core
- §13.6 Limit theorems: LLN and CLT: core
- §13.7 Stochastic processes preview: standard
- §13.8 Failure: independence assumed where there was none: core
- §13.9 Project: core
- Exercises: Calculation core, Derivation standard, Estimation core,
  Simulation standard, Design standard, Judgement core.

The Project (§13.9) is `core` and depends on the linear-algebra
machinery from Vol II Ch 9 and Ch 10 (computing left eigenvectors of
a row-stochastic matrix), which are themselves `core` in those
chapters. No core-on-standard reader-path violations.

### Estimation environments

Two `estimation` blocks: one in §13.1 (series-reliability with the
union bound vs independence, calibrating the engineer's expectation
of how loose each is) and one in §13.6 (CLT applied to sum of
factory-part weights, showing the gap to a Chebyshev bound). Both
are placed before the worked calculations they motivate, per Q20.

### Failure section

Section 13.8 names the failure mode (independence assumed where
there was none), gives the canonical 2008 instance at
recognition level, four modern engineering instances, three
diagnostic habits, and closes with a `principle` environment
naming the structural lesson.

### Project per Q55-vol02-ch13

The project (§13.9) implements the Q55-vol02-ch13 spec: a Markov
chain of the reader's choice on a finite state space, simulated
for at least $10^{4}$ steps, with empirical state-occupancy
compared against the analytical stationary distribution (computed
as the leading left eigenvector of $\mat{P}$), reporting of the
total variation distance, the second-largest eigenvalue magnitude
(spectral gap) for mixing-time analysis, and explicit verification
of LLN and CLT on a chain-derived statistic via $M = 200$
independent runs. Plus a 1500-word reflection on what the limit
theorems guarantee and what they do not, and on when a Markov
assumption is and is not safe.

### Voice

No em-dashes (linter clean). Authorial "we." No self-announcing
topic sentences. No negate-first-then-pivot constructions checked
against `docs/voice.md`. AI-tic vocabulary scrubbed. Numbers carry
year only where dated; this chapter is mostly mathematical and
carries few year-dated empirical claims. The 2008 instance is
explicitly dated in section 13.8.
