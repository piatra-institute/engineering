"""Refrigerator and heat-pump energy accounting from logged data.

Reads a daily energy-consumption log (data/refrigerator_power.csv), computes
the average electrical power, estimates the cabinet heat leak from the
recorded temperatures, and reports the coefficient of performance against
the Carnot bound.

Run:
    python refrigerator_cop.py
"""

import csv
import os

K_FOAM = 0.025   # W / (m K), polyurethane foam
L_WALL = 0.05    # m, insulation thickness
A_WALL = 3.0     # m^2, cabinet surface area

DATA = os.path.join(os.path.dirname(__file__), "..", "data",
                    "refrigerator_power.csv")


def carnot_cop_cooling(T_c, T_h):
    """Carnot COP for cooling, temperatures in kelvin."""
    return T_c / (T_h - T_c)


def heat_leak(T_in_C, T_amb_C):
    """Conductive heat leak through the cabinet walls, watts."""
    return K_FOAM * A_WALL * (T_amb_C - T_in_C) / L_WALL


def load(path=DATA):
    rows = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            rows.append({k: float(v) if k != "date" else v
                         for k, v in row.items()})
    return rows


if __name__ == "__main__":
    rows = load()
    n = len(rows)
    avg_kwh = sum(r["energy_kwh"] for r in rows) / n
    avg_power = avg_kwh * 1000.0 / 24.0           # W, averaged over the day
    T_in = sum(r["cabinet_C"] for r in rows) / n
    T_amb = sum(r["ambient_C"] for r in rows) / n

    Q_leak = heat_leak(T_in, T_amb)
    cop_actual = Q_leak / avg_power
    # condenser ~ ambient + 13 K, evaporator ~ cabinet - 9 K (typical offsets)
    T_h = (T_amb + 13.0) + 273.15
    T_c = (T_in - 9.0) + 273.15
    cop_carnot = carnot_cop_cooling(T_c, T_h)

    print(f"average power        = {avg_power:6.1f} W")
    print(f"estimated heat leak  = {Q_leak:6.1f} W")
    print(f"actual COP           = {cop_actual:6.2f}")
    print(f"Carnot COP           = {cop_carnot:6.2f}")
    print(f"fraction of Carnot   = {cop_actual / cop_carnot:6.2f}")
