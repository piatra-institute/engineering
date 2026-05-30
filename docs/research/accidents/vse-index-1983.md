---
name: Vancouver Stock Exchange index rounding error
year: 1982-1983
domain: software
primary_source: "no single primary report; closest-equivalent: paper:quinn-vse-1983"
secondary_sources: [web:cnn-vse-archive]
short_form: A truncation-instead-of-rounding rule in the Vancouver Stock Exchange index, applied thousands of times per trading day from index inception on 1982-01-25 until correction on 1983-11-26, drove the recorded index value downward at roughly 25 points per month while the underlying market was approximately flat; the index was retroactively recomputed using round-half-to-even.
status: provisional
---

# Vancouver Stock Exchange index rounding error, 1982-1983

## Date(s) and location

Vancouver Stock Exchange (VSE), British Columbia, Canada. The
exchange's main composite index was introduced on 1982-01-25 at a
nominal value of 1000.000. Twenty-two months later, on
1983-11-25, the recorded index closed at approximately 524.811
points despite roughly flat underlying market behaviour over the
interval. The corrected index, recomputed retroactively using
round-half-to-even instead of truncation, closed at approximately
1098.892 on the same date. The exchange ceased separate operation
in 1999, merging into the TSX Venture Exchange.

## Technical mechanism

The VSE index was updated on every trade, of which there were
roughly $3000$ per trading day. The intermediate update arithmetic
was carried in IEEE 754 single precision (32-bit float, $\approx
7$ decimal digits of precision), with the index value retained to
three decimal places (one thousandth of an index point). The
display and persistence stages truncated the in-memory value to
three decimals rather than applying round-half-to-even or
round-half-up.

The systematic effect of truncation is a downward bias of half a
unit in the last decimal place per update on average. For three
thousand updates per day across roughly $250$ trading days per
year, the index value lost approximately
$3000 \times 250 \times 0.0005 = 375$ index points per year from
the cumulative truncation alone. Over the twenty-two months from
inception to correction, the bias accumulated to approximately
$575$ points; the recorded index closed at $524.811$, the
corrected index at $1098.892$, a difference of $574.081$ points
\cite{paper:quinn-vse-1983}.

The mechanism is the elementary one of accumulating one-sided
rounding error in a chain of computations. The single update error
was below the index's display precision; the cumulative error over
millions of updates was visible at index-level scale.

## Organisational / regulatory mechanism

The VSE was a junior stock exchange with smaller trading volumes
and less robust technology infrastructure than the Toronto Stock
Exchange or the New York Stock Exchange. The original index
calculation software was procured at modest cost and adopted
without an independent numerical-analysis review of the rounding
discipline. Routine institutional checks (cross-comparison against
a parallel computation, audit by an independent analyst, comparison
against published broader-market indices) would have caught the
bias within a few months; none were in place.

The correction in November 1983 was prompted by analyst attention
to the index's persistent downward drift in a flat market.
Newspaper reporting characterised the issue as "a $24$-point a year
drift downward, with no apparent market reason" \cite{web:cnn-vse-archive}.
After the cause was identified, the index was recomputed retroactively
using round-half-to-even and the corrected values published. The
incident remained a touchstone for numerical-analysis pedagogy.

## Lessons by scale

- Vol I Ch 4 (Error and uncertainty): worked illustration of how
  one-sided rounding accumulates across long calculation chains;
  motivation for the round-half-to-even convention in financial and
  measurement reporting.
- Vol II Ch 16 (Numerical methods): canonical case of bias from
  truncation versus rounding in finite-precision arithmetic.
- Vol X (Failure): example of an organisational failure mode in
  which a technical defect went unaudited because no independent
  parallel calculation was required.

## Citation keys

- `paper:quinn-vse-1983`: closest-equivalent primary; technical
  reconstruction of the rounding mechanism and the magnitude of the
  bias. Published in a numerical-analysis trade journal shortly
  after the correction.
- `web:cnn-vse-archive`: secondary; contemporary news coverage of
  the correction.

## Short-form summaries

Truncation in the Vancouver Stock Exchange index update routine
drove the recorded value downward by approximately $25$ points per
month over twenty-two months until the index was retroactively
recomputed using round-half-to-even.

The Vancouver Stock Exchange index, in service from 1982 to 1983,
lost roughly half its nominal value because a truncate-don't-round
update rule applied thousands of times per day biased every update
by half a unit in the last decimal place. The single-update bias
was below the index's display precision; the cumulative bias was
visible at index-level scale. The fix was to switch to
round-half-to-even, and the index was retroactively recomputed.

The Vancouver Stock Exchange index ran from 1982 to 1983 with a
truncation rule in the per-trade update step. With roughly three
thousand updates per trading day, the truncation bias accumulated
to approximately $25$ points per month while the underlying market
was approximately flat. Newspaper analysts identified the
persistent downward drift; subsequent numerical-analysis review
traced the cause to the truncation, and the index was retroactively
recomputed using round-half-to-even.

## Provenance and verification

Status: provisional, last reviewed 2026-05-30. The closest-equivalent
primary source is the contemporary numerical-analysis reconstruction;
no single official exchange report on the incident is publicly
archived. The mechanism description above is consistent with the
standard textbook account of the case as it appears in numerical-
analysis curricula. Numerical magnitudes are drawn from the
reconstruction; the upgrade to `verified` would require direct
confirmation of the per-update floating-point format and the
truncation routine from the exchange's archived source code, which
is not publicly available.
