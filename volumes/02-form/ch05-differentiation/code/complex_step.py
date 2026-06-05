# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""The complex-step derivative: differentiation without cancellation.

For a real-analytic f, the imaginary part of f(x + i h) divided by h
approximates f'(x) with truncation error O(h^2) and, because no
subtraction of nearly equal numbers occurs, no catastrophic
cancellation. The step h can be taken as small as 1e-200 and the
derivative is accurate to machine precision. This is the mastery-box
escape from the bias-variance V of real finite differences.

Used by: Section 5.7 mastery box (complex-step differentiation).
"""
import cmath


def complex_step(f, x: float, h: float) -> float:
    return f(complex(x, h)).imag / h


def central(f, x: float, h: float) -> float:
    return (f(x + h).real - f(x - h).real) / (2.0 * h)


def main() -> None:
    f = cmath.exp
    x = 1.0
    exact = cmath.exp(x).real
    print(f"f(x) = exp(x), x = {x}, exact f'(x) = {exact:.15f}")
    print(f"{'h':>10} {'complex-step err':>20} {'central err':>20}")
    for k in range(2, 18, 2):
        h = 10.0 ** (-k)
        cs = complex_step(f, x, h)
        cd = central(f, x, h)
        print(f"{h:>10.0e} {abs(cs - exact):>20.3e} {abs(cd - exact):>20.3e}")
    print("\nThe complex-step error keeps falling as h^2 with no")
    print("round-off floor; the central difference bottoms out near")
    print("h ~ 1e-5 and then degrades from cancellation.")


if __name__ == "__main__":
    main()
