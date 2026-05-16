#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# ///
"""
Bayes-rule contingency-table calculator for diagnostic tests.

Given a prior probability of the condition, the test's sensitivity, and
the test's specificity, the script prints the 2x2 contingency table for
a population of N (default 100,000) and the posterior probability of the
condition given a positive result. Supports the chapter's worked Bayes
example and the design and judgement exercises on two-stage screening.

Dependencies:
    standard library only.

Usage:
    uv run bayes_table.py --prior 0.01 --sensitivity 0.95 --specificity 0.98
    uv run bayes_table.py --prior 0.005 --sensitivity 0.99 --specificity 0.95
"""

from __future__ import annotations

import argparse


def contingency_counts(prior: float, sensitivity: float,
                       specificity: float, n: int) -> dict[str, int]:
    diseased = round(prior * n)
    healthy = n - diseased
    true_pos = round(sensitivity * diseased)
    false_neg = diseased - true_pos
    true_neg = round(specificity * healthy)
    false_pos = healthy - true_neg
    return {
        "TP": true_pos,
        "FP": false_pos,
        "FN": false_neg,
        "TN": true_neg,
        "diseased": diseased,
        "healthy": healthy,
        "total_pos": true_pos + false_pos,
        "total_neg": false_neg + true_neg,
    }


def posterior(prior: float, sensitivity: float,
              specificity: float) -> float:
    num = sensitivity * prior
    den = sensitivity * prior + (1.0 - specificity) * (1.0 - prior)
    return num / den


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prior", type=float, default=0.01)
    parser.add_argument("--sensitivity", type=float, default=0.95)
    parser.add_argument("--specificity", type=float, default=0.98)
    parser.add_argument("--population", type=int, default=100_000)
    args = parser.parse_args()

    counts = contingency_counts(
        args.prior, args.sensitivity, args.specificity, args.population
    )
    post = posterior(args.prior, args.sensitivity, args.specificity)

    print(f"Population: {args.population:,}")
    print(f"Prior P(D)        = {args.prior:.4f}")
    print(f"Sensitivity P(+|D) = {args.sensitivity:.4f}")
    print(f"Specificity P(-|Dc) = {args.specificity:.4f}\n")

    print(f"{'':<18}{'D':>14}{'Dc':>14}{'total':>14}")
    print(f"{'positive (+)':<18}"
          f"{counts['TP']:>14,}{counts['FP']:>14,}{counts['total_pos']:>14,}")
    print(f"{'negative (-)':<18}"
          f"{counts['FN']:>14,}{counts['TN']:>14,}{counts['total_neg']:>14,}")
    print(f"{'total':<18}"
          f"{counts['diseased']:>14,}{counts['healthy']:>14,}"
          f"{args.population:>14,}")

    print(f"\nPosterior P(D | +) = {post:.4f}")


if __name__ == "__main__":
    main()
