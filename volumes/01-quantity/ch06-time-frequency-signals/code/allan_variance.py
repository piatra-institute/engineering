# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Allan variance / Allan deviation estimator.

Implements the overlapping Allan variance for a sequence of
fractional-frequency samples y[i] at uniform spacing tau0.

Reference: Allan (1966), "Statistics of atomic frequency standards",
Proc. IEEE 54(2), 221-230.

This script generates synthetic data with three different noise
families (white frequency modulation, flicker frequency modulation
approximated by an integrated random walk, and a linear drift),
computes the Allan deviation as a function of averaging time tau,
and prints a small table.
"""

import numpy as np

RNG = np.random.default_rng(2026)


def allan_dev(y: np.ndarray, tau0: float, m: int) -> float:
    """Overlapping Allan deviation at averaging time tau = m * tau0."""
    n = len(y)
    if 2 * m >= n:
        return float("nan")
    # Average over m consecutive samples
    cumsum = np.concatenate([[0.0], np.cumsum(y)])
    avg = (cumsum[m:] - cumsum[:-m]) / m
    # Adjacent differences of the averages, offset by m
    diff = avg[m:] - avg[:-m]
    var = 0.5 * np.mean(diff ** 2)
    return float(np.sqrt(var))


def main() -> None:
    tau0 = 1.0       # 1 s sample spacing
    n = 10_000

    # White FM: i.i.d. fractional-frequency samples
    y_white = RNG.normal(0.0, 1.0e-10, size=n)

    # Approximation of flicker: low-pass-filtered white noise
    raw = RNG.normal(0.0, 1.0e-10, size=n)
    alpha = 0.01
    y_flicker = np.zeros(n)
    y_flicker[0] = raw[0]
    for i in range(1, n):
        y_flicker[i] = (1 - alpha) * y_flicker[i - 1] + alpha * raw[i]

    # Linear drift
    y_drift = 1.0e-14 * np.arange(n)

    cases = (
        ("white FM",   y_white),
        ("flicker FM", y_flicker),
        ("drift",      y_white + y_drift),
    )

    taus = (1, 10, 100, 1_000)
    print(f"{'tau (s)':>8}  " + "  ".join(f"{name:>14}" for name, _ in cases))
    for tau in taus:
        row = [f"{tau:>8d}"]
        for _, y in cases:
            ad = allan_dev(y, tau0, tau)
            row.append(f"{ad:>14.3e}")
        print("  ".join(row))


if __name__ == "__main__":
    main()
