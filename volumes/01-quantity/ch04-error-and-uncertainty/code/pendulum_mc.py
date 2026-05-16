# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Monte Carlo propagation of uncertainty for pendulum g = 4 pi^2 L / T^2.

Compares the empirical standard deviation from Monte Carlo to the
linear-propagation prediction. For small relative input uncertainties
the two agree; for larger relative uncertainties Monte Carlo gives a
better estimate.
"""

import numpy as np

RNG = np.random.default_rng(101)
N_SAMPLES = 100_000

L_NOM, L_SD = 1.000, 0.001
T_NOM, T_SD = 2.007, 0.005


def main() -> None:
    L = RNG.normal(L_NOM, L_SD, size=N_SAMPLES)
    T = RNG.normal(T_NOM, T_SD, size=N_SAMPLES)
    g = 4 * np.pi**2 * L / T**2

    g_nom = 4 * np.pi**2 * L_NOM / T_NOM**2
    # Linear propagation
    rel_L = L_SD / L_NOM
    rel_T = T_SD / T_NOM
    rel_g_linear = np.sqrt(rel_L**2 + 4 * rel_T**2)
    sd_g_linear = g_nom * rel_g_linear

    print(f"nominal g                  : {g_nom:.4f}  m/s^2")
    print(f"empirical mean g (MC)      : {g.mean():.4f}  m/s^2")
    print(f"empirical sd g (MC)        : {g.std(ddof=1):.4f}  m/s^2")
    print(f"linear-propagation sd g    : {sd_g_linear:.4f}  m/s^2")
    print(f"ratio (MC / linear)        : {g.std(ddof=1) / sd_g_linear:.4f}")


if __name__ == "__main__":
    main()
