# Notes for editor: Vol II Ch 3 (trigonometry, complex numbers, phasors)

Drafted 2026-04-29. Items below are flagged for the general editor;
they touch shared files or pre-existing repository issues that this
chapter's writer was instructed not to edit directly.

## Build-state notes (not introduced by this chapter)

`make strict` does not currently complete on the repository. Two
pre-existing errors halt the build before our chapter can be
verified under `-halt-on-error`:

- `volumes/02-form/ch08-vectors-and-vector-calculus/chapter.tex`
  line 592 uses an undefined control sequence `\Sec` in the form
  `$\Sec~8.2$`. This is presumably a typo for a section reference.
- `volumes/02-form/ch09-linear-algebra/chapter.tex` line 60 uses
  an undefined control sequence `\spn` in `$\spn(\vect{v}_{1},
  \ldots, \vect{v}_{k})$`. Either `\spn` should be defined as a
  math operator macro in `eng-macros.sty`, or the chapter should
  use `\operatorname{span}` directly.

Under regular `make` (not halt-on-error), the full document builds
to a 859-page PDF. Our chapter occupies pages 271 through ~301
(approximately 31 pages of first-draft prose), which sits at the
upper end of the editorial-decisions Q12 floor for first-draft
density and below the 90-page Volume II target; further density
will accumulate during the integration pass.

## Citation policy notes

The chapter cites only `text:strang2016` (already in
`bibliography/references.bib`). Per the chapter dossier and the
brief, no named accident is required for the failure section; the
phase wrap-around mechanism is described generically with worked
domains (laser interferometry, synchrophasors, Doppler radar,
numerical phase computations).

## Cross-volume references

The chapter forward-references:

- Volume II Chapter 4 (Taylor series proof of Euler's identity).
- Volume II Chapter 5 (formal calculus arrival).
- Volume II Chapters 8 and 11 (gradient/divergence in cylindrical
  and spherical coordinates).
- Volume II Chapter 9 (orthogonal groups in formal linear algebra).
- Volume IV (waves and Volume VII (communication chapters) for
  the heterodyne and beat applications.

If any of these chapter numbers shift during integration, the
prose should be re-scanned.

## Voice items

Chapter passes the project's mechanical voice gates:

- 0 em-dashes (`---` or U+2014).
- 0 instances of the AI-tic vocabulary lint list (one occurrence
  of "robust" was rewritten to remove the filler usage).
- Estimation environment present in section 3.3.
- Failure section (3.7) explicit.
- Archetype block (stability) present in section 3.1.
- Principle block in section 3.7 ("The wrap discipline").
- Project block per Q55-vol02-ch03 with optional simulation track.

## Exercise count

Exactly 35, matching `\chapmeta{Exercise target: 35}`. Categories:
calculation (10), derivation (7), estimation (4), simulation (4),
design (2), diagnosis (3), failure analysis (2), judgement (3).

## Open items for review

- The peak-value vs. RMS-value phasor convention is named in
  section 3.4 but not pursued; if a later chapter standardises
  on RMS, the cross-reference should be added.
- The complex-power discussion in section 3.4 introduces
  $S$, $P$, $Q$, power factor without a worked numerical example;
  the chapter project's reflection prompt asks the reader to
  compute power. A worked numerical example might be added in
  the integration pass.
- Section 3.6 (spherical and cylindrical) is a preview only; the
  chapter does not exercise the coordinate systems beyond the
  conversion formulas. Exercises on cylindrical and spherical
  coordinates are deferred to Chapters 8 and 11 per the
  forward-reference convention.
