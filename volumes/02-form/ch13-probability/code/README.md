# Code assets - Volume II, Chapter 13 (Probability theory)

Executable supporting code for the chapter's worked examples,
simulation exercises, and project. Files are runnable from this
directory with a recent Python 3 interpreter. Each file carries
PEP 723 inline-script metadata so it can be run directly with
`uv run <script.py>`.

## Files

| File | Purpose | Used by |
|---|---|---|
| `markov_chain_simulation.py` | Simulates a finite-state Markov chain, computes the empirical occupancy distribution, the analytical stationary distribution, the total-variation distance, the spectral gap, and the empirical mixing time. | The Project (Markov chain simulation and convergence). |
| `clt_demo.py` | Generates standardised sample means for an underlying $\mathrm{Exp}(1)$ distribution at $n = 1$, $5$, $30$, $100$, writes histograms to `../data/clt_histograms.csv`, and prints summary statistics. | Simulation exercise on CLT convergence. |
| `bayes_table.py` | Computes the posterior probability for a diagnostic test with given sensitivity, specificity, and prior, displaying the full $2 \times 2$ contingency table. | The Bayes section worked example, the design and judgement exercises on screening tests. |
| `correlated_bernoulli.py` | Simulates correlated Bernoulli sums via a hidden common-factor (Gaussian copula) model and compares the empirical variance to the independence prediction. | Simulation exercise on correlation effects in a sum of Bernoullis. |
| `union_bound_check.py` | Numerical check that the union bound is loose by a known factor for independent events and tight under perfect positive dependence; tabulates the gap as a function of $p$ and $n$. | Estimation block, judgement exercise on independence-vs-union-bound. |

## Running

Each file can be run directly with `uv run <script.py>` or with a
standard Python 3.10+ interpreter that has `numpy` available. The
project file `markov_chain_simulation.py` additionally writes a
running-occupancy time series to `../data/markov_trace.csv` for
inspection in a spreadsheet.

## License

Code is provided under the project's overall license for illustrative
and pedagogical use. The values produced are illustrative; production
use requires verification against the intended application.
