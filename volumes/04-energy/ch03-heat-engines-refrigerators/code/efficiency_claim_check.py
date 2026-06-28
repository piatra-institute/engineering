"""Two-step diagnosis of an efficiency or COP claim (section 3.7).

Step one: compare the claimed figure to the Carnot bound for the stated
reservoir temperatures. A claim above the bound violates the second law.
Step two: if the claim passes step one, report the implied second-law
efficiency so the realised fraction can be judged against the device class.
"""

from __future__ import annotations


def check_engine_claim(eta_claimed, t_hot, t_cold):
    """Diagnose a heat-engine thermal-efficiency claim."""
    eta_carnot = 1.0 - t_cold / t_hot
    violates = eta_claimed > eta_carnot
    eta_second_law = eta_claimed / eta_carnot if eta_carnot > 0 else float("inf")
    return {
        "eta_carnot": eta_carnot,
        "violates_second_law": violates,
        "second_law_efficiency": eta_second_law,
    }


def check_heatpump_claim(cop_claimed, t_hot, t_cold):
    """Diagnose a heat-pump (heating) COP claim."""
    cop_carnot = t_hot / (t_hot - t_cold)
    violates = cop_claimed > cop_carnot
    return {
        "cop_carnot": cop_carnot,
        "violates_second_law": violates,
        "fraction_of_carnot": cop_claimed / cop_carnot,
    }


def check_furnace_claim(eta_lhv, hhv_over_lhv=1.11):
    """Diagnose a combustion-appliance first-law efficiency quoted on LHV.

    A condensing appliance can exceed 100 percent on an LHV basis without
    violating the first law, up to the HHV/LHV ratio. Above that ratio it
    violates the first law.
    """
    eta_hhv = eta_lhv / hhv_over_lhv
    violates = eta_lhv > hhv_over_lhv
    return {
        "eta_hhv": eta_hhv,
        "violates_first_law": violates,
    }


if __name__ == "__main__":
    # 2023 patent: COP 10 between 20 C indoor and 0 C outdoor.
    print(check_heatpump_claim(10.0, 293.0, 273.0))
    # Condensing furnace quoted at 108 percent LHV.
    print(check_furnace_claim(1.08))
    # Engine claiming 70 percent between 1400 K and 300 K.
    print(check_engine_claim(0.70, 1400.0, 300.0))
