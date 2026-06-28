"""Saha ionization fraction for atomic hydrogen versus temperature.

Solves the Saha equation for the ionization fraction x = n_i / n_total
of a hydrogen gas at fixed total (nucleus) number density n_tot, treating
a single ionization stage:

    n_e n_i / n_n = (m_e k_B T / (2 pi hbar^2))^{3/2} exp(-E_i / k_B T).

With charge neutrality n_e = n_i and total nuclei n_tot = n_i + n_n, and
defining x = n_i / n_tot, the right-hand side S(T) gives

    x^2 / (1 - x) = S(T) / n_tot,   so   x = (-r + sqrt(r^2 + 4 r)) / 2,
    r = S(T) / n_tot.

The ionization fraction depends on density as well as temperature; the
reference density below (1e20 per cubic metre, a tenuous laboratory gas)
fixes the curve. Doubling the density shifts the half-ionization point to
higher temperature, a reminder that "the ionization temperature" is not a
single number.

Writes data/saha_hydrogen.csv. Pure standard library; no third-party deps.
"""

import csv
import math

K_B = 1.380649e-23        # J/K
M_E = 9.1093837015e-31    # kg
HBAR = 1.054571817e-34    # J s
EV = 1.602176634e-19      # J
E_ION = 13.6 * EV         # hydrogen ionization energy, J

N_TOT = 1.0e20            # reference total nucleus density, per cubic metre


def saha_rhs(temperature_k):
    """Right-hand side S(T) of the Saha equation, units per cubic metre."""
    thermal = (M_E * K_B * temperature_k / (2.0 * math.pi * HBAR**2)) ** 1.5
    return thermal * math.exp(-E_ION / (K_B * temperature_k))


def ionization_fraction(temperature_k, n_tot=N_TOT):
    """Solve x^2/(1-x) = S/n_tot for the ionization fraction x in [0, 1]."""
    r = saha_rhs(temperature_k) / n_tot
    # x = (-r + sqrt(r^2 + 4 r)) / 2 is the physical (0..1) root.
    return 0.5 * (-r + math.sqrt(r * r + 4.0 * r))


def main():
    temps = list(range(4000, 21000, 1000)) + [25000, 30000]
    rows = [(t, ionization_fraction(t)) for t in temps]
    with open("data/saha_hydrogen.csv", "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["temperature_K", "ionization_fraction"])
        for temperature, fraction in rows:
            writer.writerow([temperature, f"{fraction:.7f}"])
    half = next(t for t, x in rows if x >= 0.5)
    print(f"Half-ionization near {half} K at n_tot = {N_TOT:.0e} per m^3")


if __name__ == "__main__":
    main()
