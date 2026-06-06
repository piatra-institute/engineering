# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
Fourier-coefficient computation pipeline by quadrature. Supports Volume
II, Chapter 6 (Fourier-coefficient subsection) and figure
fig-fourier-coefficients.

For a period-T signal s(t), the Fourier sine and cosine coefficients are
the projection integrals

    a_n = (2/T) int_0^T s(t) cos(n omega t) dt,
    b_n = (2/T) int_0^T s(t) sin(n omega t) dt,    omega = 2 pi / T.

Orthogonality of the trigonometric family makes each coefficient an
independent integral that picks out one harmonic. We compute the
coefficients of a unit square wave two ways: by the closed form
(b_n = 4/(n pi) for odd n, zero otherwise) and by trapezoidal quadrature
of the projection integral on a fine grid, and confirm the two agree.
We then reconstruct partial sums for N = 1, 3, 9 terms (the figure) and
report the L2 reconstruction error against the target, exhibiting the
Gibbs overshoot near the jumps.

Run directly with uv:
    uv run fourier_coefficients.py
"""

from __future__ import annotations

import numpy as np

T = 1.0
OMEGA = 2 * np.pi / T


def square_wave(t: np.ndarray) -> np.ndarray:
    """Unit square wave: +1 on (0, T/2), -1 on (T/2, T)."""
    return np.where((t % T) < T / 2, 1.0, -1.0)


def b_coeff_quadrature(n: int, samples: int = 20001) -> float:
    """b_n by trapezoidal quadrature of the projection integral."""
    t = np.linspace(0, T, samples)
    integrand = square_wave(t) * np.sin(n * OMEGA * t)
    integral = np.trapezoid(integrand, t)
    return 2.0 / T * integral


def b_coeff_closed(n: int) -> float:
    """b_n closed form for the unit square wave."""
    return 4.0 / (n * np.pi) if n % 2 == 1 else 0.0


def partial_sum(t: np.ndarray, n_terms: int) -> np.ndarray:
    s = np.zeros_like(t)
    n_odd = 0
    n = 1
    while n_odd < n_terms:
        s += b_coeff_closed(n) * np.sin(n * OMEGA * t)
        n_odd += 1
        n += 2
    return s


def main() -> None:
    print("Fourier sine coefficients of a unit square wave")
    print(f"{'n':>3} {'closed form':>14} {'quadrature':>14} {'rel err':>12}")
    for n in range(1, 12):
        bc = b_coeff_closed(n)
        bq = b_coeff_quadrature(n)
        rel = abs(bq - bc) / abs(bc) if bc else abs(bq)
        print(f"{n:>3} {bc:>14.6f} {bq:>14.6f} {rel:>12.2e}")

    t = np.linspace(0, T, 4001)
    target = square_wave(t)
    print("\nReconstruction L2 error vs number of terms:")
    for nt in (1, 3, 9, 25):
        recon = partial_sum(t, nt)
        l2 = np.sqrt(np.trapezoid((recon - target) ** 2, t))
        peak = recon.max()
        print(f"  N={nt:>2} terms: L2 error {l2:.4f}, peak {peak:.4f} "
              f"(Gibbs overshoot {(peak-1)*100:.1f}%)")


if __name__ == "__main__":
    main()
