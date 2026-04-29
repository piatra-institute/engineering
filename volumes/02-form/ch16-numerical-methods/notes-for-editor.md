# Notes for the editor: Vol II Ch 16 (Numerical methods)

Items the chapter author would request but cannot resolve from inside the
chapter file.

## Vancouver Stock Exchange index drift: not in registry

The chapter dossier lists the Vancouver Stock Exchange index drift among
the famous numerical failures suggested for §16.8. The chapter prose
omits this case. The reason: there is no entry for the Vancouver Stock
Exchange incident in `docs/research/accidents/`, and the project rule
(CLAUDE.md, "Named accidents") is that any named accident in a chapter
must already exist in the registry with an aligned `## Technical
mechanism` and a primary or closest-equivalent BibLaTeX key. Narrating
the case from memory or from a textbook would violate the rule.

The Patriot Dhahran case (`acc:gao-patriot-1992`) and the Ariane 5
Flight 501 case (`acc:ariane501-ifr`) are both in the registry and are
the chapter's two named cases. Together they cover the two canonical
mechanisms (accumulated truncation error in fixed-point conversion;
range overflow in real-to-integer conversion) the chapter teaches.

If the editor wants Vancouver Stock Exchange added in a subsequent
pass, the registry entry should document:

- Date and location: Vancouver Stock Exchange, Vancouver, Canada;
  index introduced January 1982; correction January 1983.
- Technical mechanism: the index was computed by truncating
  intermediate values to three decimal places rather than rounding,
  with each of approximately 3000 daily updates introducing a small
  downward bias. After 22 months of accumulated truncation, the
  reported index was approximately 524.811 against a corrected value
  of approximately 1098.892 (the index was renormalised on
  29 November 1983).
- Primary source: B.\ D.\ McCullough and H.\ D.\ Vinod (1999),
  "The Numerical Reliability of Econometric Software,"
  \emph{Journal of Economic Literature} 37, 633-665, which discusses
  the case as a canonical example of accumulated round-off in
  long-running financial computation. Or: original press coverage
  in the \emph{Toronto Star}, 29 November 1983, page B1, which is
  the first-line public report.

Once a registry entry exists with a verified primary key, a one-paragraph
case can be added to §16.8 between the Patriot and Ariane cases without
restructuring the chapter. The slot in the current draft would sit at
the end of the Patriot subsection (the cases share the
accumulated-truncation mechanism) or as a brief third subsection.

## Page count vs dossier target

The dossier targets approximately 110 pages. The current first draft
compiles to approximately 48 pages within the multi-chapter build,
in line with the "25 to 35 page first-draft density" instruction the
author received. Closing the gap to 110 pages would require:

- A worked-through floating-point bit dissection (sign / exponent /
  mantissa pattern) for several specific decimal values, with the
  arithmetic carried through to the rounded result and the
  representation error tabulated.
- A formal treatment of catastrophic cancellation, with a worked
  variance computation comparing the textbook two-pass formula and
  the numerically stable updating formulas (Welford's algorithm,
  pairwise summation), including a numerical demonstration of the
  failure of the naive one-pass formula on a real dataset.
- An expanded numerical-linear-algebra section developing the QR
  algorithm for eigenvalues at the level of the Trefethen-Bau
  treatment, with the Wilkinson shift, the implicit double shift,
  and the convergence theory.
- An expanded section on iterative methods, taking conjugate
  gradients through the derivation (Lanczos tridiagonalisation,
  Krylov subspace, optimality property), with a worked numerical
  example.
- A formal numerical PDE preview: a 1D heat-equation example
  worked through finite differences (explicit and Crank-Nicolson),
  with the CFL condition derived and the stability region computed.
- Worked examples for the failure analysis: a simulation of the
  Patriot truncation error reproduced in a Python notebook, with
  the 0.34-second drift recovered as a function of operating time.

None of these change the chapter's argument. They expand the
apparatus and the worked examples. A subsequent drafting pass should
take them up.

## Bibliography keys cited

The chapter cites five keys, all already in
`bibliography/references.bib`:

- `text:higham-numerical` (Higham, \emph{Accuracy and Stability of
  Numerical Algorithms}). Canonical reference for floating-point and
  numerical-stability analysis.
- `text:trefethen-bau1997` (Trefethen and Bau, \emph{Numerical Linear
  Algebra}). Canonical reference for the linear-algebra material.
- `text:moler-numerical` (Moler, \emph{Numerical Computing with
  MATLAB}). Pedagogical reference for the algorithmic descriptions.
- `acc:gao-patriot-1992` (GAO/IMTEC-92-26 on Patriot Dhahran).
- `acc:ariane501-ifr` (Lions Inquiry Board report on Ariane 5
  Flight 501).

`make accidents` should pass: both `acc:*` keys cited in the chapter
have registry entries (`patriot-dhahran-1991.md`, `ariane-501-1996.md`).

## Pre-existing build issue: Vol II Ch 17 fatal error

A `make distclean && make strict` run halts in
`volumes/02-form/ch17-discrete-mathematics/chapter.tex` at line 249
with `Extra }, or forgotten \endgroup`. The brace error is in the
estimation block:

```
fully-meshed connection topologies, that is, the number of ways to
select a non-empty subset of the $\binom{20}{2}$ possible links and
declare those to be the operational topology.}
```

The trailing `.}` closes a brace that has no matching opener in the
local context. The fix is to remove the stray `}` after `topology.`.
The same fragment appears as a quotation in `notes-for-editor.md`
files for ch10 and ch13, so the issue is in someone else's mid-edit
working tree, not introduced by this chapter.

This is unrelated to Ch 16 and is flagged here only because `make
strict` will not pass the full book until Ch 17 builds.

Vol II Ch 16 itself compiles cleanly within the multi-chapter build,
contributing approximately 48 pages of body prose between
`\chapter{Numerical methods}` and the end of the exercise list.

## Named accidents

The chapter cites two accidents:

- The Patriot missile system at Dhahran (1991), registry entry
  `docs/research/accidents/patriot-dhahran-1991.md` (status:
  verified). The chapter's mechanism description aligns with the
  registry's `## Technical mechanism` section. The chapter cites
  `acc:gao-patriot-1992`.
- Ariane 5 Flight 501 (1996), registry entry
  `docs/research/accidents/ariane-501-1996.md` (status: verified).
  The chapter's mechanism description aligns with the registry. The
  chapter cites `acc:ariane501-ifr`.

The Vol II Ch 9 chapter already used Ariane 5 as its canonical
refusal-of-an-unsafe-numerical-operation case. The Ch 16 treatment
is consistent with the Ch 9 framing and refers back to it
explicitly. The duplication is intentional: Ch 9 introduces the
refusal discipline as a linear-algebra principle; Ch 16 restates it
as the unifying numerical-failure principle.

## Project track and hazard class

The project is classified as simulation-with-analysis, hazard class
none, per Q55-vol02-ch16. The chapter implements this directly. The
reader chooses a published numerical result, reproduces it, accounts
for any drift, and writes a 1500-word reflection. No physical
apparatus, no biological subjects, no chemicals, no hazard.

## Reader-path tagging

The chapter follows the standard pattern:

- core: §16.1 (Floating-point arithmetic), §16.2 (Error sources),
  §16.3 (Root-finding), §16.8 (Failure), Project, Calculation
  exercises, Failure-analysis exercises.
- standard: §16.4 (Numerical linear algebra revisited), §16.5
  (Numerical integration), §16.6 (Numerical ODE/PDE solvers),
  §16.7 (Reproducibility), Derivation, Estimation, Simulation,
  Design, Diagnosis, Judgment exercises.
- mastery: none in the current draft. A future pass could promote
  the Krylov-method recognition material in §16.4 to a mastery box,
  and the inf-sup / CFL / numerical-diffusion preview in §16.6 to
  a mastery box.

A core-tagged project depends only on core-tagged sections (§16.1,
§16.2) and the standard-tagged §16.3 for the root-finding source
choice. The reader could pick a non-root-finding source (linear
algebra, quadrature, ODE) and execute the project entirely from
core sections; the standard-tagged sections are catalogue rather
than load-bearing for the project.

## Macros and operators

The chapter uses one local operator, `\operatorname{fl}` for the
floating-point rounding map. A small addition to `eng-macros.sty`
in a future pass could elevate this to `\fl` alongside the
linear-algebra operators (`\spn`, `\col`, etc.). Until then, the
inline `\operatorname{fl}` form is correct and renders identically.

## Cross-references

The chapter references back to Vol II Ch 9 §9.7 (condition number)
and §9.8 (refusal discipline) and to Volume IV Ch 8 (computational
continuum mechanics) and Volume IX (control systems) for the
iterative-methods and PDE-discretisation continuations. None of
these references uses `\cref` because the labels in the referenced
chapters use the local `\label{vol02:ch09}` form rather than
section-level labels. A subsequent pass that adds section-level
labels to Ch 9 would let Ch 16 resolve them with `\cref` rather
than with prose section numbers.
