"""k-fold cross-validation on the cooling-cup data.

Partitions the cooling-cup observations into k folds, refits Newton's
law on k-1 folds, evaluates the residuals on the held-out fold, and
aggregates. Reports the in-sample residual RMS, the held-out residual
RMS, and the inflation factor by which a parameter-only interval should
be scaled to honestly cover new measurements (section 18.5).

Dependencies: numpy, scipy.

Run:
    python cross_validation.py
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy import stats

T_INF = 22.0
K_FOLDS = 5  # leave-one-out variant if K = n


def load_data(path: Path) -> tuple[np.ndarray, np.ndarray]:
    t_list, T_list = [], []
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            t_list.append(float(row["t_min"]))
            T_list.append(float(row["T_C"]))
    return np.array(t_list), np.array(T_list)


def fit_predict(t_train, T_train, t_test):
    y_train = np.log(T_train - T_INF)
    res = stats.linregress(t_train, y_train)
    k_hat = -res.slope
    T0_eff = T_INF + np.exp(res.intercept)
    return T_INF + (T0_eff - T_INF) * np.exp(-k_hat * t_test)


def main() -> None:
    here = Path(__file__).parent
    data_path = here.parent / "data" / "cooling_cup.csv"
    t, T = load_data(data_path)
    n = len(t)
    k_folds = min(K_FOLDS, n)
    print(f"loaded {n} points; performing {k_folds}-fold cross-validation")

    # In-sample residuals (fit on all)
    T_pred_all = fit_predict(t, T, t)
    rss_in = float(np.sqrt(np.mean((T - T_pred_all) ** 2)))

    # k-fold residuals
    rng = np.random.default_rng(0)
    perm = rng.permutation(n)
    folds = np.array_split(perm, k_folds)
    cv_resids = []
    for fold_idx, fold in enumerate(folds):
        mask = np.ones(n, dtype=bool)
        mask[fold] = False
        T_pred_fold = fit_predict(t[mask], T[mask], t[fold])
        cv_resids.extend((T[fold] - T_pred_fold).tolist())
    rss_cv = float(np.sqrt(np.mean(np.array(cv_resids) ** 2)))

    print(f"\nIn-sample residual RMS:    {rss_in:.3f} deg C")
    print(f"Cross-validation RMS:      {rss_cv:.3f} deg C")
    inflation = rss_cv / max(rss_in, 1e-12)
    print(f"Inflation factor (CV/in):  {inflation:.2f}x")
    print("\nReading (section 18.5):")
    print("  inflation <= 1.1: structural error negligible; parameter interval is honest.")
    print("  inflation ~  1.5: structural error noticeable; widen prediction interval.")
    print("  inflation >= 2.0: model misses something; revise the abstraction.")


if __name__ == "__main__":
    main()
