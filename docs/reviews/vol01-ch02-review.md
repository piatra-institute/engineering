# Volume 1 Chapter 2 review: Units and dimensions

Resolved: 2026-04-28.

The 30 fixes in section G have been applied. The bibliography now has
the NASA Hubble Space Telescope Optical Systems Failure Report
(`acc:nasa-hubble-optical-systems-1990`, replacing the misapplied
`acc:nasa-challenger`); the Leveson-Turner 1993 IEEE Computer
investigation of Therac-25 (`paper:leveson-turner1993`); and the Gunn
and Kinzer 1949 raindrop terminal-velocity reference
(`paper:gunn-kinzer1949`). The chapter prose has the technical
corrections to the kilogram-prototype divergence, the electronvolt's
exact-in-revised-SI status, the standard-atmosphere definition, the
decibel framing, the raindrop estimate direction (low by a factor of
1.6, not high), the Buckingham pi chronology and statement (rank of
dimensional matrix; Bridgman as later systematiser, not earlier),
the Hubble subsection (now an OSBI-cited metrology-chain narrative,
not a Challenger-Commission misapplication), the Therac-25 subsection
(scoped to operator display interpretation only, not dosing-unit
confusion), the medication-error subsection (sourced patterns
without an unsupported Joint Commission top-five claim), and the
correct cross-volume references (Volume X Chapter 9 for human
factors, Volume III Chapter 12 for the drag curve). The exercise
preface drops the Q16 leak; the glucose enthalpy moves to ~2803
kJ/mol; the surface-tension exercise loses its current-as-of clause;
the Hubble and Therac exercises cite the new bibliography keys; the
project record loses "stapled or bound together." All `\si{\degC}`
nestings are now `\si{\degreeCelsius}`. The Buckingham pi section is
now `\pathtag{core}` so the core-tagged project no longer depends on
a standard-tagged section. The Volume I opener is updated to list
balance as the fourth Volume I archetype, aligning the opener with
this chapter's invocation.

The build is clean: `make strict` produces a 531-page `main.pdf`;
`make check` and `make audit-docs` PASS; `grep` finds no em-dashes in
the chapter source.

The structural risks named in section H (named-cases registry with
canonical mechanism and primary source per case; closest-equivalent-
to-primary citation policy for cases like Therac-25; reader-path
dependency check before exercises and projects are accepted) are
recorded as Phase 0.7 work and tracked separately. The path-
dependency issue surfaced here (core project depending on standard
section) is now fixed at the chapter level by promoting Buckingham
pi to core.

Build note: `make check` passes across the repository, and a strict `latexmk` build to `/tmp/englatex` completed without a hard LaTeX failure. The chapter still has release-blocking review issues. The largest ones are citation discipline for named cases, an incorrect Hubble citation to the Challenger report, unsupported medication and Therac claims, and several technical statements that are either wrong or too strong.

Sources checked for this review include the BIPM SI Brochure and kilogram history pages, the 27th CGPM prefix resolution, the NASA Hubble Space Telescope Optical Systems Failure Report, Leveson and Turner's IEEE Computer investigation of Therac-25, the Joint Commission sentinel-event material, NIST kilogram material, and published raindrop terminal-velocity literature summaries. Checked URLs: `https://www.bipm.org/en/publications/si-brochure`, `https://www.bipm.org/en/history-si/kilogram`, `https://www.bipm.org/en/-/resolution-cgpm-27-3`, `https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19910003124.pdf`, `https://web.mit.edu/6.033/2004/wwwdocs/papers/Therac_1.html`, `https://www.jointcommission.org/resources/sentinel-event/sentinel-event-data-summary/`, `https://www.nist.gov/si-redefinition/kilogram-present`, and `https://www.sciencedirect.com/science/article/pii/S0169809515002720`.

## A. Verdicts

Technical reviewer: blocked. Blockers: the named-case section does not meet the primary-source rule, and several numerical and physical claims are wrong, unsupported, or overstated.

Pedagogical reviewer: approved-with-corrections. The chapter teaches the unit-carrying and dimensional-analysis habit, but the core project depends on a standard-tagged section and several exercises assume later physics without enough scaffolding.

Voice reviewer: approved-with-corrections. The chapter is mostly in register, but it has self-announcing topic sentences, banned pivot constructions, and a few hype or meta sentences that should be removed before copy edit.

## B. Voice review

We walk the chapter in order. The voice problems are not pervasive, but the problem sentences are exactly the kind an external reader will notice because they appear at claims of importance.

1. Lines 16-22: "Chapter 1 said why measurement matters. This chapter says what a measurement is built from. Every measured quantity is a number paired with a unit; every unit reduces, in the end, to a small set of base dimensions. We teach the reader to carry units through every step of every calculation, to use dimensional analysis as a debugging tool, and to recognise the small group of failure modes that unit errors keep producing across decades and across domains."

Rule: `docs/voice.md`, self-announcing topic sentence. The paragraph reads like a syllabus preface before it reaches the mechanism.

Rewrite: "A measurement becomes usable only when its number, unit, and dimensional signature travel together. This chapter trains that discipline: carry the unit, check the dimensions, and treat every unitless number in an engineering calculation as suspect until it is explained."

2. Lines 76-82: "The candela's status is awkward and worth naming. Its definition involves human visual response, encoded as a fixed luminous efficacy at a single frequency. The candela exists because lighting, displays, and photometry need a unit; no engineering science recognises a base dimension for ``brightness'' independent of energy and frequency. We treat the candela as the SI's pragmatic concession to human perception."

Rule: `docs/voice.md`, meta phrasing and overbroad flourish. "Worth naming" is the same family as "worth noting"; "no engineering science recognises" is too sweeping.

Rewrite: "The candela is the base unit whose definition most visibly carries a human observer. Its fixed constant is a luminous efficacy at one frequency, so photometry can report lighting and display quantities in a way that matches visual response rather than radiant power alone."

3. Lines 175-181: "The discipline this chapter teaches is to write the unit on every quantity, in every line of every calculation, every time. The discipline pays off in three places: it lets the reader check dimensions during the calculation, it forces conversions to happen explicitly rather than in the head, and it survives the inevitable day when the reader returns to a notebook from six months ago and must reconstruct what they did."

Rule: `docs/voice.md`, generic repetition. "The discipline this chapter teaches" is self-announcing, and "every time" overplays the point.

Rewrite: "Write the unit on each quantity as the calculation moves. That habit checks dimensions while the work is still live, makes conversions explicit, and lets a six-month-old notebook remain auditable."

4. Lines 252-260: "Decibels are not a unit but a logarithmic ratio. A sound-pressure level in $\si{\deci\bel}$ is $20 \log_{10}(p/p_{0})$ where $p_{0} = 20 \,\si{\micro\pascal}$ is the reference. A voltage-ratio in $\si{\deci\bel}$ is $20 \log_{10}(V/V_{0})$. A power-ratio in $\si{\deci\bel}$ is $10 \log_{10}(P/P_{0})$, with the factor of $10$ rather than $20$ because power scales as the square of voltage or pressure. The reader who treats decibels as additive without understanding the underlying ratio will make additivity errors that compound across stages of a system."

Rule: `docs/voice.md`, banned negate-first-then-pivot pattern. It is also technically imprecise because the decibel is an accepted non-SI unit for logarithmic ratio quantities.

Rewrite: "The decibel is a dimensionless non-SI unit accepted for logarithmic ratio quantities. A sound-pressure level in $\si{\deci\bel}$ is $20 \log_{10}(p/p_{0})$ with $p_{0} = 20 \,\si{\micro\pascal}$. A voltage ratio uses $20 \log_{10}(V/V_{0})$ when the impedance basis is fixed. A power ratio uses $10 \log_{10}(P/P_{0})$."

5. Lines 416-426: "Dimensional analysis as a debugging tool has a deeper companion: the \engterm{Buckingham pi theorem}, which states that any physically meaningful equation involving $n$ variables in $k$ independent dimensions can be rewritten as a relationship among $n - k$ dimensionless groups. The theorem was published by Edgar Buckingham in 1914 \cite{paper:buckingham1914}, building on Bridgman's later systematisation \cite{text:bridgman1922} and rediscoveries that continued through the twentieth century \cite{text:barenblatt1996}. In modern engineering it is the foundation of similarity, scale modelling, and almost every dimensional argument the reader will make."

Rule: `docs/voice.md`, generic intensifier and overclaim. "Deeper companion" and "almost every" inflate an already strong result. The chronology is technically wrong.

Rewrite: "The same check becomes a design tool in the \engterm{Buckingham pi theorem}. For a dimensionally homogeneous relationship involving $n$ variables and a dimensional matrix of rank $k$, the relationship can be written in terms of $n-k$ independent dimensionless groups. Buckingham published the theorem in 1914; Bridgman later systematised dimensional analysis for engineers and physicists."

6. Lines 551-558: "The function $\Phi$ is not given by dimensional analysis. It is measured. The published drag-coefficient curve for a sphere, valid across many decades of Reynolds number, is one of the central empirical results of fluid mechanics, and we will return to it in chapter 11 of Volume III. The point here is that the structure $C_{D} = \Phi(\mathrm{Re})$ is fixed before any experiment is done. The experimentalist's job is to measure $\Phi$, not to discover that the drag depends on something else."

Rule: `docs/voice.md`, hype and negate-first pivot. "One of the central empirical results" is unearned without source; the final sentence overstates what a dimensional analysis can guarantee.

Rewrite: "Dimensional analysis gives the form, not the curve. Experiments measure $\Phi$ and also test whether the variable list was complete: roughness, compressibility, wall effects, and unsteady flow can all add dimensionless groups."

7. Lines 574-580: "Two systems with the same dimensionless groups are dynamically similar; a wind-tunnel model at the right Reynolds number predicts the full-scale drag coefficient, not by approximation but by the structure of the dimensional argument. Engineering practice in aerodynamics, naval architecture, hydraulic engineering, and turbomachinery rests on this."

Rule: `docs/voice.md`, banned "not by X but by Y" construction and overstatement. Similarity is powerful, but wind-tunnel inference still depends on geometry, boundary conditions, surface roughness, Mach number, wall interference, and measurement uncertainty.

Rewrite: "Two geometrically similar systems with the same governing dimensionless groups are dynamically similar within the assumptions of the model. Wind-tunnel data become useful when the relevant groups, boundary conditions, and corrections are named."

8. Lines 603-610: "Chapter 1 introduced three named accidents in which numbers crossed an interface without the protection of explicit units, ranges, and provenance: Mars Climate Orbiter, Air Canada Flight 143, Ariane 5 Flight 501. We will not repeat them here. The pattern they showed, unit confusion at an interface, is a recurring failure mode in every domain that handles measurements. This section names two more documented cases and one persistent class of low-level failures, then states the discipline that prevents them."

Rule: `docs/voice.md`, self-announcing topic sentence and meta transition. It also hides the fact that Hubble and Therac are not straightforward unit-confusion cases.

Rewrite: "The interface failure from Chapter 1 recurs in weaker forms: a test instrument encodes the wrong geometry, a medical device hides the meaning of a displayed dose, and a clinical order crosses from notation to action with an unsafe abbreviation."

9. Lines 663-666: "The official analyses \cite{text:leveson2011} treat Therac-25 as a software, regulatory, and human-factors failure; for our purposes, it is also an example of unit confusion in a software-mediated measurement chain, where the quantity displayed and the quantity meant did not match."

Rule: `docs/voice.md`, "for our purposes" as rhetorical license. The sentence tries to pull Therac into the chapter's theme by assertion.

Rewrite: "Therac-25 belongs first to software, safety, regulatory, and human-factors failure. It belongs here only where the operator display reported a quantity whose safety meaning the operator could not interpret."

10. Lines 708-712: "A reader who has finished this chapter has the formal vocabulary for the principle. The interface is the place where one quantity's description is translated into another's. The principle applies whenever such a translation occurs, which is approximately everywhere in engineering."

Rule: `docs/voice.md`, meta-explanation tail and vague intensifier. "Approximately everywhere" sounds like a slogan.

Rewrite: "The principle now has a name. At any interface, the receiving side must know the quantity, unit, reference condition, range, and conversion rule before it can safely act on the number."

11. Lines 791-798: "The exercises mix calculation, derivation, estimation, simulation, design, diagnosis, reverse engineering, failure analysis, and judgment per the editorial settlement on exercise types (Q16). Full solutions are provided for the calculation and derivation exercises; the estimation and dimensional-analysis exercises receive published reference derivations; the design, diagnosis, and judgment exercises receive rubrics rather than single answers. Exercises are tagged with their reader-path tier."

Rule: `docs/voice.md`, self-announcing and internal process leakage. The reader should not see "Q16" in chapter prose.

Rewrite: "The exercises move from conversion and dimensional checks to design, diagnosis, failure analysis, and judgment. Calculation and derivation problems have full solutions; open-ended problems have rubrics or reference derivations."

## C. Technical review

The SI material is close, but it needs tighter sourcing and several corrections. The seven defining constants and the 2019 effective date are correct. The wording should call them "defining constants" rather than "fundamental constants," since the candela's defining constant is a luminous efficacy, not a fundamental constant in the same sense as $c$ or $h$. The 2022 prefix claim is correct, but it is not supported by a 2019-only bibliography entry unless the entry is changed to the updated 9th edition or a separate 27th CGPM resolution entry is added. The electronvolt is exact in the revised SI: $1\,\mathrm{eV}=1.602176634\times10^{-19}\,\si{\joule}$. Line 143 says "approximately," which is wrong under the current SI.

The kilogram drift sentence needs care. BIPM's kilogram history page states a median divergence of about 25 micrograms for the original prototypes in the 1989 to 1991 verification. NIST material commonly reports about 50 micrograms for official copies over roughly a century. The chapter says the international prototype "lost" 50 micrograms. The rest of the paragraph admits that direction cannot be known, but the first sentence should say "diverged by" or use the BIPM 25 microgram value with a citation.

The conversion section has small but embarrassing defects. Lines 192-199 say "To convert an inch to a metre" and then convert one foot. The standard atmosphere sentence says sea-level pressure is "by definition"; the unit standard atmosphere is exact, but local sea-level atmospheric pressure is not. The temperature equations use `\si{\degC}`, where `\degC` is already a macro expanding to `\si{\degreeCelsius}`. The strict build tolerates it, but the source should use either `\degC` or `\si{\degreeCelsius}`, not a nested unit macro.

The decibel paragraph is technically imprecise. The decibel is a non-SI unit accepted for use with SI, used for logarithmic ratio quantities. Calling it "not a unit" will draw a correction from a metrologist or signal engineer. The voltage-ratio formula also needs the fixed-impedance condition, or it should say root-power quantity rather than voltage.

The raindrop estimation has a direct error. The estimate is $4\,\si{\meter\per\second}$, while the published value given is $6.5\,\si{\meter\per\second}$. The chapter says the dimensional argument is "high by about a factor of 1.6"; it is low by that factor. The published value needs a source, such as Gunn and Kinzer or an accepted correlation. The logic of the estimate is good, but the text should show that buoyancy and drag coefficient are part of the omitted prefactor rather than implying that dimensional analysis alone is within a factor of three by luck.

The Buckingham pi derivation is mostly right. The theorem should refer to the rank of the dimensional matrix, not simply the number of base dimensions named in the problem, although the procedure later moves in that direction. The history sentence is wrong: Buckingham did not build on Bridgman's later 1922 systematisation. The cross-reference to "chapter 4 of Volume III" is wrong as a place to sketch the theorem; Volume III Chapter 4 is dynamics and Newton's laws. If the proof is deferred, it belongs in Volume II mathematical modelling or a later fluids chapter. The return to sphere drag in Volume III Chapter 11 is also questionable; viscous drag and boundary-layer regimes sit more naturally in Volume III Chapter 12.

The dimensional examples check out. Newton's second law, kinetic energy, pendulum period, drag-force groups, Reynolds number, and the Hagen-Poiseuille exercise all have dimensions that cancel. The pendulum example is defensible because including mass and showing it drops out is pedagogically useful. The drag example should not say that the experimentalist's job is "not to discover that the drag depends on something else." Dimensional collapse is also a test of whether something else, such as roughness, compressibility, confinement, or unsteadiness, has been omitted.

The failure section blocks technical approval. Hubble is cited to `acc:nasa-challenger`, the Rogers Commission report on the Space Shuttle Challenger accident. That is the wrong source. The primary source is NASA TM-103443, The Hubble Space Telescope Optical Systems Failure Report, issued in November 1990 by the Optical Systems Board of Investigation. The chapter's broad mechanism is supported by that report: the reflective null corrector lens was mis-spaced by 1.3 mm, auxiliary tests indicated the error, and reliance on the reflective null corrector made the process fragile. But Hubble is not a unit-error case. It is a metrology, optical-test, verification, quality, and management case. It fits Chapter 7's "when the ruler was wrong" better than Chapter 2's unit-confusion theme.

Therac-25 also blocks the case section. The chapter uses `text:leveson2011`, a secondary textbook, while the citation policy requires an `acc:` primary report or closest equivalent for named accidents. Therac may not have a single public formal accident report, but the closest release-quality source is Leveson and Turner 1993, which is an IEEE Computer investigation based on public documents, FDA material, legal documents, correspondence, and user reports. The chapter's specific claims about "log-display unit-handling" and "silently overflowing counters" are muddled. The one-byte counter overflow belongs to the Yakima Class3 software path, not to a display-unit handling problem for magnetic field current and turntable angle. The Tyler "Malfunction 54" material is real, but the chapter should treat it as an unreadable safety message and dose-display interpretation problem, not as a dosing-unit confusion case.

The chronic medication unit-error section has no citation. The listed mechanisms are plausible and important, but the claim that Joint Commission reporting "current as of 2025" lists unit-related and dose-form-related errors as one of the top five categories of harmful medication events is not supported by the sources I found. The Joint Commission warns that sentinel event reporting is voluntary and not epidemiologic. The chapter should either cite the specific Joint Commission annual review or switch to a narrower, sourceable claim from Joint Commission, ISMP, FDA, or a peer-reviewed medication-safety source.

There are no `\cref`, `\autoref`, or `\ref` commands in this chapter. Textual cross-references still need correction. "Chapter 5 of Volume X under human-factors failures" is wrong: Volume X Chapter 5 is software defects; human factors is Volume X Chapter 9. "Chapter 4 of Volume III" is not a plausible Buckingham proof target. The chapter also names Air Canada Flight 143 and Ariane 5 Flight 501 in the failure section but does not include them in the `\chapmeta` named-case list.

## D. Pedagogical review

The chapter builds the habit promised in the dossier: units travel with numbers, dimensions are checked before trust, and Buckingham pi is introduced as engineering debugging rather than mathematical ornament. That is the right Chapter 2 job for Volume I. The worked pendulum and drag examples are well chosen because they show both the power and the limits of dimensional analysis.

The main pedagogical defect is path dependency. The project is tagged core and explicitly asks the reader to apply the machinery of Section 2.5, but Section 2.5 is tagged standard. A core reader cannot complete the core project without reading standard material. We should either mark Buckingham pi as core in this chapter or make the project standard. Given the settled Q55 project, the better fix is to make the theorem and procedure core, then keep optional subtleties in the mastery box.

The exercises are close to the Q16 mix. The count is 35, matching the target. The distribution is healthy: 7 calculation, 6 derivation, 6 estimation, 3 simulation, 4 design, 4 diagnosis and reverse engineering, 3 failure analysis, and 2 judgment. That is better balanced than many draft exercise sets. Difficulty calibration is uneven, though. Biot, Prandtl, Froude, Hagen-Poiseuille, capillary rise, and drag crisis are all useful, but most belong technically to later volumes. In this chapter they need either a short definition in the exercise statement or a clear expectation that the reader is using dimensional form only, not the full physics.

The project matches the Q55 settlement: analysis only, no instruments, five physical relationships, dimensional balance, dimensionless groups, and comparison to published forms. The artifact should be updated for a digital-first book. "Stapled or bound together" reads as paper-classroom language; "assembled as a short reference document" fits the project better.

The estimation block works as a model in structure: estimate first, identify variables, decide a regime, compute an order of magnitude, compare to a published value, and name what the estimate cannot recover. It fails at the sentence that says the estimate is high. That error is small to fix and large to leave because the block is supposed to model the reader's estimation discipline.

The failure section does not close the chapter's main mechanism. The principle at the end is strong, but the cases leading to it do not all demonstrate unit errors. Hubble demonstrates a flawed measurement chain and overruled verification. Therac demonstrates unsafe software, poor interface messages, inadequate regulation, and unreadable dose displays. Medication errors can demonstrate unit confusion directly, but they need sourcing. The section should either narrow itself to unit-interface failures or explicitly say that Chapter 2 is using these cases only where unit or displayed-quantity interpretation is the mechanism.

The archetype invocation is clean. Balance appears in dimensional form and is the right first balance archetype. It should be linked more explicitly to the volume opener, which says scaling, failure, and uncertainty are introduced in Volume I while balance appears later. The volume opener and this chapter currently disagree: the chapter claims balance as the first balance archetype, while the opener says balance appears from Volume II onwards. That is an architecture issue, not just a chapter issue.

## E. Citation discipline

The chapter cites six bibliography keys: `std:bipm-si2019`, `paper:buckingham1914`, `text:bridgman1922`, `text:barenblatt1996`, `acc:nasa-challenger`, and `text:leveson2011`. I read each entry in `bibliography/references.bib`.

`std:bipm-si2019` is appropriate for the seven defining constants and coherent SI units. It is insufficiently precise for the 2022 prefix expansion unless the entry is updated to the revised SI Brochure version or accompanied by a 27th CGPM resolution entry. It should also support the non-SI accepted units discussion, including the decibel, if that paragraph is corrected.

`paper:buckingham1914`, `text:bridgman1922`, and `text:barenblatt1996` are appropriate for dimensional analysis history and theory. The prose must fix the chronology and should avoid claiming that Barenblatt documents unspecified "rediscoveries" unless the sentence says what those rediscoveries are.

`acc:nasa-challenger` is a wrong citation for Hubble. It must be replaced by a new `acc:` or `web:` primary entry for NASA TM-103443, The Hubble Space Telescope Optical Systems Failure Report. Because Hubble is a named case, the prefix should be `acc:` under the current policy.

`text:leveson2011` does not satisfy the named-accident rule for Therac-25. Add `paper:leveson-turner1993` at minimum, and add FDA, Health Canada, GAO, or court-document entries where specific regulatory or legal claims are made. If no public primary investigation report exists, the chapter should say that and use the "closest equivalent" source discipline explicitly.

Uncited load-bearing claims include the IPK mass divergence, the 2 mm raindrop terminal velocity, the Hubble 2 micrometer optical error and 1.3 mm null-corrector spacing, the Therac intended and delivered dose values, the medication-error category claim, the glucose combustion enthalpy, the surface tension value for water, and the sphere drag-coefficient curve. These are empirical or historical claims and need source-tier support.

## F. Reader-path tagging

The current path tags are close but inconsistent. `SI base units`, `Derived units`, `Conversion`, `Dimensional analysis as debugging`, `Failure`, and `Project` are core. That is defensible. The problem is `Dimensional homogeneity and the Buckingham pi theorem` as standard. The project requires Buckingham pi, and the dossier names Buckingham pi as a main Chapter 2 mechanism. Mark the theorem and procedure core, then use the mastery box for non-unique repeating variables and advanced similarity families.

The simulation exercises are correctly marked mastery. Design and judgment as standard are defensible. The calculation, estimation, diagnosis, and failure-analysis exercises are defensibly core, but a few individual exercises need additional definitions if they remain core. A core reader has not yet learned Biot number, Prandtl number, Froude number, or drag crisis.

The mastery box is used well. It adds optional depth without breaking the main thread. It should stay, but the list of dimensionless groups should be split or line-broken to avoid the overfull habits already visible in the build log.

## G. Specific concrete fixes

1. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 4-6.

Current text: `\epigraph{If you wish to converse with me, define your terms.}{Voltaire, attributed to a letter, eighteenth century. Engineering keeps the sentiment and adds: define your units.}`

Proposed replacement: `\epigraph{Define the terms before trusting the argument.}{Engineering keeps the old philosophical demand and adds the engineering one: define the units.}`

2. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 8-13.

Current text: `Named cases: Mars Climate Orbiter (1999, revisited from chapter 1), Hubble Space Telescope primary mirror (1990), Therac-25 dosing-unit confusion (1985--1987).`

Proposed replacement: `Named cases: Mars Climate Orbiter (1999), Air Canada Flight 143 (1983), and Ariane 5 Flight 501 (1996), briefly revisited from chapter 1; Hubble Space Telescope primary mirror (1990), as a metrology-chain failure; Therac-25 (1985--1987), only where display quantities and operator interpretation are at issue.`

3. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 26-32.

Current text: `The International System of Units, in the form fixed by the General Conference on Weights and Measures in 2018 and entered into force on 20 May 2019, has seven base units defined by fixed numerical values of seven fundamental constants \cite{std:bipm-si2019}.`

Proposed replacement: `The International System of Units, in the form adopted by the General Conference on Weights and Measures in 2018 and effective from 20 May 2019, has seven base units defined by fixed numerical values of seven defining constants \cite{std:bipm-si2019}.`

4. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 67-74.

Current text: `The international prototype of the kilogram, the platinum-iridium cylinder used as the reference from 1889 to 2019, lost an estimated $50 \,\si{\micro\gram}$ of mass over a century relative to its sister copies. Whether the prototype was losing mass or its sisters were gaining it could not be settled, because the prototype \emph{was} the definition.`

Proposed replacement: `The international prototype of the kilogram, the platinum-iridium cylinder used as the reference from 1889 to 2019, diverged from its sister copies over repeated verifications. BIPM reports a median difference of about $25 \,\si{\micro\gram}$ for the original prototypes in the 1989--1991 verification; NIST summaries often describe about $50 \,\si{\micro\gram}$ over a century for official copies. The direction could not be settled from the artifact system alone, because the prototype \emph{was} the definition.`

5. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 76-82.

Current text: `The candela's status is awkward and worth naming...`

Proposed replacement: `The candela is the base unit whose definition most visibly carries a human observer. Its fixed constant is a luminous efficacy at one frequency, so photometry can report lighting, displays, and visual response in a common unit without pretending that visual brightness is radiant power alone.`

6. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 137-146.

Current text: `an electronvolt is approximately $1.602\,176\,634 \times 10^{-19} \,\si{\joule}$.`

Proposed replacement: `an electronvolt is exactly $1.602\,176\,634 \times 10^{-19} \,\si{\joule}$ in the revised SI.`

7. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 148-152.

Current text: `The prefixes go from $10^{-30}$ (quecto) to $10^{30}$ (quetta), with the additions of ronna, quetta, ronto, and quecto adopted at the 27th General Conference in 2022 \cite{std:bipm-si2019}.`

Proposed replacement: `The prefixes go from $10^{-30}$ (quecto) to $10^{30}$ (quetta). The 27th General Conference added ronna, quetta, ronto, and quecto in 2022; cite the 27th CGPM prefix resolution or the updated SI Brochure here, not a 2019-only entry.`

8. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 192-199.

Current text: `To convert an inch to a metre... 1 \,\text{ft} ...`

Proposed replacement: `To convert a foot to metres, write the original quantity, multiply by the version of $1$ that cancels the unwanted unit, and let the arithmetic run:`

9. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 242-250.

Current text: `approximately $1\,\text{atm} = 101{,}325 \,\si{\pascal}$ at sea level by definition.`

Proposed replacement: `The standard atmosphere is defined as $1\,\text{atm} = 101{,}325 \,\si{\pascal}$ exactly. Local atmospheric pressure near sea level is often close to that value, but it is a weather-dependent measurement, not a definition.`

10. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 252-260.

Current text: `Decibels are not a unit but a logarithmic ratio...`

Proposed replacement: `The decibel is a dimensionless non-SI unit accepted for logarithmic ratio quantities. A sound-pressure level in $\si{\deci\bel}$ is $20 \log_{10}(p/p_{0})$ where $p_{0}=20\,\si{\micro\pascal}$. A voltage ratio uses $20\log_{10}(V/V_{0})$ when the impedance basis is fixed. A power ratio uses $10\log_{10}(P/P_{0})$.`

11. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 374-378.

Current text: `The dimensional argument is high by about a factor of $1.6$...`

Proposed replacement: `The estimate is low by about a factor of $1.6$, which is well inside the factor-of-three band a useful estimate is supposed to land in. The factor-of-three check passed. Add the source for the $6.5\,\si{\meter\per\second}$ terminal velocity, such as Gunn and Kinzer or a later accepted correlation.`

12. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 421-423.

Current text: `The theorem was published by Edgar Buckingham in 1914 \cite{paper:buckingham1914}, building on Bridgman's later systematisation \cite{text:bridgman1922} and rediscoveries that continued through the twentieth century \cite{text:barenblatt1996}.`

Proposed replacement: `Buckingham published the theorem in 1914 \cite{paper:buckingham1914}. Bridgman later systematised dimensional analysis \cite{text:bridgman1922}; Barenblatt gives a modern treatment of scaling and similarity \cite{text:barenblatt1996}.`

13. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 438-440.

Current text: `The proof is short and is given in any modern fluid-mechanics text; we will sketch it in chapter 4 of Volume III.`

Proposed replacement: `The proof is short; we defer it to the mathematical-modelling treatment in Volume II and use the engineering procedure here.`

14. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 551-558.

Current text: `The published drag-coefficient curve for a sphere... not to discover that the drag depends on something else.`

Proposed replacement: `Experiments measure $\Phi$ and test whether the variable list was complete. A smooth sphere in an unbounded, incompressible flow collapses mainly by Reynolds number; roughness, wall effects, compressibility, and unsteady motion add further groups.`

15. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 574-580.

Current text: `a wind-tunnel model at the right Reynolds number predicts the full-scale drag coefficient, not by approximation but by the structure of the dimensional argument.`

Proposed replacement: `a wind-tunnel model can predict full-scale drag only when the relevant dimensionless groups, geometry, boundary conditions, and corrections are matched or accounted for.`

16. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 612-634.

Current text: the Hubble case ending with `\cite[ch.~5]{acc:nasa-challenger}`.

Proposed replacement: Keep the case only if a new bibliography entry is added for NASA TM-103443, `acc:nasa-hubble-optical-systems-1990`, and replace the final citation with that key. Recast the last sentence as: `The NASA Optical Systems Board of Investigation found a flawed reflective-null-corrector setup, missing independent verification, ignored auxiliary-test evidence, and cost and schedule pressure in the decision chain \cite{acc:nasa-hubble-optical-systems-1990}.`

17. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 642-667.

Current text: the Therac-25 subsection as a "dosing-unit confusion" case.

Proposed replacement: Retitle the subsection `Therac-25: unreadable displayed quantities, 1985--1987`. Replace the mechanism paragraph with a shorter sourced version: `Therac-25 belongs first to software safety and medical-device regulation. For this chapter, the relevant interface failure is narrower: operators saw messages such as ``Malfunction 54'' and dose displays that did not tell them whether a dangerous overdose had occurred. Leveson and Turner report six known overdose accidents between June 1985 and January 1987, with deaths and serious injuries, and describe the Tyler dose display as indicating an underdose while the patient had received a massive overdose.`

18. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 655-662.

Current text: `The unit-error component of the failure is one of several... silently overflowing counters... percentage of full scale rather than absolute centigrays...`

Proposed replacement: Delete these sentences unless each detail is sourced to Leveson and Turner, FDA records, or another primary or near-primary document. As written they conflate separate software failures and cannot carry a named-case claim.

19. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 668-693.

Current text: medication-unit error section with Joint Commission top-five claim.

Proposed replacement: `Medication-unit errors are a chronic class, not a single accident. They include microgram-milligram confusion, millilitre-milligram confusion where concentration matters, unsafe decimal notation, and insulin-unit abbreviation errors. Cite Joint Commission, ISMP, FDA, or peer-reviewed medication-safety sources here. Do not claim a 2025 top-five category unless the exact annual review table supports it.`

20. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 691-693.

Current text: `We will return to medication errors in chapter 5 of Volume X under the heading of human-factors failures.`

Proposed replacement: `We will return to medication errors in Volume X Chapter 9, under human factors and operator error, and in Volume VI where medical devices enter living systems.`

21. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 714-787.

Current text: project says the derivations are "stapled or bound together."

Proposed replacement: `Each derivation is one or two pages: variable list, dimensional signatures, count, repeating variables, group formation, conclusion, and comparison to the published formula. Assemble the five derivations as a short dated reference document.`

22. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 743-746.

Current text: `variables $v, \rho_{\text{sphere}}, \rho_{\text{fluid}}, g, D, \mu$ (Stokes regime and high-Reynolds regime should appear as different limits).`

Proposed replacement: `variables $v, \rho_{\text{sphere}}-\rho_{\text{fluid}}, \rho_{\text{fluid}}, g, D, \mu$; identify the Stokes and inertial-drag limits separately.`

23. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 791-798.

Current text: the exercise preface mentioning Q16.

Proposed replacement: `The exercises move from conversion and dimensional checks to estimation, simulation, design, diagnosis, failure analysis, and judgment. Calculation and derivation problems have full solutions; open-ended problems have rubrics or reference derivations.`

24. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 818-822.

Current text: `Express this in (a) BTU per hour, (b) horsepower, (c) tons of refrigeration. Identify which conversion is exact and which involves a defined constant.`

Proposed replacement: `Express this in (a) Btu/h using the International Table Btu, (b) mechanical horsepower, and (c) tons of refrigeration. State each conversion factor used and whether it is exact under that convention.`

25. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 847-850.

Current text: `A reaction has $\Delta H = -2870 \,\si{\kilo\joule\per\mole}$ for the combustion of glucose.`

Proposed replacement: `The standard molar enthalpy of combustion of glucose is about $-2803 \,\si{\kilo\joule\per\mole}$ for products $\mathrm{CO_2(g)}$ and $\mathrm{H_2O(l)}$ at standard conditions; cite the thermochemical source. Convert this value to (a) calories per mole and (b) electronvolts per molecule.`

26. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 940-946.

Current text: `Compare to the published value, current as of 2025, of $\sigma \approx 72 \,\si{\milli\newton\per\meter}$ at room temperature.`

Proposed replacement: `Compare to a cited room-temperature value for water, about $\sigma \approx 72 \,\si{\milli\newton\per\meter}$ near $20\,\si{\degreeCelsius}$ to $25\,\si{\degreeCelsius}$. This is a material property at a stated temperature, not a current-as-of statistic.`

27. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 951-958.

Current text: `Use any published correlation for $C_{D}(\mathrm{Re})$, citing the source.`

Proposed replacement: `Use a named published correlation for $C_{D}(\mathrm{Re})$ and cite it. State the correlation's Reynolds-number range before plotting.`

28. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 1051-1058.

Current text: `Describe (i) the dimensional analysis the polishing team did and got right...`

Proposed replacement: `Describe (i) the measurement chain from the metering rod to the reflective null corrector, (ii) the metrology step that produced the wrong spacing, and (iii) the auxiliary optical tests that indicated the error before launch. Cite the NASA Optical Systems Failure Report.`

29. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 1061-1067.

Current text: `Therac-25 displayed dose information using a counter whose unit interpretation depended on internal state.`

Proposed replacement: `Therac-25 displayed terse malfunction and dose information that operators could not interpret as a safety state. Argue, in 200 to 300 words, whether the useful classification is unit-interface failure, software-engineering failure, human-factors failure, or regulatory failure.`

30. File: `volumes/01-quantity/ch02-units-and-dimensions/chapter.tex`, lines 226, 804, and 1071.

Current text: `\si{\degC}`.

Proposed replacement: Use `\si{\degreeCelsius}` inside `\si{...}` expressions, or use the house macro `\degC` outside `\si{...}`. Do not nest `\degC` inside `\si{...}`.

## H. Structural risks for the larger project

1. The named-case registry is no longer optional. Chapter 2 repeats Chapter 1 cases, adds Hubble, adds Therac, and gestures at medication errors. Without a registry entry per case, the same accident will be bent to fit whichever chapter is using it. The registry should hold the canonical mechanism, primary source, secondary source, citation keys, and allowed short-form summaries.

2. The citation policy needs a "closest equivalent to primary" path for cases like Therac-25. The rule requiring primary accident reports is right, but some public engineering failures have no single public official report. The policy should say how to handle FDA records, legal depositions, peer-reviewed reconstructions based on official documents, and unavailable government files.

3. Reader-path tagging needs a dependency check. If a core project or core exercise depends on a standard section, the tag is wrong. A simple checker could scan project text for "section" references, but the real fix is editorial: every chapter review should include a path-dependency pass before exercises are accepted.
