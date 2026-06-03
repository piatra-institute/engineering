"""
One-dimensional Crank-style diffusion model of drug release from a
coated stent strut.

Vol VI Ch 12 sec 12.4. Used by Estimation 12.2 and Simulation
exercise 2.

The model:
- 1D slab of polymer drug-reservoir coating of thickness L (e.g.,
  5 to 15 micrometres), initial uniform concentration C0.
- Released into an effectively infinite tissue sink at x = L+.
- The polymer-side mass-balance follows Fick's second law with
  diffusivity D_polymer, typically 1e-13 to 1e-11 cm^2/s for
  rapamycin-like drugs in PEVA or PBMA matrices.
- Closed-form short-time approximation (Higuchi t^{1/2}) and long-
  time approximation (single-exponential) are both reported.

Reference: paper:v6c12-crank-diffusion-1975, sec 4.3.
Higuchi approximation: paper:v6c12-higuchi-drug-release-1961.
"""

from __future__ import annotations
import math


def crank_cumulative_release(t_s: float, L_m: float,
                              D_m2_per_s: float,
                              n_terms: int = 50) -> float:
    """
    Crank's solution for cumulative release from a 1D slab with
    constant initial concentration and zero surface concentration
    (perfect sink). M_t / M_inf = 1 - (8/pi^2) sum_{n=0}^inf
    [1/(2n+1)^2] * exp(-(2n+1)^2 pi^2 D t / L^2).

    Inputs in SI; output is dimensionless [0, 1].
    """
    if t_s <= 0 or L_m <= 0 or D_m2_per_s <= 0:
        return 0.0
    arg_prefactor = - (math.pi ** 2) * D_m2_per_s * t_s / (L_m ** 2)
    total = 0.0
    for n in range(n_terms):
        m = 2 * n + 1
        total += (1.0 / (m * m)) * math.exp((m * m) * arg_prefactor)
    return 1.0 - (8.0 / (math.pi ** 2)) * total


def higuchi_short_time(t_s: float, L_m: float,
                       D_m2_per_s: float) -> float:
    """Higuchi short-time approximation: M_t/M_inf ~ (4/L) sqrt(Dt/pi)."""
    if t_s <= 0:
        return 0.0
    return (4.0 / L_m) * math.sqrt(D_m2_per_s * t_s / math.pi)


def exponential_long_time(t_s: float, L_m: float,
                          D_m2_per_s: float) -> float:
    """Single-mode long-time approximation: M_t/M_inf ~ 1 - (8/pi^2) exp(-pi^2 D t / L^2)."""
    arg = - (math.pi ** 2) * D_m2_per_s * t_s / (L_m ** 2)
    return 1.0 - (8.0 / (math.pi ** 2)) * math.exp(arg)


def characteristic_time(L_m: float, D_m2_per_s: float) -> float:
    """tau = L^2 / (pi^2 D); the dominant Crank-mode timescale."""
    return (L_m ** 2) / (math.pi ** 2 * D_m2_per_s)


def main() -> None:
    # Default: 10 micrometre coating, D = 1e-12 cm^2/s = 1e-16 m^2/s
    L = 10.0e-6
    D = 1.0e-16

    tau = characteristic_time(L, D)
    print(f"Characteristic time tau = L^2 / (pi^2 D) = {tau:.2e} s "
          f"= {tau/86400:.1f} days")
    print()

    print(f"{'t (h)':>8} {'Crank':>10} {'Higuchi':>10} {'Exp tail':>10}")
    for t_h in (0.1, 0.5, 1.0, 4.0, 24.0, 7 * 24.0, 30 * 24.0,
                90 * 24.0):
        t_s = t_h * 3600.0
        a = crank_cumulative_release(t_s, L, D)
        b = higuchi_short_time(t_s, L, D)
        c = exponential_long_time(t_s, L, D)
        print(f"{t_h:>8.2f} {a:>10.4f} {b:>10.4f} {c:>10.4f}")


if __name__ == "__main__":
    main()
