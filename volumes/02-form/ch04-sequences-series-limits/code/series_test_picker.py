# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Walks the convergence-test decision tree on a small catalog of
series and prints the test that settles each.

This is a pedagogical companion to section 4.3; the logic mirrors
the decision tree of figure fig:vol02:ch04:test-decision-tree. The
script does not prove convergence; it picks the test the engineer
would reach for.
"""

CATALOG = [
    ("sum r^n with r=0.9",       "geometric", "converges (|r|<1)"),
    ("sum 1/n",                   "comparison vs 1/n^p (p=1)", "diverges (p<=1)"),
    ("sum 1/n^2",                 "comparison vs 1/n^p (p=2)", "converges (p>1)"),
    ("sum 1/(n^2 + 1)",           "limit comparison vs 1/n^2", "converges"),
    ("sum (-1)^(n+1)/n",          "alternating-series test",    "converges (Leibniz)"),
    ("sum n! / n^n",              "ratio test",                  "ratio -> 1/e < 1, converges"),
    ("sum c^n / n!",              "ratio test",                  "ratio -> 0, converges for all c"),
    ("sum (1 - 1/n)^(n^2)",       "root test",                   "n-th root -> 1/e < 1, converges"),
    ("sum 1/(n log n)",           "integral test",               "integral diverges as log log N, so series diverges"),
    ("sum 1/(n (log n)^2)",       "integral test",               "integral converges, so series converges"),
    ("sum sin(1/n)",              "limit comparison vs 1/n",     "diverges"),
    ("sum n * 0.5^n",             "ratio test",                  "ratio -> 0.5 < 1, converges"),
]


def main() -> None:
    print(f"{'series':<28}  {'test':<32}  {'verdict':<40}")
    print("-" * 104)
    for series, test, verdict in CATALOG:
        print(f"{series:<28}  {test:<32}  {verdict:<40}")


if __name__ == "__main__":
    main()
