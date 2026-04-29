# Volume 1 Chapter 4 review: Error and uncertainty

Resolved: 2026-04-29.

The 36 fixes in section G have been applied. The two release-blocking
process errors are closed: an `\begin{estimation}` block now sits before
the pendulum worked example with the relative-uncertainty estimate that
the calculation then confirms; the Volkswagen diesel-defeat case is now
backed by a verified registry entry at
`docs/research/accidents/volkswagen-diesel-defeat-2015.md` and cited in
prose via `\cite{acc:epa-vw-nov-2015, acc:doj-vw-2017}`.

Bibliography additions: `acc:epa-vw-nov-2015` (EPA Notice of Violation,
18 September 2015), `acc:doj-vw-2017` (DOJ January 2017 announcement of
the criminal plea), and `web:nist-optical-clock` (NIST optical-frequency
material). The optical-clock and Kibble-balance precision claims in
§4.7 now carry "current as of 2026" inline and cite the new entries.

Technical corrections: the canonical fix is the correlated-cancellation
example, replaced from a sum with $\rho = -1$ to a difference with
$\rho = +1$ (the equation flipped sign on the covariance term and the
narrative flipped from $y = x_{1} + x_{2}$ to $y = x_{1} - x_{2}$), so
the example now matches the "common-mode cancellation in difference
measurements" narrative the prose was reaching for. Other technical
fixes: partial derivatives stated at "input estimates" (not means);
correlated-product caveat added to the relative-uncertainty rule;
Type A / Type B framing rewritten away from "natural home of random /
systematic" toward VIM-aligned method-of-evaluation language; CLT
section promoted from `\pathtag{standard}` to `\pathtag{core}` (since
the chapter invokes the CLT in core reasoning); CLT regularity
conditions tightened (Lyapunov / Lindeberg referenced explicitly);
t-distribution origin clarified (population-standard-deviation
estimation, not CLT failure); significant-figures rule rewritten to
remove the internal contradiction and cite NIST SP 811;
confidence-interval guidance rewritten from "the distinction is
academic" to a name-the-interval-type instruction; manufacturer-
specification subsection rewritten to refuse coverage-factor inference
from the plus-minus sign.

Project corrections: photographic method now dimensionally complete
(pixel height converted to sensor-plane height in same units as focal
length, with the $h \approx d \cdot s_{\text{image}} / f$ small-angle
formula); hand-rule method requires the reader to calibrate their own
hand at arm length.

Exercise corrections (G30--G35): standard-vs-expanded-uncertainty
fixes applied to mass-population, refrigerator, and clinical-glucose
exercises; correlated-mean derivation reframed with equal-pair
correlation rather than adjacent-measurement covariance; clinical-
glucose exercise no longer points to ISO 15197 as an optional prop;
smartphone gyroscope exercise reframed with assumed values supplied
in the problem statement.

Two new exercises (G36) added to bring the count to 35 against the
\chapmeta target: a manufacturer-specification three-ways exercise
(rectangular half-width, $k = 2$ Gaussian, unresolved); a Monte Carlo
correlated-difference exercise that exercises the new $u_{c}^{2}(y)
= u^{2}(x_{1}) + u^{2}(x_{2}) - 2\rho u(x_{1}) u(x_{2})$ formula
across $\rho = 0, 0.5, 0.9, 0.99$.

Voice rewrites (section B): self-announcing topic sentences rewritten;
"a familiar result" cut; archetype-as-syllabus framing rewritten as
the working pattern; "for most engineering work the distinction is
academic" replaced with "name the interval type and assumptions";
"every chapter has a failure section" leak removed; aphoristic
restatements at the end of §4.8 rewritten as procedural prevention.

Hubble subsection tightened to the registry short-form with the OSBI
report cited; the chronic-class list collapsed from five named
sub-patterns to a generic-with-one-named-case prose paragraph (VW as
the named case, with citation; other patterns named as generic
audit questions).

Structural improvements landed alongside the chapter fixes:

- `make accidents` extended to scan chapter prose (excluding the
  `\chapmeta` block) for canonical accident names from the registry.
  Every named accident in prose must have at least one of its
  registry-entry citation keys cited via `\cite{}` in the chapter.
  Output now reports both the cite-resolution check and the
  prose-name scan.
- `make exercise-counts` (new target) compares each chapter's
  `\begin{exercise}` block count against the `Exercise target: N`
  line in its `\chapmeta`. Skips scaffolding-only chapters (zero
  exercises); flags chapters with prose where target ≠ actual.
  Currently passes for all 4 chapters with prose (Vol I Ch 1: 28;
  Ch 2: 35; Ch 3: 30; Ch 4: 35).

The build is clean: `make strict` produces a 574-page `main.pdf`;
`make check`, `make audit-docs`, `make accidents` (extended), and
`make exercise-counts` all PASS; `grep` finds no em-dashes in the
chapter source.

The structural risks named in section H (project-wide named-entity
detection beyond `\cite{}` keys; mechanical exercise-target
enforcement) are now closed at the Makefile level. The dossier
schema redesign (H3) remains deferred to a separate Phase 0.7 task.

Build-facing note: no chapter-specific hard build breaker was found. `make check` passes across 174 chapter shells, `make accidents` passes, and `make strict` reported `main.pdf` up to date. This was not a forced clean rebuild. The chapter has no `\cref`, `\autoref`, or `\ref` commands beyond its own `\label{vol01:ch04}`. It does have a release-blocking process error: no `\begin{estimation}` environment, although Q20 and the reviewer guide require one in every chapter.

Sources checked include the local dossier, the Volume I opener, the Hubble registry entry, the cited BibLaTeX entries, JCGM 100, JCGM 101, JCGM 200/VIM, the NIST e-Handbook t table, the NASA Hubble OSBI record, NIST Kibble balance material, and recent NIST or NIST-affiliated optical-clock material.

## A. Verdicts

Technical reviewer: blocked. Blockers: the failure section names the Volkswagen diesel-defeat case without a registry entry or primary-source citation, and the chapter contains technical errors in the correlated-cancellation example, the significant-figures rounding rule, the confidence-interval guidance, the photographic height formula, and the current precision claims for frequency and Kibble-balance measurements.

Pedagogical reviewer: blocked. Blockers: the chapter does not contain the required formal estimation environment, and the exercise set has 33 exercises against a stated target of 35 while several exercises are internally contradictory or under-specified.

Voice reviewer: approved-with-corrections. The chapter is mostly in the house register and contains no em-dashes or the major banned vocabulary hits, but several sentences are self-announcing, aphoristic, or overconfident where the text needs measurement-specific prose.

## B. Voice review

We walk the chapter in order. The voice problems are not dense, but they sit near the chapter's thesis and failure section, where a reader will notice them.

1. Lines 20-25: "A measurement returns a number. The number's value is half of what the measurement reports. The number's uncertainty is the other half. This chapter teaches the reader to compute both, to combine uncertainties from multiple input quantities, and to recognise the recurring failure mode in which the uncertainty figure is chosen for reasons other than the data."

Rule: `docs/voice.md`, self-announcing topic sentence. The first three sentences are useful. The fourth turns into syllabus prose.

Rewrite: "A measurement returns a value and an uncertainty. This chapter makes the second quantity operational: we compute it, propagate it through measurement models, and reject uncertainty figures that were selected for institutional convenience rather than derived from evidence."

2. Lines 56-57: "Random and systematic error have characteristic mechanisms."

Rule: `docs/voice.md`, authority by specificity. This is a thin topic sentence that announces the paragraph rather than doing work.

Rewrite: "The mechanism matters because it tells us which corrective action has a chance of working."

3. Lines 109-121: "The uncertainty archetype, named in the volume opener and introduced informally in chapters 1 through 3, becomes a formal device here. The archetype names the discipline of carrying an uncertainty parameter alongside every reported value, treating the parameter as a real quantity with its own propagation rules and its own physical interpretation, and refusing to report a number without it. Every later volume in this work invokes the archetype: thermodynamic quantities have measurement uncertainties (Volume IV), structural loads have uncertainties (Volume III), reliability metrics have uncertainties (Volume IX), failure rates have uncertainties (Volume X), all the way through. The archetype's first formal home is this chapter."

Rule: `docs/voice.md`, meta-explanation tail and self-announcing structure. The content is right, but the box talks about the book apparatus before it teaches the pattern.

Rewrite: "Uncertainty is the engineering habit of carrying a second quantity beside the reported value. The value says where the measurement lands; the uncertainty says how wide the defensible landing zone is. Later chapters attach the same habit to loads, temperatures, material properties, reliability estimates, and failure rates."

4. Lines 277-278: "The uncertainties of additive terms combine in quadrature, weighted by the coefficients squared. A familiar result."

Rule: `docs/voice.md`, bad pedagogical aside. "A familiar result" is a wink to the prepared reader and dead air for the reader meeting the result here.

Rewrite: "The uncertainties of additive terms combine in quadrature, weighted by the squared coefficients."

5. Lines 390-399: "The choice between linear propagation and Monte Carlo is itself an engineering judgement. Linear propagation is faster, gives analytic insight into which input dominates the output uncertainty, and is easier to document. Monte Carlo is more accurate when the function is nonlinear or the input uncertainties are large, gives the full output distribution, and is more easily extended to constraints (truncated distributions, censored data). For routine engineering measurements with small input uncertainties, linear propagation is the default; for safety-critical or research-grade work, Monte Carlo is increasingly the standard."

Rule: `docs/voice.md`, overstatement and current empirical claim without date. "Increasingly the standard" sounds like trend rhetoric unless we cite a current practice source.

Rewrite: "The choice between linear propagation and Monte Carlo is an engineering judgment. Linear propagation is fast, exposes the dominant sensitivity coefficient, and is easy to document. Monte Carlo is better when the input distributions and model are specified but the output distribution is nonlinear, asymmetric, truncated, or censored. The method still has sampling error, so the report must state the trial count or convergence criterion."

6. Lines 484-486: "The discipline is to use significant figures only as a quick communication of approximate precision. When the precision matters, report an explicit uncertainty alongside the value."

Rule: `docs/voice.md`, self-announcing formulation. The sentence is not banned, but it repeats the chapter's slogan rather than sharpening the action.

Rewrite: "Use significant figures as a quick warning label, not as the uncertainty budget. When the precision matters, report the value and its uncertainty together."

7. Lines 552-558: "For most engineering work, the distinction is academic. The intervals computed by either framework agree when the prior is non-informative and the data dominate. The reader who needs the distinction (in a regulatory submission, a legal proceeding, or a careful research paper) should use the framework's terminology explicitly. The reader who is reporting a working measurement can use either interpretation, provided the coverage factor is stated."

Rule: `docs/voice.md`, overconfident hedge and imprecise authority. "For most engineering work" smooths over a distinction the chapter has just taught.

Rewrite: "For routine laboratory reporting, the practical action is to name the interval type and coverage basis. A GUM expanded uncertainty is reported with its coverage factor and assumptions. A Bayesian credible interval is reported with its prior and likelihood model. The reader should not translate one into the other silently."

8. Lines 680-687: "Every chapter has a failure section. This chapter's failure mode is the recurring case in which an uncertainty figure is reported smaller than the underlying data supports because of commercial, regulatory, legal, or political pressure. The pattern is harder to detect than a missing measurement (chapter 1) or a unit error (chapter 2): the report contains numbers, the numbers look defensible, but the uncertainty figure has been chosen rather than computed."

Rule: `docs/voice.md`, self-announcing topic sentence. "Every chapter has a failure section" leaks the editorial rule into the reader-facing chapter.

Rewrite: "The failure mode here is quieter than a missing measurement or a unit error. The report contains numbers, the numbers look defensible, and the uncertainty figure is smaller than the evidence permits because schedule, money, legal exposure, or institutional pressure has entered the uncertainty budget."

9. Lines 721-723: "A financial stress test whose scenarios are chosen so that the institution passes is not a stress test; it is a confirmation exercise."

Rule: `docs/voice.md`, negate-first-then-pivot construction. The claim also needs sourcing if it remains.

Rewrite: "A financial stress test becomes a confirmation exercise when the scenarios are selected to protect the passing result."

10. Lines 747-753: "The pattern is the same in each case: an uncertainty figure is chosen for non-technical reasons. The discipline that prevents the pattern is to derive the uncertainty from the data, document the derivation (Type A, Type B, or Monte Carlo), and report the dominant component. The discipline that catches the pattern in others' work is independent recomputation: take the underlying data or the underlying methodology, redo the propagation, and compare."

Rule: `docs/voice.md`, thesis restatement and repeated "the discipline." The content is right but sounds like the chapter closing twice.

Rewrite: "The common failure is an uncertainty budget that answers to pressure rather than evidence. Prevention is procedural: derive the uncertainty from the data and model, document the Type A, Type B, or Monte Carlo route, report the dominant component, and make the calculation reproducible."

## C. Technical review

The chapter is promising, but not ready to ship. The main formulas are mostly correct, and the Hubble primary-source citation is the right source tier. The failures sit in caveats, current numerical claims, and rules of thumb stated too strongly.

The random and systematic error definitions at lines 29-34 match the VIM. VIM 2.17 defines systematic measurement error as a component that remains constant or varies predictably in replicate measurements, and VIM 2.19 defines random measurement error as a component that varies unpredictably. The chapter should keep the definitions but stop treating random and systematic error as if they map cleanly onto Type A and Type B uncertainty. Lines 87-99 call Type A the natural home of the random component and Type B the natural home of the systematic component, then lines 101-107 correctly say the distinction is method of evaluation rather than error character. We should keep the correction and demote the "natural home" phrasing. Bias terms can be estimated statistically through calibration campaigns, interlaboratory comparisons, or repeated measurements under varied conditions. Random effects can also enter Type B evaluations through prior data or manufacturer information.

The distribution section is serviceable but under-cited. The Gaussian coverage figures at lines 141-145 and the uniform standard deviation at lines 162-170 are correct. The quantisation sentence is too broad: quantisation error is modeled as uniform only under assumptions about input phase, variation, or dithering. The asymmetric distribution examples at lines 179-195 need a source or a lighter frame, especially "financial returns" and "network packet arrivals." The Cauchy paragraph is mathematically right, but the claim about where heavy-tailed errors occur needs a source or should be cut.

The GUM propagation formula at lines 227-245 is dimensionally correct. The covariance term has dimensions of $x_i x_j$, and each product of sensitivity coefficients and covariance has dimensions of $y^2$. The text should say the partial derivatives are evaluated at the input estimates, not necessarily the input mean values. In GUM language the model uses estimates of the input quantities. The uncorrelated special case at lines 247-261 is correct.

The product and ratio special case at lines 280-290 is missing a condition. The relative-uncertainty formula is the uncorrelated first-order case. Correlated input quantities add covariance terms in logarithmic form. As written, the paragraph can teach a false rule for measurements made by the same instrument, from the same calibration, or under shared environmental drift.

The cancellation case at lines 292-304 is the most visible technical error in the chapter. The equation for a sum with correlation coefficient $\rho$ is correct. The application to difference measurements is not. Subtracting two readings from the same drifting instrument cancels common-mode drift when the errors are positively correlated and the model is $y=x_1-x_2$, which gives a covariance term of $-2\rho u(x_1)u(x_2)$. The chapter instead presents a sum with $\rho=-1$ and then uses a difference-measurement example. That mismatch will embarrass the book in front of anyone who has done comparator measurements or common-mode rejection.

The pendulum worked example at lines 306-339 checks numerically. Using $L=1.000\,\si{\meter}$, $T=2.007\,\si{\second}$, $u(L)=0.001\,\si{\meter}$, and $u(T)=0.005\,\si{\second}$ gives $g=9.8009\,\si{\meter\per\second\squared}$, relative standard uncertainty about $5.08\times10^{-3}$, and $u_c(g)=0.0498\,\si{\meter\per\second\squared}$. The dimensions cancel. The chapter should still add an estimation block before this calculation, because Q20 requires estimation before calculation.

The Monte Carlo procedure at lines 365-380 is directionally right, but the trial-count claim is too blunt. JCGM 101 does not prescribe "typically $M \geq 10^5$" as a general engineering rule. It describes implementation, validation, and adaptive Monte Carlo procedures in which the number of trials is driven by numerical tolerance and stability of the reported quantities. If the chapter wants to give a rule of thumb, it should state that simple models often use $10^5$ to $10^6$ trials and that the report must document convergence or numerical tolerance.

The central-limit theorem statement at lines 404-408 is acceptable as a teaching version, but "regardless of the distribution" should be tightened to "under the stated regularity conditions." Lines 443-457 blur the distinction between the distribution of the sample mean and the distribution of the standardized statistic when the variance is estimated. If the parent population is Gaussian, the sample mean is Gaussian, but confidence intervals use the Student $t$ statistic because the sample standard deviation replaces the unknown population standard deviation. The NIST t table supports the small-sample correction, and the "n >= 30" rule is a useful approximation, not a metrological law.

The significant-figures section contains a direct internal inconsistency. Lines 496-503 say uncertainty should usually be reported with one or two significant figures, then give $0.052\,\si{\volt}$ as the two-significant-figure version of $0.05246\,\si{\volt}$ while also saying two significant figures are used when the leading digit is 1 or 2 and one otherwise. Since the leading digit is 5, that convention would round to $0.05\,\si{\volt}$, not $0.052\,\si{\volt}$. The rounding-rule claim at lines 490-494 also needs a source or softer language. Round-half-to-even is common in standards and software, but it is not "the standard rounding rule for engineering reporting" without qualification.

The confidence-interval section is the other high-risk technical passage. Lines 533-550 correctly distinguish frequentist procedure coverage from probability assigned to a particular interval. Lines 552-558 then tell the working reader that the distinction is academic and that either interpretation is acceptable if the coverage factor is stated. That undercuts the lesson. A GUM expanded uncertainty, a frequentist confidence interval, and a Bayesian credible interval are related tools, but they are not interchangeable merely because a coverage factor is printed. The chapter should teach the reporting action: name the interval type, coverage factor or probability, distributional assumption, and any prior or model assumptions.

The manufacturer-specification passage at lines 582-598 is too speculative. Some specifications are maximum permissible errors, some are calibration conditions, some are coverage intervals, and many consumer specifications do not expose the coverage basis at all. The text says the implicit coverage factor is often $k=2$ or a rectangular maximum-error distribution. That may be true in specific calibration contexts, but it needs a standards or manufacturer-document source. The safer engineering instruction is to avoid inferring the coverage factor from the plus-minus sign.

The cost-of-precision section at lines 651-657 contains current numerical claims that must be sourced and time-stamped. As of 2026, NIST reports optical clock frequency ratio measurements at or below $3.2\times 10^{-18}$ total fractional uncertainty, and 2024 NIST/JILA work reports an optical lattice clock with $8.1\times10^{-19}$ systematic uncertainty. The chapter's statement that $10^{-18}$ is the boundary of optical-clock research is already stale or at least underspecified. The Kibble-balance claim is worse. NIST's tabletop Kibble balance material says national-metrology-institute 1 kg Kibble balances operate with uncertainties on the order of a few parts in $10^8$, not $10^{-9}$ as a working range. This paragraph cannot ship without citations and "current as of 2026" language.

The Hubble paragraph at lines 691-709 matches the NASA OSBI record in its core mechanism: the reflective null corrector was relied on, a lens was mispositioned by 1.3 mm, auxiliary tests showed clear indications of the problem, and cost and schedule pressure inhibited independent testing. The chapter's claim that the mirror's reported figure uncertainty reflected only the reflective-null-corrector reading is a defensible inference, but it should be phrased as an inference from OSBI's findings unless the report quotes an actual uncertainty-budget document. The registry entry is verified and the chapter cites the primary report. However, the chronic-class list names Volkswagen diesel-defeat without a registry entry or primary citation. Under the reviewer guide, that alone blocks release.

The project mostly matches Q55 and the dossier. The trigonometric and shadow methods are dimensionally correct, with safety and access caveats. The photographic method is not correct as written unless image height and focal length are in the same physical units at the sensor plane. Pixel height needs a sensor scaling or an angular formula. The hand-rule method should require the reader to calibrate their own hand at arm length.

The exercise set contains several technical defects. Exercise 3 states that $u(L)=0.002\,\si{\meter}$ and then asks the reader to compute the standard uncertainty from a maximum-error specification. If $u(L)$ is already standard uncertainty, there is nothing to compute. If $0.002\,\si{\meter}$ is a half-width, the standard uncertainty is $0.002/\sqrt{3}\,\si{\meter}$. The design exercises at lines 1050-1063 confuse standard uncertainty with expanded uncertainty by saying "standard uncertainty" and "at $k=2$" in the same target. The clinical-glucose exercise names ISO 15197 without a bibliography entry and without enough context for a reader who does not have access to the standard.

## D. Pedagogical review

The chapter's promised habit is strong: a reported value travels with an uncertainty, and the uncertainty is propagated through the measurement model. The arc is correct for Volume I.

The execution falls short in three ways. First, the chapter has no formal `estimation` environment. The project and exercise set ask for estimates, but Q20 and the reviewer guide require an estimation block in every chapter, and the block should precede the corresponding calculation. The pendulum worked example is the natural place. Before computing $g$, ask the reader to estimate the relative uncertainty: length at $10^{-3}$, time at about $2.5\times10^{-3}$, doubled through $T^{-2}$, so total relative uncertainty should be around $5\times10^{-3}$. Then the calculation confirms the estimate.

Second, the exercise target is missed. The dossier and `\chapmeta` both say 35 exercises. The chapter contains 33. The distribution across types is otherwise healthy: calculation 6, derivation 5, estimation 5, simulation 4, design 3, diagnosis 4, failure analysis 3, judgment 3. The easiest repair is to add two exercises where the chapter is currently weakest: one on interpreting a real or realistic manufacturer specification without assuming the coverage factor, and one on Monte Carlo convergence or correlated uncertainty.

Third, some exercises are not calibrated to the chapter's prerequisites. Exercise 959 asks for a correction for adjacent-measurement correlation coefficient $\rho$, but the reader has not been given a time-series covariance model. It is a good standard or mastery problem, but it needs scaffolding or a narrower statement. Exercise 1066 asks for a clinical-laboratory comparison and points to ISO 15197 "if available"; that phrase makes the standard optional while the problem depends on it. A serious adult reader should not be sent to a paywalled standard as an optional prop. Either provide the acceptance criterion in the problem or reframe it as "given this excerpted criterion."

The project matches the Q55 ruling closely: household plus analysis, low hazard, smartphone, tape measure, reference height, three independent estimates, explicit error bars, and a 1500-word reflection. It should add safety and access language and give one paragraph of guidance on deriving uncertainties for tangent, ratios, and camera geometry.

The failure section closes the main mechanism well in principle. Hubble is an excellent Volume I case because it is a metrology failure, not just an optics failure. The section needs to stop naming uncited chronic examples and should use Hubble's registry short form more tightly.

The archetype invocation is cleanly introduced as uncertainty, but it reads like a map of later volumes instead of a working pattern the reader can apply immediately. Define the pattern in measurement terms first, then mention later recurrence. The depth standard is right for Volume I; the confidence-interval discussion needs precision, not length.

## E. Citation discipline

The chapter cites five keys: `std:iso-iec-guide98`, `std:jcgm-vim`, `std:jcgm-101`, `web:nist-eshandbook`, and `acc:nasa-hubble-optical-systems-1990`. All five exist in `bibliography/references.bib`. The source tiers are mostly correct: JCGM standards for metrology definitions and propagation, NIST e-Handbook for a t-table and statistical support, and the NASA OSBI report for Hubble.

The primary-source rule for Hubble is met. The NASA OSBI report supports the reflective-null-corrector mechanism, the 1.3 mm spacing error, the auxiliary test warnings, and cost and schedule pressure. The local Hubble registry entry is verified and uses the same primary key. Its empty `secondary_sources` field is a project-level gap if Hubble becomes a full case study, but this chapter's abbreviated use can pass after wording is tightened.

The Volkswagen sentence at lines 724-730 violates the named-accident rule. It names the Volkswagen diesel-defeat case, gives a year, and calls it canonical, but there is no registry entry under `docs/research/accidents/`, no `acc:` citation, no legal or regulatory source, and no secondary analysis. The sentence must be cut, cited and registered, or converted to an unnamed generic example.

The chronic-class list at lines 719-745 is under-sourced as a group. Financial stress tests, emissions test cycles, polling margins of error, manufacturer coverage factors, and regulatory cost-benefit point estimates are empirical and institutional claims. They need sources at the appropriate tiers or must be written as hypothetical patterns. A tertiary explainer would not be enough for Volkswagen or regulatory claims.

The current numerical precision claims at lines 651-657 need primary or institutional sources and inline dates. Optical-clock and Kibble-balance performance claims require "current as of 2026" language and citations to NIST, BIPM, or peer-reviewed papers. The Kibble-balance value appears wrong by roughly an order of magnitude.

The rounding rule at lines 490-503 needs a source, likely NIST SP 811, an ISO style guide, or a project convention. Manufacturer-specification claims at lines 584-598 need standards or example data sheets. Smartphone gyroscope bias and noise at lines 970-974 are empirical product-performance claims and need a source or should be turned into assumed values for the exercise.

## F. Reader-path tagging

Most path tags are defensible. The chapter's spine is random versus systematic error, distributions, propagation, cost, failure, and project. The exercise subsections use path tags consistently.

Two changes are needed. The central-limit theorem section is tagged `standard`, but the chapter invokes the CLT in the core random-error section as the mechanism behind the standard uncertainty of the mean. A core reader should not be told that averaging reduces random uncertainty by $1/\sqrt{n}$ and then have the explanatory section marked optional relative to the core path. Promote the CLT section to `core`, or move a shorter core CLT explanation into section 1 and leave the current section as `standard`.

The mastery box at lines 389-400 is placed correctly as optional judgment material, but it contains claims that the core project depends on if the reader chooses Monte Carlo. Keep the box as mastery only after the core Monte Carlo subsection states the minimum operational rule: specify input distributions, sample jointly for correlations, use a convergence criterion, and report the trial count and coverage interval.

## G. Specific concrete fixes

1. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 20-25.

Current text: "A measurement returns a number. The number's value is half of what the measurement reports. The number's uncertainty is the other half. This chapter teaches the reader to compute both, to combine uncertainties from multiple input quantities, and to recognise the recurring failure mode in which the uncertainty figure is chosen for reasons other than the data."

Proposed replacement: "A measurement returns a value and an uncertainty. The value says where the measurement lands; the uncertainty says how wide the defensible interval is. This chapter makes the second quantity operational: we compute it, propagate it through measurement models, and reject uncertainty figures selected for institutional convenience rather than derived from evidence."

2. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 37-43.

Current text: "Random error is reduced by averaging. If a quantity is measured $n$ times under the same conditions and the random component is independent across measurements, the standard uncertainty of the mean is the sample standard deviation divided by $\sqrt{n}$. The mechanism is the central limit theorem (section 4.4); the operational consequence is that more data, taken under controlled conditions, makes the random component smaller."

Proposed replacement: "Independent random error is reduced by averaging. If a quantity is measured $n$ times under repeatability conditions and the random component is independent across measurements, the standard uncertainty of the mean is the sample standard deviation divided by $\sqrt{n}$. The central-limit-theorem argument is taken up below; the operational consequence is narrower than the slogan: more data reduces only the independent random component."

3. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 87-99.

Current text: "\engterm{Type A evaluation} estimates uncertainty from the statistical analysis of repeated measurements. It is the natural home of the random component: if the random error is $\sigma$ in any single measurement, the standard uncertainty of the mean of $n$ measurements is $\sigma / \sqrt{n}$, computed from the sample standard deviation. \engterm{Type B evaluation} estimates uncertainty from non-statistical information: instrument specifications, calibration certificates, manufacturer data, documented experience, and physical models. It is the natural home of the systematic component: a calibration offset estimated from a certificate is a Type B contribution, even though the underlying error is systematic in character."

Proposed replacement: "\engterm{Type A evaluation} estimates uncertainty by statistical analysis of observed data, usually repeated measurements. If the independent random component has standard deviation $\sigma$ in a single measurement, the standard uncertainty of the mean of $n$ measurements is estimated as $s/\sqrt{n}$. \engterm{Type B evaluation} estimates uncertainty from other information: instrument specifications, calibration certificates, manufacturer data, documented experience, previous measurements, and physical models. A calibration correction taken from a certificate is commonly a Type B contribution, even when the effect being corrected is a systematic bias."

4. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 101-107.

Current text: "The distinction between Type A and Type B is in the method of evaluation, not in the random-versus-systematic character of the underlying error. A systematic error can be evaluated by Type A methods if the experimentalist has access to repeated measurements under conditions that vary the systematic mechanism; a random error can be evaluated by Type B methods if the experimentalist has documented prior data and accepts a model."

Proposed replacement: "The distinction between Type A and Type B is the method of evaluation, not the random-versus-systematic character of the effect. A bias can be estimated by Type A methods when repeated calibration data, intercomparisons, or controlled condition changes expose it statistically. A random contribution can enter a Type B evaluation when previous data, a specification, or a physical model gives the standard uncertainty without a new repeated-measurement campaign."

5. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 109-121.

Current text: the full archetype paragraph beginning "The uncertainty archetype, named in the volume opener..." and ending "this chapter."

Proposed replacement: "Uncertainty is the engineering habit of carrying a second quantity beside the reported value. The value says where the measurement lands; the uncertainty says how wide the defensible landing zone is. Later chapters attach the same habit to structural loads, temperatures, material properties, reliability estimates, and failure rates. In this chapter the pattern becomes formal: a number reported without its uncertainty is not yet a usable measurement."

6. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 162-170.

Current text: "Its mean is $(a + b)/2$ and its standard deviation is $(b - a)/(2\sqrt{3})$. The uniform distribution is appropriate when the underlying mechanism produces an error bounded above and below, with no preference for any value within the bounds. Quantisation error in a digital instrument (the last bit fluctuates between two adjacent quantisation steps) is uniformly distributed on the step interval. A specification that gives a maximum and minimum without a most-likely value, by GUM convention, is treated as a uniform distribution between those bounds \cite{std:iso-iec-guide98}."

Proposed replacement: "Its mean is $(a + b)/2$ and its standard deviation is $(b - a)/(2\sqrt{3})$. The uniform distribution is appropriate when the error is bounded above and below and the available information gives no preference for any value within the bounds. Quantisation error is often modelled as uniform over one quantisation interval when the input is not locked to the quantiser and sufficient variation or dithering is present. A specification that gives a maximum and minimum without a most-likely value is commonly treated, under the GUM's rectangular-distribution convention, as uniform between those bounds \cite{std:iso-iec-guide98}."

7. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 179-195.

Current text: the item list of lognormal, half-normal, Weibull, and Poisson patterns.

Proposed replacement: keep the list, but add a citation-bearing lead sentence before it: "The following examples are standard statistical models, not automatic assignments. The measurement report should name the mechanism or cite the convention that justifies the distribution." Add a statistics or reliability reference to `bibliography/references.bib` and cite it at the end of the lead sentence.

8. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 204-212.

Current text: "A small number of distributions have tails heavy enough that the central limit theorem does not apply. The Cauchy distribution is the canonical example: it has no finite mean and no finite variance, and the sum of independent Cauchy variables is itself Cauchy. A measurement whose underlying error is Cauchy-like cannot be improved by averaging. Heavy-tailed errors are rare in physical measurement but occur in some financial, network-traffic, and extreme-event contexts. The reader who encounters them should not treat them with Gaussian tools without verification."

Proposed replacement: "Some distributions have tails heavy enough that the ordinary finite-variance central limit theorem does not apply. The Cauchy distribution is the clean example: it has no finite mean and no finite variance, and the average of independent Cauchy variables remains Cauchy-distributed. A measurement model with Cauchy-like error is not repaired by taking more ordinary averages. The practical rule is simple: before applying Gaussian tools, check that the variance is finite and that the observed tails are compatible with the model."

9. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 241-245.

Current text: "The partial derivatives are evaluated at the input quantities' mean values. The formula is a linear (first-order) approximation: it assumes that $f$ is approximately linear over the range of the input uncertainties. For most engineering measurements with small input uncertainties, the approximation is excellent."

Proposed replacement: "The partial derivatives are evaluated at the input estimates. The formula is a first-order Taylor approximation: it assumes that $f$ is close to linear over the range of input values that carry material probability. For small relative uncertainties and smooth models, the approximation is often good; the next subsection names the cases where it is not."

10. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 280-286.

Current text: "For $y = a x_{1}^{p_{1}} x_{2}^{p_{2}} \cdots$, the relative uncertainty satisfies [formula]."

Proposed replacement: "For $y = a x_{1}^{p_{1}} x_{2}^{p_{2}} \cdots$ with uncorrelated inputs and small relative uncertainties, the relative uncertainty satisfies [same formula]. If the inputs are correlated, covariance terms must be added; the simple quadrature rule no longer applies."

11. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 292-304.

Current text: the subsection beginning "\engterm{Correlated sum: the cancellation case}" and ending "comparator measurements in metrology depend on it."

Proposed replacement: "\engterm{Correlated difference: common-mode cancellation}. For $y=x_1-x_2$ with correlation coefficient $\rho$,
\[
u_c^2(y)=u^2(x_1)+u^2(x_2)-2\rho u(x_1)u(x_2).
\]
When $\rho=+1$ and $u(x_1)=u(x_2)$, the common uncertainty component cancels. Difference measurements exploit this: subtracting two readings from the same drifting instrument can reject the shared drift while preserving the change between the readings. Comparator measurements in metrology are built around this common-mode cancellation."

12. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, before line 306.

Current text: no estimation environment precedes the pendulum worked example.

Proposed replacement: insert before `\subsection{Worked example: pendulum period gives $g$}`:
"\begin{estimation}
Before calculating, estimate which input will dominate the uncertainty in $g=4\pi^2L/T^2$. The length uncertainty is about $10^{-3}$ relative. The time uncertainty is about $0.005/2\approx2.5\times10^{-3}$ relative, and the exponent $-2$ doubles that contribution before quadrature. We should expect a combined relative uncertainty near $5\times10^{-3}$, so a $g$ value near $10\,\si{\meter\per\second\squared}$ should carry a standard uncertainty near $0.05\,\si{\meter\per\second\squared}$.
\end{estimation}"

13. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 349-354.

Current text: "Large input uncertainties such that the first-order Taylor expansion does not capture the dominant behaviour. The threshold is roughly that $u(x_{i})$ is large enough that $f(x_{i} + u)$ differs from $f(x_{i}) + (\partial f / \partial x_{i}) u$ by an amount comparable to the linear-propagation estimate."

Proposed replacement: "Large input uncertainties such that first-order Taylor terms no longer dominate the neglected second-order terms. A practical check is to compare the model evaluated at plausible high and low input values with the tangent-line prediction; if the residual is comparable to the propagated standard uncertainty, linear propagation is no longer the right tool."

14. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 375-376.

Current text: "Repeat steps 2--3 for $M$ trials, typically $M \geq 10^{5}$ for engineering uncertainty estimation."

Proposed replacement: "Repeat steps 2--3 for $M$ trials. Choose $M$ from a convergence or numerical-tolerance criterion; for simple models, $10^{5}$ to $10^{6}$ trials are common starting values, but the report should state the criterion actually used."

15. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 390-399.

Current text: the mastery paragraph beginning "The choice between linear propagation and Monte Carlo..." and ending "Monte Carlo is increasingly the standard."

Proposed replacement: "The choice between linear propagation and Monte Carlo is an engineering judgment. Linear propagation is fast, exposes the dominant sensitivity coefficient, and is easy to document. Monte Carlo is better when the input distributions and model are specified but the output distribution is nonlinear, asymmetric, truncated, or censored. The method still has sampling error, so the report must state the trial count or convergence criterion. For safety-critical work, the method is chosen from the uncertainty model and the decision consequence, not from fashion."

16. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, line 402.

Current text: "\section{The central limit theorem in practice}\pathtag{standard}"

Proposed replacement: "\section{The central limit theorem in practice}\pathtag{core}"

17. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 404-408.

Current text: "The central limit theorem (CLT) states that the sum (or mean) of a large number of independent random variables tends to a Gaussian distribution, regardless of the distribution of the individual variables, provided that the individual distributions have finite variance and that no single variable dominates the sum."

Proposed replacement: "The central limit theorem (CLT) states that, under regularity conditions, the sum or mean of many independent random variables tends toward a Gaussian distribution after centering and scaling. The working conditions are finite variance and no dominating contribution; the Lyapunov or Lindeberg forms make that last condition precise."

18. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 443-457.

Current text: the paragraph beginning "The CLT is an asymptotic result..." and ending "the $t$-correction is meaningful."

Proposed replacement: "The CLT is an asymptotic result. For finite samples, the sample mean may be approximately Gaussian, but the uncertainty of that mean is usually estimated from the same data. When the parent population is Gaussian and the population standard deviation is unknown, the standardized statistic built from the sample mean and sample standard deviation follows Student's $t$-distribution with $n-1$ degrees of freedom. For $n \geq 30$, the $t$ critical values are close to Gaussian critical values for many routine intervals; for $n<30$, and especially for $n<10$, the correction is large enough to matter."

19. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 490-503.

Current text: the rounding subsection from "The standard rounding rule..." through "one is used otherwise."

Proposed replacement: "One common reporting rule is round-half-to-even: when the discarded digit is exactly $5$ with no further nonzero digits, round to the nearest even digit. Use this rule when the applicable standard, laboratory procedure, or software environment specifies it; otherwise state the rounding convention. A separate convention applies to uncertainties: report an uncertainty with one significant figure, or with two when the leading digit is $1$ or $2$ or when the second digit changes the decision. Thus $0.05246\,\si{\volt}$ would usually become $0.05\,\si{\volt}$; $0.0146\,\si{\volt}$ would usually become $0.015\,\si{\volt}$."

20. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 552-558.

Current text: "For most engineering work, the distinction is academic. The intervals computed by either framework agree when the prior is non-informative and the data dominate. The reader who needs the distinction (in a regulatory submission, a legal proceeding, or a careful research paper) should use the framework's terminology explicitly. The reader who is reporting a working measurement can use either interpretation, provided the coverage factor is stated."

Proposed replacement: "For routine laboratory reporting, the practical action is to name the interval type and its assumptions. A GUM expanded uncertainty is reported with its standard uncertainty, coverage factor, effective degrees of freedom where relevant, and distributional assumption. A Bayesian credible interval is reported with its prior and likelihood model. The reader should not translate one statement into the other silently."

21. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 578-580.

Current text: "A reported expanded uncertainty without a stated coverage factor is ambiguous. The reader should assume $k = 2$ as a default, but the discipline is to state $k$ explicitly."

Proposed replacement: "A reported expanded uncertainty without a stated coverage factor is ambiguous. The reader should not infer $k$ from the plus-minus sign; ask for the coverage factor, coverage probability, and distributional basis, or treat the report as incomplete."

22. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 584-598.

Current text: the manufacturer accuracy subsection.

Proposed replacement: "A manufacturer's accuracy specification may be a maximum permissible error, a calibration-condition claim, a coverage interval, or a shorthand tied to a particular standard. The plus-minus sign alone does not identify a standard uncertainty. A reader who uses a specification in an uncertainty budget should record the assumption explicitly: rectangular half-width, Gaussian expanded uncertainty with stated $k$, or another distribution justified by the data sheet or calibration certificate. Treating a maximum-error specification as a standard uncertainty can understate the uncertainty by a large factor."

23. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 651-657.

Current text: "Frequency measurements at fractional uncertainty $10^{-16}$ are achievable in a national metrology laboratory; frequency measurements at $10^{-18}$ are at the boundary of what optical-clock research has achieved. Mass measurements at $10^{-9}$ relative are in the working range of Kibble-balance facilities; mass measurements at $10^{-10}$ are at the boundary."

Proposed replacement: "Frequency measurements at fractional uncertainty around $10^{-16}$ are routine for national time and frequency laboratories, while optical-clock comparisons have reached the low $10^{-18}$ range and selected optical-clock systematic uncertainties below $10^{-18}$, current as of 2026 \cite{ADD_NIST_OPTICAL_CLOCK_KEY}. Kilogram realisations by 1 kg Kibble balances at national metrology institutes are typically reported at uncertainties on the order of a few parts in $10^8$, not $10^{-9}$ as a routine working value, current as of 2026 \cite{ADD_NIST_KIBBLE_KEY}. A reader specifying a measurement should know which side of the current metrology frontier the requirement occupies."

24. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 680-687.

Current text: "Every chapter has a failure section. This chapter's failure mode is the recurring case in which an uncertainty figure is reported smaller than the underlying data supports because of commercial, regulatory, legal, or political pressure. The pattern is harder to detect than a missing measurement (chapter 1) or a unit error (chapter 2): the report contains numbers, the numbers look defensible, but the uncertainty figure has been chosen rather than computed."

Proposed replacement: "The failure mode here is quieter than a missing measurement or a unit error. The report contains numbers, the numbers look defensible, and the uncertainty figure is smaller than the evidence permits because schedule, money, legal exposure, or institutional pressure has entered the uncertainty budget."

25. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 691-709.

Current text: the Hubble auxiliary-test override subsection.

Proposed replacement: "The Hubble Space Telescope launched in April 1990 with a primary mirror figured to the wrong shape. The NASA Optical Systems Board of Investigation traced the failure to the reflective null corrector used during polishing: a field lens was mispositioned by about $1.3\,\si{\milli\meter}$ along the optical axis, and the resulting mirror figure error was about $2\,\si{\micro\meter}$ at the outer edge \cite{acc:nasa-hubble-optical-systems-1990}. Auxiliary optical tests, including an inverse null corrector and a second null corrector, showed clear indications of the problem, but the fabrication process treated the reflective null corrector as authoritative.

For this chapter, the uncertainty lesson is the treatment of disagreement. A measurement system with independent cross-checks that disagree should not report an uncertainty based only on the preferred instrument. The report should either widen the uncertainty to account for the disagreement or document why the auxiliary tests are inapplicable. The OSBI record supports the narrower statement that Hubble's process discounted the auxiliary evidence under cost and schedule pressure; it does not by itself give us a complete published uncertainty budget for the mirror."

26. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 719-745.

Current text: the chronic-class item list naming stress tests, Volkswagen, polling, manufacturer specs, and regulatory cost-benefit analyses.

Proposed replacement: either add primary and secondary citations for each named institutional class, including a Volkswagen accident registry entry and an `acc:` or `law:` key, or replace the list with generic hypotheticals. Minimal replacement: "The same pattern appears in weaker forms whenever the reporting process can benefit from a smaller interval: a test scenario selected to preserve a passing result, a specification quoted without its coverage basis, a sampling margin reported as if it included non-response bias, or a cost estimate collapsed from a range to a single favorable point. Each example requires the same audit question: what data and model produced the interval?"

27. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 755-765.

Current text: the principle box "Uncertainty derives from data, not preference."

Proposed replacement: keep the principle, but change the final sentence to: "A reported uncertainty without a documented derivation is an incomplete measurement result; the engineering action is to request the uncertainty budget before using the number in a decision."

28. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 810-815.

Current text: "From a known distance $d$, take a photograph of the building with a camera of known focal length $f$ and known sensor or image height. Measure the building's image height in pixels (or millimetres on the sensor). Compute $h = d \cdot (\text{image height}) / f$, with appropriate sensor scaling. Propagate uncertainties."

Proposed replacement: "From a known distance $d$, take a photograph of the building with a known focal length and a known mapping from pixels to sensor length. Convert the measured pixel height to a sensor-plane height $s_{\text{image}}$ in the same length units as the focal length $f$. For small angles and a camera aimed approximately perpendicular to the building face, use $h \approx d\,s_{\text{image}}/f$; otherwise compute the angular height from the camera geometry and use the trigonometric method. Propagate uncertainties from $d$, pixel measurement, focal length, sensor scaling, and camera alignment."

29. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 816-821.

Current text: "Hand-rule method. Stand at a distance where the building's apparent angular size matches a known angular reference (an outstretched fist subtends approximately $10$ degrees, an outstretched thumb approximately $2$ degrees). Measure the distance, compute the height. Propagate the larger angular uncertainty (the hand-rule is coarse)."

Proposed replacement: "Hand-rule method. First calibrate the reader's own hand rule: measure arm length and the width of the fist or thumb to compute its angular width. Stand at a safe measured distance where the building's apparent angular size can be compared with that calibrated angle. Compute the height from the angle and distance, and propagate the larger angular uncertainty explicitly."

30. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 894-899.

Current text: "A length is measured as $L = 1.250 \,\si{\meter}$ with $u(L) = 0.002 \,\si{\meter}$ (uniform distribution from a maximum-error specification). Compute the standard uncertainty as the standard deviation of the corresponding uniform distribution."

Proposed replacement: "A length is measured as $L = 1.250 \,\si{\meter}$ with a maximum-error specification of $\pm 0.002\,\si{\meter}$ and no stated distribution. Treat the error as uniformly distributed on $[-0.002,0.002]\,\si{\meter}$ and compute the standard uncertainty."

31. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 959-965.

Current text: "Show that the standard uncertainty of the mean of $n$ independent measurements, each with standard uncertainty $\sigma$, is $\sigma / \sqrt{n}$. State the assumption that fails when the measurements are positively correlated, and derive the correction for correlation coefficient $\rho$ between adjacent measurements."

Proposed replacement: "Show that the standard uncertainty of the mean of $n$ independent measurements, each with standard uncertainty $\sigma$, is $\sigma/\sqrt{n}$. Then consider the simpler correlated case in which every pair of measurements has the same correlation coefficient $\rho$. Derive the standard uncertainty of the mean and state why positive correlation reduces the benefit of averaging."

32. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 969-974.

Current text: "Estimate the standard uncertainty of a smartphone clinometer's elevation angle reading, given that smartphone gyroscopes typically have bias of order $10^{-3} \,\si{\radian}$ and noise of order $10^{-4} \,\si{\radian}$. State your assumed instrument characteristics and comment on which dominates."

Proposed replacement: "Estimate the standard uncertainty of a smartphone clinometer's elevation angle reading using assumed values supplied in the problem: bias of order $10^{-3}\,\si{\radian}$ after calibration and short-term noise of order $10^{-4}\,\si{\radian}$. State whether your result is controlled by bias or random noise, and name the measurement you would perform to replace these assumed values with data."

33. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 1050-1054.

Current text: "Design a measurement plan to determine the average mass of an object in a population of $100$ nominally identical units to a standard uncertainty of $\pm 0.5 \,\si{\gram}$ at $k = 2$. State the instrument's required accuracy, the number of measurements per unit, and the procedure for handling between-unit variability."

Proposed replacement: "Design a measurement plan to determine the average mass of an object in a population of $100$ nominally identical units with an expanded uncertainty of $U=0.5\,\si{\gram}$ at $k=2$. State the required standard uncertainty of the mean, the instrument accuracy or calibration uncertainty, the number of units sampled, the number of measurements per sampled unit, and the procedure for separating between-unit variability from measurement repeatability."

34. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 1057-1063.

Current text: "Design an uncertainty budget for a household refrigerator temperature measurement, with target $\pm 0.5 \,\si{\degreeCelsius}$ at $k = 2$. List each input source (thermometer accuracy, sampling location, time-of-day variation, defrost cycle, door-opening) with an estimated standard uncertainty contribution. Identify which component dominates."

Proposed replacement: "Design an uncertainty budget for a household refrigerator temperature measurement with target expanded uncertainty $U=0.5\,\si{\degreeCelsius}$ at $k=2$. List each input source, including thermometer calibration, sensor resolution, sampling location, time-of-day variation, defrost cycle, and door opening, with an estimated standard uncertainty contribution. Combine the contributions and identify which component dominates."

35. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, lines 1066-1072.

Current text: "Design a comparison protocol for a clinical-laboratory measurement of blood glucose by two methods. State how the laboratory would establish whether the two methods agree within their combined uncertainty, and what to do when they disagree. Consult ISO 15197 or an equivalent clinical-glucose standard if available."

Proposed replacement: "Design a comparison protocol for a clinical-laboratory measurement of blood glucose by two methods. Given an acceptance criterion supplied by the problem statement, state how the laboratory would establish whether the two methods agree within their combined uncertainty, and what investigation follows when they disagree. Do not require ISO 15197 unless the chapter adds a `std:` bibliography entry and quotes the relevant criterion."

36. File: `volumes/01-quantity/ch04-error-and-uncertainty/chapter.tex`, after line 1156.

Current text: the exercise set ends with 33 exercises against a target of 35.

Proposed replacement: add two exercises. First: "A data sheet states `accuracy: $\pm 0.8\%$ of reading` with no coverage factor and no distribution. Write the uncertainty-budget entry three ways: as a rectangular half-width, as a $k=2$ Gaussian expanded uncertainty, and as an unresolved specification requiring manufacturer clarification. Compare the resulting standard uncertainties." Second: "Run a Monte Carlo propagation for $y=x_1-x_2$ with equal standard uncertainties and correlations $\rho=0$, $0.5$, $0.9$, and $0.99$. Compare the empirical standard deviation with the correlated-difference formula and explain why common-mode cancellation depends on positive correlation."

## H. Structural risks for the larger project

1. Named-case detection is too weak. `make accidents` passes because it scans cited `acc:` keys, but this chapter names Volkswagen without an `acc:` citation. The release checklist needs a named-entity scan for accident names in prose, exercises, captions, and `\chapmeta`, then a registry check even when no accident citation is present.

2. Exercise targets are not mechanically enforced. The dossier and `\chapmeta` say 35 exercises; the chapter has 33. Prior reviews already found exercise-count drift. A simple structural check should compare `Exercise target:` against the number of `\begin{exercise}` blocks before a chapter reaches review.

3. The dossier schema is too thin for technical review. This chapter's dossier gives eight section titles, an archetype, a project sentence, and an exercise count. It does not name required standards, primary sources, numerical claims that need dated sourcing, expected estimation blocks, or known traps such as confidence-interval interpretation. The next dossier pass should add a "verification anchors" field: standards, primary reports, numerical figures requiring current-as-of dates, named cases, and exercises that must exist for the chapter to satisfy Q16 and Q20.
