# Data assets - Volume II, Chapter 11 (Multivariable calculus)

Frozen reference data tables produced by the chapter's `code/`
scripts, committed so a reader who does not run the scripts can
still consult the numbers used in the chapter's prose and exercises.

## Files

| File | Generator | Description |
|---|---|---|
| `volume_concentration.csv` | `code/volume_concentration.py` | Per-dimension table of outer-shell volume fractions (for $\varepsilon = 0.01, 0.05, 0.10$) and the inscribed-ball-to-cube ratio $V_{n}(1) / 2^{n}$, analytical and Monte Carlo, for $n \in \{2, 3, 5, 10, 20, 50, 100, 500, 1000\}$. Used by the failure-section figure (`figures/fig-volume-concentration.tex`). Monte Carlo column is zero for $n \geq 20$ because $50\,000$ uniform cube samples is insufficient to capture the ball at those dimensions. |
| `critical_points_sincos.csv` | `code/critical_points.py` | Twelve critical points of $f(x, y) = \sin(x)\cos(y)$ on $[0, 2\pi]^{2}$, with Hessian eigenvalues and classification. Used by the Simulation exercise on numerical critical-point location. |

## Reproducibility

Regenerate from the worktree root:

```
cd volumes/02-form/ch11-multivariable-calculus/code
uv run volume_concentration.py
uv run critical_points.py > ../data/critical_points_sincos.csv  # adjust the script to emit CSV if needed
```

The reference seed in `volume_concentration.py` is fixed to
`20260516`, the date of the chapter's last verified build, so the
Monte Carlo numbers reproduce exactly. The analytical columns are
deterministic in floating-point arithmetic.

## Source

Authors' computation from the chapter's analytical formulas. The
inscribed-ball / cube ratio is the closed form $V_{n}(1) / 2^{n} =
\pi^{n/2} / (2^{n}\,\Gamma(n/2 + 1))$ evaluated by `lgamma`. The
Monte Carlo column is an independent verification by uniform
sampling.
