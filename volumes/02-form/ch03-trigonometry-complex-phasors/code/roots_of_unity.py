"""Roots of a complex number and the roots of unity.

Given a nonzero complex number z = r exp(i theta) and an integer n,
the n complex nth roots are

    w_k = r**(1/n) exp(i (theta + 2 pi k) / n),   k = 0, ..., n - 1.

This script computes the nth roots, verifies that each raised to the
nth power returns z, verifies that the n roots of unity (z = 1) sum to
zero for n >= 2, and plots the roots on the complex plane as the
corners of a regular n-gon.

Usage:
    uv run --with numpy --with matplotlib roots_of_unity.py

Dependencies: numpy, matplotlib.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def nth_roots(z: complex, n: int) -> np.ndarray:
    """Return the n complex nth roots of z as a numpy array."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    r = abs(z)
    theta = np.angle(z)
    k = np.arange(n)
    return r ** (1.0 / n) * np.exp(1j * (theta + 2.0 * np.pi * k) / n)


def main() -> None:
    # Cube roots of 8: expect 2, -1 + i sqrt(3), -1 - i sqrt(3).
    roots = nth_roots(8.0 + 0.0j, 3)
    print("Cube roots of 8:")
    for w in roots:
        print(f"  {w:.6f}  (|w| = {abs(w):.6f}, arg = {np.angle(w):.6f} rad)")
    # Verify each cubes back to 8.
    residual = np.max(np.abs(roots ** 3 - 8.0))
    print(f"max |w**3 - 8| = {residual:.3e}")

    # Roots of unity for several n: each set sums to zero for n >= 2.
    for n in range(2, 9):
        units = nth_roots(1.0 + 0.0j, n)
        s = np.sum(units)
        print(f"n = {n}: sum of nth roots of unity = {s:.3e}")

    # Plot the sixth roots of unity as a hexagon, with the cube roots marked.
    units6 = nth_roots(1.0 + 0.0j, 6)
    units3 = nth_roots(1.0 + 0.0j, 3)
    fig, ax = plt.subplots(figsize=(4.5, 4.5))
    circle = plt.Circle((0, 0), 1.0, fill=False, linestyle="--", alpha=0.4)
    ax.add_patch(circle)
    ring = np.append(units6, units6[0])
    ax.plot(ring.real, ring.imag, color="#1f4e79", linewidth=1.5)
    ax.plot(units6.real, units6.imag, "o", color="#1f4e79", label="6th roots")
    ax.plot(units3.real, units3.imag, "o", color="#992a2a", markersize=10,
            label="cube roots")
    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.set_aspect("equal")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.legend(loc="best", fontsize=8)
    fig.tight_layout()
    fig.savefig("roots_of_unity.png", dpi=120)
    print("Wrote roots_of_unity.png")


if __name__ == "__main__":
    main()
