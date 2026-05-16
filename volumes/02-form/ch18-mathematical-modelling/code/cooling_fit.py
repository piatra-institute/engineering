"""Newton's law of cooling: fit, interval, and propagation.

Reads `../data/cooling_cup.csv`, fits T(t) = T_inf + (T_0 - T_inf) exp(-k t)
by linearised regression on ln(T - T_inf) versus t, reports the point
estimate of k with its 95% confidence interval, and propagates the
interval through the inverse relation t_60 = (1/k) ln((T_0 - T_inf)/
(60 - T_inf)) to give the predicted time to 60 degrees Celsius with
its propagated interval.

Dependencies: numpy, scipy.

Run:
    python cooling_fit.py
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy import stats

T_INF = 22.0  # room temperature, deg C
T_TARGET = 60.0  # the engineering question's target temperature


def load_data(path: Path) -> tuple[np.ndarray, np.ndarray]:
    """Read the cooling-cup CSV; return (t [min], T [deg C])."""
    t_list, T_list = [], []
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            t_list.append(float(row["t_min"]))
            T_list.append(float(row["T_C"]))
    return np.array(t_list), np.array(T_list)


def fit_newton(t: np.ndarray, T: np.ndarray, T_inf: float):
    """Linear regression of ln(T - T_inf) on t. Returns (k_hat, k_se, intercept_hat)."""
    y = np.log(T - T_inf)
    res = stats.linregress(t, y)
    k_hat = -res.slope
    k_se = res.stderr
    return k_hat, k_se, res.intercept


def predict_t_target(k_hat: float, k_se: float, T0: float, T_inf: float,
                     T_target: float) -> tuple[float, float]:
    """Inverse: t = (1/k) ln((T0 - T_inf)/(T_target - T_inf)).
    Propagate k's interval to t by the delta method.
    """
    ratio = (T0 - T_inf) / (T_target - T_inf)
    t_hat = np.log(ratio) / k_hat
    # dt/dk = -ln(ratio) / k^2  => sigma_t = |dt/dk| * sigma_k
    t_se = np.abs(-np.log(ratio) / k_hat ** 2) * k_se
    return t_hat, t_se


def main() -> None:
    here = Path(__file__).parent
    data_path = here.parent / "data" / "cooling_cup.csv"
    t, T = load_data(data_path)
    print(f"loaded {len(t)} points from {data_path.name}")

    k_hat, k_se, intercept = fit_newton(t, T, T_INF)
    # 95% interval via t-distribution; degrees of freedom = n - 2
    dof = len(t) - 2
    crit = stats.t.ppf(0.975, dof)
    k_lo = k_hat - crit * k_se
    k_hi = k_hat + crit * k_se
    print(f"\nNewton's law of cooling fit:")
    print(f"  k_hat = {k_hat:.4f} per minute")
    print(f"  95% CI: [{k_lo:.4f}, {k_hi:.4f}] per minute")
    print(f"  ln(T0 - T_inf) intercept = {intercept:.4f}")
    print(f"  implied T0 = {T_INF + np.exp(intercept):.2f} deg C")

    T0_est = T_INF + np.exp(intercept)
    t_hat, t_se = predict_t_target(k_hat, k_se, T0_est, T_INF, T_TARGET)
    t_lo = t_hat - crit * t_se
    t_hi = t_hat + crit * t_se
    print(f"\nTime to reach {T_TARGET} deg C:")
    print(f"  t_hat = {t_hat:.2f} minutes")
    print(f"  95% CI: [{t_lo:.2f}, {t_hi:.2f}] minutes (parameter uncertainty only)")
    print(f"  NB: structural error (radiative, evaporative, geometry) not included.")
    print(f"      For an honest interval, inflate by the validation-residual factor.")


if __name__ == "__main__":
    main()
