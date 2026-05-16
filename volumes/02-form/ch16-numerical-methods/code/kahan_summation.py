# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Compare naive sequential summation against Kahan compensated
summation on a vector of 10^6 alternating-sign numbers whose exact
sum is small relative to the partial-sum magnitudes.

Used by section 16.1 estimation and Calculation exercise 1.
"""
from __future__ import annotations

import numpy as np


def naive_sum(xs: np.ndarray) -> float:
    total = 0.0
    for x in xs:
        total = total + float(x)
    return total


def kahan_sum(xs: np.ndarray) -> float:
    total = 0.0
    c = 0.0  # compensation
    for x in xs:
        y = float(x) - c
        t = total + y
        c = (t - total) - y
        total = t
    return total


def main() -> None:
    rng = np.random.default_rng(42)
    n = 1_000_000
    # mixed magnitudes: large positive and negative summands plus a small bias
    xs = rng.standard_normal(n) * 1e3
    xs[0] += 1.0  # exact sum is approximately 1.0 plus the noise sum

    naive = naive_sum(xs)
    kahan = kahan_sum(xs)
    numpy = float(np.sum(xs))
    fsum = float(np.fsum(xs))  # math.fsum-equivalent: high-precision

    print(f"N = {n}")
    print(f"  naive sequential sum : {naive:.12e}")
    print(f"  numpy.sum            : {numpy:.12e}")
    print(f"  Kahan compensated    : {kahan:.12e}")
    print(f"  np.fsum (reference)  : {fsum:.12e}")
    print()
    print(f"  |naive - fsum|       : {abs(naive - fsum):.6e}")
    print(f"  |numpy - fsum|       : {abs(numpy - fsum):.6e}")
    print(f"  |Kahan - fsum|       : {abs(kahan - fsum):.6e}")


if __name__ == "__main__":
    main()
