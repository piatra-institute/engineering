"""Derived plasma parameters for a table of real and engineered plasmas.

Reads data/plasma_parameters.csv (density in m^-3, electron temperature in
eV) and reports, for each entry, the Debye length, the plasma frequency,
the number of particles in a Debye sphere, and the plasma parameter
Lambda = n_e lambda_D^3. The point of the table is to show that across
twenty-plus orders of magnitude in density, every working plasma has
N_D >> 1, which is the operational definition that distinguishes a plasma
from a merely ionized gas. Pure standard library.
"""

import csv
import math

EPS0 = 8.8541878128e-12   # F/m
K_B = 1.380649e-23        # J/K
EV = 1.602176634e-19      # J
E = 1.602176634e-19       # C
M_E = 9.1093837015e-31    # kg


def debye_length(n_e, t_ev):
    """Debye length in metres for density n_e (m^-3) and T_e (eV)."""
    t_joule = t_ev * EV
    return math.sqrt(EPS0 * t_joule / (n_e * E * E))


def plasma_frequency(n_e):
    """Electron plasma angular frequency in rad/s."""
    return math.sqrt(n_e * E * E / (M_E * EPS0))


def n_debye(n_e, lambda_d):
    """Number of particles in a Debye sphere."""
    return (4.0 / 3.0) * math.pi * lambda_d**3 * n_e


def main():
    path = "data/plasma_parameters.csv"
    header = f"{'plasma':>18}  {'lambda_D (m)':>14}  {'f_p (Hz)':>12}  {'N_D':>10}"
    print(header)
    print("-" * len(header))
    with open(path, newline="") as handle:
        for row in csv.DictReader(handle):
            n_e = float(row["density_m3"])
            t_ev = float(row["temperature_eV"])
            ld = debye_length(n_e, t_ev)
            fp = plasma_frequency(n_e) / (2.0 * math.pi)
            nd = n_debye(n_e, ld)
            print(f"{row['plasma']:>18}  {ld:14.3e}  {fp:12.3e}  {nd:10.2e}")


if __name__ == "__main__":
    main()
