"""Integrate the International Standard Atmosphere from sea level to 32 km.

The ISA is a piecewise-linear temperature profile. Within a layer of
constant lapse rate L = -dT/dz, the hydrostatic equation dp/dz = -rho g
together with the ideal-gas law rho = p M / (R T) integrates in closed
form:

    p(z) = p_b * (T_b - L*(z - z_b))/T_b) ** (M g / (R L))      (L != 0)
    p(z) = p_b * exp(-M g (z - z_b) / (R T_b))                  (L == 0)

This script reproduces the pressure-altitude curve plotted in
fig-atmosphere.tex and the table in data/isa_profile.csv. Run with:

    uv run volumes/03-force/ch10-fluid-statics/code/standard_atmosphere.py
"""

import math

G = 9.80665        # m/s^2, standard gravity
M = 0.0289644      # kg/mol, molar mass of dry air
R = 8.31446        # J/(mol K), universal gas constant

# ISA layers: (base altitude z_b [m], base temperature T_b [K], lapse rate L [K/m])
# Lapse rate L is positive when temperature falls with height.
LAYERS = [
    (0.0, 288.15, 0.0065),     # troposphere
    (11000.0, 216.65, 0.0),    # tropopause / lower stratosphere (isothermal)
    (20000.0, 216.65, -0.001),  # stratosphere, temperature rising
    (32000.0, 228.65, -0.0028),  # upper stratosphere
]
P0 = 101325.0  # Pa, sea-level pressure


def layer_base_pressures():
    """Pressure at the base of each layer, propagated upward."""
    pressures = [P0]
    for i in range(len(LAYERS) - 1):
        z_b, T_b, L = LAYERS[i]
        z_top = LAYERS[i + 1][0]
        p_b = pressures[-1]
        pressures.append(pressure_in_layer(z_top, z_b, T_b, L, p_b))
    return pressures


def pressure_in_layer(z, z_b, T_b, L, p_b):
    if abs(L) < 1e-12:
        return p_b * math.exp(-G * M * (z - z_b) / (R * T_b))
    T = T_b - L * (z - z_b)
    return p_b * (T / T_b) ** (G * M / (R * L))


def pressure(z):
    """ISA pressure (Pa) at geometric altitude z (m), 0 <= z <= 32000."""
    bases = layer_base_pressures()
    for i, (z_b, T_b, L) in enumerate(LAYERS):
        z_top = LAYERS[i + 1][0] if i + 1 < len(LAYERS) else 32000.0
        if z <= z_top + 1e-6:
            return pressure_in_layer(z, z_b, T_b, L, bases[i])
    raise ValueError("altitude above 32 km not modelled")


if __name__ == "__main__":
    print("z_km, p_kPa, p_isothermal_kPa")
    H = R * 288.15 / (M * G)  # isothermal scale height, m
    for z_km in range(0, 33):
        z = z_km * 1000.0
        p = pressure(z) / 1000.0
        p_iso = P0 / 1000.0 * math.exp(-z / H)
        print(f"{z_km:2d}, {p:8.3f}, {p_iso:8.3f}")
