# Notes for the editor: Vol II Ch 6 (Integration)

Items the chapter author would request but cannot resolve from inside
the chapter file.

## Page count vs dossier target

The dossier targets approximately 110 pages (sum of per-section budgets
plus apparatus). The current draft compiles to about 28 pages (pages
355-382 in the build dated 2026-04-29), which is in line with the
released Volume I chapters (Ch 7 is roughly 26 pages of body; Ch 8 is
roughly 28). Closing the gap to 110 would require: a worked
TikZ-illustrated walkthrough of the Riemann-sum convergence in section
6.1, a fully worked partial-fractions example with an irreducible
quadratic factor in section 6.3, a side-by-side error plot of the
trapezoidal, Simpson, and Gauss-Legendre rules on a chosen integrand
in section 6.5, an explicit worked Jacobian for spherical coordinates
in section 6.6, and a TikZ figure of the impulse-response convolution
of two box functions in section 6.7. None of these change the
chapter's argument; they expand the apparatus.

## Cross-references to Ch 5

The chapter cross-references Ch 5 in prose (the chain rule for
substitution, the product rule for integration by parts, the
discussion of bias-variance in numerical methods). These are made in
prose rather than via `\cref{}` because Ch 5's section labels are not
currently exposed as cross-reference targets (Ch 5 is still a stub at
the time of writing). When Ch 5 is drafted, the editor may wish to
replace the prose references with explicit `\cref{}` to specific
sections.

## The Vol I Ch 7 cross-reference in the project

The chapter's project text refers to the Vol I Ch 7 project (volume of
an irregular household object by three methods). The reference is
made in prose; if the editor wants an explicit `\cref{vol01:ch07}` or
similar, the section labels of the Ch 7 project block should be
added to that chapter first.

## The compatibility-ratio formula in the project

The project's reconciliation step uses the compatibility-ratio formula
$r = |x_{A} - x_{B}| / \sqrt{u_{A}^{2} + u_{B}^{2}}$, which was
introduced in Vol I Ch 4 (uncertainty propagation) and applied in Vol
I Ch 7 (volume of an irregular household object). The chapter cites
this in prose; an explicit `\cref{}` to Vol I Ch 4 would tighten the
trail if the relevant section labels are exposed.

## Citation policy

The chapter cites only `text:strang2016` once, in section 6.6, as the
underwriting reference for the determinant theory behind the Jacobian
in change-of-variables. The chapter intentionally does not name a
historical accident: section 6.8's failure discussion is generic
(divergent integrals, oscillatory aliasing, numerical instability,
heavy-tailed expectations) per the dossier (`make accidents` does not
need to scan it). If the editor prefers a named-case citation in the
failure section, the Patriot Dhahran 1991 case in
`docs/research/accidents/patriot-dhahran-1991.md` is a strong fit
(its mechanism is accumulated floating-point error in a fixed-point
time integration), but the existing prose already carries the
abstract lesson without naming the case.

## The Cauchy-distribution failure example

Section 6.8 uses the Cauchy distribution as the working example of an
integral that does not converge in the sense the engineer needs. This
overlaps with Volume II Chapter 13 (Probability), which is currently
a stub. When Chapter 13 lands, the editor may wish to standardise the
treatment between chapters: either keep the Cauchy diagnosis here as
a probability foreshadow, or move the full diagnosis to Chapter 13
with a brief reference in this chapter.

## TikZ figures not yet drawn

The chapter contains no figures. Five places where a TikZ figure
would help the reader:

1. Section 6.1: a Riemann-sum picture with three nested partitions
   showing the convergence to the integral.
2. Section 6.5: a side-by-side picture of the trapezoidal,
   Simpson, and Gauss-Legendre node placements on the same
   interval.
3. Section 6.5: an error-vs-step-size log-log plot of the three
   rules on a chosen smooth integrand.
4. Section 6.7: the convolution of two box functions, drawn as a
   sequence of frames showing the slide-and-multiply construction.
5. Section 6.9: the centre-of-mass and moment-of-inertia
   integrations of a thin rod, drawn as a labelled diagram.

Each is a 5-15 line TikZ block; they would close roughly 8-12 of the
80-page gap to the dossier target.

## Project deliverable file

The project's deliverable specifies a comparison table, three method
records, and a reflection. A template spreadsheet that the reader
can copy and fill (one tab per method, one summary tab) would
accelerate the project. If the editor agrees, the file would live at
`volumes/02-form/ch06-integration/project-template.xlsx` (or
`.csv`) and be referenced from the project text.
