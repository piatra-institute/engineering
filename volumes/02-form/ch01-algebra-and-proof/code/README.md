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
| `horner_eval.py` | Evaluates a polynomial by Horner's nested form against the naive term-by-term sum; returns value and derivative in one synthetic-division sweep; spot-checks against (1+x)^6. | Section 1.1 polynomial-evaluation worked example; operation-count table `data/horner-vs-naive-ops.csv`. |
| `quadratic_stability.py` | Computes quadratic roots by the naive formula and by the Vieta-companion stable recipe; reports residuals for the ill-conditioned coefficient set. | Section 1.1 cancellation discussion; calculation exercise on the ill-conditioned quadratic. |
| `welford_variance.py` | Welford single-pass running mean/variance against the naive sum-of-squares identity and the two-pass reference on a badly-scaled stream; writes the cancellation gap to `data/welford-vs-naive.csv`. | Section 1.4 case study (numerically stable running variance, derived and verified); section 1.1 catastrophic cancellation. |

## Running

```
uv run binomial_table.py 12 ../data/pascal_to_12.csv
uv run cauchy_schwarz_mc.py 10 1000 ../data/cauchy_schwarz_d10.csv
uv run am_gm_check.py 2,5,10,50 exp 10000 ../data/am_gm_exp.csv
uv run collatz_run.py 100000 ../data/collatz_to_1e5.csv
uv run horner_eval.py
uv run quadratic_stability.py
uv run welford_variance.py
```

`binomial_table.py`, `collatz_run.py`, `horner_eval.py`, and
`quadratic_stability.py` use the standard library only.
`cauchy_schwarz_mc.py` and `am_gm_check.py` require `numpy`.
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
