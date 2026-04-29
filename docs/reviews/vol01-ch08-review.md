# Vol 01 Ch 08 Review

**Resolved: 2026-04-29.** All G1-G42 fixes and voice items B1-B13 applied to `volumes/01-quantity/ch08-statistics-for-engineers/chapter.tex`. Pre-flight: introduced a new `method:` citation prefix in `docs/citation-policy.md` for research-methods literature (replication, p-hacking, HARKing, forking paths) and added five new bibliography entries: `method:simmons-nelson-simonsohn-2011`, `method:kerr-harking-1998`, `method:gelman-loken-forking-paths`, `method:open-science-collaboration-2015`, `method:errington-cancer-biology-2021`. The two technical blockers are corrected: the commute summary statistics now read $\bar{x} = 28.73 \,\text{min}$, $s = 1.98 \,\text{min}$, $Q_{1} = 27.25$, $Q_{3} = 29.75$, $\text{IQR} = 2.50 \,\text{min}$ with the linear percentile convention named, and the downstream confidence and prediction intervals are recomputed ($28.73 \pm 0.74 \,\text{min}$ and $28.73 \pm 4.11 \,\text{min}$ at $95\,\%$); the sample-size estimation block now leads with the $1\,\%$ case ($n \approx 16$ per line) and explicitly refuses to license $n < 2$ for a two-sample t-test in the $10\,\%$ regime, naming a practical minimum. The replication-crisis prose now cites the 2015 Reproducibility Project: Psychology and the 2021 Reproducibility Project: Cancer Biology with their actual numbers; p-hacking, HARKing, and the garden of forking paths each carry a primary methods citation. The Bayesian re-test scenario is now phrased as conditionally-independent given true defect status. The CI/PI t-critical notation switches from $t_{\alpha/2,n-1}$ to $t_{1-\alpha/2,n-1}$. The frequentist phrasing "the reader is $95\,\%$ confident" is replaced with "the procedure has $95\,\%$ long-run coverage." The project's pre-registration items now offer a core path (fixed $n = 30$, qualitative power reflection) alongside the standard path (computed $n$, effect-size confidence interval). The A/B and Weibull design exercises are rewritten with admissible parameters; the Weibull-test exercise is marked mastery unless the chapter adds reliability-test machinery. Verbal voice items (self-announcing topic sentences, the negate-first-then-pivot p-value list, "fraud" replaced with "misleading confirmatory claim," "the chapter has now built the framework" replaced with the working transition) all applied. Build verified: `make distclean && make strict` produces a 696-page `main.pdf`; `make check`, `make audit-docs`, `make accidents`, and `make exercise-counts` all PASS.

Build-facing note: Chapter 8 has no chapter-local unresolved citation or cross-reference in the checks we ran. `make check`, `make accidents`, `make exercise-counts`, and `make strict` completed without a Chapter 8 build failure.

Scope checked: `docs/editorial-decisions.md`, `docs/voice.md`, `docs/citation-policy.md`, `docs/reviewer-guide.md`, `docs/case-study-template.md`, `docs/research/landscape.md`, `docs/research/01-quantity/ch08-statistics-for-engineers.md`, `volumes/01-quantity/_volume.tex`, `volumes/01-quantity/ch08-statistics-for-engineers/chapter.tex`, `volumes/01-quantity/ch08-statistics-for-engineers/notes-for-editor.md`, and the cited BibLaTeX entries `text:wasserman2004`, `text:devore2015`, and `web:nist-eshandbook`. We also checked external sources for claims that the chapter makes but does not cite: [NIST/SEMATECH e-Handbook](https://www.itl.nist.gov/div898/handbook/), [Open Science Collaboration 2015](https://doi.org/10.1126/science.aac4716), [Simmons, Nelson, and Simonsohn 2011](https://doi.org/10.1177/0956797611417632), [Kerr 1998](https://doi.org/10.1207/s15327957pspr0203_4), and [Errington et al. 2021](https://doi.org/10.7554/eLife.71601).

## A. Verdicts

Technical: blocked. The commute worked example has wrong mean, standard deviation, quartiles, and downstream intervals. The sample-size estimation block tells the reader that one sample per group can be enough for a two-sample test, which is not an admissible use of the rule of thumb.

Pedagogical: approved-with-corrections. The chapter builds the right habit, but the project requires power analysis while the power section is tagged standard, several exercises require machinery not taught in the chapter, and the failure section is too generic to close the argument.

Voice: approved-with-corrections. The prose is mostly direct, but it has several self-announcing topic sentences, a banned "not X" cluster around the p-value explanation, and a few moralized or overbroad sentences that should be made concrete.

## B. Voice Review

The chapter is in the house register more often than not. It avoids em dashes, avoids rhetorical questions, and mostly keeps the reader in the work. The problems below are local.

1. `volumes/01-quantity/ch08-statistics-for-engineers/chapter.tex:22-25`

Offending sentence: "This chapter makes the second and third operational: we summarise data, fit it to distributions, draw inferences from samples to populations, and refuse the analytical practices that turn engineering reports into press releases."

Rule violated: `docs/voice.md`, "Self-announcing topic sentences." The sentence announces the chapter's route.

Rewrite: "A statistical report earns trust when it states the data summary, the distributional model, the inference, and the analytical practices it refused."

2. `chapter.tex:54-56`

Offending sentence: "Its strength is robustness: half the sample can be replaced by extreme values and the median does not move."

Rule violated: `docs/voice.md`, "AI-tic vocabulary" flags `robust` when it is filler. Here the term is technical, but the sentence also overstates the finite-sample claim.

Rewrite: "Its strength is resistance to outliers: fewer than half the sample can be moved to extreme values before the median is forced to follow."

3. `chapter.tex:110-112`

Offending sentence: "Whether an outlier is contamination, a real tail observation, or a rare event is a domain judgement, not a statistical one."

Rule violated: `docs/voice.md`, "Negate-first-then-pivot construction."

Rewrite: "Statistics can flag the point; domain knowledge decides whether it is contamination, a real tail observation, or a rare event."

4. `chapter.tex:186-189`

Offending sentence: "Five distributions cover most of what an engineer will fit."

Rule violated: `docs/voice.md`, "No invented scenes or figures" and "Not hyped." "Most" is unsupported and field-dependent.

Rewrite: "Five distributions are common enough that the reader should recognize their mechanisms before fitting data."

5. `chapter.tex:237-240`

Offending sentence: "The parameters $\mu$ and $\sigma$ here are the mean and standard deviation of $\ln X$, not of $X$ itself."

Rule violated: `docs/voice.md`, "Negate-first-then-pivot construction."

Rewrite: "In this distribution, $\mu$ and $\sigma$ describe $\ln X$; the mean of $X$ is $e^{\mu + \sigma^{2}/2}$ and the median of $X$ is $e^{\mu}$."

6. `chapter.tex:474-478`

Offending sentence: "It is not the probability that $H_{0}$ is true. It is not the probability that the result would replicate. It is not the size of the effect. It is not the importance of the result."

Rule violated: `docs/voice.md`, "Negate-first-then-pivot construction." The list is pedagogically useful, but the house rule asks us to state the positive form.

Rewrite: "It answers one narrow question: how often a null-model process would produce a test statistic at least this extreme. It leaves the truth of $H_{0}$, replication probability, effect size, and engineering importance to other evidence."

7. `chapter.tex:687-694`

Offending sentence: "The headline: a $95 \,\%$-sensitive, $98 \,\%$-specific test, applied to a population with $1 \,\%$ defect rate, returns a positive that is wrong about two thirds of the time."

Rule violated: `docs/voice.md`, "Not hyped." "The headline" is a journalistic cue.

Rewrite: "The result is direct: with a $1 \,\%$ defect prior, this $95 \,\%$-sensitive and $98 \,\%$-specific test returns false alarms for about two thirds of positive results."

8. `chapter.tex:740-742`

Offending sentence: "An engineer who is unsure of a Bayesian calculation drops to the table; the table does not lie."

Rule violated: `docs/voice.md`, "Not hyped." The second clause is a slogan.

Rewrite: "An engineer who is unsure of a Bayesian calculation should write the contingency table and check every count."

9. `chapter.tex:878-880`

Offending sentence: "A more interesting case: detect a $1 \,\%$ mean difference with the same $\sigma$."

Rule violated: `docs/voice.md`, "Not hyped." "Interesting" is filler.

Rewrite: "A more useful case is a $1 \,\%$ mean difference with the same $\sigma$."

10. `chapter.tex:932-934`

Offending sentence: "The chapter has now built the framework. We turn to its abuses, which are subtle, common, and disqualifying when discovered."

Rule violated: `docs/voice.md`, "Meta-explanation tails." It announces transition rather than naming the work.

Rewrite: "The same framework fails when the analysis plan is chosen after the data are visible."

11. `chapter.tex:943-944`

Offending sentence: "Reporting that one without disclosing the other nineteen is fraud."

Rule violated: `docs/voice.md`, "Confident" does not mean legally or morally inflated. Fraud requires intent and jurisdictional context.

Rewrite: "Reporting that one without disclosing the other nineteen is a misleading confirmatory claim."

12. `chapter.tex:1059-1061`

Offending sentence: "The pattern, current as of 2026, has appeared in multiple disciplines and is the dominant statistical failure mode of the past two decades."

Rule violated: `docs/voice.md`, "Not hyped" and "No invented scenes or figures." "Dominant" is uncited and too broad.

Rewrite: "The pattern, current as of 2026, has appeared in multiple disciplines and is one of the major statistical failure modes a working engineer must recognize."

13. `chapter.tex:1286-1290`

Offending sentence: "The exercises train calculation, derivation, estimation, simulation, design, diagnosis, failure analysis, and judgment. Calculation and derivation problems have full solutions; open-ended problems have rubrics or reference write-ups. Exercises are tagged with their reader-path tier."

Rule violated: `docs/voice.md`, "Self-announcing topic sentences." It also promises solutions and rubrics that are not present beside the chapter.

Rewrite: "The exercises test calculation, derivation, estimation, simulation, design, diagnosis, failure analysis, and judgment. The editor should attach the solution and rubric file before release."

## C. Technical Review

The chapter's broad mathematical spine is sound: sample mean, sample variance, Gaussian density, log-normal density, Weibull survival, Poisson probability mass, exponential density, one-sample and Welch two-sample test statistics, chi-square statistic, confidence interval for a mean, prediction interval for a new Gaussian observation, Bayes' rule, and the two-sample sample-size rule of thumb are dimensionally and algebraically coherent. The chapter also makes the right engineering distinction between statistical significance and engineering relevance.

The blocked defects are specific.

The worked commute dataset at lines 139-166 does not match its reported summaries. For the 30 values printed, the mean is $28.733 \,\text{min}$, not $28.6 \,\text{min}$. The sample standard deviation is about $1.98 \,\text{min}$, not $1.9 \,\text{min}$. Quartiles depend on convention, but the chapter gives no convention and prints $Q_1 = 27$ and $Q_3 = 29.75$, a mixed result. A common linear percentile convention gives $Q_1 = 27.25$ and $Q_3 = 29.75$; Tukey hinges give $Q_1 = 27$ and $Q_3 = 30$. The confidence and prediction intervals later reuse the wrong mean and standard deviation. This is an embarrassing error in a statistics chapter.

The median breakdown sentence is overstated. Fewer than half the observations can be contaminated before the median is forced to move arbitrarily. At exactly half, especially in an even sample, the median can move. The IQR sentence also says it is resistant to outliers "in the same way" as the median. It is not the same; quartiles have different breakdown behavior and can move when the relevant quarter of the data is contaminated.

The distribution section needs more precision around densities. A continuous density does not give the probability of "each value"; exact point probability is zero. The text should say that the density assigns probability to intervals through area under the curve.

The log-normal examples include "financial returns compounded over time." Returns can be negative and are not generally log-normal; asset prices or positive multiplicative growth factors are the usual log-normal examples. The chapter should either remove finance or say "prices under a simple multiplicative model."

The Poisson earthquake example is dangerous as written. Earthquake counts can be clustered by aftershock sequences and nonstationary tectonic conditions. The example can stay only if it says "under a restricted background-rate model" or uses radiation counts and defect counts instead.

The variance-to-mean diagnostic band of $0.8$ to $1.2$ at lines 301-308 is not generally valid without sample size, uncertainty on the dispersion statistic, and process context. It reads like a rule with no provenance. Use it as a rough screening heuristic or remove the numeric band.

The goodness-of-fit paragraph omits a technical trap. If parameters are fitted from the same data, the null distribution of common tests changes. The Kolmogorov-Smirnov test in particular needs adjusted critical values or simulation when parameters are estimated. The chi-square test also needs adequate expected counts and defined bins. NIST can support the catalogue, but the caveat belongs in the chapter.

The alpha guidance is too simple. A safety-critical decision does not automatically use a smaller $\alpha$. The correct choice depends on how the null is framed and on the relative costs of false acceptance and false rejection. For example, a test framed as "the design is safe" has a different error allocation from one framed as "the design is unsafe." The chapter should teach cost-of-error framing, not "safety means smaller alpha."

The p-value section is conceptually right but should add the role of the alternative hypothesis. "At least as extreme" means extreme under the test statistic and the specified one-sided or two-sided alternative.

The interval notation should change from $t_{\alpha/2,n-1}$ to a clear positive critical value such as $t_{1-\alpha/2,n-1}$ or $t^\star_{\alpha,n-1}$. As written, many statistical conventions would interpret $t_{\alpha/2}$ as a lower-tail negative value.

The sentence "The reader is $95 \,\%$ confident" conflicts with the frequentist definition the chapter just gave. The better sentence is procedural: "This interval comes from a procedure with $95 \,\%$ long-run coverage."

The operational meeting example at lines 640-644 does not follow from the numbers. The interval around tomorrow's commute is the prediction interval. The confidence interval about the long-run mean cannot plan a single arrival. The phrase "within fifteen minutes of the average" is so wide relative to the dataset that it does not clarify the error.

The Bayesian double-positive example assumes the second test is independent. A repeat of the same test on the same unit often shares specimen, calibration, operator, and threshold errors. The chapter should state that the $96 \,\%$ posterior requires conditional independence given true defect status. Otherwise it teaches a false sense of certainty.

The sample-size estimation block is the second blocker. The rule $n \approx 16\sigma^2/\delta^2$ is an approximation for planning equal-size two-sample tests, not a license to use $n < 2$ per group or to estimate a variance from one item. The example's $10 \,\%$ fill-weight difference gives $n = 0.16$, then says one sample per line is enough. A two-sample t-test with one observation per group has no within-group variance estimate and zero degrees of freedom. The chapter must impose a practical minimum and choose an example whose result is not below the method's domain.

The same sample-size section says the derivation belongs in Volume II, but Exercise 1370-1374 asks the reader to derive it in this chapter. The note for the editor correctly says the algebra is light. The chapter should either show it now or stop assigning it.

The p-hacking and replication sections are under-cited. Simmons, Nelson, and Simonsohn 2011 is the natural primary citation for undisclosed flexibility increasing false-positive rates. Kerr 1998 is the source for HARKing. Gelman and Loken are the common source for the garden of forking paths. Open Science Collaboration 2015 and Errington et al. 2021 are needed for the replication-crisis claims. The chapter's generic stance does not exempt it from citation discipline because it names years and quantitative replication patterns.

The reliability design exercise at lines 1477-1484 is internally inconsistent. A Weibull distribution with $\beta = 2$ and $\eta = 5000 \,\si{\hour}$ has $B_{10} = \eta[-\ln(0.9)]^{1/\beta} \approx 1623 \,\si{\hour}$, not $10{,}000 \,\si{\hour}$. A component with those target parameters cannot meet a $10{,}000 \,\si{\hour}$ $B_{10}$ life. This exercise needs new parameters or a different task.

## D. Pedagogical Review

The chapter teaches the habit promised in the dossier: statistics as a discipline for summarising, inferring, deciding, and refusing malpractice. It is aligned with the Volume I opener's promise that statistics should be defendable rather than performed. The best parts are the p-value interpretation, the confidence-versus-prediction distinction, the Bayesian contingency-table example, and the pre-registration principle.

The estimation block has the right form but the wrong example. It asks the reader to estimate before reading on, then shows how sample size scales as the inverse square of the effect. That is exactly the habit Q20 wants. The chosen first case, however, collapses below the minimum sample size required for the test. It teaches the scaling law at the cost of method validity.

The failure section is directionally right but too generic. The dossier asks for "replication crises across engineering disciplines." The chapter discusses psychology, cancer biology, economics, and single-study engineering exposure without naming or citing the primary studies. This weakens the closure. If the registry has no replication-crisis entries, the chapter can still cite primary papers as methodological case studies. It does not need to call them named accidents.

The archetype invocation is clean. Uncertainty is deepened from Chapter 4 by shifting from single measurement uncertainty to estimator uncertainty. Failure appears as statistical malpractice. The chapter should make the failure archetype explicit in the malpractice and replication sections as well as in metadata.

Exercise balance is strong by count: 35 exercises, matching the target, across calculation, derivation, estimation, simulation, design, diagnosis, failure analysis, and judgment. The simulation block is present, which fixes a gap we saw in Chapter 7. Difficulty is uneven. Core calculation exercises are tractable. The design exercises jump too far: daily-active-user A/B testing and Weibull reliability demonstration require formulas or design methods not taught in the chapter. Either add scaffolding or mark them as mastery.

The project mostly matches Q55. It asks for 30 trials, pre-registration, summary statistics, an inferential analysis, and a 1500-word reflection on colleague replication. The mismatch is that it requires power calculation and effect-size confidence intervals while the chapter tags sample size and power as standard and does not teach effect-size confidence intervals. A core project cannot depend on standard-path material unless the project itself is standard or the section is promoted to core.

The household examples need cleanup. A daily commute project is easy but may not produce a balanced weekday versus Friday comparison. Appliance energy use requires an energy meter, which is not in the tool list. Boiling water 30 times is low hazard but wasteful and slow; it should be framed as optional, with safer low-cost alternatives such as repeated smartphone timing, step counts, or scale readings.

## E. Citation Discipline

The chapter cites Wasserman, Devore, and NIST. Those are appropriate baseline sources for textbook statistical machinery and engineering examples. They are not enough for the chapter's most socially consequential claims.

Missing citations:

1. The Pearson mean-median-mode skew rule at lines 66-72 needs a source or softening.
2. The Sturges and Freedman-Diaconis histogram rules at lines 125-130 need citations if named.
3. The five distribution mechanisms and engineering examples at lines 181-333 need either textbook support by paragraph or local citations where examples are nontrivial.
4. The variance-to-mean diagnostic band $0.8$ to $1.2$ at lines 301-308 needs provenance or removal.
5. The convention $\alpha = 0.05$ and the safety-critical thresholds at lines 392-397 need a source or a cost-of-error rewrite.
6. The NIST e-Handbook citation at line 468 is appropriate for test catalogue material.
7. Tolerance intervals at lines 605-612 should cite NIST directly or add a precise Devore table reference. NIST has a clear tolerance-interval section.
8. P-hacking at lines 938-958 should cite Simmons, Nelson, and Simonsohn 2011.
9. Garden of forking paths at lines 960-980 should cite Gelman and Loken.
10. HARKing at lines 982-995 should cite Kerr 1998.
11. Sequential testing at lines 1006-1011 should cite a statistical source or be marked as recognition-level.
12. The reproducibility study claim at lines 1068-1071 needs Open Science Collaboration 2015. The cancer-biology claim needs Errington et al. 2021. The economics claim needs a primary replication paper or should be removed until sourced.
13. The single-study skepticism and effect-size shrinkage claims at lines 1120-1142 need replication or meta-science citations.

Citation tier: textbook citations are fine for formulas. Institutional web citation is fine for NIST test catalogue material. Primary research papers are required for named research-methods events and dated replication statistics. The chapter currently treats replication crisis claims as generic commentary; they are empirical claims and need citations.

## F. Reader-Path Tagging

The section tags are mostly plausible but not internally consistent with the project.

Core is correct for summary statistics, distributions, hypothesis testing, confidence versus prediction intervals, p-hacking, failure, project, calculation exercises, estimation exercises, diagnosis, and failure analysis. A Volume I reader needs those.

Bayesian intuition as standard is defensible. It is important, but the chapter treats it as recognition-level with a contingency table, not a full computational framework.

Sample size and statistical power should be core if the project requires a target power, effect size, and sample size calculation. The current project makes those core deliverables. Either promote section 8.6 to core or change the project so core readers can use a fixed $n=30$ project with a qualitative power reflection.

Simulation as mastery is defensible. It requires a programming environment, which the volume opener does not assume. Some simulation exercises are still valuable, but they should not be required for the core deliverable.

The A/B test and Weibull reliability design exercises should be mastery or rewritten with enough scaffolding for standard. They require methods beyond what the chapter teaches.

## G. Specific Concrete Fixes

1. `volumes/01-quantity/ch08-statistics-for-engineers/chapter.tex:22-25`

Current text: "This chapter makes the second and third operational: we summarise data, fit it to distributions, draw inferences from samples to populations, and refuse the analytical practices that turn engineering reports into press releases."

Proposed replacement: "A statistical report earns trust when it states the data summary, the distributional model, the inference from sample to population, and the analytical practices it refused."

2. `chapter.tex:29-34`

Current text: "A sample is a set of $n$ measurements $x_{1}, x_{2}, \ldots, x_{n}$ drawn from some underlying population. The summary statistics compress the sample into a few numbers that describe its centre and its spread \cite[ch.~6]{text:wasserman2004}. The compression is lossy. The discipline is to state which loss the chosen summary accepts."

Proposed replacement: "A sample is a set of $n$ measurements $x_{1}, x_{2}, \ldots, x_{n}$ drawn from an underlying population by a stated sampling process. The summary statistics compress the sample into a few numbers that describe its centre and spread \cite[ch.~6]{text:wasserman2004}. The compression is lossy. The discipline is to state which information the chosen summary discards."

3. `chapter.tex:50-56`

Current text: "The median is the value that splits the sample into halves of equal count. Its strength is robustness: half the sample can be replaced by extreme values and the median does not move. Its weakness is information: the median discards the magnitude of values away from the centre."

Proposed replacement: "The median is the value that splits the sample into halves of equal count. Its strength is resistance to outliers: fewer than half the sample can be moved to extreme values before the median is forced to follow. Its weakness is information: the median discards the magnitude of values away from the centre."

4. `chapter.tex:101-106`

Current text: "The IQR is the spread of the middle half of the data. It is robust against outliers in the same way the median is, and it carries more information than the range."

Proposed replacement: "The IQR is the spread of the middle half of the data. It resists isolated extremes better than the range, but it is not immune to changes in the lower or upper quarter of the sample."

5. `chapter.tex:108-112`

Current text: "A common rule for outlier flagging uses the IQR: a point is an outlier candidate if it lies more than $1.5 \cdot \text{IQR}$ below $Q_{1}$ or above $Q_{3}$. The rule is convention, not law. Whether an outlier is contamination, a real tail observation, or a rare event is a domain judgement, not a statistical one."

Proposed replacement: "A common rule for outlier flagging uses the IQR: a point is an outlier candidate if it lies more than $1.5 \cdot \text{IQR}$ below $Q_{1}$ or above $Q_{3}$. The rule is convention. Statistics can flag the point; domain knowledge decides whether it is contamination, a real tail observation, or a rare event."

6. `chapter.tex:150-155`

Current text: "The sample mean is $\bar{x} = 28.6 \,\text{min}$. The median, after sorting, is $28 \,\text{min}$. The sample standard deviation is $s \approx 1.9 \,\text{min}$. The range is $35 - 26 = 9 \,\text{min}$. The first and third quartiles are $Q_{1} = 27 \,\text{min}$ and $Q_{3} = 29.75 \,\text{min}$, giving an IQR of about $2.75 \,\text{min}$."

Proposed replacement: "Using the printed sample, the sample mean is $\bar{x} \approx 28.73 \,\text{min}$. The median, after sorting, is $28 \,\text{min}$. The sample standard deviation is $s \approx 1.98 \,\text{min}$. The range is $35 - 26 = 9 \,\text{min}$. Using the linear percentile convention, $Q_{1} = 27.25 \,\text{min}$ and $Q_{3} = 29.75 \,\text{min}$, giving an IQR of $2.50 \,\text{min}$. If the chapter uses a different quartile convention, state it here and use it consistently."

7. `chapter.tex:157-166`

Current text: "The standard deviation is comparable to the IQR divided by $1.35$ (the conversion that holds for a Gaussian), which suggests the bulk of the distribution is roughly Gaussian, with a tail. The reader who reports only the mean has lost the information that fifteen percent of working days produce a commute much longer than typical."

Proposed replacement: "For a Gaussian distribution, $\text{IQR}/1.349$ estimates $\sigma$; here that comparison is only a rough check because the sample is small and the upper tail contains the $35$-minute day. The reader who reports only the mean has lost the information that several working days are longer than the central cluster."

8. `chapter.tex:183-189`

Current text: "The population is modelled by a probability distribution, which is a mathematical function $p(x)$ that describes how likely each value is. Five distributions cover most of what an engineer will fit \cite[ch.~3-4]{text:devore2015}."

Proposed replacement: "The population is modelled by a probability distribution. For continuous data, the density $p(x)$ assigns probability to intervals through area under the curve; for discrete data, the probability mass function assigns probability to values. Five distributions are common enough that the reader should recognize their mechanisms before fitting data \cite[ch.~3-4]{text:devore2015}."

9. `chapter.tex:242-250`

Current text: "Examples in engineering include particle-size distributions in milling and grinding, file-size distributions in storage and network systems, species concentrations in chemical processes, financial returns compounded over time, and biological growth quantities."

Proposed replacement: "Examples in engineering include particle-size distributions in milling and grinding, file-size distributions in storage and network systems, positive concentration measurements in chemical processes, asset prices or multiplicative cost factors under simple financial models, and biological growth quantities."

10. `chapter.tex:292-299`

Current text: "Examples in engineering include radiation counts at a detector, defect counts on a manufactured surface, packet arrivals at a network interface during low-traffic intervals, and earthquake counts in a tectonic region over a fixed time window."

Proposed replacement: "Examples in engineering include radiation counts at a detector, defect counts on a manufactured surface, and packet arrivals at a network interface during low-traffic intervals. Earthquake counts can be modelled as Poisson only under a restricted background-rate model that excludes clustering from aftershocks and other nonstationary effects."

11. `chapter.tex:301-308`

Current text: "For routine defect-count data, a ratio between about $0.8$ and $1.2$ is consistent with Poisson; outside that band, the engineer should consider a different model."

Proposed replacement: "For routine defect-count data, a variance-to-mean ratio near one is a screening sign that a Poisson model may be plausible. How far from one is acceptable depends on sample size, process context, and the cost of a wrong model."

12. `chapter.tex:356-366`

Current text: "A goodness-of-fit test (Kolmogorov-Smirnov, Anderson-Darling, chi-square) returns a $p$-value for the null hypothesis that the data come from the proposed distribution. A $p$-value below the chosen significance level rejects the distribution; a $p$-value above does not prove the distribution but fails to reject it."

Proposed replacement: "A goodness-of-fit test (Kolmogorov-Smirnov, Anderson-Darling, chi-square) returns a $p$-value for the null hypothesis that the data come from the proposed distribution. If parameters were fitted from the same data, the reference distribution for the test statistic may need adjustment or simulation. A $p$-value below the chosen significance level rejects the model; a $p$-value above fails to reject it and does not prove the model."

13. `chapter.tex:392-397`

Current text: "The convention $\alpha = 0.05$ is a working default in many engineering and scientific fields. It is convention, not law, and the appropriate $\alpha$ depends on the consequences of being wrong. A safety-critical decision uses a tighter $\alpha$ (often $0.01$ or $0.001$); a screening decision in a context where false negatives matter more uses a looser $\alpha$."

Proposed replacement: "The convention $\alpha = 0.05$ is a working default in many engineering and scientific fields. It is convention. The appropriate $\alpha$ depends on how the null is framed and on the relative cost of false positives and false negatives. A safety-critical test first states which error would allow an unsafe decision, then allocates $\alpha$ and power to control that error."

14. `chapter.tex:474-478`

Current text: "The $p$-value is the probability, under $H_{0}$, of a test statistic at least as extreme as the one observed. It is not the probability that $H_{0}$ is true. It is not the probability that the result would replicate. It is not the size of the effect. It is not the importance of the result."

Proposed replacement: "The $p$-value is the probability, under $H_{0}$ and the specified alternative, of a test statistic at least as extreme as the one observed. It answers one narrow question: how often the null model would produce a statistic this extreme. The truth of $H_{0}$, the probability of replication, the effect size, and the engineering importance require other evidence."

15. `chapter.tex:530-536`

Current text: "The prediction interval is wider, sometimes much wider, and the reader who confuses the two will overstate confidence in operational decisions."

Proposed replacement: "The prediction interval is wider, sometimes much wider. A reader who uses a confidence interval for a next-unit decision will usually understate operational scatter."

16. `chapter.tex:545-553`

Current text: "\bar{x} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}, where $t_{\alpha/2, n-1}$ is the critical value of Student's $t$-distribution with $n - 1$ degrees of freedom."

Proposed replacement: "\bar{x} \pm t_{1-\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}, where $t_{1-\alpha/2, n-1}$ is the positive critical value of Student's $t$-distribution with $n - 1$ degrees of freedom."

17. `chapter.tex:568-571`

Current text: "\bar{x} \pm t_{\alpha/2, n-1} \cdot s \cdot \sqrt{1 + \frac{1}{n}}."

Proposed replacement: "\bar{x} \pm t_{1-\alpha/2, n-1} \cdot s \cdot \sqrt{1 + \frac{1}{n}}."

18. `chapter.tex:616-638`

Current text: the commute interval example uses $\bar{x} = 28.6 \,\text{min}$ and $s = 1.9 \,\text{min}$ from the incorrect summary block.

Proposed replacement: "Return to the $30$-day commute sample of section 8.1, with $\bar{x} = 28.73 \,\text{min}$, $s = 1.98 \,\text{min}$, $n = 30$. The $95 \,\%$ confidence interval for the mean is
\[
28.73 \pm 2.05 \cdot \frac{1.98}{\sqrt{30}}
= 28.73 \pm 0.74 \,\text{min},
\]
so approximately $[28.0, 29.5] \,\text{min}$. This interval comes from a procedure with $95 \,\%$ long-run coverage for the population mean, assuming the model conditions hold.

The $95 \,\%$ prediction interval for the next morning's commute is
\[
28.73 \pm 2.05 \cdot 1.98 \cdot \sqrt{1 + 1/30}
= 28.73 \pm 4.11 \,\text{min},
\]
so approximately $[24.6, 32.8] \,\text{min}$. The prediction statement concerns the next commute, not the long-run average."

19. `chapter.tex:640-644`

Current text: "The operational consequence is that planning a meeting that requires an arrival time within fifteen minutes of the average is safer at the confidence-interval scale than at the prediction-interval scale. The engineer who promises arrival within the confidence interval is making a claim about long-run average behaviour, not about tomorrow."

Proposed replacement: "The operational consequence is direct. The confidence interval supports a claim about the long-run average commute. The prediction interval supports a claim about tomorrow's commute. A schedule promise for one future trip must use the prediction interval or a percentile model, not the confidence interval."

20. `chapter.tex:648-657`

Current text: "The two readings agree, under non-informative priors and with enough data, on the numerical answer to most engineering questions. They differ in interpretation and in how they handle prior information."

Proposed replacement: "With large enough data and weak prior information, frequentist and Bayesian analyses often give similar numerical estimates for routine engineering questions. They still differ in interpretation and in how they represent prior information."

21. `chapter.tex:740-742`

Current text: "An engineer who is unsure of a Bayesian calculation drops to the table; the table does not lie."

Proposed replacement: "An engineer who is unsure of a Bayesian calculation should write the contingency table and check every count."

22. `chapter.tex:753-767`

Current text: "The unit is then re-tested, with an independent test of the same characteristics. If it tests positive again, the new prior is $0.324$ and the new posterior is..."

Proposed replacement: "The unit is then re-tested with a second test whose errors are conditionally independent of the first test given the unit's true state. If it tests positive again, the new prior is $0.324$ and the new posterior is..."

23. `chapter.tex:840-854`

Current text: "The reader applies the formula; the derivation belongs in Volume II once the calculus is in place."

Proposed replacement: "The reader applies the formula as a planning approximation. The derivation uses the standard error of the difference of means and the normal critical values; the exercises ask the reader to carry that algebra for the equal-variance case."

24. `chapter.tex:856-885`

Current text: the sample-size estimation starts with a $10 \,\%$ mean difference and concludes that "Even one sample per line would be enough."

Proposed replacement: "Use the $1 \,\%$ case as the first worked case. Begin with: `A $1 \,\%$ mean difference at nominal $500 \,\si{\gram}$ is $\delta = 5 \,\si{\gram}$. The relevant ratio is $\sigma/\delta = 5/5 = 1$, so the rule of thumb gives $n \approx 16$ per line.' Then add: `A $10 \,\%$ difference gives a formal value below one, which means the effect is far larger than the process scatter. It does not mean a two-sample t-test can be run with one observation per group; the test still needs enough observations to estimate variance and check the process.'"

25. `chapter.tex:921-926`

Current text: "Pre-registration prevents the failure modes section 8.7 develops: selecting analyses to favour the result, redefining hypotheses after seeing the data, stopping data collection at convenient sample sizes, and reporting only the analyses that worked."

Proposed replacement: "Pre-registration reduces the failure modes section 8.7 develops: selecting analyses to favour the result, redefining hypotheses after seeing the data, stopping data collection at convenient sample sizes, and reporting only the analyses that worked. It works only when deviations are recorded and reported."

26. `chapter.tex:930-934`

Current text: "A statistically significant result has weight only when the analysis that produced it was specified before the data were seen \cite[ch.~10]{text:wasserman2004}. The chapter has now built the framework. We turn to its abuses, which are subtle, common, and disqualifying when discovered."

Proposed replacement: "A statistically significant result has confirmatory weight only when the analysis that produced it was specified before the data were seen \cite[ch.~10]{text:wasserman2004}. The same framework fails when the analysis plan is chosen after the data are visible."

27. `chapter.tex:938-958`

Current text: the p-hacking subsection has no primary citation.

Proposed replacement: Add `\cite{method:simmons-nelson-simonsohn-2011}` to the first paragraph after "threshold" and add the corresponding BibLaTeX entry for Simmons, Nelson, and Simonsohn, "False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant," 2011.

28. `chapter.tex:943-950`

Current text: "Reporting that one without disclosing the other nineteen is fraud. ... With enough subgroups, a significant result is guaranteed even when the null holds in every population."

Proposed replacement: "Reporting that one without disclosing the other nineteen is a misleading confirmatory claim. ... As the number of subgroups grows, the probability of at least one false positive approaches one even when the null holds in every population."

29. `chapter.tex:960-980`

Current text: the garden-of-forking-paths subsection has no source.

Proposed replacement: Add a citation to Gelman and Loken after the first sentence, and add a bibliography entry such as `method:gelman-loken-forking-paths`.

30. `chapter.tex:982-995`

Current text: the HARKing subsection has no source.

Proposed replacement: Add `\cite{method:kerr-harking-1998}` after the first sentence and add Kerr 1998 to the bibliography.

31. `chapter.tex:1057-1076`

Current text: "A reproducibility study, current as of 2015, attempted to replicate a set of published psychology results and found that fewer than half replicated at the original effect sizes; later studies in cancer biology, economics, and other fields showed comparable patterns."

Proposed replacement: "The 2015 Reproducibility Project: Psychology attempted replications of 100 studies from three psychology journals. Thirty-six percent of replications produced statistically significant results, and replication effect sizes were much smaller than original effect sizes \cite{method:open-science-collaboration-2015}. The 2021 Reproducibility Project: Cancer Biology repeated 50 experiments from 23 papers and found smaller replication effects and mixed replication success by multiple criteria \cite{method:errington-cancer-biology-2021}. Add the economics example only after a primary citation is added."

32. `chapter.tex:1120-1125`

Current text: "A single study's effect size is not the population effect size; effect sizes shrink as more replications come in. The working rule is to size the engineering decision against the most conservative defensible effect size, not against the mean of the published literature."

Proposed replacement: "A single study's effect size is an estimate, often selected from a literature that favours positive results. Replications and meta-analyses often reduce the effect-size estimate. The working rule is to size the engineering decision against a conservative defensible effect size and to state the source of that estimate."

33. `chapter.tex:1138-1142`

Current text: "A single study is hypothesis-generating, not hypothesis-confirming, in any field where the replication base rate is below one. The engineer who treats a single study as decisive is making a statistical bet against base rates the discipline has measured."

Proposed replacement: "A single study rarely deserves to be decisive when the result will enter load-bearing design. The engineer should ask for independent replication, a preregistered analysis, or a conservative uncertainty allowance before treating the number as design input."

34. `chapter.tex:1212-1216`

Current text: "The target power $1 - \beta$ and the smallest effect size that matters for the engineering question. The sample size $n$, computed from the rule of thumb in section 8.6 if a $t$-test is planned, or from a power calculation appropriate to the chosen test."

Proposed replacement: "The target power $1 - \beta$ and the smallest effect size that matters for the engineering question, if the reader is taking the standard path through section 8.6. For the core path, $n=30$ is fixed by the project and the reader states what effect size that sample can plausibly detect."

35. `chapter.tex:1238-1243`

Current text: "The pre-registered hypothesis test, with the test statistic, the $p$-value, and the conclusion. A confidence interval for the relevant parameter at $95 \,\%$ and a prediction interval for the next observation at $95 \,\%$. An effect size with its confidence interval."

Proposed replacement: "The pre-registered hypothesis test, with the test statistic, the $p$-value, the effect size, and the engineering conclusion. A confidence interval for the relevant parameter at $95 \,\%$ and a prediction interval for the next observation at $95 \,\%$. If an effect-size confidence interval is required, add the formula or provide a software recipe in the project notes."

36. `chapter.tex:1286-1290`

Current text: "Calculation and derivation problems have full solutions; open-ended problems have rubrics or reference write-ups."

Proposed replacement: "Calculation and derivation problems need full solutions before release; open-ended problems need rubrics or reference write-ups."

37. `chapter.tex:1294-1298`

Current text: "Compute the sample mean, sample median, sample standard deviation (with the $n - 1$ denominator), range, and IQR of the dataset..."

Proposed replacement: "Compute the sample mean, sample median, sample standard deviation (with the $n - 1$ denominator), range, and IQR of the dataset using the quartile convention stated in the solution notes..."

38. `chapter.tex:1362-1366`

Current text: "Use the moment-generating function or the direct sum form; the algebra does not require calculus."

Proposed replacement: "Use the probability-generating function, the moment-generating function, or the direct sum form. If using the moment-generating function, state the derivative step explicitly."

39. `chapter.tex:1436-1445`

Current text: "Simulate a clinical-style trial... running tests on three subgroups (size, gender, location)..."

Proposed replacement: "Simulate an engineering trial in which the true effect size is zero. Run a two-sample $t$-test on $1000$ simulated trials at $\alpha = 0.05$ and verify that the false-positive rate is approximately $0.05$. Then implement p-hacking by, in each trial, running tests on three post hoc subgroups such as test rig, shift, and batch, and reporting the smallest $p$-value."

40. `chapter.tex:1468-1475`

Current text: "Design an A/B test for a software-deployment decision. The metric is daily active users; the engineer wants to detect a $2 \,\%$ relative change with $\alpha = 0.05$ and power $0.90$. State the sample size required, the duration of the test, and the stopping rule that controls the false-positive rate against optional early stopping."

Proposed replacement: "Design an A/B test for a software-deployment decision, assuming the metric is a continuous per-user response with known pilot standard deviation. State the null and alternative, the smallest effect size that matters, the sample-size calculation using the two-sample rule of thumb, the duration of the test, and a pre-specified stopping rule. If the metric remains daily active users as a count or proportion, move this exercise to mastery and provide the appropriate model."

41. `chapter.tex:1477-1484`

Current text: "Design a reliability test for a new component whose target lifetime distribution is Weibull with $\beta = 2$ and $\eta = 5000 \,\si{\hour}$. The engineer needs to verify the design meets a $10{,}000 \,\si{\hour}$ $B_{10}$ life..."

Proposed replacement: "Design a reliability test for a new component whose target lifetime distribution is Weibull with $\beta = 2$ and unknown scale $\eta$. The engineer needs evidence that the design meets a $10{,}000 \,\si{\hour}$ $B_{10}$ life. State the required relationship between $B_{10}$ and $\eta$, the test duration, censoring plan, and analysis procedure. Mark this exercise mastery unless the chapter adds the reliability-test machinery."

42. `bibliography/references.bib:584-590`

Current text: the bibliography has NIST but no method sources for p-hacking, HARKing, garden of forking paths, or reproducibility studies.

Proposed replacement: Add entries for Simmons, Nelson, and Simonsohn 2011; Kerr 1998; Gelman and Loken on the garden of forking paths; Open Science Collaboration 2015; and Errington et al. 2021. Use a new prefix such as `method:` if the citation policy accepts research-methods sources, or classify them under `text:` only if `method:` is rejected by the editor.

## H. Structural Risks For The Larger Project

1. The citation policy has no clear prefix for research-methods failures. Chapter 8 needs primary methodological papers, not accident reports and not textbooks. Add a `method:` or `paper:` prefix convention for reproducibility, p-hacking, statistical practice, and research-methods evidence before more methods chapters are drafted.

2. The reader-path model allows a core project to depend on standard material. Here the project requires power analysis while the power section is tagged standard. Add a release-checklist rule: every required project operation must be taught in a core section, or the project must have explicit core and standard variants.

3. The exercise architecture still lacks solution/rubric artifacts. Chapter 8 promises full solutions and rubrics, and many exercises depend on exact conventions, software choices, or external formulas. The project should require a companion solution file before a chapter can claim exercise completeness.
