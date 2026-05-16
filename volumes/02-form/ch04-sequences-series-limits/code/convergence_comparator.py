# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Compares iteration counts to reach a fixed tolerance for three
iteration patterns:

  - fixed-point (linear), rate r in (0, 1): error_n approx r^n * error_0
  - Newton (quadratic), |error_{n+1}| approx C * error_n^2
  - secant (super-linear, order phi = 1.618...): error_{n+1} approx C * error_n^{phi}

The script prints the number of iterations needed to reach
tolerances 1e-3, 1e-6, 1e-9, 1e-12 from a starting error of 1.0.

Used in the second estimation block on iterative-scheme precision.
"""

import math

PHI = (1.0 + math.sqrt(5.0)) / 2.0  # 1.6180...


def linear_iters(r: float, tol: float, e0: float = 1.0) -> int:
    """Smallest n with r^n * e0 <= tol."""
    if r >= 1:
        return -1
    return math.ceil(math.log(tol / e0) / math.log(r))


def quadratic_iters(c: float, tol: float, e0: float = 1.0) -> int:
    """Smallest n with c^(2^n - 1) * e0^(2^n) <= tol.

    Equivalent to log2 log(tol) form. Take logs: 2^n log(c * e0) - log c <= log tol.
    For c = 1, e0 = 1 the residual squares each step: e_n = e0^(2^n).
    We solve numerically.
    """
    e = e0
    n = 0
    while e > tol and n < 100:
        e = c * e * e
        n += 1
    return n


def super_linear_iters(c: float, order: float, tol: float, e0: float = 1.0) -> int:
    e = e0
    n = 0
    while e > tol and n < 100:
        e = c * (e ** order)
        n += 1
    return n


def main() -> None:
    tols = (1e-3, 1e-6, 1e-9, 1e-12)
    print(f"Iterations to reach tolerance from e_0 = 1.0\n")
    print(f"{'tolerance':>12}  {'fp r=0.5':>10}  {'fp r=0.1':>10}  {'Newton (c=1)':>14}  {'secant (c=1)':>14}")
    for tol in tols:
        n_lin5 = linear_iters(0.5, tol)
        n_lin1 = linear_iters(0.1, tol)
        n_quad = quadratic_iters(1.0, tol)
        n_sec = super_linear_iters(1.0, PHI, tol)
        print(f"{tol:>12.0e}  {n_lin5:>10d}  {n_lin1:>10d}  {n_quad:>14d}  {n_sec:>14d}")


if __name__ == "__main__":
    main()
