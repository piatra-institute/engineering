# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Demonstrate catastrophic cancellation in the quadratic formula and the
Vieta-companion fix used in the chapter's calculation exercise.

The roots of a x^2 + b x + c = 0 are (-b +/- sqrt(b^2 - 4ac)) / (2a).
When b^2 >> 4ac, the root for which -b and sqrt(...) nearly cancel
loses precision. The stable recipe computes the well-conditioned root
first (the one where the two terms add), then recovers the other from
the Vieta product x_+ x_- = c/a.

Supports Volume II, Chapter 1, section 1.1 and the calculation
exercise with a = 1.7e-3, b = -2.4e2, c = 1.1e4.

Usage:
  python quadratic_stability.py
"""

from __future__ import annotations

import math


def naive_roots(a: float, b: float, c: float) -> tuple[float, float]:
    disc = math.sqrt(b * b - 4 * a * c)
    return ((-b + disc) / (2 * a), (-b - disc) / (2 * a))


def stable_roots(a: float, b: float, c: float) -> tuple[float, float]:
    disc = math.sqrt(b * b - 4 * a * c)
    # Add the magnitudes so no cancellation occurs in the numerator.
    if b >= 0:
        q = -(b + disc) / 2
    else:
        q = -(b - disc) / 2
    x1 = q / a
    x2 = c / q  # Vieta companion: x1 * x2 = c / a.
    return (x1, x2)


def main() -> int:
    a, b, c = 1.7e-3, -2.4e2, 1.1e4
    n1, n2 = naive_roots(a, b, c)
    s1, s2 = stable_roots(a, b, c)
    print(f"naive roots:  {n1:.6e}  {n2:.6e}")
    print(f"stable roots: {s1:.6e}  {s2:.6e}")
    # Residual check: which recipe satisfies the equation better?
    for name, (r1, r2) in (("naive", (n1, n2)), ("stable", (s1, s2))):
        res = max(abs(a * r * r + b * r + c) for r in (r1, r2))
        print(f"{name:>6} max residual |a x^2 + b x + c| = {res:.3e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
