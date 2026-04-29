# Notes for the editor: Vol II Ch 9 (Linear algebra)

Items the chapter author would request but cannot resolve from inside
the chapter file.

## Page count vs dossier target

The dossier targets approximately 110 pages. The current first draft
compiles to about 22 pages (chapter 9 spans pages 445-466 in the
current build). This is in line with the first-draft density of the
released Volume I chapters (Ch 8 is roughly 28 pages of body) and
well short of the dossier number.

Closing the gap would require, in roughly the order an expansion
pass should take them:

1. A worked Householder QR walk-through in §9.3, including the
   reflector geometry and a numerical step-by-step on a $4 \times 3$
   matrix. Currently the algorithm is named and its cost stated but
   not shown working.
2. A second worked example in §9.6 on a moderate-size polynomial fit
   (degree 4 on 20 data points), comparing the normal-equations and
   QR coefficients side by side, ahead of the project. This grounds
   the conditioning argument before the project asks the reader to
   reproduce it.
3. A TikZ figure in §9.5 illustrating the orthogonal projection
   geometrically (vector $\vect{b}$, subspace $W$, projection
   $\proj_{W}\vect{b}$, residual $\vect{b} - \proj_{W}\vect{b}$).
4. A TikZ figure or numerical table in §9.7 of the
   condition-number-versus-degree relationship for the Vandermonde
   matrix on equally-spaced points, which gives the "rule of thumb"
   teeth.
5. A second estimation block (the chapter currently has one). One
   candidate: estimate the operation count required to factor a
   million-equation finite-element stiffness matrix by sparse direct
   methods.
6. Optional mastery-box derivations for the rank-nullity theorem and
   for the singular-value characterisation of the condition number.
   The algebra is light and the reader benefits from seeing it.

None of these change the chapter's argument; they expand the
apparatus.

## Macros

The chapter uses `\spn`, `\col`, `\nul`, `\rank`, `\sgn`, `\proj`,
which are not currently in `eng-macros.sty`. The chapter declares
them locally with `\providecommand` (see the top of `chapter.tex`).
These are likely to recur across Volume II chapters 10 (eigenvalues),
11 (multivariable calculus), 12 (PDEs), and 14 (statistical
inference), so the cleaner solution is to promote them to
`eng-macros.sty`. The proposed additions:

```latex
% === Linear algebra operators ===
\newcommand{\spn}{\operatorname{span}}
\newcommand{\col}{\operatorname{col}}
\newcommand{\nul}{\operatorname{null}}
\newcommand{\rank}{\operatorname{rank}}
\newcommand{\sgn}{\operatorname{sgn}}
\newcommand{\proj}{\operatorname{proj}}
```

Once promoted, the chapter's local `\providecommand` block becomes
redundant and can be removed in an integration pass.

## Cross-references to Volume I Chapter 8

The chapter cross-references Volume I Chapter 8's straight-line fit
and its uncertainty machinery in three places (the opener, the
worked example in §9.6, the design-matrix discussion in §9.6). The
references are made in prose because Ch 8's section labels are not
exposed for `\cref{}` use. Adding labels to Ch 8 §8.1 and §8.4 (the
summary statistics and the confidence-interval section) and using
`\cref{}` here would tighten the cross-volume connection. This is a
small editorial pass on Ch 8, not on this chapter.

## Cross-reference to Volume II Chapter 10 (eigenvalues, SVD)

The chapter introduces the SVD at recognition level in §9.7 with
the note that Volume II Chapter 10 develops its derivation. When
Chapter 10 is written, its SVD derivation should reference
back to this chapter's §9.7 cutoff-and-truncation discussion, which
the project relies on. The `\cref{vol02:ch09}` cross-reference is
in place; the reciprocal needs to wait for Chapter 10's prose.

## Citation tier

The chapter cites two textbook references and one accident
report:

- `text:strang2016` (Strang, *Introduction to Linear Algebra*) as
  the canonical reference for the algebraic content (subspaces,
  rank, projection).
- `text:trefethen-bau1997` (Trefethen and Bau, *Numerical Linear
  Algebra*) as the reference for the numerical content (operation
  counts, Householder QR, conditioning, SVD).
- `acc:ariane501-ifr` (Lions Inquiry Board) as the primary
  source for the §9.8 case.

No standards (`std:`) keys are cited. The IEEE 754
floating-point standard is mentioned in §9.7's overflow
discussion; if the editor wants a standards anchor, IEEE
754-2019 is the natural addition. It is not currently in
`bibliography/references.bib`. The mention is general enough
that the chapter does not require the citation, but the editor
may prefer to add it for completeness.

## Project: reference solution

The project asks the reader to fit a polynomial three ways on a
dataset of their choice. The general editor's reference solution,
mentioned in the project text as available online, has not been
written. A reasonable reference dataset is a year of NOAA
daily-mean temperature readings from a single station, on which a
degree-5 polynomial fit shows the conditioning trouble described
in §9.7 cleanly. The reference solution should be ~1500 words plus
code, deposited in a project-solutions repository, and linked from
the published edition.

## Half-life tag and the SVD section

The chapter's half-life tag is "foundational." The §9.7
recognition-level treatment of the SVD references Volume II
Chapter 10 for the full derivation. When Chapter 10 lands, the
editor should consider whether §9.7's SVD subsection should be
demoted or replaced by a short forward-reference, to avoid
redundant exposition. Currently the section earns its place by
the truncated-SVD apparatus the project depends on, even before
Chapter 10's derivation.

## Reader-path tagging audit

The chapter tags §9.1, §9.2, §9.3, §9.5, §9.6, §9.7, §9.8 as `core`,
§9.4 as `standard`. The exercise sets are tagged `core` (Calculation,
Estimation, Diagnosis, Failure analysis), `standard` (Derivation,
Design, Judgment), and `mastery` (Simulation). The project is tagged
`core`. The project does not depend on the `standard` Determinants
section; it depends on §9.6 (core) and §9.7 (core). The reader-path
discipline holds. The editor may want to demote the Determinants
section to a fuller `standard` treatment by adding the geometric
derivation; the current section is recognition-level and adequate
for the chapter's working content.
