"""Lawson / triple-product check for a deuterium-tritium fusion plasma.

For D-T fusion the power-balance condition for ignition is usually written
as a triple product

    n * tau_E * T  >=  (12 k_B T^2) / (E_alpha * <sigma v>),

where n is the (equal) deuteron and triton density, tau_E the energy
confinement time, T the ion temperature, E_alpha = 3.5 MeV the alpha-
particle energy carried back into the plasma, and <sigma v> the
Maxwell-averaged D-T reactivity. Evaluated near the minimum (T ~ 10-20
keV) the required triple product is about 3e21 m^-3 keV s.

This module tabulates the reactivity from data/fusion_reactivity.csv,
computes the required triple product versus temperature, and reports the
margin for a sample operating point. Pure standard library.
"""

import csv

EV = 1.602176634e-19      # J
E_ALPHA = 3.5e6 * EV      # alpha energy returned to plasma, J


def load_reactivity(path="data/fusion_reactivity.csv"):
    """Return [(T_keV, <sigma v>_DT in m^3/s), ...]."""
    rows = []
    with open(path, newline="") as handle:
        for row in csv.DictReader(handle):
            rows.append((float(row["temperature_keV"]),
                         float(row["DT_sigmav_m3_s"])))
    return rows


def required_triple_product(temperature_kev, sigma_v):
    """Required n*tau_E*T in m^-3 keV s for ignition at this temperature.

    Triple product threshold n tau_E T >= 12 (k_B T)^2 / (E_alpha <sigma v>).
    Working in energy units T_J = T_keV * 1000 * EV so the result carries a
    factor of T_keV to land in m^-3 keV s.
    """
    t_joule = temperature_kev * 1000.0 * EV
    n_tau = 12.0 * t_joule / (E_ALPHA * sigma_v)   # required n*tau_E, s/m^3
    return n_tau * temperature_kev                  # multiply by T in keV


def main():
    table = load_reactivity()
    best_t, best_req = None, float("inf")
    print(f"{'T (keV)':>8}  {'<sigma v> (m^3/s)':>18}  {'req nTtau (m^-3 keV s)':>22}")
    for temperature, sigma_v in table:
        req = required_triple_product(temperature, sigma_v)
        print(f"{temperature:8.0f}  {sigma_v:18.2e}  {req:22.2e}")
        if req < best_req:
            best_req, best_t = req, temperature
    print(f"\nMinimum required triple product ~ {best_req:.2e} m^-3 keV s "
          f"near T = {best_t:.0f} keV")
    # Sample operating point: ITER-class.
    n, tau_e, t_kev = 1.0e20, 3.0, 15.0
    achieved = n * tau_e * t_kev
    print(f"Sample point n={n:.0e}, tau_E={tau_e}s, T={t_kev}keV -> "
          f"triple product {achieved:.2e} m^-3 keV s")


if __name__ == "__main__":
    main()
