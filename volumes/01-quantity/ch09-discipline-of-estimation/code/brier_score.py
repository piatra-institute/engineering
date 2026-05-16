# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Brier score and reliability-diagram scorer for probabilistic forecasts.

Reference: Brier, "Verification of forecasts expressed in terms of
probability," Monthly Weather Review 78(1), 1950.

The Brier score is the mean squared error between predicted probability
and observed binary outcome. Lower is better. A perfect forecaster
(0/1 predictions matching truth) scores 0. A useless forecaster
(predicting 0.5 for everything) scores 0.25 in the balanced case.
"""

from __future__ import annotations

import numpy as np


def brier_score(probabilities: np.ndarray, outcomes: np.ndarray) -> float:
    return float(np.mean((probabilities - outcomes) ** 2))


def reliability_bins(
    probabilities: np.ndarray, outcomes: np.ndarray, n_bins: int = 10
) -> list[tuple[float, float, int]]:
    """Return (bin_mean_prob, observed_freq, count) per bin."""
    edges = np.linspace(0, 1, n_bins + 1)
    out: list[tuple[float, float, int]] = []
    for lo, hi in zip(edges[:-1], edges[1:]):
        mask = (probabilities >= lo) & (probabilities < hi if hi < 1 else probabilities <= hi)
        if mask.sum() == 0:
            continue
        out.append(
            (
                float(probabilities[mask].mean()),
                float(outcomes[mask].mean()),
                int(mask.sum()),
            )
        )
    return out


def demo() -> None:
    """Reader-supplied calibration demonstration with a synthetic dataset.

    The reader's fifty Fermi-problem 90-percent intervals become a binary
    outcome (truth in interval = 1, truth outside = 0); the probabilistic
    forecast for the interval is 0.9. A perfectly calibrated reader
    will have 0.9 of the outcomes equal to 1; an overconfident reader
    will have fewer.
    """
    rng = np.random.default_rng(2026)
    # Overconfident: claims 0.9, achieves 0.75
    probabilities = np.full(50, 0.9)
    truth = (rng.uniform(size=50) < 0.75).astype(int)
    bs = brier_score(probabilities, truth)
    print(f"Brier score (overconfident reader): {bs:.4f}")
    print(f"Observed hit-rate at 0.9 stated:    {truth.mean():.2f}")
    print(f"Discrepancy from calibration:        {0.9 - truth.mean():.2f}")


if __name__ == "__main__":
    demo()
