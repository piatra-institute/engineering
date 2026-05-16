"""
Demonstrate the stiffness phenomenon: forward Euler requires a step
size set by the fast mode, while implicit Euler tolerates much
larger steps. Reproduces the stiffness exercise in the chapter.

System:
    y1' = -1000 y1 + 999 y2
    y2' =     y1 -    2 y2
with y1(0) = 1, y2(0) = 0. Fast eigenvalue ~ -1001, slow ~ -1.

Supports:
  - Volume II, Chapter 7, Simulation exercise 5 (stiff system)
  - The chapter's stiffness section

Dependencies:
  numpy

Usage:
  python stiff_demo.py [--h 0.001] [--method explicit|implicit]
"""

import argparse

import numpy as np


def jacobian() -> np.ndarray:
    return np.array([[-1000.0, 999.0],
                     [1.0, -2.0]])


def f(t: float, y: np.ndarray) -> np.ndarray:
    A = jacobian()
    return A @ y


def explicit_euler(h: float, t_final: float, y0: np.ndarray) -> np.ndarray:
    n = int(round(t_final / h))
    y = y0.copy()
    for _ in range(n):
        y = y + h * f(0.0, y)
        if not np.all(np.isfinite(y)) or np.max(np.abs(y)) > 1e12:
            return y  # blow-up signal
    return y


def implicit_euler(h: float, t_final: float, y0: np.ndarray) -> np.ndarray:
    """One linear solve per step for linear y' = A y: (I - h A) y_{n+1} = y_n."""
    n = int(round(t_final / h))
    I = np.eye(2)
    A = jacobian()
    M = I - h * A
    Minv = np.linalg.inv(M)
    y = y0.copy()
    for _ in range(n):
        y = Minv @ y
    return y


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t-final", type=float, default=1.0)
    args = parser.parse_args()

    y0 = np.array([1.0, 0.0])

    # Eigenvalue diagnosis
    eigs = np.linalg.eigvals(jacobian())
    print("Jacobian eigenvalues:", eigs)
    print(f"Stiffness ratio: |lambda_fast/lambda_slow| ="
          f" {abs(eigs.min()/eigs.max()):.0f}")
    print()

    # Try explicit Euler at three step sizes
    print(f"{'method':<14} {'h':>10}  {'y1(t_f)':>14}  {'y2(t_f)':>14}  {'status':>20}")
    for h in [0.001, 0.0015, 0.0025]:
        y = explicit_euler(h, args.t_final, y0)
        status = "stable" if (np.all(np.isfinite(y)) and
                              np.max(np.abs(y)) < 1.0) else "BLOW-UP"
        print(f"{'explicit Euler':<14} {h:>10.4f}  "
              f"{y[0]:>14.3e}  {y[1]:>14.3e}  {status:>20}")

    # Implicit Euler at a much larger step
    for h in [0.001, 0.01, 0.1]:
        y = implicit_euler(h, args.t_final, y0)
        print(f"{'implicit Euler':<14} {h:>10.4f}  "
              f"{y[0]:>14.3e}  {y[1]:>14.3e}  {'stable':>20}")


if __name__ == "__main__":
    main()
