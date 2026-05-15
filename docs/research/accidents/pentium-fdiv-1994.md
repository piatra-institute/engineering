---
name: Pentium FDIV bug
year: 1994
domain: software
primary_source: paper:coe-tang-pratt-1995
secondary_sources: [paper:edelman-1997]
short_form: A lookup-table omission in the Intel Pentium floating-point division unit produced incorrect quotients on a small fraction of operand pairs; the bug was discovered by an academic user in 1994, became public through Internet discussion, and led to a recall costing Intel approximately 475 million US dollars.
status: verified
---

# Pentium FDIV bug, 1994

## Date(s) and location

The Pentium processor was released in March 1993. The FDIV bug was discovered by Thomas Nicely of Lynchburg College, Virginia, in June 1994 while computing reciprocal sums of twin primes for a number-theory project. Nicely reported the issue privately to Intel in October 1994; it became public through Internet discussion in November 1994 (cs.compilers and comp.sys.intel newsgroups). Intel announced a no-questions-asked replacement programme on 20 December 1994. The defect affected all Pentium processors shipped between March 1993 and the firmware fix in late 1994.

## Technical mechanism

The Pentium floating-point division unit implemented the Sweeney-Robertson-Tocher (SRT) radix-4 algorithm. SRT division uses a lookup table of pre-computed quotient digits, indexed by the leading bits of the partial remainder and the divisor. The table holds quotient-digit values from a redundant signed-digit set $\{-2, -1, 0, +1, +2\}$. The implementation team transferred the table values from a host development computer to the Pentium die using a script. The script transferred 1066 of the 1067 table entries correctly; five entries were inadvertently left empty and were read as zero by the division hardware \cite{paper:coe-tang-pratt-1995}.

The empty entries lay in a region of the table that is exercised only by operand pairs whose leading bits drive the partial remainder into that specific cell. The probability of hitting an affected entry on a uniformly random operand pair is approximately $1$ in $9$ billion; the probability on operands typical of spreadsheet or financial work is much lower. The error, when triggered, was a quotient incorrect from the fifth significant decimal digit; the relative error was bounded above by approximately $5 \times 10^{-5}$ \cite{paper:coe-tang-pratt-1995}. The error affected division only; multiplication, addition, subtraction, and the transcendental functions were unaffected.

Coe, Tang, and Pratt's 1995 analysis identified the affected operand region exactly and provided a small set of operand pairs that reliably triggered the bug; the canonical test (4195835.0 / 3145727.0) returns approximately 1.33373906 on a correct processor and approximately 1.33382044 on an affected Pentium, a relative error of about $6 \times 10^{-5}$ \cite{paper:coe-tang-pratt-1995}.

## Organisational / regulatory mechanism

Intel's initial response (October 1994) was to acknowledge the defect privately, characterise it as too rare to matter in practice, and replace processors only for users who could demonstrate they were doing affected calculations. The public response that followed in November (IBM halted Pentium PC shipments; the Internet press cycle picked up the case) forced a wider remedy. On 20 December 1994 Intel announced an unconditional no-questions-asked replacement; the eventual write-off was approximately 475 million US dollars (1994 dollars).

The case is recurrently cited as the first major Internet-driven consumer engineering issue: the technical community surfaced the defect, characterised it independently, and forced a remedy at a scale and speed the affected manufacturer would have preferred to manage. The episode also recalibrated semiconductor companies' release-verification practice: formal verification of arithmetic units became standard at major vendors over the next decade, with Intel funding substantial formal-methods research after 1994 \cite{paper:edelman-1997}.

## Lessons by scale

- Volume I, Chapter 4 ("Error and uncertainty"): a single hardware bug that produces predictable error in a specific operand region, undetectable by ordinary statistical testing.
- Volume II, Chapter 16 ("Numerical methods"): the cost of a single bad operation in floating-point lookup-table arithmetic.
- Volume VII, Chapter 2 ("Number representations, arithmetic, precision"): the canonical case of a hardware floating-point defect; the design of post-FDIV verification practice.
- Volume VII, Chapter 7 ("Computer architecture"): the SRT algorithm and the lookup-table organisation of the division unit.
- Volume VII, Chapter 19 ("Software engineering as discipline"): the Internet-driven discovery process and the institutional response.
- Volume X, Chapter 5 ("Software defects"): the bug as a defect that survived all internal testing because internal tests did not cover the affected operand cells.
- Volume X, Chapter 11 ("Regulatory and certification failure"): the gap between Intel's risk-based remedy and the public's demand for an unconditional fix.

## Citation keys

- Primary: `paper:coe-tang-pratt-1995`. Coe, Tang, and Pratt, "Computational aspects of the Pentium affair," IEEE Computational Science and Engineering, 1995. Detailed reverse-engineering of the affected lookup-table cells and the operand-pair characterisation.
- Secondary: `paper:edelman-1997`. Edelman, "The mathematics of the Pentium division bug," SIAM Review, 1997. Mathematical analysis of the SRT algorithm and the error bound; the canonical academic reference for the bug's mathematical structure.

## Short-form summaries

\textbf{One sentence}: A lookup-table omission in the Intel Pentium floating-point division unit produced incorrect quotients on a small fraction of operand pairs; the bug was discovered by an academic user in 1994, became public through Internet discussion, and led to a recall costing Intel approximately 475 million US dollars.

\textbf{Two sentences}: The Intel Pentium processor, released in 1993, contained five missing entries in the lookup table of its SRT-based floating-point division unit; operand pairs whose computation crossed the missing cells produced a quotient incorrect from the fifth significant decimal digit. The defect was discovered by Thomas Nicely at Lynchburg College in 1994, characterised in detail by Coe, Tang, and Pratt in 1995, and remedied by an unconditional Intel replacement programme costing approximately 475 million US dollars.

\textbf{One paragraph}: The Pentium FDIV bug was a defect in the floating-point division unit of Intel's Pentium processor, released in March 1993. The division unit used the Sweeney-Robertson-Tocher (SRT) algorithm, which indexes a lookup table of pre-computed quotient digits by the leading bits of the partial remainder and divisor. Five entries in the 1067-cell table were inadvertently zeroed during the table transfer to the die; operand pairs whose intermediate state hit one of these cells produced a quotient incorrect from the fifth significant decimal digit, a relative error of approximately $5 \times 10^{-5}$. The defect was discovered in June 1994 by Thomas Nicely, became public on Internet newsgroups in November 1994, and forced Intel to announce an unconditional replacement programme on 20 December 1994 at an eventual cost of approximately 475 million US dollars. The case is the canonical example of a hardware arithmetic defect found by an end user and remedied under public pressure, and it triggered widespread adoption of formal verification in semiconductor design.

## Provenance and verification

Sources consulted: Coe, Tang, and Pratt 1995 (primary technical analysis with operand-pair characterisation and table-cell identification); Edelman 1997 (mathematical analysis); Intel's public statements from October-December 1994. The technical mechanism (SRT algorithm, missing table entries, error magnitude) is from Coe-Tang-Pratt. The 475-million-dollar figure is the publicly reported write-off. Verified: 2026-05-15.
