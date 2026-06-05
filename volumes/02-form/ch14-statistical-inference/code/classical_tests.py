# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Worked classical tests from section 14.2, from primitives.

Reproduces the one-sample t-test (machined shafts), the
pooled-variance two-sample t-test (two ceramic batches), the
Pearson chi-square goodness-of-fit (a die), and the one-way ANOVA F
statistic (three catalysts). No scipy: the test statistics are
computed by hand and compared against tabulated critical values so
the arithmetic is inspectable. p-values are not computed (they need
the t, chi-square, and F cdfs); the script prints the statistic and
the relevant critical value for a reject/no-reject call.

Run:
    uv run classical_tests.py
"""
from __future__ import annotations

from math import sqrt


def one_sample_t(xbar: float, mu0: float, s: float, n: int) -> float:
    return (xbar - mu0) / (s / sqrt(n))


def two_sample_t(
    xbar1: float, s1: float, n1: int,
    xbar2: float, s2: float, n2: int,
) -> tuple[float, float]:
    sp2 = ((n1 - 1) * s1 ** 2 + (n2 - 1) * s2 ** 2) / (n1 + n2 - 2)
    sp = sqrt(sp2)
    t = (xbar1 - xbar2) / (sp * sqrt(1 / n1 + 1 / n2))
    return t, sp


def chi_square_gof(observed: list[float], expected: list[float]) -> float:
    return sum((o - e) ** 2 / e for o, e in zip(observed, expected))


def one_way_anova(group_means: list[float], n_per: int,
                  within_var: float) -> tuple[float, float, float]:
    g = len(group_means)
    grand = sum(group_means) / g
    ss_between = n_per * sum((m - grand) ** 2 for m in group_means)
    ms_between = ss_between / (g - 1)
    ms_within = within_var
    f = ms_between / ms_within
    return ss_between, ms_between, f


def main() -> None:
    t1 = one_sample_t(25.06, 25.00, 0.10, 16)
    print(f"one-sample t (shaft): {t1:.3f}  vs t_0.975,15 = 2.131")

    t2, sp = two_sample_t(480, 30, 20, 465, 25, 18)
    print(f"two-sample t (ceramic): {t2:.3f}  sp = {sp:.2f}"
          f"  vs t_0.975,36 ~ 2.028")

    chi = chi_square_gof([18, 24, 16, 22, 20, 20], [20] * 6)
    print(f"chi-square (die): {chi:.2f}  vs chi2_0.95,5 = 11.07")

    ssb, msb, f = one_way_anova([72, 78, 75], 10, 20.0)
    print(f"ANOVA: SS_between = {ssb:.0f}  MS_between = {msb:.0f}"
          f"  F = {f:.2f}  vs F_0.95,2,27 = 3.35")


if __name__ == "__main__":
    main()
