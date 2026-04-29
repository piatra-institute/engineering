# Notes for the editor: Vol II Ch 14 (Statistical inference)

Items the chapter author would request but cannot resolve from
inside the chapter file.

## Page count vs dossier target

The dossier targets approximately 100 pages. The current first
draft compiles to about 27 pages (chapter 14 spans pages 540-566 in
the build immediately after this draft was integrated). This is in
line with the first-draft density of the released Volume I and
already-drafted Volume II chapters and is short of the dossier
number by design. Closing the gap would require, in roughly the
order an expansion pass should take them:

1. A worked numerical example in §14.1 on the Gaussian-mean
   confidence interval, mirroring the Volume I Chapter 8 commute
   sample, so the reader sees the formal apparatus on familiar
   data.
2. A worked Neyman-Pearson likelihood-ratio example in §14.2 on a
   Gaussian mean shift (a clean closed-form case in which the
   threshold $k$ becomes a $z$-quantile). Currently the lemma is
   stated and its working consequence named, but not exhibited.
3. A second worked MLE in §14.3 for the Gaussian with both
   parameters unknown, including the observed-Fisher-information
   matrix and the joint asymptotic distribution. This pays off the
   asymptotic-normality property on a non-trivial case.
4. A second worked Bayesian update in §14.4 on the
   Gaussian-Gaussian model with known variance, with explicit
   prior, likelihood, posterior, and posterior predictive,
   propagating to a numerical credible interval.
5. A worked OLS regression with diagnostic plots in §14.5,
   including a residual-vs-fitted scatter and a Q-Q plot, on a
   small (~30 point) dataset. This grounds the diagnostic
   discipline before the project demands it.
6. A TikZ figure in §14.5 showing the geometry of the
   $\ell_{1}$-versus-$\ell_{2}$ penalty on a 2D coefficient
   space, which is the standard visual that makes lasso's
   variable-selection corner intuition land.
7. A second estimation block (the chapter currently has one). One
   candidate: estimate the cross-validated standard error of an
   MSE estimator across $5$ folds for a linear regression with $n
   = 100$, given an in-sample residual standard deviation; the
   exercise version is in the estimation block, but the text
   would benefit from a worked one too.
8. A short worked Bonferroni-versus-BH comparison in §14.7 on a
   simulated $m = 20$ test set, exhibiting the difference in the
   number of rejections.
9. Optional mastery-box derivations for the Cram\'er-Rao bound and
   for the asymptotic equivalence of leave-one-out cross-validation
   and the AIC. The algebra is standard and the reader benefits
   from seeing it.

None of these change the chapter's argument; they expand the
apparatus.

## Cross-references to Volume I Chapter 8 and Volume II Chapter 9

The chapter references Volume I Chapter 8 in three places (the
opener, the confidence-versus-prediction subsection of §14.1, and
the regression introduction of §14.5) and Volume II Chapter 9 in
two places (the linear-algebra apparatus of §14.5 and the
ill-conditioning rationale for ridge regression). The references
are made in prose because Ch 8's and Ch 9's section labels are not
exposed for `\cref{}` use. Adding labels to Ch 8 §8.1, §8.4 and Ch
9 §9.5, §9.6, §9.7, and using `\cref{}` here, would tighten the
cross-volume connection. This is a small editorial pass on those
chapters.

## Cross-reference to Volume II Chapter 13 (probability) and Chapter 15 (optimisation)

The chapter forward-references Vol II Ch 13 once (probability
backbone) and Vol II Ch 15 twice (the IRLS solver for logistic
regression and the proximal-gradient solver for lasso). Once Ch 13
and Ch 15 are written, both should reciprocate the reference, so
the reader who arrives in those chapters after Ch 14 sees the
connection back. The forward references are robust to either
order of drafting.

## Citation tier

The chapter cites two textbook references and five method papers:

- `text:wasserman2004` (Wasserman, *All of Statistics*) as the
  canonical reference for the formal apparatus (estimators,
  hypothesis testing, MLE, Bayesian inference, cross-validation).
- `text:devore2015` (Devore, *Probability and Statistics for
  Engineering and the Sciences*) as the reference for the
  applied-engineering catalogue of MLE for canonical
  distributions.
- `method:simmons-nelson-simonsohn-2011`,
  `method:gelman-loken-forking-paths`,
  `method:kerr-harking-1998`,
  `method:open-science-collaboration-2015`,
  `method:errington-cancer-biology-2021` for the §14.7
  malpractice and replication discussion. All five entries were
  added to the bibliography during the Vol I Ch 8 review and are
  available.

No standards (`std:`) keys are cited. The chapter does not name
any accident, so no `acc:` keys appear and the registry is not
touched.

## Reader-path tagging audit

The chapter tags §14.1, §14.2, §14.3, §14.5, §14.6, §14.7 as
`core` and §14.4 (Bayesian inference) as `standard`. Volume I
Chapter 8 also tagged the Bayesian section as `standard`, and the
project here does not require a Bayesian fit; the reader-path
discipline holds. The exercise sets are tagged `core` (Calculation,
Estimation, Diagnosis, Failure analysis), `standard` (Derivation,
Design, Judgment), and `mastery` (Simulation). The project is
tagged `core` and depends only on `core` sections (estimation,
hypothesis testing, regression, cross-validation, malpractice).

## Project: reference solution

The project asks the reader to fit a regression model with $k$-fold
cross-validation on a real dataset. The general editor's reference
solution, mentioned in the project text as available online, has
not been written. A reasonable reference dataset is a UCI
``Concrete Compressive Strength'' set or an OpenML
``housing-prices'' set, on which a ridge regression with $\lambda$
chosen by $5$-fold cross-validation produces the right working
example: a non-trivial regularisation parameter, a clear
diagnostic-plot signal, and a meaningful generalisation gap. The
reference solution should be ~1500 words plus code, deposited in
a project-solutions repository, and linked from the published
edition.

## Pre-emptive Vol I Ch 8 review fixes already applied

The Volume I Chapter 8 review (resolved 2026-04-29) listed
forty-two G-fixes, several of which apply structurally to any
chapter on inference. We applied them preemptively here:

- The frequentist confidence-interval definition is procedural,
  not psychological. The chapter says "the procedure has $1-\alpha$
  long-run coverage," not "the reader is $1-\alpha$ confident."
- Critical values are positive: $t_{1-\alpha/2,n-1}$, not
  $t_{\alpha/2,n-1}$.
- The $p$-value is defined narrowly, with the supremum over the
  composite null and the explicit choice of test statistic. The
  ban on the negate-first construction ("It is not the probability
  that $H_{0}$ is true...") is honoured: the positive form is the
  only form.
- The replication-crisis section cites primary papers for every
  dated empirical claim. Both the 2015 and the 2021 reproducibility
  numbers are there with citations.
- Multiple comparisons are handled formally, with Bonferroni and
  Benjamini-Hochberg both presented and the choice between them
  named.
- The decision-theoretic framing of hypothesis testing replaces
  ``safety-critical means smaller alpha'' with the cost-of-error
  argument.
- Cross-validation is stated as a procedure: every operation that
  adapts to the data sits inside the loop. Data-leakage modes are
  enumerated.
- The principle box at the end of §14.6 makes the discipline
  explicit.

## Half-life tag

The chapter's half-life tag is "foundational." The mathematics of
estimation, MLE, Bayesian inference, regression, and
cross-validation has been stable since the late 1990s and will
remain stable on the timescale of this book. The two areas where
the chapter ages are: (i) the cross-validation discipline as
embodied in software libraries (`scikit-learn`, `statsmodels`,
`tidymodels`), where API conventions shift on a five-year cadence
and the book's prose should not name an API; and (ii) the
replication-rate numbers cited in §14.7, which are dated to 2015
and 2021 and may be superseded by larger-scale registered-report
literatures by the time of a 2046 reissue. The "current as of
YYYY" idiom is in place for both numbers.

## Empty epigraph note

The chapter epigraph is the canonical Box ``All models are wrong''
quote, attributed to Box's 1979 paper on robustness in scientific
model building. The exact published wording varies across Box's
later papers; the editor may want to substitute a more carefully
pinned wording (Box and Draper 1987, p.~424, has a specific
formulation). The current attribution is honest: "the closest
published form is in..." and is acceptable for a first draft.
