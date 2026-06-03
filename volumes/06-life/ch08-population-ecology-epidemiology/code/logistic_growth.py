# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numpy",
#     "matplotlib",
# ]
# ///
"""Logistic-growth examples for Vol VI Ch 8 §8.1.

Reproduces:
  * The closed-form logistic solution N(t) = K / (1 + A exp(-rt))
    against exponential N(t) = N0 exp(rt).
  * Harvested-logistic equilibria and maximum-sustainable-yield (MSY).
  * The Verhulst 1838 fit to Belgian-population data (illustrative,
    not historically reconstructive).

Usage:
  uv run logistic_growth.py
"""

import numpy as np
import matplotlib.pyplot as plt


def logistic_closed_form(t, r, K, N0):
    """Closed-form solution N(t) = K / (1 + ((K - N0)/N0) exp(-r t))."""
    A = (K - N0) / N0
    return K / (1 + A * np.exp(-r * t))


def exponential_growth(t, r, N0):
    """Pure exponential N(t) = N0 exp(r t) (no carrying capacity)."""
    return N0 * np.exp(r * t)


def msy_constant_harvest(r, K):
    """Maximum sustainable yield: H_max = r K / 4 at N = K/2."""
    return r * K / 4.0


def harvested_equilibria(r, K, H):
    """Equilibria of dN/dt = r N (1 - N/K) - H.

    For 0 < H < r K / 4, returns two real roots (stable high, unstable low).
    For H = r K / 4, returns the single tangent equilibrium K/2.
    For H > r K / 4, returns no real equilibrium (population collapses).
    """
    discriminant = 1 - 4 * H / (r * K)
    if discriminant < 0:
        return None
    sqrt_d = np.sqrt(discriminant)
    n_high = K * (1 + sqrt_d) / 2
    n_low = K * (1 - sqrt_d) / 2
    return (n_high, n_low)


def main():
    r = 0.5  # per unit time
    K = 1.0
    N0 = 0.05 * K
    t = np.linspace(0, 20, 400)

    N_logistic = logistic_closed_form(t, r, K, N0)
    N_exp = exponential_growth(t, r, N0)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(t, N_logistic, "-", label="logistic", linewidth=2)
    ax.plot(t, np.clip(N_exp, 0, 1.5), "--", label="exponential", linewidth=2)
    ax.axhline(K, color="gray", linestyle=":", linewidth=1, label="K")
    ax.axhline(K / 2, color="gray", linestyle=":", linewidth=0.5, label="K/2")
    ax.set_xlabel("time t")
    ax.set_ylabel("N(t) / K")
    ax.set_title("Logistic growth vs exponential, r = 0.5, N0 = 0.05 K")
    ax.legend(loc="lower right")
    ax.set_ylim(0, 1.3)
    fig.tight_layout()
    fig.savefig("logistic_growth.png", dpi=150)

    # MSY analysis
    print(f"Maximum sustainable yield H_max = r K / 4 = {msy_constant_harvest(r, K):.4f}")
    print("Harvest equilibria:")
    for H in [0.05, 0.10, 0.125, 0.14]:
        eq = harvested_equilibria(r, K, H)
        if eq is None:
            print(f"  H = {H:.3f}: no real equilibrium (collapse)")
        else:
            print(f"  H = {H:.3f}: stable high = {eq[0]:.3f}, unstable low = {eq[1]:.3f}")

    plt.close("all")


if __name__ == "__main__":
    main()
