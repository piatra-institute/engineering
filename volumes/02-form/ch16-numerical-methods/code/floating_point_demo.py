# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Print binary64 unit round-off, machine epsilon, and the absolute
representation error of the decimal constant 0.1.

Used by section 16.1 and Calculation exercises 1 and 2.
"""
from __future__ import annotations

import struct

import numpy as np


def binary64_bits(x: float) -> str:
    """Return the 64-bit IEEE 754 bit pattern of x as a string."""
    packed = struct.pack(">d", x)
    bits = "".join(f"{byte:08b}" for byte in packed)
    return f"{bits[0]} {bits[1:12]} {bits[12:]}"


def main() -> None:
    u_d = 2.0 ** -53
    eps_d = 2.0 ** -52
    u_s = 2.0 ** -24
    eps_s = 2.0 ** -23

    print("IEEE 754 unit round-off and machine epsilon")
    print(f"  binary64  u = 2^-53 = {u_d:.6e}, eps_m = 2^-52 = {eps_d:.6e}")
    print(f"  binary32  u = 2^-24 = {u_s:.6e}, eps_m = 2^-23 = {eps_s:.6e}")
    print()

    print("Numpy-reported epsilons (independent check):")
    print(f"  np.finfo(np.float64).eps = {np.finfo(np.float64).eps:.6e}")
    print(f"  np.finfo(np.float32).eps = {np.finfo(np.float32).eps:.6e}")
    print()

    print("Spacing near 1.0 and near 2^20:")
    print(f"  nextafter(1.0, 2.0) - 1.0   = {np.nextafter(1.0, 2.0) - 1.0:.6e}")
    near = 2.0 ** 20
    print(f"  nextafter(2^20, +inf) - 2^20 = {np.nextafter(near, np.inf) - near:.6e}")
    print()

    one_tenth = 0.1
    err = one_tenth - 0.1  # the literal 0.1 already rounded; for clarity
    # absolute error vs the exact rational 1/10 reconstructed at high precision
    # using Python's Fraction
    from fractions import Fraction

    exact = Fraction(1, 10)
    repr_frac = Fraction(*one_tenth.as_integer_ratio())
    abs_err = float(repr_frac - exact)
    print("Binary64 representation of 0.1:")
    print(f"  IEEE 754 bit pattern (sign | exponent | mantissa):")
    print(f"    {binary64_bits(one_tenth)}")
    print(f"  fl(0.1) - 0.1 = {abs_err:.6e}  (predicted ~ 0.1 * u ~ {0.1 * u_d:.6e})")
    print(f"  literal-vs-literal diff = {err} (zero by construction)")


if __name__ == "__main__":
    main()
