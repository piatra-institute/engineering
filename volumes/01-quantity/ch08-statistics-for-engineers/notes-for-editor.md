# Notes for the editor: Vol I Ch 8 (Statistics for engineers)

Items the chapter author would request but cannot resolve from inside the
chapter file.

## Page count vs dossier target

The dossier targets approximately 90 pages (sum of per-section budgets
plus apparatus). The current draft compiles to about 28 pages, which is
in line with the released chapters in this volume (Ch 4 is roughly 24
pages of body) but well short of the dossier number.

Closing the gap would require: expanded worked examples in §8.2 (a full
Weibull fit walk-through with plot), additional contingency-table
examples in §8.5 (a sensor-fusion example to complement the medical-test
one), a complete A/B-test worked example in §8.6, and one or more TikZ
plots (a histogram, a Q-Q plot, a power curve, a confidence-vs-
prediction interval comparison). None of these change the chapter's
argument; they expand the apparatus.

A future drafting pass should also consider promoting the rule-of-thumb
sample-size formula derivation to a mastery box in §8.6, since the
algebra is light and the reader benefits from seeing where the constant
$16$ comes from.

## Replication-crisis registry entries

§8.8 discusses the replication-crisis pattern in general terms, per the
chapter brief. The registry currently has no replication-crisis entries.
Three candidates would strengthen the chapter if and when they are
written into the registry per the SCHEMA:

1. The 2015 reproducibility study in psychology (Open Science
   Collaboration, *Estimating the reproducibility of psychological
   science*, Science, 2015). This would justify naming the
   Reproducibility Project: Psychology in §8.8 and citing its primary
   publication.
2. A representative cancer-biology reproducibility study (the
   Reproducibility Project: Cancer Biology has a series of papers,
   2017-2021; eLife is the publication venue).
3. The fMRI cluster-size methodological errors (Eklund, Nichols, and
   Knutsson 2016, *Cluster failure: Why fMRI inferences for spatial
   extent have inflated false-positive rates*, PNAS).

Each would be a registry entry of the kind currently used for industrial
accidents, with the appropriate domain tag (research-methods rather
than aerospace, civil, etc.). The schema would need either light
extension or the entries would record the replication-failure mechanism
in the Technical mechanism section and the methodological consequences
in the Lessons section.

If the editor adds these entries, the chapter's §8.8 prose could be
revised to name them and add their citation keys. Until then, the
section stays generic per the brief.

## Bayesian section: numerical example choice

§8.5 uses a manufacturing defect-test example with a $1\,\%$ prior. An
alternative or supplementary example would use a structural integrity
test (the kind familiar from Ch 5 sensors and Ch 7 mass measurement)
where the prior comes from a known failure rate of an inspected
component class. The medical-test framing was chosen for its
recognisability; the editor may prefer a more engineering-flavoured
example.

## Cross-references to Ch 4

The chapter cross-references Ch 4 §4.4 (CLT, sample size and the
t-distribution) and Ch 4 §4.6 (confidence intervals). These are made
in prose rather than via `\cref{}` because Ch 4's section labels are
not currently exposed as cross-reference targets; the section heading
text is used. If the editor wants explicit `\cref{}` cross-references,
section labels should be added to Ch 4 first, then the references
inserted here.

## Citation key tier

The chapter cites `text:wasserman2004` as the primary statistical
reference and `text:devore2015` for engineering framing where it is
sharper (sample-size in §8.6, tolerance intervals in §8.4). The NIST
e-Handbook `web:nist-eshandbook` is cited in §8.3 as a working catalogue
of common tests. No standards (`std:`) keys are cited in this chapter
because the GUM and VIM are not load-bearing for the chapter's content;
they were the spine of Ch 4 and remain so for the uncertainty
framework. If the editor prefers a standards anchor, ISO 5725 (accuracy
and precision of measurement methods) would be the natural citation
addition; it is not currently in `bibliography/references.bib`.
