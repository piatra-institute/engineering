# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Rounding-accumulation simulation along a 50-step measurement chain.

Each step is a multiplicative correction of size near 1.000; the
chain models a calibration cascade in which each step's correction
was reported to three decimal places. The simulation compares three
strategies:

  (a) round-to-nearest-ties-to-even at each step (IEEE 754 default;
      banker's rounding);
  (b) round-toward-positive (always round up) at each step;
  (c) carry full IEEE 754 binary64 precision through and round only
      at the final report.

The expectation: (a) shows zero mean bias and a random-walk spread
that grows as sqrt(N); (b) shows linear-in-N bias (the Vancouver-
Stock-Exchange failure mode); (c) shows essentially no rounding
error.

Run:    uv run rounding_chain.py
"""

import numpy as np


RNG = np.random.default_rng(1117)
N_STEPS = 50
N_TRIALS = 10_000

# Each correction is drawn from a uniform on (0.997, 1.003): the
# product of N_STEPS such corrections has expected value 1.0 and
# multiplicative spread proportional to sqrt(N_STEPS).
LO, HI = 0.997, 1.003


def round_half_even(x, places):
    """Round x to the given number of decimal places, ties to even."""
    return np.round(x, decimals=places)


def round_up(x, places):
    """Round x toward +infinity at the given number of decimal places."""
    factor = 10.0 ** places
    return np.ceil(x * factor) / factor


def main() -> None:
    corrections = RNG.uniform(LO, HI, size=(N_TRIALS, N_STEPS))
    truth_final = corrections.prod(axis=1)

    # (a) round-half-to-even, 3 decimal places, at every step.
    chain_a = np.ones(N_TRIALS)
    for k in range(N_STEPS):
        chain_a = chain_a * corrections[:, k]
        chain_a = round_half_even(chain_a, 3)

    # (b) round-up, 3 decimal places, at every step.
    chain_b = np.ones(N_TRIALS)
    for k in range(N_STEPS):
        chain_b = chain_b * corrections[:, k]
        chain_b = round_up(chain_b, 3)

    # (c) full precision, round only the final value.
    chain_c = round_half_even(truth_final, 3)

    print(f"chain length                : {N_STEPS} steps")
    print(f"trials                      : {N_TRIALS}")
    print(f"mean of true final value    : {truth_final.mean():.6f}")
    print()
    print("(a) round-half-to-even per step:")
    print(f"  mean of (a) - truth       : {(chain_a - truth_final).mean():+.6f}")
    print(f"  std of (a) - truth        : {(chain_a - truth_final).std(ddof=1):.6f}")
    print()
    print("(b) round-up per step:")
    print(f"  mean of (b) - truth       : {(chain_b - truth_final).mean():+.6f}")
    print(f"  std of (b) - truth        : {(chain_b - truth_final).std(ddof=1):.6f}")
    print()
    print("(c) round only at end:")
    print(f"  mean of (c) - truth       : {(chain_c - truth_final).mean():+.6f}")
    print(f"  std of (c) - truth        : {(chain_c - truth_final).std(ddof=1):.6f}")
    print()
    # The directional-rounding bias scales linearly with N_STEPS;
    # the round-to-even bias is consistent with zero.
    print(f"predicted bias per step (b)  : ~0.0005 (half the last-place unit)")
    print(f"predicted total bias (b)     : {0.0005 * N_STEPS:+.4f}")


if __name__ == "__main__":
    main()
