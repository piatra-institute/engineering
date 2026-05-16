"""
Drag coefficient of a sphere vs Reynolds number using the
Morsi-Alexander piecewise correlation.

Reference:
  Morsi, S. A. and Alexander, A. J. (1972), "An investigation of
  particle trajectories in two-phase flow systems", J. Fluid Mech.

Supports Volume I, Chapter 2, Simulation exercise on the drag curve;
generates the data used in figure 1.3.

Dependencies:
  numpy, matplotlib

Usage:
  python drag_curve.py
"""

import numpy as np


def schiller_naumann(re: np.ndarray) -> np.ndarray:
    """Schiller-Naumann correlation (valid for Re < 1000), extended
    smoothly to higher Re with a constant Newton-regime term."""
    return 24.0 / re + 6.0 / (1.0 + np.sqrt(re)) + 0.4


def morsi_alexander(re: float) -> float:
    """Morsi-Alexander piecewise correlation (1972), valid roughly
    0.1 < Re < 5e4."""
    if re < 0.1:
        return 24.0 / re  # Stokes
    elif re < 1.0:
        return 22.73 / re + 0.0903 / re ** 2 + 3.69
    elif re < 10.0:
        return 29.1667 / re - 3.8889 / re ** 2 + 1.222
    elif re < 100.0:
        return 46.5 / re - 116.67 / re ** 2 + 0.6167
    elif re < 1000.0:
        return 98.33 / re - 2778 / re ** 2 + 0.3644
    elif re < 5000.0:
        return 148.62 / re - 47500 / re ** 2 + 0.357
    elif re < 10000.0:
        return -490.546 / re + 5.787e5 / re ** 2 + 0.46
    elif re < 50000.0:
        return -1662.5 / re + 5.4167e6 / re ** 2 + 0.5191
    else:
        # Drag crisis at ~3e5 not captured here
        return 0.4


def main() -> None:
    re = np.logspace(-1, 6, 200)
    cd_sn = schiller_naumann(re)

    print(f"{'Re':>12} {'C_D (SN)':>12} {'24/Re':>12}")
    for r, c in zip(re[::20], cd_sn[::20]):
        print(f"{r:12.4g} {c:12.4g} {24.0/r:12.4g}")

    # Optional matplotlib plot (commented out for headless run)
    # import matplotlib.pyplot as plt
    # plt.loglog(re, cd_sn, label='Schiller-Naumann')
    # plt.loglog(re, 24.0/re, '--', label='Stokes 24/Re')
    # plt.xlabel('Reynolds number')
    # plt.ylabel('Drag coefficient C_D')
    # plt.legend()
    # plt.grid(True, which='both')
    # plt.savefig('drag_curve.pdf')


if __name__ == "__main__":
    main()
