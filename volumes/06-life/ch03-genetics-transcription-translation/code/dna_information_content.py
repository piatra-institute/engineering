"""Information content of DNA sequences.

We treat a DNA sequence as a stream of symbols from the alphabet
{A, C, G, T} and compute the Shannon entropy under three assumptions:

  1. Uniform i.i.d. nucleotides (theoretical maximum 2 bits per base).
  2. Empirical single-nucleotide frequencies for a human-genome sample
     (slightly less than 2 bits because of GC skew).
  3. Empirical dinucleotide frequencies (lower still because of CpG
     suppression and other neighbour correlations).

The script reports the per-base entropy for each assumption and the
implied information content of the human haploid genome
(3.2e9 base pairs).

Run:
    python dna_information_content.py path/to/sequence.fasta

If no FASTA is supplied, the script uses a synthetic uniform-random
sequence of 1e6 bases to confirm the 2-bit upper bound.
"""
from __future__ import annotations

import collections
import math
import random
import sys
from pathlib import Path


def read_fasta(path: Path) -> str:
    """Concatenate sequence lines from a FASTA file into a single string."""
    seq_chars: list[str] = []
    with path.open("r", encoding="ascii", errors="ignore") as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            seq_chars.append(line.strip().upper())
    return "".join(seq_chars)


def shannon_entropy(counts: dict[str, int]) -> float:
    """Shannon entropy in bits per symbol from a counts dictionary."""
    total = sum(counts.values())
    if total == 0:
        return 0.0
    entropy = 0.0
    for n in counts.values():
        if n == 0:
            continue
        p = n / total
        entropy -= p * math.log2(p)
    return entropy


def single_base_entropy(seq: str) -> float:
    counts = collections.Counter(c for c in seq if c in "ACGT")
    return shannon_entropy(counts)


def dinucleotide_entropy(seq: str) -> float:
    """Conditional entropy H(X_i | X_{i-1}) in bits per symbol."""
    pair_counts: dict[str, int] = collections.Counter()
    first_counts: dict[str, int] = collections.Counter()
    for i in range(len(seq) - 1):
        a, b = seq[i], seq[i + 1]
        if a in "ACGT" and b in "ACGT":
            pair_counts[a + b] += 1
            first_counts[a] += 1
    total = sum(pair_counts.values())
    if total == 0:
        return 0.0
    cond = 0.0
    for ab, n in pair_counts.items():
        a = ab[0]
        p_ab = n / total
        p_b_given_a = n / first_counts[a]
        if p_b_given_a > 0:
            cond -= p_ab * math.log2(p_b_given_a)
    return cond


def random_sequence(n: int, seed: int = 42) -> str:
    rng = random.Random(seed)
    return "".join(rng.choices("ACGT", k=n))


def report(seq: str, label: str) -> None:
    if not seq:
        print(f"{label}: empty sequence; skipping.")
        return
    h1 = single_base_entropy(seq)
    h2 = dinucleotide_entropy(seq)
    print(f"{label}: {len(seq):,} bases")
    print(f"  H1 (single-base entropy)      = {h1:.4f} bits/base")
    print(f"  H2|1 (dinucleotide cond. ent) = {h2:.4f} bits/base")
    # human haploid genome implied storage at the empirical entropy
    bits = h1 * 3.2e9
    print(f"  implied storage at H1 for 3.2e9 bp = {bits / 8 / 1e6:.1f} MB")


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        path = Path(argv[1])
        seq = read_fasta(path)
        report(seq, label=str(path))
    else:
        seq = random_sequence(1_000_000)
        report(seq, label="synthetic uniform-random sequence")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
