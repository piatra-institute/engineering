# Code assets — Volume I, Chapter 4 (Error and uncertainty)

Each script is self-contained and runnable with `uv run`:

```
uv run code/<script>.py
```

## Files

| File | Purpose | Used by |
|---|---|---|
| `correlated_sum.py` | Empirical sd of $x + y$ for correlated normals (Simulation exercise 1). | Simulation exercise 1. |
| `clt_uniform.py` | CLT convergence for the sample mean of a uniform parent (Simulation exercise 2). | Simulation exercise 2. |
| `pendulum_mc.py` | Monte Carlo propagation per JCGM 101 for the pendulum $g$-measurement; comparison to linear propagation. | Section 4.3, Simulation exercise 3. |
| `cauchy_mean.py` | Sample mean of Cauchy variables: CLT fails (Simulation exercise 4). | Simulation exercise 4. |
| `common_mode.py` | Monte Carlo of $x_1 - x_2$ for correlated normals; common-mode cancellation (Judgment exercise on common-mode). | Section 4.3, Judgment exercise on $y = x_1 - x_2$. |

## Conventions

- Random-number generator seeded for reproducibility (per script).
- Sample counts are at the low end of practical Monte Carlo (10^4 to 10^5); production work would increase by an order of magnitude.
- Output is human-readable text on stdout, not files.

## Provenance

Editor's reference implementations. Verify with your own tools.
