# Notes for editor: Vol II Ch 8 (Vectors and vector calculus)

## Build status

- `grep -c '\---\|—' chapter.tex` returns `0`. Em-dash discipline holds.
- `make exercise-counts` reports my chapter as PASS at target 35, actual 35. The target itself reports FAIL because of pre-existing mismatches in ch05 and ch09.
- `make distclean && make strict` halts before completion at a pre-existing error in `volumes/02-form/ch09-linear-algebra/chapter.tex` line 60, where `\spn` is used but is not defined in `eng-macros.sty` or `preamble.tex`. The error sits past my chapter in the input stream; my chapter itself compiles cleanly. Two paths to a green strict build, neither in scope for Ch 8:
  - Define `\newcommand{\spn}{\operatorname{span}}` in `eng-macros.sty`, or
  - Replace `\spn` with `\operatorname{span}` in ch09's prose.

A non-strict `make` from a clean state runs to completion: I confirmed a 921-page PDF was generated.

## Notation choices made

- Vectors set in boldface throughout: `\vect{v}` (the existing `\vect` macro). The `\vec{}` form is mentioned once in section 8.1 as alternate working notation but not used.
- `\oint` is used for both line and closed-surface integrals in this chapter. The double-integral surface symbol `\oiint` is not available in the current preamble (no `esint` package). If `esint` is added later, `\oint` in surface-integral contexts could be mechanically upgraded.
- `\unitvec`, `\norm`, `\inner`, `\set`, `\divg`, `\curl`, `\grad`, `\laplacian`, `\dd`, `\dv`, `\pdv`, `\transpose`, `\inv` all used as defined in `eng-macros.sty`.

## Cross-volume references

- The chapter references `\cref{vol02:ch10}` (linear algebra) for the determinant test of linear independence. Ch 10's label is `vol02:ch10`; the ref will resolve once the whole document compiles.
- The chapter references Volume I Chapter 7 (length-area-volume-mass) by description rather than `\cref` because the project explicitly reconciles against that chapter's water-displacement result. Editor may upgrade to `\cref{vol01:ch07}` if desired.
- The chapter references Volume II Chapter 12 for the heat equation, Laplace, and Poisson; Volume III for rigid-body kinematics, conservative forces, magnetostatics; Volume IV for electromagnetism; Volumes VIII/IX for inertial navigation and control. All by description, not `\cref`.

## Citation

- Single citation, `\textcite{text:strang2016}` in the epigraph and the body. The chapter could plausibly cite `text:trefethen-bau1997` for the Helmholtz decomposition discussion; declined to keep citation density honest.

## Project artifact

- The project is the Q55-vol02-ch08 hybrid: divergence theorem applied to a sampled household-object surface, reconciled against Vol I Ch 7's water-displacement. The 1500-word reflection is specified per the editorial-decisions Q55-vol02-ch08 wording.
- Per-triangle volume formula derived in Exercise 13 (Derivation set). The full divergence-theorem-from-position-vector derivation is Exercise 12.

## Failure section

- Treats orientation errors generically as instructed by Q55-vol02-ch08. No named accident; no registry entry needed. The worked counterexample (a piecewise unit-cube parametrisation that flips the bottom-face normal) is constructed in section 8.8 and reused in Exercise 28.

## Page count

- LaTeX preview page count for this chapter (within the 921-page main build) is approximately 35-40 pages of body plus exercises. First-draft density target met.

## Open editorial questions for the chapter

- The chapter takes the physics convention for spherical coordinates ($\theta$ polar, $\phi$ azimuthal). The mathematics convention swaps these. Volume II's other chapters should agree on one convention; the editor may want to confirm the other Vol II chapters use the physics convention or flag conflicts.
- The "active vs passive transformations" distinction in §8.3 is signalled but not exhaustively developed; Volume III will own it. If the editor wants more in §8.3, the natural extension is one worked example showing the inverse-transpose relation between the two.
- The Frenet-Serret formulas are mentioned in §8.4 but not stated. They belong in Volume III's rigid-body kinematics chapter; flagging here in case the editor prefers them stated in this chapter as a reference.
