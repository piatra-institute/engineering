"""Estimate per-base mutation rate from parent-offspring trio sequencing.

The standard method is to take a parent-parent-child trio that have
each been sequenced at high coverage and to enumerate the variants
that appear de novo in the child (i.e. that are absent from both
parents). The de novo count, normalised by the number of callable
genome positions, gives the per-base mutation rate per generation.

We provide:

  - estimate_rate: take counts and callable-genome size, return rate
  - confidence_interval: Wilson interval for the binomial proportion
  - simulate_trio: generate a synthetic trio with a known rate

Reference order-of-magnitude values (current as of 2024):

  E. coli                ~10^-9 per bp per generation
  Yeast (S. cerevisiae)  ~3e-10 per bp per generation
  D. melanogaster        ~3e-9 per bp per generation
  Human germline         ~1.2e-8 per bp per generation
"""
from __future__ import annotations

import argparse
import math
import random


def estimate_rate(n_denovo: int, callable_bases: int) -> float:
    if callable_bases <= 0:
        return 0.0
    return n_denovo / callable_bases


def confidence_interval(n: int, total: int, z: float = 1.96
                        ) -> tuple[float, float]:
    """Wilson 95% confidence interval for a binomial proportion."""
    if total == 0:
        return (0.0, 0.0)
    phat = n / total
    denom = 1.0 + z**2 / total
    centre = (phat + z**2 / (2 * total)) / denom
    margin = (z * math.sqrt(phat * (1 - phat) / total
              + z**2 / (4 * total**2))) / denom
    return (max(0.0, centre - margin), centre + margin)


def simulate_trio(genome_size: int, mu_per_bp: float,
                  seed: int = 42) -> tuple[int, int]:
    """Simulate a trio with known per-bp mutation rate.

    Returns (n_denovo, callable_bases) where n_denovo is drawn from a
    Poisson approximation Binomial(2 * genome_size, mu) and
    callable_bases is 0.9 * 2 * genome_size (the typical 90% callable
    fraction of a diploid genome).
    """
    rng = random.Random(seed)
    expected = 2 * genome_size * mu_per_bp
    # Poisson sample via Knuth method (fine for our expected values)
    k = 0
    L = math.exp(-expected)
    p = 1.0
    while True:
        p *= rng.random()
        if p < L:
            break
        k += 1
    callable_bases = int(0.9 * 2 * genome_size)
    return k, callable_bases


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--denovo", type=int, default=None,
                        help="observed de novo variant count")
    parser.add_argument("--callable", type=int, default=None,
                        help="callable diploid bases in the trio")
    parser.add_argument("--simulate", action="store_true",
                        help="run a synthetic-trio demonstration")
    parser.add_argument("--genome-size", type=int, default=3_200_000_000)
    parser.add_argument("--mu", type=float, default=1.2e-8)
    args = parser.parse_args()

    if args.simulate or args.denovo is None:
        n, c = simulate_trio(args.genome_size, args.mu)
        print(f"Simulated trio: {n} de novo variants, "
              f"{c:,} callable bases (true mu = {args.mu:.2e}/bp).")
    else:
        n, c = args.denovo, args.callable

    rate = estimate_rate(n, c)
    lo, hi = confidence_interval(n, c)
    print(f"Estimated mu = {rate:.3e} per bp per generation")
    print(f"95% Wilson CI = ({lo:.3e}, {hi:.3e}) per bp per generation")
    print(f"Implied de novo per genome (3.2 Gb haploid): {rate * 3.2e9:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
