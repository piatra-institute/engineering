# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "numpy>=1.26",
# ]
# ///
"""
Five-fold cross-validation of ridge regression on the synthetic
``flexural-strength.csv`` dataset.

The script implements ridge from the closed form
``(X'X + lambda I)^{-1} X' y`` and rolls cross-validation by hand
so the reader can see the loop structure with no library hidden
behind it.

Usage:
    uv run kfold_ridge.py ../data/flexural-strength.csv
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import numpy as np


def load_csv(path: Path) -> tuple[np.ndarray, np.ndarray, list[str]]:
    with path.open() as fh:
        reader = csv.reader(fh)
        header = next(reader)
        rows = [list(map(float, row)) for row in reader]
    data = np.asarray(rows, dtype=float)
    response = data[:, -1]
    predictors = data[:, :-1]
    predictor_names = header[:-1]
    return predictors, response, predictor_names


def ridge_fit(x: np.ndarray, y: np.ndarray, lam: float) -> np.ndarray:
    p = x.shape[1]
    a = x.T @ x + lam * np.eye(p)
    b = x.T @ y
    return np.linalg.solve(a, b)


def standardise(x_train: np.ndarray, x_test: np.ndarray):
    mu = x_train.mean(axis=0)
    sigma = x_train.std(axis=0, ddof=1)
    sigma[sigma == 0.0] = 1.0
    return (x_train - mu) / sigma, (x_test - mu) / sigma


def kfold_cv(
    x: np.ndarray,
    y: np.ndarray,
    lam: float,
    k: int = 5,
    seed: int = 14,
) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    n = len(y)
    order = rng.permutation(n)
    folds = np.array_split(order, k)
    losses = np.empty(k)
    for j, fold in enumerate(folds):
        mask = np.ones(n, dtype=bool)
        mask[fold] = False
        x_tr, y_tr = x[mask], y[mask]
        x_te, y_te = x[fold], y[fold]
        # Standardise inside the loop, never on the full dataset.
        x_tr_s, x_te_s = standardise(x_tr, x_te)
        # Centre y on the training fold.
        y_mean = y_tr.mean()
        beta = ridge_fit(x_tr_s, y_tr - y_mean, lam)
        y_pred = x_te_s @ beta + y_mean
        losses[j] = float(np.mean((y_te - y_pred) ** 2))
    return float(losses.mean()), float(losses.std(ddof=1) / np.sqrt(k))


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: uv run kfold_ridge.py <path-to-csv>", file=sys.stderr)
        sys.exit(2)

    path = Path(sys.argv[1])
    x, y, names = load_csv(path)
    print(f"n = {len(y)}, p = {x.shape[1]}, predictors = {names}")

    grid = [0.0, 0.1, 1.0, 5.0, 25.0, 100.0]
    print(f"\n{'lambda':>10}  {'CV-MSE':>10}  {'CV-SE':>10}")
    for lam in grid:
        mean, se = kfold_cv(x, y, lam, k=5)
        print(f"{lam:10.2f}  {mean:10.4f}  {se:10.4f}")

    # In-sample MSE for comparison.
    x_s = (x - x.mean(axis=0)) / x.std(axis=0, ddof=1)
    y_c = y - y.mean()
    beta_full = ridge_fit(x_s, y_c, 1.0)
    in_sample = float(np.mean((y_c - x_s @ beta_full) ** 2))
    print(f"\nIn-sample MSE at lambda = 1.0: {in_sample:.4f}")


if __name__ == "__main__":
    main()
