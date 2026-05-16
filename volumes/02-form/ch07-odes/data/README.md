# Data assets — Volume II, Chapter 7 (Differential equations: ODEs)

Reference datasets supporting the chapter's exercises and worked
examples.

## Files

| File | Source | Year | Used by |
|---|---|---|---|
| `pendulum_periods_reference.csv` | Computed by the authors from $T = (4/\omega_{0}) K(\sin(\theta_{0}/2))$, where $K$ is the complete elliptic integral of the first kind; cross-checked against Abramowitz \& Stegun table 17.1. | 2026 | Chapter project (the pendulum at large amplitudes); `code/pendulum_period.py`; the pendulum-period figure. |
| `stiffness_test_eigenvalues.csv` | Compiled by the authors from standard stiff-ODE benchmark literature (Hairer \& Wanner 1996) and the chapter's own demonstration system. | 2026 | Simulation exercise 5; the chapter's stiffness section. |

## Provenance

Each file's first row is a header. Numerical values in
`pendulum_periods_reference.csv` are computed from the
elliptic-integral formula and rounded to five decimal places; the
exact column is the reference against which a reader's numerical
extraction is checked.

The eigenvalue table in `stiffness_test_eigenvalues.csv` lists
representative stiff ODE systems with their Jacobian's largest
(magnitude) and smallest eigenvalues at the operating point. The
stiffness ratio is the ratio of magnitudes; systems with ratio
$\gtrsim 10$ are routinely treated as stiff in working practice.

## Use

Files are CSV (UTF-8, RFC 4180). The chapter's exercises and the
code in `code/` reference specific files; the reader can extend
the tables with their own systems while preserving the file
structure.
