# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy"]
# ///
"""Monte Carlo tolerance stack for a three-part linear assembly.

Each part is drawn from a Gaussian truncated at the specification
limits. Two scenarios are run:

  (i)  centred process: manufacturing mean equals the nominal,
       so truncation barely bites.
  (ii) shifted process: manufacturing mean offset by +t/2 inside
       the upper specification limit, so truncation removes a
       substantial fraction of the upper tail.

The reference uses N=1,000,000 draws per scenario to drive the
standard error of the estimator below 0.1 percent of sigma. The
seed is fixed for reproducibility.
"""

import numpy as np

RNG = np.random.default_rng(202)
N = 1_000_000

# Three parts, each with nominal length mu = 25 mm and
# specification half-width t = 0.05 mm. Treat t as 3 sigma on
# the (untruncated) manufacturing distribution.
MU = np.array([25.0, 25.0, 25.0])      # mm
T = np.array([0.05, 0.05, 0.05])       # mm, +/- spec half-width
SIGMA = T / 3.0

SCENARIOS = {
    "centred": np.zeros(3),                # process means at nominal
    "shifted": np.array([T[0] / 2, 0.0, 0.0]),  # part 1 offset by +t/2
}


def draw_truncated(mu_eff, sigma, lo, hi, n, rng):
    """Draw n samples from N(mu_eff, sigma) truncated to [lo, hi].

    Uses rejection sampling. Returns the accepted samples and the
    rejection fraction for diagnostic purposes.
    """
    samples = np.empty(n)
    filled = 0
    drawn = 0
    while filled < n:
        batch_size = int(1.2 * (n - filled))
        batch = rng.normal(mu_eff, sigma, size=batch_size)
        drawn += batch_size
        accepted = batch[(batch >= lo) & (batch <= hi)]
        take = min(len(accepted), n - filled)
        samples[filled : filled + take] = accepted[:take]
        filled += take
    rejection = 1.0 - n / drawn
    return samples, rejection


def main() -> None:
    nominal_L = MU.sum()
    # Linear-propagation prediction (RSS on the untruncated Gaussians).
    u_c_linear = np.sqrt((SIGMA ** 2).sum())
    print(f"nominal L                  : {nominal_L:.4f}  mm")
    print(f"linear-prop sd of L (RSS)  : {u_c_linear:.4f}  mm")
    print()

    for name, offset in SCENARIOS.items():
        print(f"--- scenario: {name} ---")
        parts = np.empty((3, N))
        for i in range(3):
            mu_eff = MU[i] + offset[i]
            lo, hi = MU[i] - T[i], MU[i] + T[i]
            parts[i], rej = draw_truncated(mu_eff, SIGMA[i], lo, hi, N, RNG)
            print(f"  part {i+1}: mu_eff={mu_eff:.4f}  rejected={rej*100:.2f}%")
        L = parts.sum(axis=0)
        print(f"  empirical mean L     : {L.mean():.4f}  mm")
        print(f"  empirical sd L       : {L.std(ddof=1):.4f}  mm")
        print(f"  ratio sd/(RSS)       : {L.std(ddof=1) / u_c_linear:.4f}")
        # Fraction outside +/- 3 * u_c_linear of nominal_L.
        out = ((L < nominal_L - 3 * u_c_linear)
               | (L > nominal_L + 3 * u_c_linear))
        print(f"  fraction > 3 sigma   : {out.mean()*100:.2f}%")
        print()


if __name__ == "__main__":
    main()
