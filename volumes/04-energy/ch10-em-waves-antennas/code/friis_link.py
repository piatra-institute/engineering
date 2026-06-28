"""Friis free-space link budget in linear and decibel forms.

Compute received power from transmit power, antenna gains, frequency, and range,
either with linear gains via the Friis equation directly, or with the decibel
link-budget arithmetic preferred in practice. Also returns free-space path loss
and the effective aperture of the receive antenna. This is the working content
of section 10.6 and the satellite-link estimation block.

Powers in watt unless a dBm form is requested; gains in linear ratio for the
linear routine and in dBi for the decibel routine; range and wavelength in metre.
"""

from __future__ import annotations

import math

C0 = 299_792_458.0


def wavelength(freq_hz: float) -> float:
    return C0 / freq_hz


def free_space_path_loss_db(freq_hz: float, range_m: float) -> float:
    """FSPL = 20 log10(4 pi R / lambda), in dB."""
    lam = wavelength(freq_hz)
    return 20.0 * math.log10(4.0 * math.pi * range_m / lam)


def friis_linear(p_t_w: float, g_t: float, g_r: float,
                 freq_hz: float, range_m: float) -> float:
    """Received power in watt, Friis equation with linear gains."""
    lam = wavelength(freq_hz)
    return p_t_w * g_t * g_r * lam * lam / (4.0 * math.pi * range_m) ** 2


def friis_db(p_t_dbm: float, g_t_dbi: float, g_r_dbi: float,
             freq_hz: float, range_m: float) -> float:
    """Received power in dBm via the decibel link budget."""
    return p_t_dbm + g_t_dbi + g_r_dbi - free_space_path_loss_db(freq_hz, range_m)


def dbm(power_w: float) -> float:
    return 10.0 * math.log10(power_w / 1.0e-3)


def watt(power_dbm: float) -> float:
    return 1.0e-3 * 10.0 ** (power_dbm / 10.0)


def effective_aperture(g_r: float, freq_hz: float) -> float:
    """A_eff = G_r lambda^2 / (4 pi), in m^2."""
    lam = wavelength(freq_hz)
    return g_r * lam * lam / (4.0 * math.pi)


if __name__ == "__main__":
    # exercise 7: WiFi access point, 2.45 GHz, 100 mW, Gt = 6 dBi, Gr = 2 dBi, 30 m
    pr_dbm = friis_db(dbm(0.1), 6.0, 2.0, 2.45e9, 30.0)
    print(f"FSPL    = {free_space_path_loss_db(2.45e9, 30.0):.1f} dB")
    print(f"Pr      = {pr_dbm:.1f} dBm = {1e6*watt(pr_dbm):.3f} uW")
