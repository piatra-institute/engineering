# Notes for editor: Vol II Ch 5, Differentiation

Drafted 2026-04-29.

## Status

First-draft prose at production density. Approximately 32 pp in the
current PDF (chapter 14, pages 327 to 358). Below the 110 pp dossier
target but consistent with the editor's "30 to 40 pp first-draft
density acceptable" guidance for this lane. Expansion candidates are
listed below.

## Structure

Nine sections plus project and exercises.

- 5.1 The derivative as rate. Motivates from kinematics, formal
  limit definition, geometric reading, units, examples computed
  from the limit, table of elementary derivatives.
- 5.2 Rules. Linearity, product rule (proof), chain rule (with
  caveat on the locally-constant case), quotient rule (two
  derivations), implicit differentiation (with a deliberately
  unwieldy worked example), logarithmic differentiation, working
  tactics.
- 5.3 Higher-order derivatives. Polynomial, exponential, and
  trigonometric cycles; concavity reading; brief catalogue of
  where higher derivatives matter.
- 5.4 Local linearisation. Taylor's theorem to first order with
  remainder; three worked linearisations with remainder bounds
  (square root, sine, logarithm); the working approximation
  identified as the formal home of the small-angle, binomial, and
  uncertainty-propagation rules from Volume I.
- 5.5 Mean value theorem and L'Hopital. MVT with proof sketch
  via Rolle. L'Hopital as a tool for indeterminate forms.
  Includes the GUM partial-derivative legitimisation paragraph
  the editor's brief flagged: a sentence near the start of the
  section explicitly retroactively legitimises the formula
  $u^{2}(y) = \sum_{i} (\partial f / \partial x_{i})^{2} u^{2}
  (x_{i})$ that Vol I Ch 4's mastery box deferred.
- 5.6 Optimisation of one variable. Formal first introduction of
  the optimisation archetype. First-order Fermat condition,
  second-derivative test, three worked examples (aluminium can,
  power transfer, drag minimisation), constrained one-variable
  optimisation on a closed interval.
- 5.7 Numerical differentiation. Forward, backward, central
  differences with truncation error from Taylor; round-off error;
  catastrophic cancellation; bias-variance tradeoff; higher-order
  stencils; differentiating noisy data.
- 5.8 Failure section. Jumps, kinks, cusps, oscillations,
  derivatives that exist but are bad working tools, Patriot case
  as a numerical-precision analogue. Closes with the principle
  "The derivative serves the function it differentiates."
- 5.9 Worked examples across domains. Kinematics, electrical
  engineering (capacitor, RC charging), thermodynamics (heat
  capacity, Newton's law of cooling), biology (logistic growth).

Project: simulation-with-analysis on a noisy time series,
three-method comparison (finite differences, smoothing then
differentiation, parametric fit then differentiation), 1500-word
reflection on the bias-variance tradeoff. Matches Q55-vol02-ch05.

Exercises: 40 across calculation (8), derivation (6), estimation
(6), simulation (4), design (3), diagnosis (3), failure
analysis (4), judgment (6).

## Archetypes

- Optimisation: introduced formally for the first time in §5.1's
  archetype box and developed in §5.6.
- Transport (gradient as flux density): previewed informally in
  the opener and the worked-examples section. Awaits formal
  treatment in chapter 11 (multivariable calculus) and chapter 13
  (PDEs).

## Citations

Two distinct citation keys are invoked in the prose:

- `acc:gao-patriot-1992`. Patriot missile system, Dhahran, 1991.
  The named-cases registry entry already exists at
  `docs/research/accidents/patriot-dhahran-1991.md` (status
  verified). Used in the failure section §5.8 and in one failure-
  analysis exercise. The accident is listed in `\chapmeta`'s Named
  cases line. `make accidents` PASS.

The chapter does not cite `text:strang2016` or `text:taylor1997`
in this draft. Both were on the editor's recommended list. The
draft does not yet need them: Strang's linear algebra is Vol II
Ch 9's home, and Taylor's error analysis was the Vol I Ch 4 home.
If a reviewer wants either text added as a recommended-reading
footnote, they can be cited at §5.4 (linearisation) and §5.7
(numerical differentiation) respectively.

## Expansion candidates

If the editor wants to push the chapter toward the 110 pp target,
the most natural expansion lanes are:

1. §5.4 Local linearisation. Add second-order Taylor expansion
   formally with remainder bound, plus three more worked second-
   order linearisations and a worked uncertainty-propagation
   example using the GUM general formula. Estimated: 8 to 12 pp.
2. §5.7 Numerical differentiation. Add Richardson extrapolation,
   finite differences on non-uniform grids, automatic
   differentiation as a brief preview, and Savitzky-Golay
   coefficients table. Estimated: 6 to 10 pp.
3. §5.6 Optimisation. Add gradient-descent preview as a numerical
   alternative to $f'(x) = 0$ for functions where the derivative
   is not closed-form. Estimated: 4 to 6 pp.
4. §5.9 Worked examples. Add a software-engineering domain
   (response-time gradients) and a structural-mechanics domain
   (beam bending as the second derivative of deflection).
   Estimated: 6 to 8 pp.
5. §5.2 Rules. Add inverse-function differentiation as a
   subsection (currently only implicit covers it indirectly).
   Estimated: 3 to 5 pp.

Estimated full-target expansion: ~30 to 40 pp added, taking the
chapter to ~70 pp. To reach 110 pp would require either a deeper
treatment of Taylor series (which belongs in Ch 4 of this volume)
or a longer numerical-differentiation appendix.

## Voice notes for the reviewer

- No em-dashes (verified by `grep -c '\---|—'` returning 0).
- All "current as of" claims are dated 2026; one in the drag-
  minimisation worked example.
- The chapter does not name any accident in prose without the
  registry entry; Patriot is the only named case.
- The implicit differentiation worked example (line ~700) uses
  the deliberately unwieldy expression $x \sin y + y \cos x =
  e^{x y}$ to illustrate that the technique works even when
  solving for $y$ explicitly is impractical. A reviewer who finds
  the example excessive may wish to swap in a tamer one (e.g. an
  ellipse), at the cost of losing the demonstration that the
  method is exactly what one needs when explicit solution is not
  available.

## Build status (current as of 2026-04-29)

- `grep -c '\---|—' volumes/02-form/ch05-differentiation/chapter.tex`: 0
- `make exercise-counts`: PASS, 40 exercises matching the chapmeta target
- `make check`: PASS
- `make accidents`: PASS
- `make audit-docs`: PASS
- `make distclean && make strict`: PASS, 928-page PDF

## Outstanding editor decisions

None release-blocking. Suggested:

1. Confirm whether `text:strang2016` and `text:taylor1997` should
   be added as recommended-reading footnotes at §5.4 and §5.7.
2. Confirm the page-count target for Phase 1 closure: leave at
   first-draft density (~32 pp) or expand toward 70 pp via the
   five lanes above.
3. The opener epigraph is a working paraphrase rather than a
   sourced quotation; a reviewer may wish to replace it with a
   sourced epigraph from Newton, Leibniz, or a working-engineer
   primary source.
