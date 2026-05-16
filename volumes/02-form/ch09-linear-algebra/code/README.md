Code assets, Volume II Chapter 9 (Linear algebra)

Each script is self-contained and runnable with `uv run`:

```
uv run code/<script>.py
```

Files

| File | Purpose | Used by |
|---|---|---|
| `lu_demo.py` | LU factorisation by hand-coded Doolittle elimination on the section 9.3 worked $3 \times 3$; verifies $\mat{L}\mat{U} = \mat{A}$ and back-solves. | Worked example, Calculation exercise 1. |
| `condition_visualiser.py` | Sweeps polynomial degree $p$ from 1 to 12; reports $\kappa(\mat{V})$ and $\kappa(\mat{V}^{\transpose}\mat{V})$ for monomial-on-$[0,1]$, monomial-on-$[-1,1]$, and Chebyshev bases on $100$ equispaced points. Reproduces Figure 9.5. | Section 9.7, Simulation exercise 1, project block. |
| `least_squares_three_ways.py` | Fits a degree-$p$ polynomial to a CSV dataset by normal equations (LU), QR (Householder), and SVD with truncation cutoff. Prints coefficient table, three condition numbers, residual norms. | Project block, Simulation exercise 2. |

Conventions

- Random-number generator seeded for reproducibility (per script).
- Output is human-readable text on stdout; coefficient vectors and conditioning numbers print to four significant figures.
- The least-squares script reads `data/temperature-sample.csv` by default; pass a path argument to use another CSV with two columns `x,y`.

Provenance

Editor's reference implementations. The project block instructs the reader to write their own; the editor's code is a reference to compare against after completing the deliverable.
