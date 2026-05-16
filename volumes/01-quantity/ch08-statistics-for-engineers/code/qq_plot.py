# /// script
# requires-python = ">=3.11"
# dependencies = ["numpy", "matplotlib"]
# ///
"""Q-Q plot of a sample against the standard normal reference.

Demonstrates the diagnostic used in section 8.2 of chapter 8. We
draw three samples of n = 100 each: a true Gaussian, a t with five
degrees of freedom (heavy tails), and a lognormal (right-skewed).
Plot each as a Q-Q plot against N(0, 1). The script writes a PNG
to ./qq-plot-demo.png in the current working directory.
"""

import math
import numpy as np
import matplotlib.pyplot as plt

RNG = np.random.default_rng(2026)
N = 100


def qq_theoretical_quantiles(n: int) -> np.ndarray:
    # Plotting positions (i - 0.5) / n.
    p = (np.arange(1, n + 1) - 0.5) / n
    # Approximate standard normal inverse CDF (Beasley-Springer-Moro
    # could be used; here a rational approximation suffices for a plot).
    return np.array([math.sqrt(2) * math.erfinv(2 * pp - 1) for pp in p])


def main() -> None:
    samples = {
        "Gaussian": RNG.normal(0, 1, N),
        "t(5) (heavy)": RNG.standard_t(5, N),
        "lognormal": np.log(RNG.lognormal(0, 0.6, N)) - 0.18,  # roughly centred
    }
    z = qq_theoretical_quantiles(N)

    fig, axes = plt.subplots(1, 3, figsize=(11, 4), sharey=False)
    for ax, (name, sample) in zip(axes, samples.items()):
        sorted_sample = np.sort(sample)
        ax.scatter(z, sorted_sample, s=12, alpha=0.7)
        lo = min(z.min(), sorted_sample.min())
        hi = max(z.max(), sorted_sample.max())
        ax.plot([lo, hi], [lo, hi], "k--", lw=0.8)
        ax.set_title(name)
        ax.set_xlabel("theoretical z")
        ax.set_ylabel("observed (sorted)")
    fig.suptitle("Q-Q plot demonstration (n = 100)")
    fig.tight_layout()
    fig.savefig("qq-plot-demo.png", dpi=120)
    print("wrote qq-plot-demo.png")


if __name__ == "__main__":
    main()
