"""Steady-state open-system first-law residual checker.

Given inlet and outlet conditions, heat rate, and shaft-work rate for a
control volume, return the residual of the steady-state energy balance

    0 = Qdot + Wsdot + mdot * (h1 - h2 + 0.5*(V1^2 - V2^2) + g*(z1 - z2)).

A residual far from zero flags an inconsistency in the stated numbers or a
missing energy flow. The script verifies itself on the steam-turbine
exercise from the chapter.

Run:
    python first_law_balance.py
"""

G = 9.81  # m / s^2


def residual(mdot, h1, h2, Qdot=0.0, Wsdot=0.0,
             V1=0.0, V2=0.0, z1=0.0, z2=0.0):
    """First-law residual in watts (enthalpies in J/kg)."""
    flow = mdot * (h1 - h2
                   + 0.5 * (V1 ** 2 - V2 ** 2)
                   + G * (z1 - z2))
    return Qdot + Wsdot + flow


def shaft_power(mdot, h1, h2, Qdot=0.0, V1=0.0, V2=0.0, z1=0.0, z2=0.0):
    """Solve the balance for the shaft work rate (W on the CV)."""
    flow = mdot * (h1 - h2
                   + 0.5 * (V1 ** 2 - V2 ** 2)
                   + G * (z1 - z2))
    return -(Qdot + flow)


if __name__ == "__main__":
    # Steam turbine: h1 = 3231 kJ/kg, h2 = 2403 kJ/kg, mdot = 5 kg/s,
    # adiabatic, KE and PE negligible.
    mdot = 5.0
    h1 = 3231e3
    h2 = 2403e3
    Ws = shaft_power(mdot, h1, h2)  # negative: work done BY the CV
    print(f"shaft work on CV  = {Ws/1e3:8.1f} kW")
    print(f"power delivered   = {-Ws/1e3:8.1f} kW")
    r = residual(mdot, h1, h2, Qdot=0.0, Wsdot=Ws)
    print(f"balance residual  = {r:8.3e} W  (should be ~0)")
    assert abs(r) < 1e-6, "balance must close"
    print("first law closes for the steam turbine.")
