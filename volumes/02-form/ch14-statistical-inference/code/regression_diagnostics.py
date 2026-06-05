# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Worked ordinary-least-squares fit with residual diagnostics.

Reproduces the section 14.5 worked example on tensile-yield.csv:
the closed-form slope and intercept, the residual standard
deviation, the slope confidence interval, and R^2. Everything is
hand-rolled from primitives so the arithmetic of the normal
equations is visible. No numpy, no scipy: the point is the
procedure, not the library.

Run:
    uv run regression_diagnostics.py ../data/tensile-yield.csv
"""
from __future__ import annotations

import sys
from math import sqrt


def read_xy(path: str) -> tuple[list[float], list[float]]:
    xs: list[float] = []
    ys: list[float] = []
    with open(path) as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("x,"):
                continue
            a, b = line.split(",")
            xs.append(float(a))
            ys.append(float(b))
    return xs, ys


# Student t critical value, two-sided 95%, for small df. A short
# lookup table keeps the script dependency-free; extend as needed.
T_975 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571,
         6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228}


def ols_fit(xs: list[float], ys: list[float]) -> dict[str, float]:
    n = len(xs)
    xbar = sum(xs) / n
    ybar = sum(ys) / n
    s_xx = sum((x - xbar) ** 2 for x in xs)
    s_xy = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    s_yy = sum((y - ybar) ** 2 for y in ys)

    b1 = s_xy / s_xx
    b0 = ybar - b1 * xbar

    fitted = [b0 + b1 * x for x in xs]
    resid = [y - f for y, f in zip(ys, fitted)]
    rss = sum(r * r for r in resid)
    df = n - 2
    sigma2 = rss / df
    sigma = sqrt(sigma2)
    se_b1 = sigma / sqrt(s_xx)
    r2 = 1.0 - rss / s_yy

    tcrit = T_975.get(df, 1.96)
    ci_lo = b1 - tcrit * se_b1
    ci_hi = b1 + tcrit * se_b1

    return {
        "n": n, "b0": b0, "b1": b1, "sigma": sigma, "se_b1": se_b1,
        "r2": r2, "ci_lo": ci_lo, "ci_hi": ci_hi,
        "rss": rss, "fitted": fitted, "resid": resid,
    }


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "../data/tensile-yield.csv"
    xs, ys = read_xy(path)
    fit = ols_fit(xs, ys)

    print(f"n          = {fit['n']}")
    print(f"intercept  = {fit['b0']:.4f}")
    print(f"slope      = {fit['b1']:.4f}")
    print(f"resid sd   = {fit['sigma']:.4f}")
    print(f"se(slope)  = {fit['se_b1']:.4f}")
    print(f"slope 95%  = [{fit['ci_lo']:.4f}, {fit['ci_hi']:.4f}]")
    print(f"R^2        = {fit['r2']:.4f}")
    print("residuals against fitted:")
    for f, r in zip(fit["fitted"], fit["resid"]):
        print(f"  fitted={f:6.3f}  resid={r:+6.3f}")


if __name__ == "__main__":
    main()
