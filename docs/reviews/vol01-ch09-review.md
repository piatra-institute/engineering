# Vol 01 Ch 09 Review

**Resolved: 2026-04-29.** All G1-G35 fixes and voice items B1-B13 applied to `volumes/01-quantity/ch09-discipline-of-estimation/chapter.tex`. Pre-flight: added five new bibliography entries (`data:census-cbsa-2024`, `data:bls-oews-2023-chicago`, `paper:zhao2025-ocean-microplastics`, `text:national-academies-energy-1989`, `paper:elhacham2020-anthropogenic-mass`). The technical blockers are corrected: the human-lifetime metabolic-energy upper bound now reads $2.5\times 10^{11}$ to $4\times 10^{11}\,\si{\joule}$ (was $3\times 10^{9}$, off by ~100x); the Chicago piano-tuner block now cites the Census Vintage 2024 metro estimate ($9.41\times 10^{6}$) and the BLS OEWS May 2023 employment row (350 musical instrument repairers and tuners, RSE $24.6\,\%$, occupation 49-9063) instead of Mahajan; the factor-of-three derivation is rewritten in log space with the worst-case caveat; the pendulum limiting case now reads $T = 2\pi\,\si{\second}$ when $L/g = 1\,\si{\second\squared}$ rather than the dimensionally incoherent $L = g$; the Fermi problem definition is replaced with a decompose-before-lookup framing; the uncertainty-propagation paragraph is reformulated in log space; the independent-method check no longer claims that safety-critical analyses share no inputs; the microplastics example now requires compartment, size range, and source set; the Challenger section is realigned with Appendix F's actual range estimates ($1$ in $100$ to $1$ in $100{,}000$, with management favoring the lower end and engineers the higher) and the retrospective two-losses-in-135-flights claim now also cites `acc:caib-columbia`. Section 9.5 promoted from `standard` to `core` so the deep-uncertainty Fermi problems can sit inside the core project. The 747 paragraph now cites `web:boeing-commercial-reference` rather than Mahajan. Project deliverable rephrased to require an editor source-pack rather than asserting one already exists. Eight Fermi problems rewritten to remove uncitable folklore numbers, soften ground-truth requirements, or name reproducible reference values; Fermi 50 promoted to mastery and tied to `paper:elhacham2020-anthropogenic-mass`. Voice items: self-announcing topic sentences cut, banned `not X / it is Y` constructions rewritten, "robust" filler removed, moral-close hyperbole replaced with the audit-trail framing. Build verified: `make distclean && make strict` produces a 696-page `main.pdf` with no undefined references; `make check`, `make audit-docs`, `make accidents`, and `make exercise-counts` all PASS. The transient `make strict` "Maximum runs of pdflatex reached" Codex saw was caused by Ch 8 churn from the prior review pass; the current book stabilises in three latexmk runs.

Build-facing note: Chapter 9 has no chapter-local unresolved cross-reference in the checks we ran. `make check`, `make accidents`, and `make exercise-counts` pass. `make strict` processed Chapter 9 and wrote `main.pdf`, but exited with `latexmk` "Maximum runs of pdflatex reached without getting stable files," with the rerun cause pointing at the already modified Chapter 8 source. We should not treat that as a Chapter 9 build block, but it belongs in the release checklist before any final pass.

Scope checked: `docs/editorial-decisions.md`, `docs/voice.md`, `docs/citation-policy.md`, `docs/reviewer-guide.md`, `docs/case-study-template.md`, `docs/research/landscape.md`, `docs/research/01-quantity/ch09-discipline-of-estimation.md`, `volumes/01-quantity/_volume.tex`, `volumes/01-quantity/ch09-discipline-of-estimation/chapter.tex`, `docs/research/accidents/challenger-1986.md`, and the cited BibLaTeX entries `text:mahajan2014`, `gen:mackay2009`, `acc:nasa-challenger`, and `hist:vaughan1996`. We also checked external sources for claims the chapter makes or should cite: [NASA Rogers Commission Appendix F](https://www.nasa.gov/history/rogersrep/v2appf.htm), [NASA Rogers Commission index](https://www.nasa.gov/history/rogersrep/genindex.htm), [BLS OEWS Chicago 2023 row for musical instrument repairers and tuners](https://www.bls.gov/oes/2023/May/oes_16980.htm), [BLS OEWS data tables for May 2024](https://www.bls.gov/oes/tables.htm), [U.S. Census 2024 metro estimates press release](https://www.census.gov/newsroom/press-releases/2025/population-estimates-counties-metro-micro.html), [IEA data-centre electricity estimate](https://www.iea.org/energy-system/digitalisation/data-centres-and-data-transmission-networks), [Nature 2025 subsurface microplastics synthesis](https://www.nature.com/articles/s41586-025-08818-1), [National Academies dietary energy reference](https://www.ncbi.nlm.nih.gov/books/NBK234938/), and [Nature 2020 anthropogenic mass paper](https://www.nature.com/articles/s41586-020-3010-5).

## A. Verdicts

Technical: blocked. The human-lifetime energy upper bound is wrong by roughly two orders of magnitude, and the chapter uses current empirical claims with missing or wrong citations, including the Chicago piano-tuner comparison, ocean microplastic mass, and several exercise ground-truth anchors.

Pedagogical: approved-with-corrections. The chapter builds the estimation habit promised in the dossier, but the project has no source pack or reference-solution rubric even though it requires 50 ground-truth comparisons, and several Fermi problems are unanswerable as written.

Voice: approved-with-corrections. The prose is mostly in the house register, but it has banned negate-first pivots, self-announcing topic sentences, `robust` as filler, and a moral close that overstates what estimation can guarantee.

## B. Voice Review

The chapter is stronger than the earlier Volume I drafts in rhythm. It largely avoids theatrical transitions and it keeps the reader doing work. The problems below are local, but they matter because this chapter explicitly teaches the habit the voice guide also asks the prose to model.

1. `volumes/01-quantity/ch09-discipline-of-estimation/chapter.tex:21-25`

Offending sentence: "The chapter assembles the moves into a discipline, gives the discipline a formal home in the \verb|estimation| environment, and asks the reader to exercise that discipline against fifty problems whose answers span the physical, urban, biological, technological, and environmental scales an engineer is likely to meet."

Rule violated: `docs/voice.md`, "Self-announcing topic sentences." The sentence describes the chapter's machinery instead of doing the work.

Rewrite: "We put the moves in one place, name the `estimation` block as their formal home, and then make the reader use them on fifty problems across physical, urban, biological, technological, and environmental scales."

2. `chapter.tex:27-33`

Offending sentence: "This consolidates a year of habit-building into a single deliverable."

Rule violated: `docs/voice.md`, "Not hyped." It is a summary flourish. The concrete deliverable has already been named.

Rewrite: "The deliverable is the reader's evidence that the Volume I habit has become usable."

3. `chapter.tex:115-117`

Offending sentence: "The point is the moves, not the answer."

Rule violated: `docs/voice.md`, "Negate-first-then-pivot construction."

Rewrite: "The moves matter more than the final count."

4. `chapter.tex:360`

Offending sentence: "Estimation is performed before the calculation, not after."

Rule violated: `docs/voice.md`, "Negate-first-then-pivot construction."

Rewrite: "The estimate is recorded before the calculation begins."

5. `chapter.tex:519-520`

Offending sentence: "When the two routes agree, the result is robust against arithmetic error; when they disagree, the engineer investigates."

Rule violated: `docs/voice.md`, "AI-tic vocabulary." `Robust` is doing ordinary filler work here.

Rewrite: "When the two routes agree, the result has been checked against arithmetic error; when they disagree, the engineer investigates."

6. `chapter.tex:577`

Offending sentence: "In a deep-uncertainty estimate, the answer is the range, not a point."

Rule violated: `docs/voice.md`, "Negate-first-then-pivot construction."

Rewrite: "A deep-uncertainty estimate reports the range as the answer."

7. `chapter.tex:619-620`

Offending sentence: "The answer is not final; it is current as of the date of the estimate."

Rule violated: `docs/voice.md`, "Negate-first-then-pivot construction."

Rewrite: "The estimate is dated, so a later reader knows when to revisit it."

8. `chapter.tex:679-681`

Offending sentence: "An estimation block that omits move 2 is not an estimate."

Rule violated: `docs/voice.md`, "Negate-first-then-pivot construction."

Rewrite: "A block earns the name `estimation` only when it records the estimate before lookup or calculation."

9. `chapter.tex:680-682`

Offending sentence: "An estimation block that omits move 4 is an estimate that has wasted the learning opportunity it generated."

Rule violated: `docs/voice.md`, "Not hyped." "Wasted the learning opportunity" sounds like instructional scolding.

Rewrite: "A block without a postmortem leaves the dominant error source unnamed."

10. `chapter.tex:750-754`

Offending sentence: "Every chapter in this work has a failure section. The estimation chapter's failure section names a class of estimates that, in working engineering practice, have not been sanity-checked."

Rule violated: `docs/voice.md`, "Self-announcing topic sentences" and "Meta-explanation tails."

Rewrite: "A failure-rate estimate can become dangerous when it travels through an organisation without an independent sanity check. The Space Shuttle Challenger O-ring case is the chapter's canonical example \cite{acc:nasa-challenger}."

11. `chapter.tex:857-858`

Offending sentence: "A failure-rate estimate that has not been sanity-checked against component data, against the historical record of comparable systems, and against observed in-service anomalies is not a defensible estimate."

Rule violated: `docs/voice.md`, "Negate-first-then-pivot construction." The sentence is correct in substance, but the construction is banned.

Rewrite: "A defensible failure-rate estimate is checked against component data, the historical record of comparable systems, and observed in-service anomalies."

12. `chapter.tex:908-918`

Offending sentences: "A profession that estimates honestly is one whose buildings stand, whose vehicles arrive, whose drugs cure, and whose software runs. A profession that estimates dishonestly is one whose record of failure is the record of numbers that were chosen rather than derived."

Rule violated: `docs/voice.md`, "Not hyped" and "No invented scenes or figures." The claim overpromises. Honest estimation helps; it does not make buildings stand or drugs cure by itself.

Rewrite: "Honest estimation leaves an audit trail. It lets a later engineer see which numbers came from data, which came from models, which came from judgement, and which still need to be checked."

13. `chapter.tex:936-938`

Offending sentence: "Volume I closes here. The fifty Fermi problems below are the volume's closing project, and the artifact by which the reader proves to themselves that the habit has taken."

Rule violated: `docs/voice.md`, "Meta-explanation tails." It announces the close twice.

Rewrite: "The fifty Fermi problems below are the volume's closing project."

## C. Technical Review

The chapter's basic engineering thesis is sound. Estimate first, record the estimate, compare to the calculated or measured result, and perform a postmortem on the dominant error source. The four-move structure is useful and deserves to become the book's formal pattern. The scaling and uncertainty archetypes are the right pair for this chapter.

The blocked defects are specific.

The factor-of-three derivation is mathematically loose. Lines 98-105 mix worst-case multiplication with what appears to be independent log-error propagation. If four factors are each within $\sqrt{3}$ in the worst case, the product can be off by $(\sqrt{3})^{4}=9$, not roughly $3$. A factor of $3$ across four factors follows only if independent log-errors are being combined in quadrature. The chapter needs to say that explicitly or drop the derivation.

The Chicago piano-tuner comparison is miscited. Lines 130-132 cite Mahajan 2014 for a 2024 Chicago metropolitan population. A 2014 textbook cannot support a 2024 statistic. The U.S. Census Bureau's Vintage 2024 metro estimate gives Chicago-Naperville-Elgin at 9,408,576 on July 1, 2024. Lines 159-161 cite Mahajan for a Bureau of Labor Statistics claim. The BLS OEWS row we checked for May 2023 gives 350 musical instrument repairers and tuners in the Chicago-Naperville-Elgin metropolitan area, with a high relative standard error. The estimate itself is good; the provenance is wrong.

The Fermi problem definition at lines 196-204 says the answer is a quantity the asker "cannot look up," yet most of the chapter's project asks the reader to estimate and then look up ground truth. The intended rule is that the reader must not look it up before estimating. That distinction matters because the whole habit depends on preventing lookup from anchoring the estimate.

The uncertainty-propagation paragraph at lines 316-330 is half correct. The relative-uncertainty formula is the Chapter 4 small-error rule. A factor-of-1.5 uncertainty is not cleanly a relative standard uncertainty of 0.4 unless the chapter changes to log space. For Fermi estimates, log uncertainty is the natural variable. Write $\sigma_{\ln X}^{2}=\sum_i\sigma_{\ln f_i}^{2}$ and then convert back by exponentiating. Otherwise the paragraph teaches the wrong formalism for the size of error it uses.

The limiting-case check for the pendulum has a dimensional error. Lines 503-507 say $T \to 2\pi$ when $L=g$ "in whatever units make the two numerically equal." Length and acceleration cannot be set equal. The correct statement is that if $L/g = 1\,\si{\second\squared}$, then $T=2\pi\,\si{\second}$. This is embarrassing in a volume that has spent eight chapters training dimensions.

The independent-method check is overbroad. Lines 526-528 say that for safety-critical work the two paths are not allowed to share any input or intermediate result. In real safety-critical practice, independent analyses may share requirements, environmental assumptions, load cases, or certified material data; the discipline is to identify shared inputs and audit them, not to pretend every input can be independent.

The microplastics example is uncited and likely too narrow. Lines 563-575 claim 2024 literature spans $10^{4}$ to $10^{7}$ tonnes. Recent synthesis work shows that microplastic abundance and mass estimates depend heavily on particle size, depth, sampling method, and whether the estimate is surface-only or water-column-wide. The 2025 Nature synthesis reports five to eight orders of magnitude spread in concentrations, and one Atlantic top-200-metre mass estimate of 11.6 to 21.1 million metric tons. The chapter can use microplastics as a deep-uncertainty example, but it must not print a clean global range without naming the compartment and sources.

The human lifetime energy upper bound is wrong by about two orders of magnitude. Lines 589-597 say metabolic rate times maximum lifespan gives about $3 \times 10^{9}\,\si{\joule}$. A human using roughly $100\,\si{\watt}$ metabolic power for 80 years expends about $100 \times 80 \times 365.25 \times 86400 \approx 2.5 \times 10^{11}\,\si{\joule}$. A high-lifetime upper bound is closer to $3 \times 10^{11}$ to $4 \times 10^{11}\,\si{\joule}$, not $3 \times 10^{9}$. This is the clearest technical block in the chapter.

The formal apparatus section miscounts prior estimation use. Lines 645-651 say the reader has used the environment in five chapters. The repo contains one `estimation` block in each prior Volume I chapter, Chapters 1 through 8. If the point is to name five canonical examples, say so. If the claim is about chapter count, change it to eight.

The Chapter 1 747 paragraph is miscited. Lines 686-693 cite Mahajan for a specific Chapter 1 estimate and the Boeing 747-400 maximum take-off weight. Chapter 1 itself cites `web:boeing-commercial-reference` for $396{,}890\,\si{\kilogram}`. Use that source, or cite the chapter-local result without pretending Mahajan supplies the Boeing figure.

The Challenger case mostly aligns with the registry and the Rogers Commission source. The date, 73-second breakup, right SRB aft field-joint O-ring, low temperature, and Morton Thiokol engineer objection are correct. The risk-estimate discussion should be tightened. Appendix F says estimates ranged from roughly 1 in 100 to 1 in 100,000, with higher figures from working engineers and lower figures from management. It also gives range-safety solid rocket evidence around 1 in 50 for mature rockets and says below 1 in 100 might be achievable with special care, while 1 in 1,000 was probably not attainable with the technology of the time. The chapter's "range safety office, about 1 in 100" is supportable as a compressed summary, but the bottom-up component-data sentence at lines 825-828 overstates the precision. Replace it with Feynman's own range language.

The retrospective Shuttle failure rate at lines 806-810 is arithmetically correct: two catastrophic losses in 135 flights gives $1.48 \times 10^{-2}$, or about 1 in 68. It needs a retrospective marker and a source that covers Columbia or the full Shuttle flight count, such as `acc:caib-columbia` or a NASA mission dataset. A 1986 accident report cannot cite flights that happened through 2011.

The moral close overstates causality. Estimation is a discipline that reduces error and makes records auditable. It does not, by itself, make drugs cure or software run. The chapter can keep moral seriousness without turning estimation into a universal guarantor.

Cross-references are simple. The chapter has `\label{vol01:ch09}` and no `\cref`, `\autoref`, or `\ref` calls. There are no chapter-local unresolved cross-references to fix.

## D. Pedagogical Review

The chapter builds the habit promised in the dossier. It takes a practice used informally across the volume and names its moves: question, recorded estimate, comparison, postmortem. That is exactly what Volume I needs before Volume II begins.

The best pedagogical material is the shape of a Fermi solution, the postmortem requirement, and the insistence that the estimate be recorded before lookup or calculation. Those moves are concrete enough for an adult reader to adopt immediately. The Challenger section also connects the habit to a real engineering failure, which gives the chapter weight.

The estimation block works as a model once its citations are repaired. The piano-tuner estimate is the right canonical problem. It decomposes the unknown, identifies dominant uncertainty, compares to an occupational data source, and records the lesson. The current citation errors weaken it, but the teaching move is strong.

The exercise architecture matches Q55 in count and track. The dossier and editorial decision say that this chapter's exercise set is the project: 50 Fermi problems, analysis only, no hazard, internet lookup after the estimate is recorded, plus a reflection. The chapter meets that decision.

The problem is support. A 50-problem project that asks for ground-truth comparison needs a source pack or reference key. Without it, readers will spend too much time deciding whether a source counts and future reviewers cannot tell whether a result is defensible. The chapter should ship with a `notes-for-editor.md` or solution file listing acceptable ground-truth sources by problem, with access dates and units.

Q16's exercise-type balance is intentionally overridden by Q55 for this chapter, but the exercise set still needs internal balance. Right now it is almost entirely estimation, with a few deep-uncertainty problems. That is acceptable for Chapter 9, but the problem statements should label which ones are ordinary Fermi estimates, which require bounding, and which require a source-quality judgement. The last group should mostly be `standard` or `mastery`, because they require more than the base four moves.

Difficulty is uneven. Several early physical-scale problems are excellent: atmosphere mass, ocean mass, coin atoms, aircraft kinetic energy. Several later current-data problems are too source-dependent for core status: global internet throughput, smartphone accelerometer readings, lines of code in proprietary operating systems, and worldwide acetaminophen consumption. Those can be good estimation problems only if the source uncertainty is part of the task and the expected comparison is specified.

The failure section closes the chapter's main mechanism. It shows what happens when an estimate is accepted without independent sanity checks. It should become more exact about what the Rogers Commission and Feynman Appendix F actually say, but the pedagogical placement is right.

The archetype invocation is clean. Scaling is the canonical home, and uncertainty recurs naturally from Chapters 4 and 8. The chapter should mention that deep uncertainty introduces a boundary between Volume I estimation and later risk analysis, but it does not drift into science-undergraduate depth. The technical content is engineering-depth: enough formalism to make the habit disciplined, not a probability textbook hidden in Chapter 9.

## E. Citation Discipline

The chapter currently cites four sources. That is enough by count, but not enough by load.

The two Chicago data claims need primary data citations. The population claim needs the U.S. Census Vintage 2024 metro estimate. The tuner employment claim needs BLS OEWS, with year, occupation code 49-9063, geography, and RSE.

The Fermi/Trinity attribution needs a historical source or removal. Mahajan can support estimation pedagogy, but it does not automatically support the specific historical claim about Fermi's Trinity paper-fragment estimate unless the page is cited and verified.

The microplastics range needs peer-reviewed environmental literature. A deep-uncertainty example cannot ask the reader to respect a range while giving no sources for the range.

The confirmation-bias paragraph uses a psychological mechanism as a load-bearing reason for estimate-before-calculation. It should cite a cognitive-bias or judgement-under-uncertainty source, or it should be reframed as a practical engineering record rule rather than an empirical psychology claim.

The Challenger case uses the required primary report, `acc:nasa-challenger`, and the secondary Vaughan source. That is good. The retrospective two-losses-in-135-flights claim needs a later primary source. The Rogers Commission cannot support Columbia and final Shuttle flight count.

The exercise set contains many current empirical claims and "typical answer" ranges that need citations in a source pack: world primary energy, data-centre electricity use, global transistors, internet throughput, global plastics and steel, TOP500 floating-point performance, fossil-fuel CO2, radiative forcing, irrigation withdrawals, GDP, aviation revenue, anthropogenic mass, and soil erosion. These can be cited in the solutions rather than prose, but the release artifact needs them.

## F. Reader-Path Tagging

The section tags are mostly defensible. Sections 9.1 through 9.4 are core. The formal estimation apparatus is core. The Challenger failure section is core. The project is core because Q55 makes it the chapter deliverable.

The problem is Section 9.5. Deep uncertainty is tagged `standard`, but the project requires deep-uncertainty problems, including Fermi 45, 49, and 50. A core project cannot require concepts held in a standard-only section. Either move Section 9.5 to `core`, or mark the deep-uncertainty problems as `standard` and make the core project require only a defined subset. The cleaner fix is to promote 9.5 to core because bounding is central to estimation.

Exercise-level `\pathtag{standard}` tags appear after `\begin{exercise}` on several items. The reader-path convention in `editorial-decisions.md` says tags follow headings. If exercise-level tags are intended, the macro convention should be documented. If they are not intended, those tags may render but they do not communicate a stable reader path.

Fermi 50 is untagged but clearly mastery or at least standard. It asks for cumulative engineered mass across human history and a reflection on the next eleven volumes. That is a synthesis problem, not an ordinary core Fermi estimate.

## G. Specific Concrete Fixes

1. `volumes/01-quantity/ch09-discipline-of-estimation/chapter.tex:21-25`

Current text: "The chapter assembles the moves into a discipline, gives the discipline a formal home in the \verb|estimation| environment, and asks the reader to exercise that discipline against fifty problems whose answers span the physical, urban, biological, technological, and environmental scales an engineer is likely to meet."

Proposed replacement: "We put the moves in one place, name the \verb|estimation| environment as their formal home, and then make the reader use them on fifty problems across physical, urban, biological, technological, and environmental scales."

2. `chapter.tex:98-105`

Current text: "The convention has structural roots. An estimation built from a sequence of independent multiplicative factors compounds the errors by multiplication; if each factor carries a multiplicative error of around $1.5$, four such factors compound to about $5$, and three to about $3.4$. A reader who keeps each individual factor within $\sqrt{3}$ of its truth ends up with a product within roughly $3$ of its truth across three or four factors. The factor-of-three target is what falls out of the typical Fermi estimate naturally; it is not arbitrary."

Proposed replacement: "The convention has structural roots, but the structure is logarithmic. If $X=\prod_i f_i$, then multiplicative errors add in $\ln X$. Four independent factor errors with log-width $\ln(1.5)$ combine to a log-width of about $2\ln(1.5)$, which is a factor of about $2.25$. Four factor errors with log-width $\ln(\sqrt{3})$ combine to a factor of about $3$ when treated in quadrature. Worst-case multiplication is looser: four factors each high by $\sqrt{3}$ would put the product high by $9$. The factor-of-three target is therefore a working statistical target for independent factor errors, not a worst-case guarantee."

3. `chapter.tex:115-117`

Current text: "The chapter's first formal estimation block trains the basic moves. The question is one whose answer can be looked up for comparison. The point is the moves, not the answer."

Proposed replacement: "The chapter's first formal estimation block trains the basic moves. The question has an external comparison value, but the work is in the decomposition, the recorded assumptions, and the postmortem."

4. `chapter.tex:130-132`

Current text: "The Chicago metropolitan area has a population of about $9 \times 10^{6}$ people, current as of 2024 \cite{text:mahajan2014}. We take that as the denominator."

Proposed replacement: "The Chicago-Naperville-Elgin metropolitan area had a population of $9.41 \times 10^{6}$ on July 1, 2024, in the U.S. Census Bureau Vintage 2024 estimate \cite{data:census-cbsa-2024}. We round that to $9 \times 10^{6}$ for the estimate and take it as the denominator."

5. `chapter.tex:159-161`

Current text: "The U.S.~Bureau of Labor Statistics reports a few hundred working piano tuners and technicians in the Chicago metropolitan area, current as of 2024 \cite{text:mahajan2014}, well within our defensible range."

Proposed replacement: "For comparison, the U.S.~Bureau of Labor Statistics OEWS table for May 2023 reports $350$ musical instrument repairers and tuners in the Chicago-Naperville-Elgin metropolitan area, occupation code 49-9063, with a relative standard error of $24.6\,\%$ \cite{data:bls-oews-2023-chicago}. That is within our defensible range."

6. `chapter.tex:196-204`

Current text: "A \engterm{Fermi problem} is one whose answer is a quantity the asker cannot look up and whose estimate the asker is willing to defend within a factor of three. The genre is named for Enrico Fermi, who used the genre as both a teaching device and a working tool, including a famous estimate of the Trinity test yield from the displacement of paper fragments by the blast wave. The habit predates Fermi; the name has stuck because his use of it became iconic among working physicists and because his standard, that an answer is worth defending only if it comes with a method, has become the genre's standard."

Proposed replacement: "A \engterm{Fermi problem} is a quantitative question answered by decomposition before lookup. The reader may be able to find a published value later; the discipline is to make and record the estimate first. The genre is named for Enrico Fermi. If we keep the Trinity paper-fragment anecdote here, it needs a historical citation with page or archive reference; otherwise the chapter should leave the historical note at the name."

7. `chapter.tex:316-330`

Current text: the full paragraph beginning "A product of factors compounds its uncertainties multiplicatively."

Proposed replacement: "A product of factors compounds its uncertainties in log space. If $X=\prod_i f_i$, then $\ln X=\sum_i \ln f_i$. For independent factor uncertainties, the log-uncertainty obeys
\[
\sigma_{\ln X}^{2}=\sum_i \sigma_{\ln f_i}^{2}.
\]
A factor-of-$1.5$ uncertainty corresponds to $\sigma_{\ln f}\approx \ln(1.5)\approx 0.41$ if we treat the factor as a one-sigma log-width. Four such factors combine to $\sigma_{\ln X}\approx 0.82$, or a multiplicative one-sigma factor of $e^{0.82}\approx 2.3$. Seven such factors combine to $e^{\sqrt{7}\ln(1.5)}\approx 2.9$. The approximation is only a model of independent factor errors, but it teaches the right habit: a long decomposition widens the result."

8. `chapter.tex:359-367`

Current text: "The discipline that makes estimation useful is the order in which it is applied. Estimation is performed before the calculation, not after. Once the calculation has produced a number, the calculator's confidence in that number is too high for the estimate to function as a check. The reader who estimates after calculating reaches a different estimate from the one they would have reached blind, because the calculation has anchored their judgement. The estimate-before-calculate discipline is what defends the calculation against silent error."

Proposed replacement: "The discipline that makes estimation useful is the order in which it is applied. The estimate is recorded before the calculation begins. Once the calculation has produced a number, that number anchors judgement; later factors tend to drift toward it. The estimate-before-calculate discipline defends the calculation against silent error by preserving a blind comparison value."

9. `chapter.tex:440-445`

Current text: "The habit costs about ten minutes per estimate in the first weeks of practice. After several months it costs two minutes; after a year it is automatic, performed in the engineer's head while reading the question. The habit's productivity per minute, measured as errors caught per unit time spent, exceeds that of any other engineering defence we know of."

Proposed replacement: "The habit costs about ten minutes per estimate in the first weeks of practice. After several months it often costs two minutes; after enough repetition it becomes part of how the engineer reads the question. The cost is small enough that the check belongs before any calculation whose result will leave the desk."

10. `chapter.tex:503-507`

Current text: "The pendulum period $T = 2\pi \sqrt{L/g}$ has the limiting forms: $T \to 0$ as $L \to 0$ (a pendulum with no length has no period); $T \to \infty$ as $g \to 0$ (a pendulum with no gravity does not oscillate); $T \to 2\pi$ when $L = g$ (in whatever units make the two numerically equal). Each limit can be checked against intuition."

Proposed replacement: "The pendulum period $T = 2\pi \sqrt{L/g}$ has the limiting forms: $T \to 0$ as $L \to 0$ (a pendulum with no length has no period); $T \to \infty$ as $g \to 0$ (a pendulum with no gravity does not oscillate); and $T=2\pi\,\si{\second}$ when $L/g = 1\,\si{\second\squared}$. Each limit can be checked against intuition and dimensions."

11. `chapter.tex:519-528`

Current text: "When the two routes agree, the result is robust against arithmetic error; when they disagree, the engineer investigates. The independent-method check is the most labour-intensive of the sanity checks, because it requires building two paths to the same result. It is also the most thorough; it catches errors that all the other checks miss. For safety-critical work, the independent-method check is performed by a different engineer, and the two paths are not allowed to share any input or any intermediate result."

Proposed replacement: "When the two routes agree, the result has been checked against arithmetic error; when they disagree, the engineer investigates. The independent-method check is the most labour-intensive of the sanity checks because it requires building two paths to the same result. For safety-critical work, the second path is normally performed by a different engineer. Shared inputs, such as requirements, material properties, and environmental assumptions, are named explicitly and audited because common inputs can create common-mode error."

12. `chapter.tex:550`

Current text: "\section{Estimation under deep uncertainty}\pathtag{standard}"

Proposed replacement: "\section{Estimation under deep uncertainty}\pathtag{core}"

13. `chapter.tex:563-575`

Current text: the full microplastics paragraph beginning "For \emph{the total mass of microplastics in the world's oceans}..."

Proposed replacement: "For \emph{the total mass of microplastics in the world's oceans}, the answer depends on particle-size cutoff, sampling depth, polymer identification method, and whether the estimate concerns surface waters, the upper water column, sediments, or the whole ocean. Published estimates therefore span orders of magnitude rather than a neat factor-of-three band. A defensible estimate must state the compartment, size range, sampling assumption, and source set before it reports a range \cite{paper:zhao2025-ocean-microplastics}."

14. `chapter.tex:577-582`

Current text: "In a deep-uncertainty estimate, the answer is the range, not a point. The discipline is to identify the upper and lower bounds defensible from the available evidence, to state the range explicitly, and to identify the factor whose uncertainty contributes most to the range's width. A point estimate quoted without its range, in a deep-uncertainty problem, is a fiction."

Proposed replacement: "A deep-uncertainty estimate reports the range as the answer. The discipline is to identify the upper and lower bounds defensible from the available evidence, state the range explicitly, and identify the factor whose uncertainty contributes most to the range's width. A point estimate without its range misrepresents the problem."

15. `chapter.tex:589-597`

Current text: "For \emph{total energy a single human can expend in their lifetime}, an upper bound is set by the metabolic rate times the maximum lifespan, which gives about $3 \times 10^{9} \,\si{\joule}$. No human has ever exceeded that; the conservation argument is hard."

Proposed replacement: "For \emph{total metabolic energy a single human expends in their lifetime}, an upper bound is set by metabolic power times lifespan. A rough adult metabolic power of $100\,\si{\watt}$ sustained for $80$ years gives $100 \times 80 \times 365.25 \times 86400 \approx 2.5 \times 10^{11}\,\si{\joule}$; a long-lived, active upper bound is therefore closer to $3 \times 10^{11}$ to $4 \times 10^{11}\,\si{\joule}$ \cite{text:national-academies-energy-1989}. The conservation argument is hard; the previous power-of-ten must still be checked."

16. `chapter.tex:645-651`

Current text: "The reader has by now used the \verb|estimation| environment in five chapters of this volume. The Boeing 747 maximum take-off weight in chapter 1; the small-raindrop terminal velocity in chapter 2; the recalibration interval for a kitchen scale in chapter 3; the pendulum $g$-measurement uncertainty in chapter 4; the analog-to-digital converter resolution required for the thermistor measurement in chapter 5."

Proposed replacement: "The reader has by now used the \verb|estimation| environment in every previous chapter of this volume. Five early examples are the Boeing 747 maximum take-off weight in Chapter 1, the small-raindrop terminal velocity in Chapter 2, the recalibration interval for a kitchen scale in Chapter 3, the pendulum $g$-measurement uncertainty in Chapter 4, and the analog-to-digital converter resolution required for the thermistor measurement in Chapter 5."

17. `chapter.tex:679-682`

Current text: "The four moves are not optional. An estimation block that omits move 2 is not an estimate. An estimation block that omits move 4 is an estimate that has wasted the learning opportunity it generated."

Proposed replacement: "The four moves are required. A block earns the name \verb|estimation| only when it records the estimate before lookup, calculation, measurement, or simulation. A block without a postmortem leaves the dominant error source unnamed."

18. `chapter.tex:686-693`

Current text: "The 747 estimate in chapter 1 used the four-move structure \cite{text:mahajan2014}: the question (mass at maximum take-off weight, in tonnes); the recorded estimate ($390$ to $430$ tonnes, decomposed into passenger load, operating empty mass, and fuel); the comparison ($397$ tonnes, ratio $1.0$, well within a factor of three); the postmortem (the empty-mass factor was the riskiest move; a beginner's intuition can mistakenly anchor it on the payload)."

Proposed replacement: "The 747 estimate in Chapter 1 used the four-move structure: the question (mass at maximum take-off weight, in tonnes); the recorded estimate ($390$ to $430$ tonnes, decomposed into passenger load, operating empty mass, and fuel); the comparison to Boeing's $396{,}890\,\si{\kilogram}$ maximum take-off weight for the 747-400 \cite{web:boeing-commercial-reference}; and the postmortem (the empty-mass factor was the riskiest move; a beginner's intuition can mistakenly anchor it on the payload)."

19. `chapter.tex:750-754`

Current text: "Every chapter in this work has a failure section. The estimation chapter's failure section names a class of estimates that, in working engineering practice, have not been sanity-checked. The canonical case is the Space Shuttle Challenger O-ring failure rate \cite{acc:nasa-challenger}."

Proposed replacement: "A failure-rate estimate can become dangerous when it travels through an organisation without an independent sanity check. The Space Shuttle Challenger O-ring case is the chapter's canonical example \cite{acc:nasa-challenger}."

20. `chapter.tex:758-769`

Current text: the single sentence beginning "The Space Shuttle Challenger broke up $73$ seconds after launch..."

Proposed replacement: "The Space Shuttle Challenger broke up $73$ seconds after launch on $28$ January $1986$. The proximate cause was failure of an O-ring seal in the right solid rocket booster's aft field joint at an ambient launch temperature of approximately $-2\,\si{\degreeCelsius}$. Hot combustion gas escaped through the joint, damaged the external tank attachment region, and led to vehicle breakup \cite{acc:nasa-challenger}. The launch decision occurred after Morton Thiokol engineers had objected to launch under the expected cold-temperature conditions. The Rogers Commission report is the primary source; Diane Vaughan's 1996 analysis is the canonical secondary source on the organisational mechanism \cite{hist:vaughan1996}."

21. `chapter.tex:779-786`

Current text: "The shuttle programme had an internal estimate of the catastrophic failure rate, used in budgeting, scheduling, and risk acceptance. The estimate, as recorded in the Rogers Commission's report, was on the order of $1$ catastrophic failure per $100{,}000$ flights: a probability per flight of about $10^{-5}$. The Rogers Commission contrasted this with an independent estimate, by NASA's range safety office, of about $1$ in $100$, or $10^{-2}$, three orders of magnitude higher \cite{acc:nasa-challenger}."

Proposed replacement: "Appendix F of the Rogers Commission report records estimates of loss-of-vehicle-and-crew probability ranging from roughly $1$ in $100$ to $1$ in $100{,}000$. Feynman reports that the higher-risk estimates came from working engineers and the lower-risk estimates from management; he also summarizes range-safety evidence from prior solid rocket flights as far closer to the $10^{-2}$ scale than to $10^{-5}$ \cite{acc:nasa-challenger}."

22. `chapter.tex:798-810`

Current text: the paragraph beginning "The investigation was not performed at the level the discrepancy demanded."

Proposed replacement: "The discrepancy did not receive the level of investigation it demanded. A top-down management number near $10^{-5}$ and engineering estimates near $10^{-2}$ cannot both guide the same launch decision without reconciliation. Retrospectively, the Shuttle programme suffered two catastrophic losses in $135$ flights, Challenger in 1986 and Columbia in 2003, a rate of about $1.5 \times 10^{-2}$ over the completed programme \cite{acc:nasa-challenger,acc:caib-columbia}. That retrospective figure does not prove what could have been known before STS-51-L, but it shows which order of magnitude the historical programme eventually occupied."

23. `chapter.tex:825-836`

Current text: "Each of those questions has a defensible answer. The bottom-up estimate, when component failure data and observed prior anomalies are incorporated, lands near $10^{-2}$, not near $10^{-5}$. The historical record of comparable launch vehicles also lands near $10^{-2}$. The observations of O-ring erosion on prior flights, treated as data rather than as anomalies to be normalised, support the higher estimate. Three independent lines of evidence, each at the level the discipline of this chapter would have insisted on, agreed within a factor of three of one another. The fourth, lower estimate, was the outlier; the discipline would have insisted that the outlier be explained or discarded."

Proposed replacement: "Each of those questions points away from $10^{-5}$. Feynman's Appendix F reports working estimates around $1$ in $100$ and engineering estimates for related Shuttle subsystems as high as $1$ in $300$ or $1$ to $2$ per $100$, while management still claimed $1$ in $100{,}000$ \cite{acc:nasa-challenger}. The observations of O-ring erosion and blow-by on prior flights, treated as data rather than as accepted anomalies, also push the estimate toward the higher-risk order of magnitude. The lower number was the outlier; the discipline would have required an explanation before using it."

24. `chapter.tex:855-865`

Current text: "A failure-rate estimate that has not been sanity-checked against component data, against the historical record of comparable systems, and against observed in-service anomalies is not a defensible estimate. The Challenger case is the canonical instance because the disagreement between the working estimate and the available cross-checks was three orders of magnitude. The same pattern, at smaller magnitudes of disagreement, recurs in many engineering programmes that adopt a failure-rate or reliability number for budgetary or scheduling purposes without the bottom-up calculation the number implicitly claims to represent."

Proposed replacement: "A defensible failure-rate estimate is checked against component data, the historical record of comparable systems, and observed in-service anomalies. The Challenger case is the canonical instance because the disagreement between the management estimate and the available cross-checks was three orders of magnitude. The same failure mode can appear whenever a programme adopts a reliability number for budgetary or scheduling purposes without the calculation the number appears to represent."

25. `chapter.tex:893-906`

Current text: the paragraph beginning "The discipline has a moral content."

Proposed replacement: "The discipline has professional content. An engineer who records an estimate before calculation is harder to move toward a number selected for institutional convenience. The piano-tuner estimate is a small case; the Challenger O-ring failure-rate estimate is a large one. The same record discipline applies to both. An engineer who declines to report a failure rate derived from allocation rather than from component data preserves the distinction between what is known, what is assumed, and what remains to be checked."

26. `chapter.tex:908-918`

Current text: the paragraph beginning "The discipline scales further still."

Proposed replacement: "The discipline scales further still because records accumulate into culture. A profession that estimates honestly leaves a traceable account of its numbers: which came from measurements, which came from models, which came from judgement, and which were later checked against reality. A profession that estimates dishonestly loses that trace. The difference is built one estimate at a time, repeated across projects, reviews, and years."

27. `chapter.tex:977-983`

Current text: "The deliverable is graded against a public rubric. The general editor's reference solutions to all fifty problems, with the editor's own working and ratios to ground truth, are published online; the reader is encouraged to compare \emph{after} completing their own. There is no single correct answer to a Fermi problem; there are defensible answers and indefensible ones, and the reflection's job is to make the reader's defence explicit."

Proposed replacement: "The deliverable is graded against a public rubric. Before release, the editor should publish reference solutions to all fifty problems, with working, acceptable ground-truth sources, access dates, units, and ratios to the reference values. The reader compares only \emph{after} completing their own estimates. A Fermi problem has defensible and indefensible answers; the reflection's job is to make the reader's defence explicit."

28. `chapter.tex:1000-1006`

Current text: "Estimate the mass of all the human beings alive today, in tonnes, current as of 2024. State your assumptions for the mean adult mass, the fraction of the population that is adult, the fraction that is child, the mean child mass, and the world population. Compute the ratio of your estimate to the published world-population times mean-adult-mass figure."

Proposed replacement: "Estimate the mass of all human beings alive today, in tonnes, current as of 2024. State your assumptions for world population, adult fraction, child fraction, mean adult mass, and mean child mass. Compare your result to a reference calculation built from a named population source and a named body-mass source; do not require a published product of population times mean adult mass."

29. `chapter.tex:1049-1055`

Current text: "Estimate the total annual primary energy consumption of the world, in joules, current as of 2022. Decompose into the world population, the per-capita primary energy consumption (a rough mean across high- and low-income countries), and the seconds in a year. Compare to the figure published by the International Energy Agency or the BP Statistical Review of World Energy."

Proposed replacement: "Estimate the total annual primary energy consumption of the world, in joules, current as of 2022. Decompose into world population, per-capita primary energy consumption, and seconds in a year. Compare to the figure published by the International Energy Agency or the Energy Institute Statistical Review of World Energy."

30. `chapter.tex:1167-1173`

Current text: "Estimate the total mass of concrete poured in your country in the last calendar year, in tonnes. Decompose into the population, the per-capita annual concrete consumption (a working anchor point is $1$ to $5$ tonnes per person per year in developed economies), and any structural correction. Compare to the figure published by the cement industry's national association."

Proposed replacement: "Estimate the total mass of concrete poured in your country in the last calendar year, in tonnes. Decompose into population, per-capita annual concrete consumption, and a structural correction for construction intensity. If the published source reports cement rather than concrete, state the assumed cement fraction in concrete and convert explicitly. Compare to the figure published by the national cement or ready-mix concrete association."

31. `chapter.tex:1258-1264`

Current text: "Estimate the total number of transistors fabricated worldwide in one year, current as of 2022. Decompose into the global semiconductor industry's wafer output, the transistors per wafer, and the structural correction for chip-mix. Compare to the figure published by SEMI or by an industry analyst (typical answer is on the order of $10^{21}$ to $10^{22}$)."

Proposed replacement: "Estimate the total number of transistors fabricated worldwide in one year, current as of 2022. Decompose into wafer starts, die per wafer, transistors per die, and chip mix. Treat the comparison as an industry-estimate problem: name the source used for wafer starts and the source used for representative transistor counts, then report the answer as an order-of-magnitude range rather than as a single published truth."

32. `chapter.tex:1275-1280`

Current text: "Estimate the total volume of data transmitted across the global internet in one second, in bytes per second, current as of 2024. Decompose into the global internet user count, the per-user bandwidth, and the duty cycle. Compare to the figure published by Cisco's annual networking report or by similar industry sources."

Proposed replacement: "Estimate the total volume of data transmitted across the global internet in one second, in bytes per second, current as of 2024. Decompose into annual global internet traffic or user count, per-user traffic, and duty cycle. Compare to a named current source such as ITU, TeleGeography, Cloudflare, or a current Cisco archived forecast only if the year and metric match."

33. `chapter.tex:1299-1306`

Current text: "Estimate the number of lines of source code in a modern desktop operating system. Decompose into the historical record of operating-system source-code growth, the relative sizes of kernel, application, and shared library code, and the structural correction for code reuse. Compare to the figure cited for the Linux kernel (roughly $30$ million lines as of 2024) and for Windows or macOS (figures vary; the rough order is $50$ to $100$ million lines)."

Proposed replacement: "Estimate the number of lines of source code in one named open-source operating-system component, such as the Linux kernel, current as of 2024. Decompose into subsystem count, files per subsystem, lines per file, and generated-code exclusions. Compare to a reproducible source-line count from the release tarball or repository. Do not use uncitable Windows or macOS line-count folklore as ground truth."

34. `chapter.tex:1309-1314`

Current text: "Estimate the total number of accelerometer readings produced by all the smartphones in the world in one second. Decompose into the number of smartphones, the fraction sampling the accelerometer at that instant, the sampling rate, and the structural correction. Compare where industry analytics are available."

Proposed replacement: "Estimate the total number of accelerometer readings produced by all smartphones in the world in one second. Decompose into installed smartphone count, fraction of phones sampling at that instant, sampling rate, and whether the phone stores, discards, or transmits the samples. Treat this as a no-ground-truth Fermi problem unless the reference solution supplies a named industry data source; the postmortem should identify the sampling-duty-cycle assumption as the dominant uncertainty."

35. `chapter.tex:1404-1414`

Current text: "Estimate the total cumulative mass of all the engineered objects produced by humans across the entire history of the species, in tonnes. Acknowledge that this is a deep-uncertainty problem. Decompose into the cumulative population, the per-capita lifetime mass of engineered goods, and the structural correction for weighting recent decades more heavily than earlier centuries. State the upper and lower bounds defensible from the published literature, and reflect, in two or three sentences at the end of your reflection, on what this single number tells you about the twelve volumes you are about to read."

Proposed replacement: "Estimate the present stock of human-made material, or anthropogenic mass, in tonnes. Acknowledge that this is a deep-uncertainty problem. Decompose into major material classes such as concrete, aggregates, bricks, asphalt, metals, plastics, and glass, then compare to the anthropogenic-mass literature \cite{paper:elhacham2020-anthropogenic-mass}. In two or three sentences at the end of your reflection, state what this number teaches about the material scale of the twelve volumes ahead."

## H. Structural Risks For The Larger Project

1. The citation policy needs a "source pack" requirement for project-heavy chapters. Chapter 9 has 50 exercises that depend on current empirical reference values. The prose can remain uncluttered, but the release artifact needs an answer-source table with citation keys, access dates, units, and acceptable alternatives. Without that table, every future reviewer will redo the same source triage.

2. The reviewer protocol should separate "mechanical build pass" from "chapter-local build pass." `make strict` failed here because the full book did not stabilize after earlier modified content, while Chapter 9 itself had no fatal error. Reviews should report both full-book status and chapter-local status, or a later chapter can be blocked by an unrelated dirty file.

3. Reader-path tagging needs a rule for exercises and projects. Q51 says section tags follow headings, but Chapter 9 uses `\pathtag{standard}` inside exercise declarations and requires standard/deep-uncertainty ideas in a core project. Before the next review, decide whether exercise-level path tags are supported, where they appear, and whether a core project may require standard-path sections.
