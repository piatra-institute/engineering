# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Garden-of-forking-paths simulator.

Under a true null (no effect), simulate an experimenter who tries
several analysis specifications and reports the smallest p-value.
The empirical false-positive rate of that smallest-p strategy is
much higher than the nominal alpha. This is the mechanism behind
section 8.7.

Specifications considered per trial:
  - test on the full dataset
  - test with outliers (|z| > 2) removed
  - test on subgroup A only
  - test on subgroup B only
  - test on full data with log-transformed outcome
"""

import numpy as np

RNG = np.random.default_rng(2026)
TRIALS = 5_000
N_PER_GROUP = 40
ALPHA = 0.05


def welch_t_p(x: np.ndarray, y: np.ndarray) -> float:
    """Two-sided Welch t-test p-value using the normal approximation.

    Adequate for sample sizes used here; for tiny n use the exact
    t-distribution from scipy.stats in a real analysis."""
    nx, ny = len(x), len(y)
    if nx < 2 or ny < 2:
        return 1.0
    mx, my = x.mean(), y.mean()
    vx, vy = x.var(ddof=1), y.var(ddof=1)
    se = (vx / nx + vy / ny) ** 0.5
    if se == 0:
        return 1.0
    t = (mx - my) / se
    # Two-sided p-value under standard normal approximation.
    from math import erf, sqrt
    return 1.0 - erf(abs(t) / sqrt(2.0))


def one_trial(rng: np.random.Generator) -> tuple[float, float]:
    """Return (single_p, min_p_of_five_paths)."""
    x = rng.normal(0, 1, N_PER_GROUP)
    y = rng.normal(0, 1, N_PER_GROUP)
    # Assign random subgroup labels A/B.
    subgroup_x = rng.integers(0, 2, N_PER_GROUP)
    subgroup_y = rng.integers(0, 2, N_PER_GROUP)

    p_full = welch_t_p(x, y)

    # Outlier trim (|z| > 2)
    x_trim = x[np.abs((x - x.mean()) / x.std(ddof=1)) <= 2.0]
    y_trim = y[np.abs((y - y.mean()) / y.std(ddof=1)) <= 2.0]
    p_trim = welch_t_p(x_trim, y_trim)

    p_sub_a = welch_t_p(x[subgroup_x == 0], y[subgroup_y == 0])
    p_sub_b = welch_t_p(x[subgroup_x == 1], y[subgroup_y == 1])

    x_log = np.log(x - x.min() + 1.0)
    y_log = np.log(y - y.min() + 1.0)
    p_log = welch_t_p(x_log, y_log)

    return p_full, min(p_full, p_trim, p_sub_a, p_sub_b, p_log)


def main() -> None:
    single = np.empty(TRIALS)
    min_p = np.empty(TRIALS)
    for i in range(TRIALS):
        single[i], min_p[i] = one_trial(RNG)
    fpr_single = float((single < ALPHA).mean())
    fpr_forking = float((min_p < ALPHA).mean())
    print(f"trials: {TRIALS}; alpha: {ALPHA}; n per group: {N_PER_GROUP}")
    print(f"FPR with single pre-specified test:  {fpr_single:.3f}")
    print(f"FPR with 5-path minimum-p strategy: {fpr_forking:.3f}")
    print("The second rate is the cost of selecting analyses after seeing data.")


if __name__ == "__main__":
    main()
