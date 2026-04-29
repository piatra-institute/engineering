# Notes for editor: Vol II Ch 2 (Functions and graphs)

Drafted: 2026-04-29.

## Pre-existing build breakages encountered (not introduced by this chapter)

When running `make distclean && make strict`, the build fails partway
through with fatal errors in chapters other than this one:

1. `volumes/02-form/ch09-linear-algebra/chapter.tex` uses `\spn`,
   `\col`, `\rank`, `\nul` (linear-algebra operator macros). None of
   these is defined in `eng-macros.sty` or `preamble.tex`. The first
   `\spn` (line 60 of ch09) is the fatal stop; the subsequent
   `Undefined control sequence` errors compound. Suggested fix: add
   `\DeclareMathOperator{\spn}{span}`,
   `\DeclareMathOperator{\col}{col}`,
   `\DeclareMathOperator{\rank}{rank}`,
   `\DeclareMathOperator{\nul}{null}` to `eng-macros.sty`. (The
   conventional spellings vary across textbooks; an editor should
   pick the convention before adding the macros.)

2. `make exercise-counts` fails on `ch01-algebra-and-proof`
   (target 35, actual 32) and `ch03-trigonometry-complex-phasors`
   (target 35, actual 36). This chapter (ch02) passes
   exercise-counts at 30/30.

## Chapter-level notes

- The Strang reference (`text:strang2016`) was suggested in the
  brief but is on linear algebra, not pre-calculus. This chapter
  does not cite it; the pedagogical anchor for graph-reading is
  Polya (`gen:polya1945`) cited inside a mastery box. If the editor
  has a preferred pre-calculus or graphical-reasoning reference
  (a Strang calculus volume; Tufte; Mahajan), it could be slotted
  into Section 2.6 as a citation for the frame-check discipline.

- The Challenger pre-launch chart-preparation case is treated only
  as a chart defect. The Rogers Commission report is cited as the
  primary source. The named-cases chapmeta entry notes the case is
  briefly used here and properly developed in Volumes X chapters 9
  and 11. This follows the cross-chapter citation pattern from
  Vol I Ch 2's Hubble subsection.

- Section 2.4 (Trigonometric functions) is intentionally short
  (`\pathtag{standard}`) because the full trigonometric apparatus
  arrives in Vol II Ch 3 (trigonometry, complex numbers, phasors).
  The chapter's stated scope is functions-as-objects; Ch 3 owns
  the apparatus. If the editor prefers a fuller trig treatment
  here, the dossier's section 2.4 page allotment (10 pp) supports
  expansion.

- Q55-vol02-ch02 is fully resolved by the project section: 10-plot
  diagnostic write-up plus 1500-word reflection, analysis-only,
  hazard class none.

- The chapter's failure section names three cases (Challenger,
  Mars Climate Orbiter, Air France 447). Mars and AF447 are
  briefly revisited from Vol I; Challenger is the chapter's
  load-bearing graph-reading case. All three are in the
  `\chapmeta{... Named cases: ...}` block and `make accidents`
  PASSes.
