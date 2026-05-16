# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
Monte Carlo integration of

    I = int_0^1 int_0^1 exp(-(x^2 + y^2)) dx dy,

with the result compared to a trapezoidal-rule double integral on a
fixed grid. Reports the Monte Carlo mean, standard error, and the
trapezoidal approximation.

Supports Volume II, Chapter 6:
  - Simulation exercise 4 (Monte Carlo vs trapezoidal double).

Run directly with uv:
    uv run monte_carlo_2d.py
"""

from __future__ import annotations

import math

import numpy as np


def integrand(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.exp(-(x * x + y * y))


def monte_carlo(n_samples: int, rng: np.random.Generator) -> tuple[float,
                                                                   float]:
    """Returns (mean, standard error of the mean)."""
    x = rng.random(n_samples)
    y = rng.random(n_samples)
    values = integrand(x, y)
    mean = float(values.mean())
    sem = float(values.std(ddof=1) / math.sqrt(n_samples))
    return mean, sem


def trapezoidal_2d(n: int) -> float:
    """Trapezoidal rule on an n x n grid covering [0, 1] x [0, 1]."""
    x = np.linspace(0.0, 1.0, n + 1)
    y = np.linspace(0.0, 1.0, n + 1)
    X, Y = np.meshgrid(x, y, indexing="xy")
    Z = integrand(X, Y)
    # Iterated trapezoid: integrate over y at each x, then over x.
    inner = np.trapz(Z, y, axis=0)
    return float(np.trapz(inner, x))


def main() -> None:
    rng = np.random.default_rng(seed=42)

    # Reference: a fine trapezoidal value.
    I_ref = trapezoidal_2d(n=400)
    print(f"Trapezoidal reference (n = 400): {I_ref:.6f}")

    # Coarser trapezoidal (the exercise's comparison point).
    I_trap40 = trapezoidal_2d(n=40)
    print(f"Trapezoidal (n = 40):            {I_trap40:.6f} "
          f"(err vs ref {abs(I_trap40 - I_ref):.3e})")

    # Monte Carlo.
    for n_samples in (10 ** k for k in (3, 4, 5)):
        mean, sem = monte_carlo(n_samples, rng)
        err = abs(mean - I_ref)
        print(f"Monte Carlo (N = {n_samples:>6d}): "
              f"{mean:.6f}  sem {sem:.3e}  err vs ref {err:.3e}")


if __name__ == "__main__":
    main()
