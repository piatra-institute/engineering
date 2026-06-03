"""Wright-Fisher drift simulation, supporting the chapter project.

The standard Wright-Fisher model treats a finite diploid population of
size N as follows. Each generation, 2N gametes are sampled with
replacement from the previous generation's allele pool. With initial
allele frequency p_0 = 0.5 and no selection, the focal allele either
fixes (frequency = 1) or is lost (frequency = 0) with probability 0.5,
and the expected number of generations to fixation conditional on
fixation scales as ~2.8 N for a diploid population.

The script:

  1. Runs n_reps independent populations for each of several N values.
  2. Records the fixation generation and the eventual fate.
  3. Reports the empirical mean fixation time and the fixation
     probability with a selective advantage s.

Usage:
    python wright_fisher_drift.py
    python wright_fisher_drift.py --N 10,100,1000 --reps 1000 --s 0.01
"""
from __future__ import annotations

import argparse
import random
import statistics


def wright_fisher_step(n_alleles: int, two_n: int,
                       s: float, rng: random.Random) -> int:
    """Sample a new count of the focal allele under Wright-Fisher.

    With selection coefficient s on the focal allele, the effective
    sampling probability is

        p_eff = (1 + s) * p / (1 + s * p)
    """
    p = n_alleles / two_n
    if s != 0.0:
        p = (1.0 + s) * p / (1.0 + s * p)
    # Binomial sampling: 2N independent Bernoulli draws
    n_new = sum(1 for _ in range(two_n) if rng.random() < p)
    return n_new


def simulate_one(N: int, p0: float, s: float, max_gen: int,
                 rng: random.Random) -> tuple[int, int]:
    """Run a single population until fixation or max_gen.

    Returns (generation_at_fix, final_count). final_count is 0 (loss)
    or 2N (fixation) if the run reached an absorbing state.
    """
    two_n = 2 * N
    n_alleles = int(round(p0 * two_n))
    for g in range(1, max_gen + 1):
        n_alleles = wright_fisher_step(n_alleles, two_n, s, rng)
        if n_alleles in (0, two_n):
            return g, n_alleles
    return max_gen, n_alleles


def run_batch(N: int, n_reps: int, p0: float, s: float, seed: int) -> dict:
    rng = random.Random(seed)
    fix_times = []
    losses = 0
    fixes = 0
    cutoffs = 0
    max_gen = 50 * N
    for _ in range(n_reps):
        g, final = simulate_one(N, p0, s, max_gen, rng)
        if final == 0:
            losses += 1
        elif final == 2 * N:
            fixes += 1
            fix_times.append(g)
        else:
            cutoffs += 1
    summary = {
        "N": N,
        "n_reps": n_reps,
        "fixed": fixes,
        "lost": losses,
        "cutoff": cutoffs,
        "p_fix_empirical": fixes / n_reps,
        "mean_fix_time": statistics.mean(fix_times) if fix_times else 0.0,
        "stdev_fix_time": (statistics.stdev(fix_times)
                           if len(fix_times) > 1 else 0.0),
        "expected_neutral_T_fix": 2.8 * N,
    }
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=str, default="10,100,1000",
                        help="comma-separated list of population sizes")
    parser.add_argument("--reps", type=int, default=1000)
    parser.add_argument("--p0", type=float, default=0.5)
    parser.add_argument("--s", type=float, default=0.0,
                        help="selection coefficient on the focal allele")
    parser.add_argument("--seed", type=int, default=20251201)
    args = parser.parse_args()

    Ns = [int(x) for x in args.N.split(",")]
    print(f"# Wright-Fisher batch, p0={args.p0}, s={args.s}, "
          f"reps={args.reps}, seed={args.seed}")
    print("N, fixed, lost, p_fix, mean_T_fix, expected_neutral_T_fix")
    for i, N in enumerate(Ns):
        summary = run_batch(N, args.reps, args.p0, args.s,
                            seed=args.seed + i)
        print(f"{summary['N']}, {summary['fixed']}, {summary['lost']}, "
              f"{summary['p_fix_empirical']:.3f}, "
              f"{summary['mean_fix_time']:.1f}, "
              f"{summary['expected_neutral_T_fix']:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
