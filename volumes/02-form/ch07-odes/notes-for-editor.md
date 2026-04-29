# Notes for the editor: Vol II Ch 7 (Differential equations: ODEs)

Items the chapter author would request but cannot resolve from inside the
chapter file.

## Build issue: undefined control sequences in Vol II Ch 9

The chapter compiles cleanly in isolation, producing approximately 30
pages between the section opener and the end of the exercise list. A
direct `pdflatex` run on the full book however halts in
`volumes/02-form/ch09-linear-algebra/chapter.tex` at lines 60, 147,
169, 170, 174, 180, 190, with `\spn`, `\col`, `\rank`, `\nul`
undefined.

These macros are not defined in `preamble.tex`, `eng-macros.sty`, or
any of the chapters that load before Vol II Ch 9. The Vol II Ch 9
shell appears to have been written in a working tree where those
macros are pre-defined; the macros themselves never landed in the
shared preamble. The fix is one of:

1. Add to `eng-macros.sty`:

   ```latex
   \DeclareMathOperator{\spn}{span}
   \DeclareMathOperator{\col}{col}
   \DeclareMathOperator{\rank}{rank}
   \DeclareMathOperator{\nul}{null}
   ```

   (The package `amsmath` is already loaded; `\DeclareMathOperator` is
   the standard idiom for these.)

2. Or rewrite the Vol II Ch 9 prose to use `\operatorname{span}` etc.
   inline.

The first is the lower-friction option and is consistent with the
project's pattern of putting cross-domain notation in
`eng-macros.sty`. The block could sit alongside the existing
`\engterm`, `\repopath`, and `\TODO` definitions.

This is unrelated to Ch 7 and is flagged here only because `make
strict` will not pass the full book until Ch 9 builds.

## Page count vs dossier target

The dossier targets approximately 120 pages (sum of per-section
budgets). The current first-draft compiles to about 30 pages, in line
with the volume-opener guidance that 30-40 page first drafts are
acceptable for the largest chapters.

Closing the gap to 120 pages would require:

- A worked-through derivation of the elliptic-integral exact period
  for the simple pendulum, with the series expansion shown to
  three or four orders.
- An expanded treatment of the Laplace transform as a method for
  linear ODEs (left for Volume VIII per the chapter's current scope,
  but the editor may prefer to introduce it here).
- A formal stability section developing Lyapunov functions beyond
  the preview, with two or three worked examples (linear quadratic
  Lyapunov function, energy function for a damped oscillator,
  construction of $V$ for a non-mechanical system).
- TikZ phase-plane figures: a saddle, a stable spiral, a centre with
  closed orbits, the predator-prey level curves of $H(x, y)$.
- A figure of the frequency response $A(\omega)$ and phase $\varphi
  (\omega)$ for the second-order forced oscillator, parameterised by
  damping ratio.
- A figure of the period-versus-amplitude curve for the simple
  pendulum with the small-angle, first-correction, and exact curves
  overlaid (the chapter's project produces this figure; an
  illustrative version in the body would help the reader before the
  project).
- An expanded numerical methods section with a short formal proof
  of RK4's order, the Butcher-tableau notation, and a brief catalogue
  of modern adaptive methods (Dormand-Prince, BDF, Rosenbrock).

None of these change the chapter's argument; they expand the
apparatus and the worked examples. A subsequent drafting pass should
take them up.

## Bibliography keys cited

The chapter cites two keys:

- `acc:gao-patriot-1992` (the GAO report on the Patriot Dhahran
  incident; already in `bibliography/references.bib`).
- The Boyce-DiPrima textbook (`text:boyce-diprima`) is not currently
  cited in the body. The current draft handles the standard ODE
  apparatus through derivation rather than citation; a future pass
  may want a working-bibliography pointer in the chapter opener
  for readers who want a longer second-source reference.

If the editor prefers an explicit Boyce-DiPrima pointer, it would
naturally sit in §7.1's opening paragraph or in an end-of-chapter
"further reading" note. The closest candidate slot in the current
draft is the introduction to the integrating factor in §7.2.

## Named accidents

The chapter mentions two accidents:

- The Patriot missile system at Dhahran (1991), which is a registry
  entry at `docs/research/accidents/patriot-dhahran-1991.md` (status:
  verified). The chapter's mechanism description aligns with the
  registry's `## Technical mechanism` section. The chapter cites
  `acc:gao-patriot-1992`.
- The Tacoma Narrows Bridge collapse (1940), which is referenced in
  passing as a popular example of resonance whose actual mechanism
  is aeroelastic flutter, with a pointer to the registry entry. The
  registry has `tacoma-narrows-1941.md`. The chapter does not assert
  the resonance reading; it explicitly disclaims it. No additional
  citation is required for this kind of reference, but the editor
  may prefer one for completeness.

`make accidents` should pass cleanly since the only `\cite{acc:*}`
key in the chapter is `acc:gao-patriot-1992`, which has a registry
entry.

## Project track and hazard class

The project is classified as simulation-with-analysis, hazard class
none, per Q55-vol02-ch07. The chapter implements this directly.
The reader does not build a physical pendulum; the simulation is
fully numerical. No mains power, no biological subjects, no
chemicals.

## Reader-path tagging

The chapter follows the standard vol-I pattern:

- core: §7.1 (What an ODE is), §7.2 (First-order linear), §7.3
  (Separable), §7.4 (Second-order linear), §7.5 (Forced response),
  §7.8 (Numerical solvers), §7.9 (Failure), Project, Calculation,
  Estimation, Diagnosis, Failure analysis exercises.
- standard: §7.1 subsection on existence and uniqueness, §7.6
  (Systems), §7.7 (Phase-plane), §7.10 (Worked examples), and
  Derivation, Simulation, Design, Judgment exercises.
- mastery: none in the current draft. A future pass could promote
  the Lyapunov-function preview in §7.7 to a mastery box, and the
  variation-of-parameters formula in §7.6 to a mastery box.

A core-tagged project depends only on core-tagged sections (§7.1,
§7.4, §7.8) and the explicit small-angle-correction derivation in
§7.10 (which is also exercised in the Derivation block). The
core/standard/mastery dependency check should pass.
