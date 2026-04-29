# Notes for editor: Vol II Ch 10 (Eigenvalues and decompositions)

## Pre-existing build error elsewhere blocking `make strict`

`make strict` after a clean rebuild fails on a fatal LaTeX error inside
`volumes/02-form/ch17-discrete-mathematics/chapter.tex` at line 249:

```
declare those to be the operational topology.}
```

The closing brace is unmatched. The line lives inside an `\begin{estimation}` block opened at line 242 with `\textbf{Question.}` (already closed). The stray `}` is independent of Vol II Ch 10's drafting and predates this draft. The error does not arise from `volumes/02-form/ch10-eigenvalues-and-decompositions/chapter.tex`. `make check`, `make audit-docs`, and the per-chapter `exercise-counts` for Ch 10 (35 of 35) all pass.

Suggested fix: delete the stray `}` at end of line 249 of `volumes/02-form/ch17-discrete-mathematics/chapter.tex`.

## Cross-references

The chapter cross-references Vol II Ch 9 sections by section number (e.g.\ "section 9.7" rather than `\autoref`). This matches the Vol II Ch 9 prose style. If the editor prefers `\cref{vol02:ch09}` cross-references, the substitutions are local to the prose body of sections 10.3, 10.4, and the Project block.

## Named cases

The dossier permits omitting a named accident; the chapter's failure section (10.7) treats defective and complex-eigenvalue regimes generically as instructed. No accident registry entry is therefore added.

## Optional follow-ups

- A figure of the SVD geometric picture (unit ball mapping to ellipsoid through $\mat{V}\transpose$, $\mat{\Sigma}$, $\mat{U}$) would help section 10.3. Deferred to figure-acquisition stage.
- A scree plot example accompanying the worked PCA in section 10.8 would reinforce the truncation discussion. Deferred similarly.
