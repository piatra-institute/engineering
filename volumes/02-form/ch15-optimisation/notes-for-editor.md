# Notes for editor: Vol II Ch 15 Optimisation

## Build infrastructure issue (shared, not from this chapter)

`make distclean && make strict` fails on the second pdflatex pass with

```
[1070] (./main.aux! Unable to read an entire line---bufsize=200000.
Please increase buf_size in texmf.cnf.
```

The error appears after the appendices have rendered (page 1070 reached) and pdflatex re-opens `main.aux` for the cross-reference resolution pass. The longest line in `main.aux` measured directly is 375 characters; the buffer limit reported is 200000. The mismatch suggests pdflatex internally allocates a larger token expansion when reading some single `\newlabel` or `\@writefile` entry. With the latest chapter additions the document is at 1083 pages, past the 928-page baseline noted in `CLAUDE.md` "Status".

The error is not caused by this chapter. Removing this chapter from `main.tex` does not change the position at which the buffer is exhausted (the error occurs after all 174 chapters and the appendices have been read).

Recommended remediations for the editor (any one of these resolves it):

1. Set `buf_size = 1000000` in a project-local `texmf.cnf` (pre-launches the existing TeX Live install with the larger buffer).
2. Add `-extra-mem-bot=200000000 -buf-size=1000000` to the latexmk pdflatex args in `Makefile`.
3. Run `pdflatex` with `--buf-size=1000000` once, then resume normal `make`.

The chapter itself compiles cleanly through pdflatex's first pass. The "Output written on main.pdf (1083 pages)" message confirms the chapter typeset; only the cross-reference resolution pass fails on the buffer size.

## Project-track resolution applied

Q55-vol02-ch15 (settled 2026-04-29 in `editorial-decisions.md`) was applied: gradient descent from scratch (vanilla, plus at least one of momentum/Nesterov/RMSProp/Adam) on a chosen objective (polynomial-fit, Rosenbrock, small neural-network loss, or logistic regression). The project's "1500-word reflection" requirement is included; the suggested objectives include the Vol II Ch 9 polynomial-fit problem as the canonical convex reference.

## Citation usage

- `text:boyd-vandenberghe2004` cited in chapter opener (canonical reference for the chapter), in convex-function-library passage (Section 15.2.2), in QP/SOCP/SDP passage (Section 15.3.3), in approximation-algorithms passage (Section 15.7.5), and in one judgment exercise.
- `text:strang2016` cited in chapter opener (linear-algebra machinery), in approximation-algorithms passage (Section 15.7.5), and in one judgment exercise.
- `text:cormen-clrs` and `text:kleinberg-tardos` cited (recognition level) for combinatorial-optimisation pointer in Section 15.7.5.

## Archetype placement

The chapter announces itself as the formal home of the optimisation archetype in the chapter opener and in the Section 15.2 archetype block "Optimisation, formal home." The Vol II Ch 5 ("Optimisation, first formal introduction") and Vol II Ch 11 ("Optimisation, multivariable form") archetype blocks are referenced as the local cases. No new archetype is invoked elsewhere; scaling is mentioned in `\chapmeta` but not given its own block (it appears organically through condition number, dimensionality scaling of branch-and-bound, and large-N motivation for SGD).

## Exercises

40 exercises across 8 Q16 categories: Calculation 6, Derivation 6, Estimation 5, Simulation 5, Design 5, Diagnosis 4, Failure analysis 4, Judgment 5. Total exactly 40, matching the chapmeta target. `make exercise-counts` PASSES on this chapter (the two failures it reports are pre-existing in ch12-pdes and ch16-numerical-methods, unrelated to this work).

## Hard-constraint verification

- `grep -c '\---\|—' volumes/02-form/ch15-optimisation/chapter.tex` returns 0 (no em-dashes).
- 40 exercise blocks (see above).
- All math operators used (`\spn` not used; `\diag`, `\argmin`, `\argmax`, `\transpose`, `\grad` all from `eng-macros.sty`).
- `\repopath{}` used for the SciPy reference path.
- "We" voice throughout; no negate-first-then-pivot constructions; no AI-tic vocabulary; no self-announcing topic sentences.

## Open editorial questions raised by this chapter

1. Should the failure section's "optimisation theatre" treatment cite a specific named instance (e.g. Volkswagen diesel 2015, already in the registry) or stay generic? Currently the section is generic with the worked overfit example, per the brief's "treat generically with worked example" instruction.
2. The chapter mentions Goodhart's law as a principle but cites no primary source; Goodhart's 1975 lecture is the original. The bibliography does not currently have a `paper:goodhart1975` entry. Suggested addition for a future review pass.
3. Section 15.5 mentions L-BFGS through SciPy's `minimize` interface. The repo path reference uses `\repopath{scipy.optimize.minimize}`, which is a Python module path rather than a repo path. The `\repopath` macro is currently the only macro for code-style paths; a reviewer may prefer `\verb|...|` here. Left as-is for first draft.
