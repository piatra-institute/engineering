# Notes for editor: Vol II Ch 1 (Algebra and proof discipline)

Author run: 2026-04-29.

This chapter passes its own verification gates. The two items below
are pre-existing repository conditions in other files, not introduced
by this chapter.

## 1. `make strict` fails on pre-existing chapter shells, not on this chapter

`make distclean && make strict` fails before completing because of
undefined macros in two other Volume II chapter shells that have been
populated with prose by an earlier pass:

- `volumes/02-form/ch08-vectors-and-vector-calculus/chapter.tex`
  has been drafted with prose but has at least one undefined control
  sequence, surfacing as a fatal `! Undefined control sequence` (the
  earlier strict pass reported a stray `\Sec` near line 592, though
  the chapter file is currently in flux during the parallel-author
  pass).
- `volumes/02-form/ch09-linear-algebra/chapter.tex` uses `\spn`,
  `\col`, `\rank`, `\nul` which are not defined in `eng-macros.sty`.
  Fatal at first occurrence, line 60 onward.

Recommended fix outside this chapter (one of):

- Add `\DeclareMathOperator{\spn}{span}`, `\rank`, `\col`, `\nul` to
  `eng-macros.sty` (the linear-algebra macro family the next pass
  will need anyway).
- Or guard those drafted chapters from compilation until they are
  ready by commenting their `\input` lines in `main.tex` until their
  authors land them.

Verification limited to this chapter alone: with `latexmk -pdf -f`
(force through pre-existing errors elsewhere), this chapter compiles
to PDF without any error or warning attributable to it. The chapter
occupies pages 224-251 of the running compile, i.e. about 27 pages,
within the Vol I 25-35pp acceptance window.

## 2. `make exercise-counts` flags two unrelated chapters

`make exercise-counts` reports failures for `ch05-differentiation`
(target 40, actual 35) and `ch09-linear-algebra` (target 40, actual
39). This chapter (`ch01-algebra-and-proof`) reports `target 35,
actual 35` and is correct.

## 3. No new bibliography entries needed

The chapter cites `gen:polya1945`, `text:strang2016`,
`acc:nasa-mco-mib`, `acc:lockwood-gimli1985`, and `acc:ariane501-ifr`,
all already present in `bibliography/references.bib`.

## 4. No new accident-registry entries needed

The chapter names Mars Climate Orbiter (1999), Air Canada Flight 143
(1983), and Ariane 5 Flight 501 (1996); all three have verified
registry entries under `docs/research/accidents/` and are listed in
this chapter's `\chapmeta` Named-cases line. `make accidents` PASS.
