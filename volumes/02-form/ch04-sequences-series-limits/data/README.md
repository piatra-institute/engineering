# Data assets — Volume II, Chapter 4 (Sequences, series, limits)

## Files

| File | Source | Used by |
|---|---|---|
| `small_angle_errors.csv` | Computed by the editor from the exact $\sin\theta$, $\cos\theta$, $\tan\theta$ and the leading and next-order Taylor truncations at six angles ($1^{\circ}$, $5^{\circ}$, $10^{\circ}$, $25^{\circ}$, $45^{\circ}$, $60^{\circ}$). | Project (error tabulation step), small-angle figure, judgment exercise on the small-angle rule. |
| `taylor_sin_orders.csv` | Output of `code/taylor_sin_error.py`: empirical truncation error vs Lagrange bound for $\sin x$ at orders $1, 3, 5, 7, 9$ and $x \in \{0.5, 1.0, 1.5, 2.0\}$. | Simulation exercise on Taylor polynomials of $\sin$; figure `fig:vol02:ch04:taylor-error`. |
| `harmonic_decades.csv` | Output of `code/harmonic_partial_sums.py`: $H_N$ at $N = 10^{1}\ldots 10^{6}$ and the gap to $\log N + \gamma$. | Simulation exercise on harmonic partial sums; failure section. |

## Provenance

All values are computed (not measured). The computations are exact
to floating-point precision; reproducibility is by running the
corresponding `code/*.py` script under `uv run`.

## Conventions

- Angles given in both degrees and radians where both are relevant.
- Errors stated in both absolute and relative form when both are
  informative.
- Floating-point output truncated to the precision that supports the
  pedagogical point; the underlying computation is double precision.
