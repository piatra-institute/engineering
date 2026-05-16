"""Logistic-growth fit by nonlinear least squares.

Reads `../data/logistic_growth.csv`, fits N(t) = K / (1 + (K/N0 - 1) exp(-rt))
with (r, K) as free parameters (N0 taken as the first observation),
reports point estimates with parameter intervals from the inverse-Hessian
approximation, and prints the Jacobian condition number as an
identifiability diagnostic.

Dependencies: numpy, scipy.

Run:
    python logistic_fit.py
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy.optimize import curve_fit


def load_data(path: Path) -> tuple[np.ndarray, np.ndarray]:
    """Read the logistic-growth CSV; return (t [h], N [cells/mL])."""
    t_list, N_list = [], []
    with path.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            t_list.append(float(row["t_h"]))
            N_list.append(float(row["N"]))
    return np.array(t_list), np.array(N_list)


def logistic(t: np.ndarray, r: float, K: float, N0: float) -> np.ndarray:
    """Closed-form solution to dN/dt = r N (1 - N/K)."""
    return K / (1.0 + (K / N0 - 1.0) * np.exp(-r * t))


def jacobian(t: np.ndarray, r: float, K: float, N0: float) -> np.ndarray:
    """Analytic Jacobian wrt (r, K), evaluated at the supplied parameter values."""
    A = (K / N0 - 1.0)
    e = np.exp(-r * t)
    D = 1.0 + A * e
    # dN/dr
    dNdr = K * A * t * e / D**2
    # dN/dK
    dNdK = 1.0 / D - K * (e / N0) / D**2
    return np.column_stack([dNdr, dNdK])


def main() -> None:
    here = Path(__file__).parent
    data_path = here.parent / "data" / "logistic_growth.csv"
    t, N = load_data(data_path)
    print(f"loaded {len(t)} points from {data_path.name}")

    N0 = N[0]
    p0 = (0.5, N[-1] * 1.05)  # initial guess

    def model(t, r, K):
        return logistic(t, r, K, N0)

    popt, pcov = curve_fit(model, t, N, p0=p0)
    r_hat, K_hat = popt
    perr = np.sqrt(np.diag(pcov))
    print(f"\nLogistic fit:")
    print(f"  r_hat = {r_hat:.4f} per hour    (SE = {perr[0]:.4f})")
    print(f"  K_hat = {K_hat:.4f}              (SE = {perr[1]:.4f})")

    # Identifiability diagnostic: Jacobian condition number
    J = jacobian(t, r_hat, K_hat, N0)
    cond = np.linalg.cond(J)
    print(f"\nIdentifiability diagnostic (Jacobian condition number):")
    print(f"  cond(J) = {cond:.2f}")
    print("  rule of thumb: cond > 1e3 indicates weak joint identifiability;")
    print("  the data window may not span both the exponential and saturation phases.")

    # Relative intervals
    rel_r = perr[0] / r_hat * 100
    rel_K = perr[1] / K_hat * 100
    print(f"\nRelative interval widths:")
    print(f"  r: +/- {rel_r:.1f}%")
    print(f"  K: +/- {rel_K:.1f}%")
    if rel_K > 2 * rel_r:
        print("  K is more loosely identified than r (data may emphasise the exponential phase).")
    elif rel_r > 2 * rel_K:
        print("  r is more loosely identified than K (data may emphasise the saturation phase).")
    else:
        print("  r and K are comparably identified (data span the inflection).")


if __name__ == "__main__":
    main()
