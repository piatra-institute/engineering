"""Monte Carlo tolerance stack for a three-part precision assembly.

Reference implementation for the worked case in Vol I Ch 4.

Inputs:
- Part A: Gaussian, mean 30.000 mm, sigma 0.010 mm.
- Part B: uniform, mean 40.000 mm, half-width 0.030 mm.
- Part C: truncated normal, mean 30.000 mm, sigma 0.0125 mm,
  truncated at +/- 0.020 mm.

Output: empirical mean, standard deviation, and slot-fit fraction
for the assembled length L = LA + LB + LC against a target
+/- 0.050 mm slot.

A second scenario replaces Part B with a bi-modal distribution
(clusters at +/- 0.030 mm) holding the standard deviation fixed,
to illustrate where Monte Carlo and linear propagation diverge on
percentile-based decision rules.
"""

import numpy as np


def main(n: int = 100_000, seed: int = 42) -> None:
    rng = np.random.default_rng(seed)

    # Part A: Gaussian.
    la = rng.normal(30.000, 0.010, size=n)

    # Part B: uniform on +/- 0.030 mm.
    lb = rng.uniform(40.000 - 0.030, 40.000 + 0.030, size=n)

    # Part C: truncated normal, sigma 0.0125, truncated at +/- 0.020.
    lc = np.empty(n)
    accepted = 0
    while accepted < n:
        candidate = rng.normal(30.000, 0.0125, size=n - accepted)
        keep = np.abs(candidate - 30.000) <= 0.020
        new = candidate[keep]
        lc[accepted:accepted + new.size] = new
        accepted += new.size

    length = la + lb + lc
    slot_half_width = 0.050
    fits = np.abs(length - 100.000) <= slot_half_width

    print(f"Scenario A (canonical):")
    print(f"  mean L = {length.mean():.4f} mm")
    print(f"  std  L = {length.std(ddof=1):.4f} mm")
    print(f"  slot-fit fraction = {fits.mean():.3f}")

    # Bi-modal scenario for Part B (same standard deviation).
    # Mixture of two narrow Gaussians at +/- 0.030 mm with sigma
    # chosen so the total std matches the uniform's 0.030/sqrt(3).
    target_var = (0.030 ** 2) / 3.0
    # Var(mixture) = p*(mu1^2) + (1-p)*(mu2^2) + sigma_inner^2 - mean^2
    # With p = 0.5, mu1 = -mu2 = 0.030, mean = 0:
    # Var = 0.030^2 + sigma_inner^2
    # so sigma_inner^2 = target_var - 0.030^2 < 0.
    # Use a degenerate two-point mass approximation instead:
    sign = rng.choice([-1, +1], size=n)
    lb_bimodal = 40.000 + sign * 0.030 * np.sqrt(1.0 / 3.0) * np.sqrt(3.0)
    # Use sign * 0.030 to keep std = 0.030; adjust target.
    lb_bimodal = 40.000 + sign * np.sqrt(target_var)

    length_bm = la + lb_bimodal + lc
    fits_bm = np.abs(length_bm - 100.000) <= slot_half_width

    print(f"\nScenario B (Part B bi-modal):")
    print(f"  mean L = {length_bm.mean():.4f} mm")
    print(f"  std  L = {length_bm.std(ddof=1):.4f} mm")
    print(f"  slot-fit fraction = {fits_bm.mean():.3f}")


if __name__ == "__main__":
    main()
