"""Work, heat, and entropy change for the four canonical ideal-gas processes.

Convention: W is the work done ON the gas (positive when the gas is
compressed). For each process the script returns W, Q, and Delta S per mole.

Run:
    python ideal_gas_processes.py
"""

import numpy as np

R = 8.314  # J / (mol K)


def isothermal(n, T, V1, V2):
    W = -n * R * T * np.log(V2 / V1)          # on the gas
    Q = -W                                     # dU = 0
    dS = n * R * np.log(V2 / V1)
    return W, Q, dS


def isobaric(n, p, V1, V2, cp):
    T1 = p * V1 / (n * R)
    T2 = p * V2 / (n * R)
    W = -p * (V2 - V1)
    Q = n * cp * (T2 - T1)
    dS = n * cp * np.log(T2 / T1)
    return W, Q, dS


def isochoric(n, V, p1, p2, cv):
    T1 = p1 * V / (n * R)
    T2 = p2 * V / (n * R)
    W = 0.0
    Q = n * cv * (T2 - T1)
    dS = n * cv * np.log(T2 / T1)
    return W, Q, dS


def adiabatic(n, V1, V2, T1, gamma, cv):
    T2 = T1 * (V1 / V2) ** (gamma - 1.0)
    W = n * cv * (T2 - T1)                      # = dU since Q = 0
    Q = 0.0
    dS = 0.0                                    # reversible adiabatic
    return W, Q, dS, T2


if __name__ == "__main__":
    n, T = 1.0, 293.0
    V1, V2 = 24e-3, 12e-3                       # halve the volume
    cv = 2.5 * R
    cp = 3.5 * R
    gamma = cp / cv

    print("Isothermal compression to half volume:")
    W, Q, dS = isothermal(n, T, V1, V2)
    print(f"  W = {W:7.1f} J   Q = {Q:7.1f} J   dS = {dS:6.3f} J/K")

    print("Adiabatic compression to half volume:")
    W, Q, dS, T2 = adiabatic(n, V1, V2, T, gamma, cv)
    print(f"  W = {W:7.1f} J   Q = {Q:7.1f} J   dS = {dS:6.3f} J/K   T2 = {T2:6.1f} K")
    print("Adiabatic takes more work because the gas heats as it is compressed.")
