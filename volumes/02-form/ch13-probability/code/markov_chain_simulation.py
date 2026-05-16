#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
Markov chain simulation: empirical occupancy vs analytical stationary
distribution, spectral gap, and empirical mixing time.

Supports the chapter's Project (Markov chain simulation and convergence).
The default chain is the two-state weather chain of section 13.7:

    P = [[0.9, 0.1],
         [0.5, 0.5]]

with analytical stationary distribution pi = (5/6, 1/6). The script
accepts a user-supplied transition matrix via CLI.

Dependencies:
    numpy

Usage:
    uv run markov_chain_simulation.py
    uv run markov_chain_simulation.py --steps 100000 --seed 7
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np


WEATHER_P = np.array([
    [0.9, 0.1],
    [0.5, 0.5],
])


def stationary_distribution(P: np.ndarray) -> np.ndarray:
    """Left eigenvector of P with eigenvalue 1, normalised to sum to 1."""
    eigvals, eigvecs = np.linalg.eig(P.T)
    idx = int(np.argmin(np.abs(eigvals - 1.0)))
    pi = np.real(eigvecs[:, idx])
    pi = pi / pi.sum()
    return pi


def spectral_gap(P: np.ndarray) -> float:
    """1 - |lambda_2|, where lambda_2 is the second-largest-magnitude eig."""
    eigvals = np.linalg.eigvals(P)
    mags = np.sort(np.abs(eigvals))[::-1]
    return float(1.0 - mags[1])


def simulate(P: np.ndarray, steps: int, x0: int, rng: np.random.Generator) -> np.ndarray:
    """Sample a trajectory of length `steps` starting from state x0."""
    k = P.shape[0]
    trajectory = np.zeros(steps, dtype=np.int64)
    state = x0
    for t in range(steps):
        trajectory[t] = state
        state = int(rng.choice(k, p=P[state]))
    return trajectory


def occupancy(trajectory: np.ndarray, k: int) -> np.ndarray:
    """Empirical occupancy distribution over k states."""
    counts = np.bincount(trajectory, minlength=k)
    return counts / counts.sum()


def total_variation(p: np.ndarray, q: np.ndarray) -> float:
    return 0.5 * float(np.abs(p - q).sum())


def running_fraction(trajectory: np.ndarray, state: int) -> np.ndarray:
    indicator = (trajectory == state).astype(np.float64)
    cumsum = np.cumsum(indicator)
    t = np.arange(1, len(trajectory) + 1)
    return cumsum / t


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--steps", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument(
        "--write-trace",
        type=str,
        default="../data/markov_trace.csv",
        help="CSV path for the running fraction in state 0",
    )
    args = parser.parse_args()

    P = WEATHER_P
    k = P.shape[0]
    rng = np.random.default_rng(args.seed)

    pi = stationary_distribution(P)
    gap = spectral_gap(P)

    trajectory = simulate(P, args.steps, x0=0, rng=rng)
    pi_hat = occupancy(trajectory, k)
    tv = total_variation(pi_hat, pi)

    # Empirical mixing time: smallest T such that the running estimate is
    # within 0.05 in total variation of pi for every t >= T (clipped check
    # against state 0 for simplicity).
    running = running_fraction(trajectory, state=0)
    diffs = np.abs(running - pi[0])
    above_tol = np.where(diffs > 0.05)[0]
    mix_time = int(above_tol[-1] + 1) if len(above_tol) > 0 else 1

    print("Transition matrix P:")
    print(P)
    print(f"\nAnalytical stationary distribution pi = {pi}")
    print(f"Spectral gap (1 - |lambda_2|) = {gap:.4f}")
    print(f"Empirical occupancy after {args.steps:,} steps = {pi_hat}")
    print(f"Total variation TV(pi_hat, pi) = {tv:.4f}")
    print(f"Empirical mixing time (TV < 0.05 for state 0): T = {mix_time:,}")

    # Write running-fraction trace
    out_path = Path(args.write_trace).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["step", "running_fraction_state_0", "pi_0"])
        # Subsample for compactness
        sample_steps = np.unique(
            np.geomspace(1, args.steps, num=200).astype(int)
        )
        for s in sample_steps:
            writer.writerow([int(s), float(running[s - 1]), float(pi[0])])
    print(f"Wrote running-fraction trace to {out_path}")


if __name__ == "__main__":
    main()
