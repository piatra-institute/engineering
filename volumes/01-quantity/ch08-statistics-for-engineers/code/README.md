# Code assets — Volume I, Chapter 8 (Statistics for engineers)

Each script is self-contained and runnable with `uv run`:

```
uv run code/<script>.py
```

## Files

| File | Purpose | Used by |
|---|---|---|
| `bootstrap_ci.py` | Nonparametric bootstrap CI for the commute-time mean; comparison to the parametric t-based interval. | Section 8.4, Simulation exercise on bootstrap. |
| `power_calc.py` | Two-sample t-test sample size and power calculator under the normal approximation. | Section 8.6, the rule-of-thumb derivation, and the design exercises. |
| `qq_plot.py` | Q-Q-plot demonstration for Gaussian, t(5), and lognormal samples; writes PNG. | Section 8.2 (choosing a distribution), QQ-plot figure. |
| `p_hacking_demo.py` | Garden-of-forking-paths simulator: empirical false-positive rate under a five-path minimum-p strategy. | Section 8.7, Simulation exercise on p-hacking. |
| `clt_skewed.py` | Central limit theorem on an exponential parent; tracks sample-mean standard deviation and skewness against $n$. | Section 8.1 archetype, Simulation exercise on CLT for skewed parents. |

## Conventions

- Random-number generator seeded for reproducibility (per script).
- Sample counts are at the low end of practical Monte Carlo (10^3 to 10^4); production work would increase by an order of magnitude.
- Output is human-readable text on stdout; `qq_plot.py` additionally writes a PNG to the current working directory.
- Scripts intentionally avoid scipy.stats so the dependency footprint is minimal; the normal-approximation Welch test in `p_hacking_demo.py` is adequate for n = 40 per group and would be replaced by the exact t-distribution in a real analysis.

## Provenance

Editor's reference implementations. Verify with your own tools.
