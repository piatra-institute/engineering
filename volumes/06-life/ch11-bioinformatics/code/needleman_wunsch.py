"""
Needleman-Wunsch global pairwise alignment by dynamic programming.

Implements the canonical recurrence

    M[i,j] = max{ M[i-1,j-1] + s(a_i, b_j),
                  M[i-1,j]   + g,
                  M[i,j-1]   + g }

with linear gap penalty and an arbitrary substitution function s. Returns
the optimal score, the full DP matrix, and one optimal alignment recovered
by traceback. Reproduces the example in
volumes/06-life/ch11-bioinformatics/figures/fig-nw-matrix.tex.

Dependencies:
  numpy (optional, only used for pretty-printing)

Usage:
  python needleman_wunsch.py

Supports Volume VI, Chapter 11, Section 11.1 (Sequence data: alphabets,
alignment, search), the project (phase 1), and the alignment calculation
and derivation exercises.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


def match_mismatch(match: int = 1, mismatch: int = -1) -> Callable[[str, str], int]:
    """Default substitution scoring: match/mismatch integers."""
    def s(a: str, b: str) -> int:
        return match if a == b else mismatch
    return s


@dataclass
class Alignment:
    score: int
    matrix: list[list[int]]
    a_aligned: str
    b_aligned: str


def needleman_wunsch(
    a: str,
    b: str,
    score: Callable[[str, str], int] | None = None,
    gap: int = -1,
) -> Alignment:
    """Compute the optimal global alignment of a against b.

    Args:
        a, b: input sequences over an arbitrary alphabet.
        score: pairwise scoring function s(a_i, b_j). Defaults to
            match +1, mismatch -1.
        gap: linear gap penalty (negative integer).

    Returns:
        Alignment dataclass with score, full DP matrix, and aligned strings
        (gaps shown as '-').
    """
    if score is None:
        score = match_mismatch()

    m, n = len(a), len(b)
    M = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialise borders with cumulative gap penalties.
    for i in range(1, m + 1):
        M[i][0] = M[i - 1][0] + gap
    for j in range(1, n + 1):
        M[0][j] = M[0][j - 1] + gap

    # Fill interior.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diag = M[i - 1][j - 1] + score(a[i - 1], b[j - 1])
            up = M[i - 1][j] + gap
            left = M[i][j - 1] + gap
            M[i][j] = max(diag, up, left)

    # Traceback from (m, n) to (0, 0).
    i, j = m, n
    aa, bb = [], []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and M[i][j] == M[i - 1][j - 1] + score(a[i - 1], b[j - 1]):
            aa.append(a[i - 1])
            bb.append(b[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and M[i][j] == M[i - 1][j] + gap:
            aa.append(a[i - 1])
            bb.append("-")
            i -= 1
        else:
            aa.append("-")
            bb.append(b[j - 1])
            j -= 1

    return Alignment(
        score=M[m][n],
        matrix=M,
        a_aligned="".join(reversed(aa)),
        b_aligned="".join(reversed(bb)),
    )


def print_alignment(alignment: Alignment, line_width: int = 60) -> None:
    """Print an alignment in two-line blocks with a mid-line marker."""
    a, b = alignment.a_aligned, alignment.b_aligned
    marker = "".join("|" if x == y and x != "-" else " " for x, y in zip(a, b))
    print(f"Score: {alignment.score}")
    for start in range(0, len(a), line_width):
        end = start + line_width
        print(f"  {a[start:end]}")
        print(f"  {marker[start:end]}")
        print(f"  {b[start:end]}\n")


def main() -> None:
    examples = [
        ("GATTACA", "GCATGCU"),
        ("ATGCGTACGTAA", "ATGCATACGTAA"),
        ("HEAGAWGHEE", "PAWHEAE"),  # classic textbook example
    ]
    for a, b in examples:
        print("=" * 60)
        print(f"Aligning {a!r} vs {b!r}")
        align = needleman_wunsch(a, b)
        print_alignment(align)


if __name__ == "__main__":
    main()
