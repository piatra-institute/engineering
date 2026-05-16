# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Newton's iteration for the root of g(x) = x^3 - 2x - 5.

Demonstrates quadratic convergence near the root. Reports each
iterate, the residual, and the decade of error reduction at each
step.

Used by: Section 5.4 (linearisation as the engine of Newton's method)
and Simulation exercise on Newton iteration for g(x) = x^3 - 2x - 5.
"""
from math import log10


def g(x: float) -> float:
    return x**3 - 2.0 * x - 5.0


def gp(x: float) -> float:
    return 3.0 * x**2 - 2.0


def newton(g_fun, gp_fun, x0: float, n: int) -> list[float]:
    xs = [x0]
    for _ in range(n):
        x = xs[-1]
        xs.append(x - g_fun(x) / gp_fun(x))
    return xs


def main() -> None:
    x0 = 2.0
    xs = newton(g, gp, x0, n=8)
    # Reference root (from converged Newton)
    root = xs[-1]
    print(f"reference root x* = {root:.15f}")
    print(f"{'n':>3} {'x_n':>20} {'|g(x_n)|':>14} {'|x_n - x*|':>14}")
    for k, x in enumerate(xs):
        err = abs(x - root)
        print(f"{k:>3d} {x:>20.15f} {abs(g(x)):>14.3e} {err:>14.3e}")

    # Decade reductions: log10(err_{n+1}) - log10(err_n) ~ -1 expected per step
    # near convergence (quadratic). We compare consecutive log10 errors.
    print("\nConvergence rate (log10 ratio of consecutive errors):")
    for k in range(1, len(xs) - 1):
        e_prev = abs(xs[k - 1] - root)
        e_curr = abs(xs[k] - root)
        if e_prev > 0 and e_curr > 0:
            ratio = log10(e_curr) / log10(e_prev) if log10(e_prev) != 0 else float("nan")
            print(f"  step {k}: log10(e_{k}) / log10(e_{k - 1}) = {ratio:.3f}")


if __name__ == "__main__":
    main()
