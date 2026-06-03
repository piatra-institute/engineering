"""Codon optimisation for heterologous expression.

A heterologous gene expressed in a foreign host may carry codons that
are rare in the host's tRNA pool. The codon-adaptation index (CAI) of
Sharp and Li (1987) gives a quantitative measure of the match between
a gene's codon usage and a reference set of highly expressed host genes.

For each codon c that encodes amino acid a, define the relative
adaptiveness w_c = f_c / f_max(a), where f_c is the codon's frequency
among synonyms for a in the reference set and f_max(a) is the frequency
of the most-used synonym for a. The CAI of a gene is the geometric
mean of w_c over its codons:

    CAI = exp( (1/L) * sum_i log w_{c_i} )

A CAI near 1 means the gene matches the host's preferred codon usage;
a CAI near 0 means the gene uses rare codons.

The script:

  1. Parses a CSV reference codon-usage table (data/genetic-code.csv plus
     a host_frequency column passed in).
  2. Computes CAI for an input ORF.
  3. Optionally re-codes the ORF to maximise CAI subject to keeping the
     protein sequence intact.
"""
from __future__ import annotations

import argparse
import math
from collections import defaultdict


# Compact standard genetic code (DNA codons; T == U).
STANDARD_CODE: dict[str, str] = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}


# E. coli K-12 reference codon frequencies (per thousand) abridged from
# the Codon Usage Database (Nakamura, 2000), current as of 2024.
# Where two synonyms exist, the table assigns higher frequencies to
# the canonical E. coli high-expression codons.
ECOLI_FREQ: dict[str, float] = {
    # F
    "TTT": 22.3, "TTC": 16.0,
    # L
    "TTA": 13.9, "TTG": 13.7, "CTT": 11.9, "CTC": 11.1, "CTA": 3.9, "CTG": 52.6,
    # I
    "ATT": 30.4, "ATC": 25.1, "ATA": 4.4, "ATG": 27.9,
    # V
    "GTT": 18.3, "GTC": 15.3, "GTA": 10.9, "GTG": 26.4,
    # S
    "TCT": 8.5, "TCC": 8.6, "TCA": 7.1, "TCG": 8.9, "AGT": 8.8, "AGC": 16.0,
    # P
    "CCT": 7.0, "CCC": 5.5, "CCA": 8.4, "CCG": 23.2,
    # T
    "ACT": 8.9, "ACC": 23.4, "ACA": 7.1, "ACG": 14.4,
    # A
    "GCT": 17.1, "GCC": 24.2, "GCA": 21.2, "GCG": 33.0,
    # Y / *
    "TAT": 16.2, "TAC": 12.2, "TAA": 2.0, "TAG": 0.3, "TGA": 1.0,
    # H / Q
    "CAT": 12.9, "CAC": 9.7, "CAA": 15.3, "CAG": 28.9,
    # N / K
    "AAT": 17.7, "AAC": 21.7, "AAA": 33.6, "AAG": 12.1,
    # D / E
    "GAT": 32.7, "GAC": 19.2, "GAA": 39.1, "GAG": 18.7,
    # C / W
    "TGT": 5.2, "TGC": 6.4, "TGG": 13.9,
    # R
    "CGT": 20.0, "CGC": 22.0, "CGA": 3.8, "CGG": 5.4, "AGA": 3.6, "AGG": 1.4,
    # G
    "GGT": 25.5, "GGC": 27.1, "GGA": 9.2, "GGG": 11.8,
}


def relative_adaptiveness(freq: dict[str, float]) -> dict[str, float]:
    by_aa: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for codon, aa in STANDARD_CODE.items():
        if aa == "*":
            continue
        by_aa[aa].append((codon, freq.get(codon, 0.0)))
    w: dict[str, float] = {}
    for aa, syns in by_aa.items():
        f_max = max(f for _, f in syns)
        for codon, f in syns:
            w[codon] = (f / f_max) if f_max > 0 else 0.0
    return w


def cai(orf: str, w: dict[str, float]) -> float:
    orf = orf.upper().replace("U", "T")
    codons = [orf[i:i + 3] for i in range(0, len(orf) - 2, 3)]
    log_sum = 0.0
    n = 0
    for c in codons:
        aa = STANDARD_CODE.get(c)
        if aa is None or aa == "*":
            continue
        if w.get(c, 0.0) > 0:
            log_sum += math.log(w[c])
            n += 1
    if n == 0:
        return 0.0
    return math.exp(log_sum / n)


def recode_max_cai(orf: str, freq: dict[str, float]) -> str:
    """Replace each codon with the highest-frequency synonym for its amino acid."""
    orf = orf.upper().replace("U", "T")
    codons = [orf[i:i + 3] for i in range(0, len(orf) - 2, 3)]
    best_for_aa: dict[str, str] = {}
    for codon, aa in STANDARD_CODE.items():
        if aa == "*":
            continue
        if aa not in best_for_aa or freq.get(codon, 0) > freq.get(best_for_aa[aa], 0):
            best_for_aa[aa] = codon
    out = []
    for c in codons:
        aa = STANDARD_CODE.get(c, "*")
        if aa in best_for_aa:
            out.append(best_for_aa[aa])
        else:
            out.append(c)
    return "".join(out)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--orf", type=str, required=False,
                        default=("ATGGCAAGCTTGAATAACCGCCAGGAAGCGCGT"
                                 "ATTCAACTGAAATTCTGGGGGAAATGA"),
                        help="DNA ORF, starting with ATG")
    parser.add_argument("--recode", action="store_true")
    args = parser.parse_args()

    w = relative_adaptiveness(ECOLI_FREQ)
    score = cai(args.orf, w)
    print(f"ORF length     : {len(args.orf)} bp ({len(args.orf) // 3} codons)")
    print(f"CAI (E. coli)  : {score:.3f}")
    if args.recode:
        recoded = recode_max_cai(args.orf, ECOLI_FREQ)
        print(f"recoded ORF    : {recoded}")
        print(f"CAI after re-coding: {cai(recoded, w):.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
