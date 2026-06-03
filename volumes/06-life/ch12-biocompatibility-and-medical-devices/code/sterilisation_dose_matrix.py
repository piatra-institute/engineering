"""
Sterilisation-process / material compatibility lookup.

Vol VI Ch 12 sec 12.5. Used by Design exercise 1 and the
sterilisation-matrix figure.

The lookup returns a compatibility tag for each (material, process)
pair, together with a recommended process window (dose, temperature,
or dwell). The data are illustrative and reflect the standard
references cited in the chapter; specific cycle parameters require
process-development validation under the relevant ISO standard.

References:
- std:v6c12-iso-11135-2014 (EtO sterilisation)
- std:v6c12-iso-11137-1-2006 (radiation sterilisation)
- text:v6c12-ratner-biomaterials-2020 (material responses)
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Compatibility:
    tag: str             # 'ok', 'caution', 'bad'
    window: str          # plain-text recommended cycle window
    notes: str = ""


# Plain literal table; rows are materials, columns are processes.
MATRIX: dict[tuple[str, str], Compatibility] = {

    # Stainless steel: all standard processes work.
    ("316L stainless", "autoclave"): Compatibility(
        "ok", "121-134 C steam, 15-30 min"),
    ("316L stainless", "EtO"): Compatibility(
        "ok", "30-60 C, 600-1200 mg/L, 2-6 h"),
    ("316L stainless", "gamma"): Compatibility(
        "ok", "25-40 kGy"),
    ("316L stainless", "e-beam"): Compatibility(
        "ok", "25-40 kGy"),
    ("316L stainless", "H2O2 gas"): Compatibility(
        "ok", "50-60 C, 6 mg/L peroxide"),

    # Co-Cr-Mo: same as stainless.
    ("Co-Cr-Mo", "autoclave"): Compatibility("ok", "121-134 C steam"),
    ("Co-Cr-Mo", "EtO"): Compatibility("ok", "30-60 C, 600-1200 mg/L"),
    ("Co-Cr-Mo", "gamma"): Compatibility("ok", "25-40 kGy"),
    ("Co-Cr-Mo", "e-beam"): Compatibility("ok", "25-40 kGy"),
    ("Co-Cr-Mo", "H2O2 gas"): Compatibility("ok", "50-60 C"),

    # Ti-6Al-4V: same as stainless.
    ("Ti-6Al-4V", "autoclave"): Compatibility("ok", "121-134 C steam"),
    ("Ti-6Al-4V", "EtO"): Compatibility("ok", "30-60 C, 600-1200 mg/L"),
    ("Ti-6Al-4V", "gamma"): Compatibility("ok", "25-40 kGy"),
    ("Ti-6Al-4V", "e-beam"): Compatibility("ok", "25-40 kGy"),
    ("Ti-6Al-4V", "H2O2 gas"): Compatibility("ok", "50-60 C"),

    # UHMWPE: avoid autoclave (creep), radiation causes oxidation;
    # EtO and peroxide are the standard.
    ("UHMWPE", "autoclave"): Compatibility(
        "caution", "Avoid: creep at 121 C",
        "Use only for pre-implant insert cleaning, not terminal sterilisation."),
    ("UHMWPE", "EtO"): Compatibility(
        "ok", "30-60 C, 600-1200 mg/L"),
    ("UHMWPE", "gamma"): Compatibility(
        "bad", "Oxidation, chain scission",
        "Gamma at 25-40 kGy embrittles UHMWPE; vacuum-packed inert atmosphere is required."),
    ("UHMWPE", "e-beam"): Compatibility(
        "bad", "Oxidation, chain scission",
        "Same as gamma; inert atmosphere is required."),
    ("UHMWPE", "H2O2 gas"): Compatibility("ok", "50-60 C"),

    # PMMA (bone cement): autoclave softens it.
    ("PMMA", "autoclave"): Compatibility(
        "bad", "Softens above 105 C"),
    ("PMMA", "EtO"): Compatibility("ok", "30-60 C"),
    ("PMMA", "gamma"): Compatibility(
        "caution", "Yellowing; mechanical loss",
        "Acceptable for some indications; verify mechanical retention."),
    ("PMMA", "e-beam"): Compatibility(
        "caution", "Yellowing; mechanical loss"),
    ("PMMA", "H2O2 gas"): Compatibility("ok", "50-60 C"),

    # PLA / PLGA bioresorbables.
    ("PLA / PLGA", "autoclave"): Compatibility(
        "bad", "Hydrolysis at 121 C in steam"),
    ("PLA / PLGA", "EtO"): Compatibility("ok", "30-40 C"),
    ("PLA / PLGA", "gamma"): Compatibility(
        "caution", "Chain scission; lower MW",
        "Acceptable below ~25 kGy with controlled MW shift."),
    ("PLA / PLGA", "e-beam"): Compatibility(
        "caution", "Chain scission; lower MW"),
    ("PLA / PLGA", "H2O2 gas"): Compatibility("ok", "low temperature"),

    # Silicone.
    ("Silicone", "autoclave"): Compatibility("ok", "121-134 C steam"),
    ("Silicone", "EtO"): Compatibility(
        "caution", "Residual outgassing",
        "Long aeration required to meet ISO 10993-7 EtO residual limits."),
    ("Silicone", "gamma"): Compatibility("ok", "25-40 kGy"),
    ("Silicone", "e-beam"): Compatibility("ok", "25-40 kGy"),
    ("Silicone", "H2O2 gas"): Compatibility("ok", "50-60 C"),

    # PEEK.
    ("PEEK", "autoclave"): Compatibility("ok", "121-134 C steam"),
    ("PEEK", "EtO"): Compatibility("ok", "30-60 C"),
    ("PEEK", "gamma"): Compatibility("ok", "25-40 kGy"),
    ("PEEK", "e-beam"): Compatibility("ok", "25-40 kGy"),
    ("PEEK", "H2O2 gas"): Compatibility("ok", "50-60 C"),

    # Electronics / battery.
    ("Electronics", "autoclave"): Compatibility(
        "bad", "Thermal damage above 80 C"),
    ("Electronics", "EtO"): Compatibility(
        "ok", "30-40 C, low humidity"),
    ("Electronics", "gamma"): Compatibility(
        "caution", "Dose limited to ~10-15 kGy"),
    ("Electronics", "e-beam"): Compatibility(
        "caution", "Dose limited to ~10-15 kGy"),
    ("Electronics", "H2O2 gas"): Compatibility(
        "ok", "50-60 C, electronics-safe"),
}


def lookup(material: str, process: str) -> Compatibility:
    key = (material, process)
    if key not in MATRIX:
        raise KeyError(f"Unknown material/process: {key}")
    return MATRIX[key]


def main() -> None:
    materials = ["316L stainless", "Co-Cr-Mo", "Ti-6Al-4V", "UHMWPE",
                 "PMMA", "PLA / PLGA", "Silicone", "PEEK",
                 "Electronics"]
    processes = ["autoclave", "EtO", "gamma", "e-beam", "H2O2 gas"]

    header = f"{'Material':<18}" + "".join(f"{p:<14}" for p in processes)
    print(header)
    for m in materials:
        row = f"{m:<18}"
        for p in processes:
            c = lookup(m, p)
            row += f"{c.tag:<14}"
        print(row)


if __name__ == "__main__":
    main()
