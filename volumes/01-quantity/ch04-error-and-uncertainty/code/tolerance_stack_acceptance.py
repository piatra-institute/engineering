# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Tolerance stack acceptance-fraction comparison: linear vs Monte Carlo.

A three-part assembly with one widened, asymmetric tolerance. The
linear root-sum-square (RSS) approximation predicts a symmetric
Gaussian assembly distribution; the Monte Carlo run draws from the
specified manufacturing distributions (including one lognormal part)
and computes the empirical acceptance fraction inside the assembly
specification limits.

Run:    uv run tolerance_stack_acceptance.py

Reproduces the figures cited in Vol I Ch 4.3 (tolerance-stack
acceptance-fraction expansion).
"""

import numpy as np


RNG = np.random.default_rng(311)
N = 1_000_000

# Three-part assembly, nominal sum 75 mm. Parts 1 and 2 are Gaussian
# at tight tolerance; part 3 is the widened, asymmetric one.
NOMINAL = np.array([25.0, 25.0, 25.0])     # mm
T_LIMIT = np.array([0.05, 0.05, 0.08])     # mm, half-width spec
# Manufacturing Gaussian sigmas: tolerance interpreted as 3-sigma for
# parts 1 and 2; for part 3 the Gaussian model is replaced by a
# lognormal so the asymmetry is built into the input.
SIGMA_GAUSS = T_LIMIT / 3.0                # for parts 1 and 2

# Assembly specification (the design-side acceptance limits) is
# +/- 0.10 mm around the nominal of 75 mm.
ASSEMBLY_SPEC = 0.10


def draw_truncated_gaussian(mu, sigma, lo, hi, n, rng):
    """Rejection sampling from N(mu, sigma) truncated to [lo, hi]."""
    samples = np.empty(n)
    filled = 0
    while filled < n:
        batch_size = int(1.3 * (n - filled))
        batch = rng.normal(mu, sigma, size=batch_size)
        accepted = batch[(batch >= lo) & (batch <= hi)]
        take = min(len(accepted), n - filled)
        samples[filled : filled + take] = accepted[:take]
        filled += take
    return samples


def draw_truncated_lognormal_shifted(mu_center, t_half, n, rng):
    """A lognormal distribution centred at mu_center, with the long tail
    extending toward +mu_center + t_half. The right tail is heavier
    than the left tail by construction. Truncated to +/- t_half around
    mu_center."""
    # Working parameters: 95 percent of mass lies inside (-0.5 t_half, +t_half).
    # Choose the underlying log-normal scale so the empirical SD on
    # the truncated draw is comparable to the Gaussian case.
    sigma_log = 0.45  # shape parameter
    raw = rng.lognormal(mean=0.0, sigma=sigma_log, size=int(1.6 * n))
    # Translate so the mode lies near zero, then scale so the bulk
    # falls inside +/- 0.8 t_half.
    centred = (raw - np.exp(-sigma_log * sigma_log)) * (t_half * 0.55)
    inside = centred[(centred >= -t_half) & (centred <= t_half)]
    return mu_center + inside[:n]


def main() -> None:
    nominal_L = NOMINAL.sum()
    rss_sigma_linear = np.sqrt(
        SIGMA_GAUSS[0] ** 2 + SIGMA_GAUSS[1] ** 2 + (T_LIMIT[2] / 3.0) ** 2
    )

    print(f"nominal L                    : {nominal_L:.4f} mm")
    print(f"linear RSS sigma             : {rss_sigma_linear:.5f} mm")
    print(f"linear RSS pred. P(in spec)  : "
          f"{(2 * 0.5 * (1 + np.math.erf(ASSEMBLY_SPEC / (rss_sigma_linear * np.sqrt(2.0)))) - 1):.4f}")

    # Build the three parts.
    p1 = draw_truncated_gaussian(
        NOMINAL[0], SIGMA_GAUSS[0],
        NOMINAL[0] - T_LIMIT[0], NOMINAL[0] + T_LIMIT[0],
        N, RNG,
    )
    p2 = draw_truncated_gaussian(
        NOMINAL[1], SIGMA_GAUSS[1],
        NOMINAL[1] - T_LIMIT[1], NOMINAL[1] + T_LIMIT[1],
        N, RNG,
    )
    p3 = draw_truncated_lognormal_shifted(NOMINAL[2], T_LIMIT[2], N, RNG)

    n_min = min(len(p1), len(p2), len(p3))
    L = p1[:n_min] + p2[:n_min] + p3[:n_min]

    print()
    print(f"empirical L mean             : {L.mean():.5f} mm")
    print(f"empirical L std              : {L.std(ddof=1):.5f} mm")
    print(f"empirical skewness           : "
          f"{((L - L.mean()) ** 3).mean() / L.std() ** 3:.4f}")

    in_spec = ((L >= nominal_L - ASSEMBLY_SPEC) & (L <= nominal_L + ASSEMBLY_SPEC))
    above = (L > nominal_L + ASSEMBLY_SPEC).mean()
    below = (L < nominal_L - ASSEMBLY_SPEC).mean()
    print()
    print(f"Monte Carlo P(in spec)       : {in_spec.mean():.4f}")
    print(f"  fraction above USL         : {above:.4f}")
    print(f"  fraction below LSL         : {below:.4f}")


if __name__ == "__main__":
    main()
