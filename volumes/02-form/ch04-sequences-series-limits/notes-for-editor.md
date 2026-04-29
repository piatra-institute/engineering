# Vol II Ch 4 (Sequences, series, limits) — notes for editor

Drafted 2026-04-29. Stage 3 (drafting) complete; Stage 4 (review) pending.

## Build status

The chapter compiles cleanly within `main.tex`. Page span on the
2026-04-29 build: 301--322 (about 22 pages of typeset prose, exercises
included). The first-draft density target (25--35 pp) lands close to
the lower edge of the band; if reviewers want closer to the 80 pp
nominal, the obvious expansion lanes are: more worked Taylor-series
algebra (composition, inversion, multiplication of series), more
convergence-test worked examples, and a longer treatment of asymptotic
series (Stirling, Borel summation as a mastery box).

`make strict` currently fails on a pre-existing fatal error in
`volumes/02-form/ch09-linear-algebra/chapter.tex` line 60: the macro
`\spn` is undefined. This is unrelated to Ch 4. The Ch 4 chapter passes
through pdflatex without errors and produces clean typeset output;
warnings in Ch 4 are limited to undefined citations on the first pass
(normal, resolves after biber) and a single overfull hbox in the
Calculation exercise on the radius of convergence (cosmetic).

## Shared-file requests

1. **None required.** All citations used (`text:strang2016`,
   `text:mahajan2014`) already exist in `bibliography/references.bib`.
   No new accident registry entries; the failure section is generic
   (harmonic-series trap), per the dossier guidance and Q55-vol02-ch04.

2. **Suggested cross-volume hooks.** Section 4.5 lists "convergence of
   an iteration" as a limit application; Volume II Chapter 16 (numerical
   methods) is the formal home of this discussion and could open with a
   back-reference to §4.5 to close the loop. The estimation block
   (geometric-residual decay) likewise prefigures the convergence-rate
   discussion of Newton's iteration in Ch 5.

3. **Optional: a "Taylor series catalogue" appendix.** Five canonical
   series (`exp`, `sin`, `cos`, `log(1+x)`, `(1+x)^alpha`) appear in
   §4.4.3 and are referenced in Vol II Ch 5--7 and Vol III. If reviewers
   want, this catalogue could be promoted to an appendix
   (`appendices/taylor-series.tex`) for cross-volume reuse.

## Editorial choices made during drafting

- **Epsilon-delta as motivating discipline only.** The chapter states
  the formal definition once (§4.5.2) but does not work
  epsilon-delta proofs. This matches the dossier ("limits are
  introduced informally") and the volume opener's "usable power, not
  disciplinary completeness" clause. Reviewers who want a worked
  epsilon-delta proof for $\lim_{x \to 1} (x^{2} - 1)/(x - 1) = 2$
  might suggest one as a mastery box; the current draft does not
  include one.

- **Taylor's theorem with remainder.** Used as a known result
  (Lagrange form). The differential calculus that would derive it
  formally arrives in Ch 5. The chapter cites the result and uses the
  bound; it does not derive the remainder formula. This was an
  explicit dossier instruction.

- **Pendulum-period correction in the project.** The expansion
  $T(\theta_{0}) = 2\pi\sqrt{L/g}(1 + \theta_{0}^{2}/16 + 11
  \theta_{0}^{4}/3072 + \cdots)$ is given to two terms; the elliptic
  integral of the first kind appears as a stated identity. The
  derivation of the elliptic-integral form is deferred to Ch 6
  (integration). The project notes this explicitly.

- **No named accident.** Per the dossier, the failure section is
  generic (the harmonic series as canonical case). The chapter does
  not invoke any accident registry entries. `\chapmeta{... Named
  cases: none}` reflects this.

- **Project hazard class is "none".** Analysis only, no field
  measurement, no instrument operation. Per Q55-vol02-ch04.

- **Reader-path tags.** §4.1, §4.2, §4.4, §4.6 (failure), §4.7,
  Project: `core`. §4.3 (convergence tests catalogue) and §4.5
  (limits): `standard`. Calculation, Estimation, Diagnosis, Failure
  exercises: `core`. Derivation, Design, Judgment exercises:
  `standard`. Simulation: `mastery`. Core project does not depend on
  standard sections (the small-angle approximation at the leading
  order is core; the convergence-test catalogue, used to certify the
  Taylor series convergence in passing, is standard but not
  load-bearing for the project itself).

## Things a reviewer might want to flag

- The "logarithmically divergent on log-log plot" sentence in §4.6.2
  ("$S_{N}$ growing as $\log \log N$ asymptotically") is a description
  of the visual diagnostic on a log-log plot; literally,
  $\log S_{N} \approx \log \log N$ for the harmonic case. The phrasing
  could mislead a reader into thinking the series itself grows as
  $\log \log N$. Consider tightening.

- The perturbation-expansion worked example (§4.7.2) computes the
  $\varepsilon^{2}$ coefficient by collecting like powers; the
  intermediate step labelled "$2 a_{2} + a_{1}^{2} + 2 a_{1} = 0$" can
  be expanded for clarity. The published version should include the
  full algebraic derivation rather than the compressed form.

- Exercise 13.2 (radius of convergence of $\sum (n!) x^{n}/n^{n}$)
  triggers an overfull hbox warning because of the long expression;
  cosmetic only, but a typesetter could split the equation across two
  lines.

## Provisional answers to anticipated review questions

- **Why no $1/(1 - r)^{2}$ in the canonical series list?** It is
  derived as a derived series in §4.4.5 (manipulating Taylor series)
  and appears in Exercise 13.10 (derivation of the Maclaurin
  expansion of $1/(1 - x)^{2}$). The five canonical series stay
  small.

- **Why not introduce big-Theta alongside big-O?** The dossier limits
  this chapter to $O$, $o$, and $\sim$. Big-Theta is the right tool
  for tight asymptotics; it appears in Vol II Ch 17 (algorithms) where
  the asymmetry-of-bounds question becomes load-bearing. Here the
  engineer's working tool is the upper bound and the asymptotic
  equivalence; promoting big-Theta to this chapter would fragment
  attention.

- **Why is Euler's identity in §4.4.6 rather than §4.5 (limits)?**
  Euler's identity is an algebraic consequence of the exponential
  Maclaurin series. Limits as a topic come immediately after, but the
  identity itself does not require limit machinery beyond convergence
  of the underlying series.
