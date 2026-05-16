# Code assets - Volume II, Chapter 1 (Algebra and proof discipline)

Executable supporting code for the chapter's worked examples and
simulation exercises. Each file carries PEP 723 inline metadata and
runs under `uv run`.

## Files

| File | Purpose | Used by |
|---|---|---|
| `binomial_table.py` | Generates Pascal's triangle by the integer recurrence; writes (n, k, binom_n_k) CSV; spot-checks against the five-card poker count and C(30, 15). | Simulation exercise (integer binomial coefficient); Pascal-triangle figure. |
| `cauchy_schwarz_mc.py` | Monte-Carlo verification of Cauchy-Schwarz over R^d; writes per-trial ratios; asserts the upper bound holds on every trial. | Simulation exercise (numerical Cauchy-Schwarz). |
| `am_gm_check.py` | Empirical AM/GM ratio across several n and several non-negative distributions; logs per-n mean and standard deviation. | Simulation exercise (AM-GM in practice). |
| `collatz_run.py` | Runs the Collatz iteration for 1 <= n <= n_max; logs (n, steps); reports the maximum step count and the starting value achieving it. | Simulation exercise (Collatz); chapter remark that demonstration is not proof. |

## Running

```
uv run binomial_table.py 12 ../data/pascal_to_12.csv
uv run cauchy_schwarz_mc.py 10 1000 ../data/cauchy_schwarz_d10.csv
uv run am_gm_check.py 2,5,10,50 exp 10000 ../data/am_gm_exp.csv
uv run collatz_run.py 100000 ../data/collatz_to_1e5.csv
```

`binomial_table.py` and `collatz_run.py` use the standard library
only. `cauchy_schwarz_mc.py` and `am_gm_check.py` require `numpy`.
Random seeds are fixed (`20260516`) for reproducibility.

## What these scripts are and are not

Each script demonstrates the chapter's identity, inequality, or
recurrence on a finite empirical sample. None is a proof. The
chapter's standing remark applies here: a million Collatz trajectories
that reach 1 do not establish the conjecture; ten thousand
AM-GM-conforming samples do not establish the inequality; a thousand
Cauchy-Schwarz-conforming trials do not establish the bound. The
proofs live in the chapter prose. The simulations are tools for
building working intuition and for catching the kind of error that a
proof might overlook in implementation.
