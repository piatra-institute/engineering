"""Synthetic Langmuir-probe I-V characteristic and a temperature fit.

Models the three regions of an idealised cylindrical Langmuir probe:
ion saturation, the exponential electron-retardation region, and electron
saturation. The retardation current follows

    I_e(V) = I_es * exp((V - V_p) / T_e_volts)   for V < V_p,

clamped to the electron-saturation value I_es above the plasma potential
V_p. The total probe current is I = I_e(V) - I_is, where I_is is the
(positive) ion-saturation magnitude flowing the other way.

Generates data/langmuir_iv.csv and recovers T_e from the slope of
ln(I + I_is) in the exponential region, demonstrating the standard probe
analysis. Pure standard library.
"""

import csv
import math

T_E_VOLTS = 3.0      # electron temperature in volts (i.e. eV)
V_P = 5.0            # plasma potential, V
I_ES = 10.0         # electron-saturation current, mA
I_IS = 1.5          # ion-saturation magnitude, mA


def probe_current(bias_v):
    """Total probe current in mA at a given bias."""
    if bias_v >= V_P:
        electron = I_ES
    else:
        electron = I_ES * math.exp((bias_v - V_P) / T_E_VOLTS)
    return electron - I_IS


def generate(path="data/langmuir_iv.csv"):
    biases = [(-40 + i) for i in range(0, 66)]   # -40 V to +25 V
    rows = [(v, probe_current(v)) for v in biases]
    with open(path, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["bias_V", "current_mA"])
        for v, current in rows:
            writer.writerow([v, f"{current:.4f}"])
    return rows


def fit_temperature(rows):
    """Recover T_e from the slope of ln(I + I_is) in the retardation region."""
    pts = [(v, math.log(c + I_IS)) for v, c in rows
           if -2.0 < c < 0.9 * (I_ES - I_IS) and (c + I_IS) > 0]
    n = len(pts)
    sx = sum(v for v, _ in pts)
    sy = sum(y for _, y in pts)
    sxx = sum(v * v for v, _ in pts)
    sxy = sum(v * y for v, y in pts)
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    return 1.0 / slope   # T_e in volts = inverse slope


def main():
    rows = generate()
    t_e = fit_temperature(rows)
    print(f"Input T_e = {T_E_VOLTS:.2f} V; recovered from slope = {t_e:.2f} V")


if __name__ == "__main__":
    main()
