#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""
Availability of a two-unit repairable redundant system (section 13.8
case study). Builds the continuous-time-Markov-chain generator on the
number of failed units {0, 1, 2}, solves the stationary distribution in
closed form, simulates the CTMC, and reports the raw and
control-variate estimates of the steady-state unavailability against the
analytical value, for the single-crew and two-crew repair policies.

State n = number of failed units. System is UP in states 0 and 1, DOWN
in state 2. Each working unit fails at rate lambda; the repair crew(s)
restore a failed unit at rate mu (single crew: rate mu out of state 2;
two crews: rate 2*mu out of state 2).

Generator (single crew), rows summing to zero:

    Q = [[-2L,      2L,        0   ],
         [ mu, -(L + mu),      L   ],
         [  0,      mu,      -mu   ]]

Closed-form stationary (single crew), r = lambda/mu:
    pi0 = 1/(1 + 2r + 2r^2)
    pi1 = 2r * pi0
    pi2 = 2r^2 * pi0
    unavailability Abar = pi2.

Two crews: state-2 exit rate is 2*mu, giving Abar = r^2 / (1 + r)^2.

The control-variate estimator subtracts the (correlated) state-1
occupancy, whose mean pi1 is known analytically:
    Abar_cv = pihat2 - c * (pihat1 - pi1),
with c chosen to minimise variance (estimated across replications).

Usage:
    uv run availability_ctmc.py
    uv run availability_ctmc.py --mttf 2000 --mttr 8 --horizon 5e6 --reps 200
    uv run availability_ctmc.py --two-crew
"""

from __future__ import annotations

import argparse

import numpy as np


def generator(lam: float, mu: float, two_crew: bool) -> np.ndarray:
    """Return the 3x3 CTMC generator on states {0, 1, 2}."""
    down_rate = 2.0 * mu if two_crew else mu
    return np.array([
        [-2.0 * lam, 2.0 * lam, 0.0],
        [mu, -(lam + mu), lam],
        [0.0, down_rate, -down_rate],
    ])


def stationary_analytic(lam: float, mu: float, two_crew: bool) -> np.ndarray:
    """Closed-form stationary distribution from detailed balance."""
    r = lam / mu
    if two_crew:
        # pi1 = 2r pi0 ; pi2 = (r/2) pi1 = r^2 pi0
        weights = np.array([1.0, 2.0 * r, r * r])
    else:
        weights = np.array([1.0, 2.0 * r, 2.0 * r * r])
    return weights / weights.sum()


def simulate_occupancy(Q: np.ndarray, horizon: float,
                       rng: np.random.Generator) -> np.ndarray:
    """Gillespie-style CTMC simulation; return time-fraction in each state."""
    n = Q.shape[0]
    exit_rate = -np.diag(Q)
    time_in_state = np.zeros(n)
    state = 0
    t = 0.0
    while t < horizon:
        rate = exit_rate[state]
        hold = rng.exponential(1.0 / rate)
        time_in_state[state] += hold
        t += hold
        # jump probabilities to other states
        probs = Q[state].copy()
        probs[state] = 0.0
        probs = probs / probs.sum()
        state = rng.choice(n, p=probs)
    return time_in_state / time_in_state.sum()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mttf", type=float, default=2000.0,
                    help="mean time to failure of one unit (hours)")
    ap.add_argument("--mttr", type=float, default=8.0,
                    help="mean time to repair of one unit (hours)")
    ap.add_argument("--horizon", type=float, default=2.0e6,
                    help="simulated time horizon per replication (hours)")
    ap.add_argument("--reps", type=int, default=200,
                    help="number of independent replications")
    ap.add_argument("--two-crew", action="store_true",
                    help="use two repair crews instead of one")
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()

    lam = 1.0 / args.mttf
    mu = 1.0 / args.mttr
    rng = np.random.default_rng(args.seed)

    Q = generator(lam, mu, args.two_crew)
    pi = stationary_analytic(lam, mu, args.two_crew)
    abar_exact = pi[2]

    # check pi Q = 0
    residual = np.abs(pi @ Q).max()

    pihat1 = np.empty(args.reps)
    pihat2 = np.empty(args.reps)
    for k in range(args.reps):
        occ = simulate_occupancy(Q, args.horizon, rng)
        pihat1[k] = occ[1]
        pihat2[k] = occ[2]

    raw_mean = pihat2.mean()
    raw_se = pihat2.std(ddof=1) / np.sqrt(args.reps)

    # control variate: subtract correlated state-1 occupancy (known mean)
    cov = np.cov(pihat2, pihat1)
    c = cov[0, 1] / cov[1, 1]
    cv = pihat2 - c * (pihat1 - pi[1])
    cv_mean = cv.mean()
    cv_se = cv.std(ddof=1) / np.sqrt(args.reps)

    policy = "two crews" if args.two_crew else "single crew"
    print(f"Repairable two-unit redundant system ({policy})")
    print(f"  lambda = {lam:.3e} /h, mu = {mu:.3e} /h, r = {lam/mu:.4f}")
    print(f"  || pi Q ||_inf = {residual:.2e}  (should be ~0)")
    print(f"  analytical pi = {np.array2string(pi, precision=6)}")
    print(f"  analytical availability A = {1 - abar_exact:.7f}")
    print(f"  analytical unavailability Abar = {abar_exact:.4e}")
    print()
    print(f"  raw MC unavailability    = {raw_mean:.4e} +/- {raw_se:.2e}")
    print(f"  control-variate estimate = {cv_mean:.4e} +/- {cv_se:.2e}")
    if cv_se > 0:
        print(f"  variance reduction factor = {(raw_se / cv_se) ** 2:.1f}x")


if __name__ == "__main__":
    main()
