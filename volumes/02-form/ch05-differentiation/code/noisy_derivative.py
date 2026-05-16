# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Numerical derivative of a noisy sinusoid; bias-variance illustration.

Generates y(t) = sin(2 pi t) on a grid sampled at 200 samples per period
over five periods, adds Gaussian noise of stated sigma, and computes
the central-difference derivative at sub-sampling intervals h = dt,
2*dt, 4*dt, 8*dt. Reports the root-mean-square error of the estimate
against the true derivative 2 pi cos(2 pi t).

The standard library random module is used so the script has no
third-party dependencies.

Used by: Section 5.7 (Differentiating noisy data) and Simulation
exercise on Gaussian-noise central difference.
"""
import math
import random
import statistics


def true_signal(t: float) -> float:
    return math.sin(2.0 * math.pi * t)


def true_derivative(t: float) -> float:
    return 2.0 * math.pi * math.cos(2.0 * math.pi * t)


def central_diff_series(ts: list[float], ys: list[float], stride: int) -> tuple[list[float], list[float]]:
    """Central difference with sample stride; returns (t_evaluated, dy_estimate)."""
    if stride < 1:
        raise ValueError("stride must be at least 1")
    n = len(ys)
    ts_out: list[float] = []
    dy_out: list[float] = []
    for i in range(stride, n - stride):
        h = ts[i + stride] - ts[i - stride]
        if h <= 0:
            continue
        dy = (ys[i + stride] - ys[i - stride]) / h
        ts_out.append(ts[i])
        dy_out.append(dy)
    return ts_out, dy_out


def rms_error(estimates: list[float], truths: list[float]) -> float:
    sq = [(e - t) ** 2 for e, t in zip(estimates, truths, strict=True)]
    return math.sqrt(sum(sq) / len(sq))


def main() -> None:
    random.seed(2026)
    samples_per_period = 200
    periods = 5
    n = samples_per_period * periods + 1
    dt = 1.0 / samples_per_period

    ts = [k * dt for k in range(n)]
    sigma = 0.05
    ys_clean = [true_signal(t) for t in ts]
    ys = [y + random.gauss(0.0, sigma) for y in ys_clean]

    print(f"sigma = {sigma}, samples = {n}, dt = {dt:.4f}")
    print(f"{'stride':>7} {'effective h':>14} {'rms error':>14}")
    for stride in (1, 2, 4, 8, 16, 32):
        ts_e, dy_e = central_diff_series(ts, ys, stride)
        dy_true = [true_derivative(t) for t in ts_e]
        rms = rms_error(dy_e, dy_true)
        print(f"{stride:>7d} {stride * dt:>14.4f} {rms:>14.4e}")

    # Without noise, for reference
    print("\nNo-noise baseline:")
    for stride in (1, 2, 4, 8, 16, 32):
        ts_e, dy_e = central_diff_series(ts, ys_clean, stride)
        dy_true = [true_derivative(t) for t in ts_e]
        rms = rms_error(dy_e, dy_true)
        print(f"{stride:>7d} {stride * dt:>14.4f} {rms:>14.4e}")


if __name__ == "__main__":
    main()
