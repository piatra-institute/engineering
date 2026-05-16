"""
Phase-plane plotter for 2D autonomous ODE systems. Reproduces
trajectories and equilibria for the chapter's worked phase-portrait
examples (damped oscillator, predator-prey, van der Pol).

Supports:
  - Volume II, Chapter 7, Simulation exercise 4 (predator-prey orbits)
  - The phase-plane analysis section's worked examples
  - The chapter's exercise on the trace-determinant classification

Dependencies:
  numpy, matplotlib

Usage:
  python phase_plane.py --system damped_oscillator
  python phase_plane.py --system predator_prey
"""

import argparse
import sys

import numpy as np


# --- right-hand sides -------------------------------------------------

def damped_oscillator(t: float, y: np.ndarray,
                      omega0: float = 1.0,
                      zeta: float = 0.10) -> np.ndarray:
    x, v = y
    return np.array([v, -omega0**2 * x - 2.0 * zeta * omega0 * v])


def predator_prey(t: float, y: np.ndarray,
                  a: float = 1.0, b: float = 0.5,
                  c: float = 0.75, d: float = 0.25) -> np.ndarray:
    x, y_ = y
    return np.array([a * x - b * x * y_,
                     -c * y_ + d * x * y_])


def van_der_pol(t: float, y: np.ndarray, mu: float = 1.0) -> np.ndarray:
    x, v = y
    return np.array([v, mu * (1.0 - x**2) * v - x])


# --- RK4 integrator ---------------------------------------------------

def rk4_step(f, t: float, y: np.ndarray, h: float) -> np.ndarray:
    k1 = f(t, y)
    k2 = f(t + h / 2.0, y + h * k1 / 2.0)
    k3 = f(t + h / 2.0, y + h * k2 / 2.0)
    k4 = f(t + h, y + h * k3)
    return y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)


def integrate(f, y0: np.ndarray, t_span: tuple,
              h: float = 0.01) -> tuple:
    t0, t_final = t_span
    n = int(round((t_final - t0) / h))
    ts = np.linspace(t0, t_final, n + 1)
    ys = np.zeros((n + 1, len(y0)))
    ys[0] = y0
    for i in range(n):
        ys[i + 1] = rk4_step(f, ts[i], ys[i], h)
    return ts, ys


# --- main -------------------------------------------------------------

SYSTEMS = {
    "damped_oscillator": (damped_oscillator, [(4.0, 0.0), (0.0, 3.0)],
                          (0.0, 30.0)),
    "predator_prey": (predator_prey, [(2.0, 1.0), (5.0, 2.0), (8.0, 3.0)],
                      (0.0, 30.0)),
    "van_der_pol": (van_der_pol, [(0.1, 0.0), (3.0, 0.0)],
                    (0.0, 30.0)),
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--system", choices=SYSTEMS.keys(),
                        default="damped_oscillator")
    parser.add_argument("--h", type=float, default=0.01)
    parser.add_argument("--no-plot", action="store_true",
                        help="Skip plotting; print trajectory endpoints only.")
    args = parser.parse_args()

    f, ics, t_span = SYSTEMS[args.system]
    for ic in ics:
        ts, ys = integrate(f, np.array(ic), t_span, h=args.h)
        print(f"IC {ic}: endpoint y(t_f) = {ys[-1]}")

    if args.no_plot:
        return

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not available; skipping plot", file=sys.stderr)
        return

    fig, ax = plt.subplots(figsize=(6, 6))
    for ic in ics:
        ts, ys = integrate(f, np.array(ic), t_span, h=args.h)
        ax.plot(ys[:, 0], ys[:, 1], lw=1.2, label=f"IC {ic}")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$\\dot{x}$ or $y$")
    ax.set_title(args.system.replace("_", " "))
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(f"{args.system}_phase.png", dpi=150)
    print(f"Saved {args.system}_phase.png")


if __name__ == "__main__":
    main()
