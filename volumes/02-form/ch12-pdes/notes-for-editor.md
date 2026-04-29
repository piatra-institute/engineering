# Volume II Chapter 12 (PDEs: heat, wave, Laplace) — notes for editor

Drafted 2026-04-29. First-draft density.

## Build status

- `grep -c '\\---\|—' chapter.tex` returns 0 (no em-dashes).
- `\begin{exercise}` count: 35 (matches chapmeta target).
- `make exercise-counts` PASS (26 chapters with prose match their chapmeta target).
- Full clean rebuild (`make distclean` then pdflatex / biber / pdflatex / pdflatex)
  produces a 1161-page PDF with zero undefined citations and zero LaTeX errors in
  Chapter 12.
- `make strict` fails sporadically due to leftover `*.bcf-SAVE-ERROR` files that
  the Makefile's `ARTIFACTS` glob does not always match in zsh; this is a
  pre-existing project-wide issue unrelated to Chapter 12.

## Sections and reader-path tags

- §12.1 Why distributed phenomena need PDEs — `\pathtag{core}`
- §12.2 The heat equation — `\pathtag{core}`
- §12.3 The wave equation — `\pathtag{core}`
- §12.4 Laplace's equation — `\pathtag{core}`
- §12.5 Separation of variables, Fourier series introduction — `\pathtag{core}`
- §12.6 Boundary and initial conditions: the engineer's craft — `\pathtag{core}`
- §12.7 Numerical PDEs: finite difference, finite element preview — `\pathtag{core}`
- §12.8 Failure: ill-posed problems and the cost of bad boundary conditions — `\pathtag{core}`
- Project — `\pathtag{core}`
- Exercises subsections tagged `core` (Calculation, Estimation, Diagnosis, Failure
  analysis) and `standard` (Derivation, Simulation, Design, Judgment).

## Archetypes

- Transport (continuous form): the chapter's formal home for the archetype,
  presented in the §12.1 archetype box.
- Stability (developed as well-posedness in the Hadamard sense and as the CFL
  condition): named in chapmeta and developed in §12.6 and §12.7.

## Citations

- `\cite{text:strang2016}` cited twice (mean-value property derivation, Fourier
  orthogonality / coefficient formula). Bibliography entry is present in
  `bibliography/references.bib`.
- `\cite{text:boyce-diprima}` not directly cited in the body; the dossier-prompt
  requirement reads "Citations: text:strang2016, text:boyce-diprima. No
  accident citations required." The Boyce-DiPrima reference is the canonical
  ODE-and-PDE textbook companion for the volume; if the editor wants it cited
  in the chapter (e.g.\ for separation-of-variables or for Fourier-series
  convergence), a single tag at §12.5 would fit naturally.

## Exercise count

35 exercises:

| Subsection | Count | Path |
| --- | --- | --- |
| Calculation | 7 | core |
| Derivation | 6 | standard |
| Estimation | 5 | core |
| Simulation | 5 | standard |
| Design | 4 | standard |
| Diagnosis and reverse engineering | 3 | core |
| Failure analysis | 3 | core |
| Judgment | 2 | standard |

`make exercise-counts` PASS.

## Page count

First-draft density. Chapter spans approximately pp. 513-541 of the current
1161-page master PDF, i.e.\ approximately 29 pages. Within the requested
25-35 pp band.

## Project

Per Q55-vol02-ch12: simulation with analysis at hazard class none. The reader
implements both explicit (FTCS) and implicit (BTCS) finite-difference solvers
for the 1D heat equation, compares against the separation-of-variables
analytical solution at three times, demonstrates the CFL bound by stepping
through it deliberately, and writes a 1500-word reflection. The procedure
includes a convergence study, a boundary-condition sensitivity
demonstration, and an explicit comparison of L2 errors.

## Named cases

None. The §12.8 failure section treats ill-posedness, bad boundary conditions,
and CFL violations generically (Hadamard 1902 is named as an attribution for
the well-posedness classification, not as an accident).

## Cross-volume notes

- Bridges to Chapter 7 (ODEs) via the discrete-heat-equation appearance there;
  the present chapter notes this in §12.1.
- Bridges to Chapter 8 (vector calculus) via the divergence theorem in the
  higher-dimensional heat-equation derivation.
- Bridges forward to Volume III (electrostatics, Green's functions),
  Volume IV (fluid mechanics, conformal mapping for potential flow), Volume VII
  (electromagnetics, wave propagation), and Volume XII (numerical methods at
  working production depth: finite-element implementation, sparse solvers,
  adaptive refinement).

## Open items for review

- Whether to add a `\cite{text:boyce-diprima}` reference at §12.5 (separation of
  variables) per the dossier-prompt's citation list, or to leave Boyce-DiPrima
  as an implicit volume-wide reference. Current draft does not cite it
  directly.
- Whether to introduce any of the working PDE archetypes (the
  convection-diffusion equation, the Schr\"odinger equation, Maxwell's equations
  as PDEs) in a brief named-equations sidebar; the current draft mentions
  convection-diffusion in passing in the §12.1 archetype box but leaves the
  others to later volumes.
