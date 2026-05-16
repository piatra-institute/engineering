# Data assets, Volume II, Chapter 16 (Numerical methods)

## Files

| File | Purpose | Provenance |
|---|---|---|
| `patriot-drift.csv` | One row per operating hour, $0$ to $120$ hours: counter ticks, cumulative timing error in seconds, predicted-position error in metres at Scud speed ($1{,}676 \,\text{m/s}$). | Computed by `code/patriot_drift.py` from the GAO Patriot report timing model \cite{acc:gao-patriot-1992}. |
| `hilbert-conditioning.csv` | Hilbert matrix order $n$, $2$-norm condition number $\kappa_{2}(\mat{H}_{n})$, expected loss-of-digits estimate in binary64 ($\log_{10}\kappa_{2} - 16$ negated and clamped at zero). | Computed by the editor; the condition-number growth is well known and matches the closed-form Wilbraham-style asymptotic. |

## Conventions

- All CSVs are UTF-8, comma-separated, with a header row.
- Numerical values are in plain decimal form.
- Where a value derives from an empirical source, the bibliography
  key is given in the column header comment or in this README.

## Provenance summary

The Patriot drift series is a reconstruction of the GAO Patriot
report's timing model \cite{acc:gao-patriot-1992}; the parameters
(per-tick error $9.54 \times 10^{-8}$ s, Scud speed
$1{,}676 \,\text{m/s}$) are quoted from the report. The Hilbert
conditioning table is reproducible from standard linear-algebra
libraries (NumPy `np.linalg.cond`).
