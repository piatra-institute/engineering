"""
Frequency response of the forced second-order oscillator

    m x'' + c x' + k x = F0 cos(omega t).

Computes the analytical steady-state amplitude and phase across a
frequency sweep, and optionally verifies a few points by direct RK4
integration of the transient until the steady state is reached.

Supports:
  - Volume II, Chapter 7, section 7.5 (forced response, resonance)
  - The driven-oscillator worked example
  - Simulation exercise on the forced oscillator amplitude/phase sweep

Dependencies:
  numpy  (matplotlib optional, for the response plot)

Usage:
  python forced_oscillator.py [--zeta 0.1] [--verify] [--no-plot]

Output:
  A table of (omega/omega0, amplitude/static, phase lag) and, with
  --verify, the RK4-extracted amplitude at the resonance ratio for a
  direct check against the closed form.
"""

import argparse
import math

import numpy as np


def amplitude_static_ratio(r: float, zeta: float) -> float:
    """A(omega)/(F0/k) as a function of r = omega/omega0 and zeta."""
    return 1.0 / math.sqrt((1.0 - r * r) ** 2 + (2.0 * zeta * r) ** 2)


def phase_lag(r: float, zeta: float) -> float:
    """Phase lag in radians, continuous on [0, pi], pi/2 at r = 1."""
    return math.atan2(2.0 * zeta * r, 1.0 - r * r)


def rk4_steady_amplitude(omega0: float, zeta: float, omega: float,
                         h: float = 1.0e-3, n_periods: int = 400) -> float:
    """Integrate the forced oscillator (m=k=1 normalisation) and read off
    the steady-state amplitude from the tail of the run."""
    c = 2.0 * zeta * omega0
    k = omega0 * omega0

    def rhs(t, y):
        x, v = y
        return np.array([v, math.cos(omega * t) - c * v - k * x])

    t, y = 0.0, np.array([0.0, 0.0])
    t_final = n_periods * 2.0 * math.pi / max(omega, 1e-9)
    n_steps = int(t_final / h)
    tail_start = int(0.75 * n_steps)
    xs = []
    for i in range(n_steps):
        k1 = rhs(t, y)
        k2 = rhs(t + h / 2, y + h * k1 / 2)
        k3 = rhs(t + h / 2, y + h * k2 / 2)
        k4 = rhs(t + h, y + h * k3)
        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
        if i >= tail_start:
            xs.append(y[0])
    return 0.5 * (max(xs) - min(xs))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zeta", type=float, default=0.1)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()

    zeta = args.zeta
    ratios = [0.0, 0.25, 0.5, 0.75, 0.9, 1.0, 1.1, 1.5, 2.0, 3.0]

    print(f"  zeta = {zeta}   Q ~ {1.0 / (2.0 * zeta):.2f}")
    print(f"{'omega/omega0':>14}  {'A/(F0/k)':>12}  {'phase (rad)':>12}")
    for r in ratios:
        a = amplitude_static_ratio(r, zeta)
        p = phase_lag(r, zeta)
        print(f"{r:>14.3f}  {a:>12.4f}  {p:>12.4f}")

    r_peak = math.sqrt(max(1.0 - 2.0 * zeta * zeta, 0.0))
    print(f"\n  resonant ratio omega_r/omega0 = {r_peak:.4f}")
    print(f"  peak amplitude / static       = "
          f"{amplitude_static_ratio(r_peak, zeta):.4f}")

    if args.verify:
        omega0 = 1.0
        a_num = rk4_steady_amplitude(omega0, zeta, omega0)
        print(f"\n  RK4 steady amplitude at omega = omega0: {a_num:.4f}")
        print(f"  closed-form at omega0:                  "
              f"{amplitude_static_ratio(1.0, zeta):.4f}")

    if not args.no_plot:
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            print("\n(matplotlib not available; skipping plot)")
            return
        rs = np.linspace(0.01, 2.5, 400)
        for z in (0.1, 0.25, 0.5, 0.7071):
            plt.plot(rs, [amplitude_static_ratio(r, z) for r in rs],
                     label=f"zeta = {z:.3g}")
        plt.xlabel("omega / omega0")
        plt.ylabel("A / (F0/k)")
        plt.legend()
        plt.title("Resonance: forced second-order oscillator")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
