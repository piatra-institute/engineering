# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Related-rates: the sliding ladder.

A ladder of fixed length L rests against a wall. The foot slides out
at constant speed dx/dt = v. The constraint x^2 + y^2 = L^2 fixes the
vertical rate dy/dt = -(x/y) v. This script tabulates the top's speed
as the foot approaches the wall's base, illustrating the kinematic
singularity dy/dt -> -infinity as y -> 0.

Used by: Section 5.2 (implicit differentiation, related rates) and
the related-rates figure.
"""
from math import sqrt


def top_rate(L: float, x: float, v: float) -> float:
    """dy/dt for foot at horizontal distance x moving at speed v."""
    y = sqrt(L * L - x * x)
    if y == 0.0:
        return float("-inf")
    return -(x / y) * v


def main() -> None:
    L = 5.0  # metres
    v = 0.5  # foot slides out at 0.5 m/s
    print(f"ladder length L = {L} m, foot speed v = {v} m/s")
    print(f"{'x (m)':>8} {'y (m)':>8} {'dy/dt (m/s)':>14}")
    for x in [1.0, 2.0, 3.0, 4.0, 4.5, 4.9, 4.99, 4.999]:
        y = sqrt(L * L - x * x)
        print(f"{x:>8.3f} {y:>8.3f} {top_rate(L, x, v):>14.3f}")
    print("\nAs the foot nears the wall base (y -> 0) the top speed")
    print("diverges in the idealised constraint; real ladders leave")
    print("the wall before this regime.")


if __name__ == "__main__":
    main()
