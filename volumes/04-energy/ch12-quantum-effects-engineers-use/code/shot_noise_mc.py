#!/usr/bin/env python3
"""Monte Carlo check that photon counting is Poisson: the variance of the
count equals the mean, so the shot-noise standard deviation is sqrt(N).

Simulates the number of photons arriving in a fixed window for several mean
rates, and reports the sample mean, variance, and the Gaussian-approximation
quality. No external libraries; uses the standard library random module.

Run:
    python3 code/shot_noise_mc.py
"""
import random
import math

random.seed(20240601)

TRIALS = 200_000


def poisson_sample(mean):
    """Knuth's algorithm for a Poisson deviate (adequate for modest means)."""
    L = math.exp(-mean)
    k = 0
    p = 1.0
    while True:
        k += 1
        p *= random.random()
        if p <= L:
            return k - 1


def run(mean):
    counts = [poisson_sample(mean) for _ in range(TRIALS)]
    n = len(counts)
    m = sum(counts) / n
    var = sum((c - m) ** 2 for c in counts) / n
    return m, var


def main():
    print(f"{'mean N':>8} {'sample mean':>12} {'sample var':>12} "
          f"{'var/mean':>9} {'sqrt(N)':>9}")
    for mean in (1.0, 4.0, 16.0, 64.0):
        m, var = run(mean)
        print(f"{mean:8.1f} {m:12.3f} {var:12.3f} "
              f"{var/m:9.3f} {math.sqrt(mean):9.3f}")
    print("\nvar/mean approaches 1: the count is Poisson and the shot-noise")
    print("standard deviation is sqrt(N). The Gaussian approximation is")
    print("useful once the mean exceeds roughly 10 to 20 counts.")


if __name__ == "__main__":
    main()
