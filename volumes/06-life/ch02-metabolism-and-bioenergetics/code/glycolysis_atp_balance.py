"""
Per-step ATP and NADH ledger for glycolysis from glucose to pyruvate.

The script lists each of the ten enzymatic steps, the substrate and
product, the reaction's standard Gibbs free energy, and the running
ATP / NADH balance. Useful for checking that the textbook net of
"+2 ATP, +2 NADH per glucose" reconciles with the per-step accounting.

Dependencies: standard library only.

Usage:
    python glycolysis_atp_balance.py

Supports Vol VI Chapter 2, Section 2.2 (glycolysis), the calculation
exercises on free-energy balance, and the worked-example figure
fig-glycolysis-ledger.tex.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GlycolysisStep:
    n: int
    enzyme: str
    substrate: str
    product: str
    dG_standard_kJ_mol: float       # standard free energy of reaction
    dG_cellular_kJ_mol: float        # estimated cellular value, erythrocyte
    atp_delta: int                   # signed ATP balance for this step
    nadh_delta: int                  # signed NADH balance for this step


# Values from Nelson & Cox, Lehninger Principles of Biochemistry,
# 7th ed., table 14-2 (erythrocyte values approximated).
STEPS = [
    GlycolysisStep(1,  "Hexokinase",            "Glucose",          "G6P",    -16.7, -33.5, -1, 0),
    GlycolysisStep(2,  "PGI",                   "G6P",              "F6P",     +1.7,  -2.5,  0, 0),
    GlycolysisStep(3,  "PFK-1",                 "F6P",              "F1,6BP", -14.2, -22.2, -1, 0),
    GlycolysisStep(4,  "Aldolase",              "F1,6BP",           "GAP+DHAP",+23.8,  -1.3,  0, 0),
    GlycolysisStep(5,  "TPI",                   "DHAP",             "GAP",     +7.5,   +2.5,  0, 0),
    # Steps below act on each of the two GAP / per glucose, so atp_delta
    # is already doubled (+2 per glucose):
    GlycolysisStep(6,  "GAPDH",                 "GAP",              "1,3BPG",  +6.3,  -1.3,  0, +2),
    GlycolysisStep(7,  "PGK",                   "1,3BPG",           "3PG",   -18.8,  +0.4, +2, 0),
    GlycolysisStep(8,  "PGM",                   "3PG",              "2PG",     +4.4,  +0.8,  0, 0),
    GlycolysisStep(9,  "Enolase",               "2PG",              "PEP",     +7.5,  -3.3,  0, 0),
    GlycolysisStep(10, "Pyruvate kinase",       "PEP",              "Pyruvate",-31.4,-16.7, +2, 0),
]


def ledger() -> None:
    atp_balance = 0
    nadh_balance = 0
    print(f"{'Step':>4}  {'Enzyme':<18} {'Substrate':>10} -> {'Product':<10} "
          f"{'dG° kJ/mol':>10}  {'dG_cell':>10}  {'ATP':>4}  {'NADH':>4}  "
          f"{'sumATP':>7}  {'sumNADH':>8}")
    for s in STEPS:
        atp_balance += s.atp_delta
        nadh_balance += s.nadh_delta
        print(f"{s.n:>4}  {s.enzyme:<18} {s.substrate:>10} -> {s.product:<10} "
              f"{s.dG_standard_kJ_mol:>10.1f}  {s.dG_cellular_kJ_mol:>10.1f}  "
              f"{s.atp_delta:>4d}  {s.nadh_delta:>4d}  "
              f"{atp_balance:>7d}  {nadh_balance:>8d}")
    print()
    print(f"Net per glucose: {atp_balance:+d} ATP, {nadh_balance:+d} NADH")
    dG_sum_std = sum(s.dG_standard_kJ_mol for s in STEPS)
    dG_sum_cell = sum(s.dG_cellular_kJ_mol for s in STEPS)
    print(f"Pathway dG (standard, sum): {dG_sum_std:+.1f} kJ/mol")
    print(f"Pathway dG (cellular, sum): {dG_sum_cell:+.1f} kJ/mol "
          f"(should be strongly negative for forward flux)")


if __name__ == "__main__":
    ledger()
