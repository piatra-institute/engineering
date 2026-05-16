# Code assets — Volume II, Chapter 4 (Sequences, series, limits)

Each script is self-contained and runnable with `uv run`:

```
uv run code/<script>.py
```

## Files

| File | Purpose | Used by |
|---|---|---|
| `harmonic_partial_sums.py` | Computes harmonic partial sums at decades and compares to the asymptotic $\log N + \gamma$. | Simulation exercise on harmonic partial sums. |
| `alternating_harmonic.py` | Computes alternating-harmonic partial sums and confirms the alternating-series error bound. | Simulation exercise on alternating harmonic. |
| `taylor_sin_error.py` | Tabulates the empirical Taylor-truncation error for $\sin x$ at orders 1, 3, 5, 7, 9 against the Lagrange remainder bound. | Simulation exercise on Taylor polynomials of $\sin$; second estimation block. |
| `newton_sqrt2.py` | Newton's iteration for $\sqrt{2}$ from $a_0 = 1$, tabulating the residual at each step. | Simulation exercise on Newton's iteration. |
| `convergence_comparator.py` | Side-by-side iteration-count tables for fixed-point (linear), Newton (quadratic), and secant ($\phi$-order) iterations to a fixed tolerance. | Second estimation block; diagnostic exercise on convergence-rate identification. |
| `series_test_picker.py` | Walks the convergence-test decision tree of figure `fig:vol02:ch04:test-decision-tree` on a small catalog of series and prints the test that settles each. | Pedagogical companion to section 4.3 and the test decision-tree figure. |

## Conventions

- Random-number generator seeded for reproducibility where used (none of these scripts is stochastic; floating-point determinism is sufficient).
- Output is human-readable text on stdout, not files.
- Numerical comparisons use `math.isclose` with a stated relative tolerance.

## Provenance

Editor's reference implementations. Verify with your own tools.
