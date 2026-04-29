# Volume 1 Chapter 3 review: Calibration and traceability

Resolved: 2026-04-29.

The 37 fixes in section G have been applied. The bibliography now
has four new web-tier entries (`web:bipm-kilogram-history`,
`web:nist-cesium-fountain`, `web:nist-kibble-balance`,
`web:bipm-cct-its90`) so the BIPM SI Brochure is no longer the only
source for kilogram history, cesium fountain uncertainty, Kibble
balance realisation, and ITS-90.

The chapter prose has the technical corrections to the calibration
definition (relation between indication and quantity values
provided by standards, with uncertainties on both sides);
"traceability is a property of measurement results" framing applied
throughout (the traceable-instrument shorthand has been replaced
with traceable-result language); the standards-hierarchy
rigid-three-to-five-links claim relaxed to "real chains vary";
the NMI list framed as NMIs and designated institutes; the CIPM MRA
description corrected (institutional and technical recognition
through comparisons, not automatic regulatory acceptance); the
ISO/IEC 17025 cost claim rewritten without an unsourced range and
the assessment-cycle universal claim replaced with a UKAS example;
the IPK paragraph updated with BIPM-sourced verifications (1946 second,
1989--1991 third, 2019 redefinition) and the 25 \si{\micro\gram}
median figure cited; ITS-90 corrected to fixed points plus
interpolation instruments and equations; the Hubble subsection
tightened to the registry short-form with the OSBI report cited
directly; the Josephson uncertainty range removed in favour of
a system-and-budget-dependent statement; the Kibble balance
description corrected (Planck-constant-tied methods including
Kibble balance and XRCD); the kilogram primary realisation list
generalised to "several national metrology institutes and the
BIPM"; recalibration interval claims softened to drift-risk-versus-
stakes principle; calibration price ranges removed in favour of
companion-note placement.

The voice rewrites flagged in section B are applied: the epigraph
is now sourced to VIM and the NIST traceability policy; "we unpack
it" is gone; the negate-first-then-pivot constructions are rewritten;
"by magic" and "asserts itself" are gone; self-announcing topic
sentences are removed; "few dozen operational primary realisations"
is replaced with the supported BIPM language. The exercise preface
no longer leaks Q16; the platinum thermometer exercise uses the
$W(T)$ resistance ratio convention; the voltage drift exercise
asks for worst-case allowance and uniform-distribution standard
uncertainty; the cement-style worldwide certificate count exercise
is scoped to one country with sources required; the laser distance
exercise asks for the limit length and three real error sources;
the kitchen-scale design exercise is reframed as local verification
not accredited calibration; the IPK failure-analysis exercise asks
for both Kibble-balance failure modes and the BIPM kilogram history
citation.

Three new simulation exercises now sit between estimation and design
(linear drift with random variation; five-link uncertainty chain;
recalibration cost model). The chapter has 30 exercises total,
matching the dossier and `\chapmeta` target. All exercise
subsections carry reader-path tags.

The build is clean: `make strict` produces a 553-page `main.pdf`;
`make check`, `make audit-docs`, and `make accidents` all PASS;
`grep` finds no em-dashes in the chapter source.

The structural risks named in section H (project-wide traceability
wording rule; finer-grained bibliography schema for standards-heavy
chapters; mechanical exercise-target check before review) are
recorded as Phase 0.7 work and tracked separately. The chapter-
specific exercise-count gap (27 against target 30) that the third
risk surfaced is fixed at the chapter level by the simulation
subsection landed in this resolution.

Draft review returned 2026-04-29.

Build-facing note: no obvious chapter-specific build breaker was found. `make check` passes across 174 chapter shells, `make accidents` passes, and `make strict` reported `main.pdf` up to date. This was not a forced clean rebuild. The chapter has no `\cref`, `\autoref`, or `\ref` commands beyond its own `\label{vol01:ch03}`.

Sources checked for this review include the BIPM SI Brochure page, the BIPM kilogram history page, the BIPM CIPM MRA toolbox, the NIST traceability policy and FAQ, ISO's ISO/IEC 17025 page, NIST's cesium fountain and Kibble balance pages, BIPM CCT guides to thermometry, the NASA Hubble Space Telescope Optical Systems Failure Report record, and the local Hubble named-case registry entry. Checked URLs: `https://www.bipm.org/en/publications/si-brochure`, `https://www.bipm.org/en/history-si/kilogram`, `https://www.bipm.org/en/toolbox-cipm-mra`, `https://www.nist.gov/metrology/metrological-traceability`, `https://www.iso.org/standard/66912.html`, `https://www.nist.gov/pml/time-and-frequency-division/time-realization/primary-standard-nist-f1`, `https://www.nist.gov/si-redefinition/kilogram-kibble-balance`, `https://www.bipm.org/en/committees/cc/cct/guides-to-thermometry`, and `https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19910003124.pdf`.

## A. Verdicts

Technical: blocked. Blockers: the chapter repeatedly treats traceability as a property of instruments and certificates rather than measurement results, and it makes unsupported current claims about costs, accreditation periods, recalibration intervals, and operating primary realisations.

Pedagogical: approved-with-corrections. The chapter's habit is right, but the exercise architecture misses the stated target and omits simulation, while several exercises are under-specified for a serious adult reader.

Voice: approved-with-corrections. The prose is mostly serviceable, but it contains banned "unpack" language, negate-first pivots, self-announcing sentences, and several aphoristic or overconfident claims.

## B. Voice review

We walk the chapter in order. The voice faults are not everywhere, but the worst ones coincide with definitional claims, where the book can least afford generic phrasing.

1. Lines 4-7: "A measurement that cannot be traced back to a defining constant is a private opinion expressed in the syntax of numbers."

Rule: `docs/voice.md`, no invented scenes or figures, and authority by specificity rather than aphorism. The sentence sounds memorable, but it is unsourced and technically too strong because traceability can be to specified references, not only directly to a defining constant.

Rewrite: "A measurement result earns public meaning when its value and uncertainty can be related to a specified reference through documented calibrations."

2. Line 43: "The definition is precise but dense. We unpack it."

Rule: `docs/voice.md`, AI-tic vocabulary. "Unpack" is named in the ban list.

Rewrite: "The definition has two steps."

3. Lines 48-53: "A calibration is not the act of adjusting the instrument to read correctly. Adjustment is a separate operation that the calibration may inform; an instrument that has been adjusted has not necessarily been calibrated, and an instrument that has been calibrated has not necessarily been adjusted."

Rule: `docs/voice.md`, negate-first-then-pivot. The technical distinction is necessary, but the syntax leads with negation.

Rewrite: "Calibration records the relation between indication and reference. Adjustment changes the instrument after that relation is known; the adjustment record and the calibration record serve different purposes."

4. Lines 70-72: "The chain is not optional: a reference whose own calibration is unknown produces a calibration whose meaning is unknown."

Rule: `docs/voice.md`, negate-first-then-pivot. It also compresses the traceability claim too hard.

Rewrite: "Each reference needs its own documented calibration, because an undocumented reference passes undocumented uncertainty downstream."

5. Lines 80-82: "A chapter that omits an interface in its description has produced a description in which engineering quantities arise by magic."

Rule: `docs/voice.md`, hype and theatrical flourish. "By magic" is a cute insult where a specific failure mode belongs.

Rewrite: "A chapter that omits the interface has not explained how a physical quantity became a usable indication."

6. Lines 105-108: "A calibration produces a number; an adjustment changes a setting; a verification produces a yes-or-no judgement against a specification. Section 3.4 takes up validation, the fourth member of the family, and the language gets sharper there."

Rule: `docs/voice.md`, meta-explanation tail. The first sentence is good. The second announces the chapter's own structure.

Rewrite: "A calibration produces a relation; an adjustment changes a setting; a verification produces a yes-or-no judgment against a specification; validation asks whether the measurement is fit for its intended use."

7. Lines 150-154: "Realising a primary standard is not a routine laboratory operation. A national metrology institute typically has one or two of these realisations operational at any given time. The whole edifice of calibration laboratories around the world rests on these few dozen operational primary realisations."

Rule: `docs/voice.md`, overstatement and unsupported grand framing. "The whole edifice" is rhetorical pressure, and the numerical claim is not sourced.

Rewrite: "Primary realisations require specialised apparatus, intercomparisons, and uncertainty budgets. Major national metrology institutes maintain selected realisations and disseminate them through comparisons, calibration services, and published capabilities."

8. Lines 282-286: "An ISO/IEC 17025 accreditation is not free. The application, audit, and ongoing surveillance costs run from a few thousand to several tens of thousands of dollars per year for a small laboratory, and substantially more for a high-volume one."

Rule: `docs/voice.md`, negate-first construction and current empirical claim without source. The cost may be true in some markets, but the sentence needs provenance.

Rewrite: "ISO/IEC 17025 accreditation carries application fees, assessment fees, corrective-action cost, proficiency-testing cost, and recurring surveillance cost. The chapter should give a sourced 2026 example from named accreditation bodies rather than a generic range."

9. Lines 299-302: "These three words, plus a fourth (qualification) that we will not take up here, are routinely confused in working engineering."

Rule: `docs/voice.md`, self-announcing topic sentence and "we will not" throat clearing.

Rewrite: "Working engineering separates calibration, validation, and verification because each answers a different audit question."

10. Lines 504-508: "The chain we have described looks generic when stated abstractly. At the primary-standard end of the chain it is anything but: each quantity has its own physical realisation, with its own apparatus, its own scientific community, and its own characteristic uncertainty budget. We sketch five."

Rule: `docs/voice.md`, self-announcing topic sentence and generic contrast. "We sketch five" is syllabus prose.

Rewrite: "At the primary-standard end, each quantity has its own apparatus, comparison programme, and uncertainty budget. Five examples show how different the realisations are."

11. Lines 604-611: "For working laboratories, the kelvin is disseminated through the International Temperature Scale of 1990 (ITS-90), a practical scale defined by interpolation between sixteen fixed points (the triple points of equilibrium hydrogen, neon, oxygen, argon, mercury, and water; the freezing points of indium, tin, zinc, aluminium, silver, gold, copper; and others). ITS-90 is not a definition; it is a practical realisation of the thermodynamic kelvin to within the accuracy of contemporary temperature metrology."

Rule: `docs/voice.md`, negate-first-then-pivot. It also has a technical count problem.

Rewrite: "For working laboratories, the kelvin is commonly disseminated through ITS-90, a practical temperature scale defined by fixed points, interpolation instruments, and interpolation equations. ITS-90 approximates thermodynamic temperature over defined ranges and remains the working scale for many calibrations."

12. Lines 671-678: "The case is canonical for the chapter's theme. A reference instrument is itself a measurement; treating any single instrument as the unchallengeable standard, even when it is the most precise instrument in the chain, is a discipline failure. The discipline that prevents the failure is independent verification of the reference instrument before the reference is used. The cross-check is not optional; the cross-check is what distinguishes a standard from an instrument that asserts itself to be one."

Rule: `docs/voice.md`, hype, aphorism, and negate-first pivot. "Canonical" and "asserts itself" overplay a strong case.

Rewrite: "The case fits the chapter because the reference instrument also needed verification. The missing barrier was an independent check of the reflective null corrector before the polishing process treated it as authoritative."

13. Lines 687-689: "A more chronic class of failure: a calibration laboratory's secondary standard drifts undetected, contaminating downstream calibrations. The mechanism is straightforward..."

Rule: `docs/voice.md`, fragment plus generic assurance. "Straightforward" adds no evidence.

Rewrite: "A chronic failure begins when a laboratory's reference standard drifts undetected and downstream calibrations inherit the bias."

14. Lines 810-814: "The exercises move from calibration-arithmetic and traceability-mechanics to design, diagnosis, and judgment. Calculation and derivation problems have full solutions; open-ended problems have rubrics or reference write-ups. Exercises are tagged with their reader-path tier."

Rule: `docs/voice.md`, self-announcing and internal apparatus. The line is also inaccurate because the exercise set lacks simulation and has only 27 exercises against a target of 30.

Rewrite: "The exercises should train calculation, derivation, estimation, simulation, design, diagnosis, failure analysis, and judgment, with full solutions for closed problems and rubrics for open ones."

## C. Technical review

The chapter's core direction is right: calibration establishes a relation between an indication and a reference; traceability is a documented chain with uncertainty contributions; the post-2019 SI ties base units to fixed constants; Hubble is a good case for a failed reference instrument. The technical block is a pattern of over-specific statements, not a single failed derivation.

The largest technical problem is the treatment of traceability. NIST and VIM define metrological traceability as a property of a measurement result. The chapter often writes as if instruments, certificates, laboratories, and services are themselves traceable in the same sense. That shortcut is common in shop talk, but it is exactly the shortcut Chapter 3 should correct. Lines 61-63 say an instrument with no calibration certificate has no measurement chain. Lines 205-213 say a traceable measurement result is one whose certificate can be followed link by link. Lines 291-295 imply that a non-accredited laboratory's certificate has unverified value. NIST's FAQ is sharper: a calibrated instrument alone is insufficient, and the result needs a documented chain with uncertainties. The chapter should reserve "traceable" for results and write "calibrated by a laboratory whose scope supports the claimed result" when it means instruments or services.

The standards hierarchy is too rigid. A primary standard is not simply "a physical realisation of a defined value," and "since 2019, of a defined relationship" is vague. VIM-style wording should call a measurement standard a realisation of the definition of a quantity, with stated value and uncertainty, used as a reference. Secondary standards are not always calibrated by direct comparison against a primary standard. Calibration chains can be short or long; NIST explicitly says they may vary. The line "every chain has between three and five links" is false as a general statement. It may be a useful teaching example, but the chapter states it as law.

The institutional description needs correction. The CIPM MRA is an institutional and technical framework for recognition of NMI standards, calibration certificates, and calibration and measurement capabilities. It does not by itself make every regulator accept a German PTB-traceable certificate "as if it had been issued domestically." Regulatory acceptance depends on law, accreditation, customer requirements, scope, and the relevant CMC. The chapter also says there is one NMI per major industrialised country. BIPM's own CIPM MRA material says some countries use designated institutes, and authorities other than NMIs may sign for some countries. The accreditation body under ISO/IEC 17025 is not necessarily "national" in the simplistic sense used here.

Several numerical figures need source or revision. The "examples as of 2026" list gives primary frequency uncertainty around $10^{-16}$, Josephson array uncertainty around $10^{-9}$ to $10^{-10}$, laser frequency references around $10^{-14}$, a typical four-year ISO/IEC 17025 accreditation period, one-year and six-month recalibration intervals, accreditation costs from a few thousand to several tens of thousands of dollars per year, and calibration-service prices for multimeters, thermocouples, torque wrenches, and pressure gauges. These are empirical or institutional claims. They need current sources, dates, and jurisdictions. Some are also too broad: UKAS has a four-year reassessment cycle with annual surveillance, while other accreditation bodies use different cycles. The chapter should either source a jurisdiction-specific example or avoid the universal "typically."

The SI source is stale in form. The bibliography entry `std:bipm-si2019` points to the 2019 SI Brochure, while BIPM currently cites the 9th edition as updated in 2025. A chapter making "as of 2026" claims should cite the current BIPM version or add separate entries for the 2019 SI definition and the 2025 updated brochure. The 2019 revision itself remains central, but the bibliography should not hide later updates.

The IPK section has a date and sourcing problem. BIPM's kilogram history page says divergence was found by the time of the second verification in 1946 and confirmed by the 1989 to 1991 third verification, with a median difference of about $25 \,\si{\micro\gram}$ for the original prototypes. The chapter says verifications occurred in 1939, 1989 to 1991, and 2014, then gives $25 \,\si{\micro\gram}$ and $50 \,\si{\micro\gram}$ without separate provenance. The 2014 comparison and the "order $50 \,\si{\micro\gram}$ over a century" claim may be defensible, but not from the present citation alone. The phrase "no external check" in the exercise is also too absolute. Before 2019, the IPK had no external check with definitional authority, which is a different and more accurate claim.

The Hubble subsection is technically sound in outline. The NASA OSBI report supports the 1.3 mm reflective null corrector lens spacing error, clear auxiliary-test indications, and lack of independent verification of the RNC dimensions. The local registry is verified and aligns with the paragraph. The chapter should cite the registry's short form more closely and avoid "canonical," but the source tier is correct because it uses `acc:nasa-hubble-optical-systems-1990`.

The equations mostly check dimensionally. The Josephson relation $V_n=nf/K_J$ has voltage dimensions because $K_J$ has hertz per volt. The Kibble balance exercise $m=UI/(gv)$ checks because $UI$ is mechanical power and $gv$ is $\si{\meter\squared\per\second\cubed}$. The linear drift interval formula in the exercise is dimensionally sound if $d$ is drift per unit time, $\Delta$ and $\sigma$ share the same quantity dimension, and $\Delta>k\sigma$. The exercise should state whether the random variation is one-sided or two-sided and whether $\sigma$ is stationary.

The temperature section has the clearest technical wording issue in a base-unit example. ITS-90 is not simply "sixteen fixed points." The scale includes fixed points, vapor-pressure relations, interpolation instruments, and interpolation procedures across ranges. The chapter omits gallium from the named fixed points even though a later exercise uses it, and the count does not survive a careful ITS-90 table. This is exactly the kind of sentence a thermometry reviewer will mark.

The project examples are good but need guardrails. A smartphone clock can often be traced only through a messy NTP or cellular time path, not a clean public chain to a national standard. A GPS coordinate depends on GPS system time, ephemerides, receiver algorithms, antenna environment, and a geodetic reference frame, not just a metrology-style calibration chain. Those are useful cases precisely because they expose gaps, but the project must warn the reader that these are traceability investigations, not neat chains.

## D. Pedagogical review

The chapter builds the habit promised in the dossier: a measurement gets its meaning through a documented chain, and the reader should ask where the reference came from. The core sections are in the right sequence: calibration, standards hierarchy, traceability institutions, validation and verification, drift, examples, failure, project, exercises.

The exercise architecture misses the editorial target. The `\chapmeta` and dossier both say 30 exercises. The chapter has 27: five calculation, four derivation, five estimation, three design, four diagnosis and reverse engineering, three failure analysis, and three judgment. It has no simulation exercises. Q16 names simulation as a regular exercise type, and the user prompt explicitly asks us to check it. The easiest correction is to add three simulation or spreadsheet exercises after the estimation block: simulate linear drift plus random variation, simulate uncertainty accumulation across a chain, and simulate recalibration interval cost versus out-of-tolerance risk.

The estimation block is structurally useful but technically weak. It asks the reader to estimate before reading on and uses headroom between required tolerance and instrument accuracy. That is the right habit. The numerical assumptions, however, are invented without a sourced instrument specification. A kitchen scale may have resolution, repeatability, nonlinearity, creep, and zero behavior that differ from a blanket accuracy claim. The conclusion that five-year recalibration "matches household practice" is also false in ordinary language: most households do not recalibrate kitchen scales. The block should turn into a verification-interval model: yearly check with known masses for low-stakes use, formal calibration only when the measurement has external consequences.

The project matches Q55 well. It asks for a traceability-chain document, gaps, sources, and a 1500-word reflection. It would work better if the deliverable required a chain diagram and an uncertainty table, even when the table contains unknowns. The project should also distinguish an official calibration certificate from a manufacturer specification and from a user's local check. The current wording risks teaching the reader to treat a product datasheet as a link in a calibration chain.

The failure section closes the chapter's main mechanism better than Chapter 2's case section did. IPK shows artifact-standard drift, Hubble shows a failed reference instrument, and drifting transfer standards show downstream contamination. The section still needs source discipline and should frame the third case as generic unless a named recall is added. It also needs one explicit sentence that ties failure detection to the chapter's mechanism: a standard fails safely only when independent comparisons and control data reveal the drift before downstream decisions depend on it.

The archetype invocation is partly misaligned with the volume opener. The chapter introduces "interface" in Volume I, while the opener says the remaining six archetypes, including interface, appear from Volume II onward. The dossier names interface for this chapter, so the chapter is following its own dossier. The opener should be updated, or the chapter should mark this as a preview rather than a formal first introduction.

The depth standard is right for Volume I. The chapter does not drift into metrology graduate depth. The danger is the opposite: where the source standard is complex, the prose compresses too much. We do not need a full ISO/IEC 17025 course here. We do need the distinctions to be exact enough that a calibration professional does not flinch.

## E. Citation discipline

The chapter cites `std:jcgm-vim`, `std:bipm-si2019`, `std:bipm-cipm-mra`, `std:nist-traceability`, `std:iso-iec-17025`, and `acc:nasa-hubble-optical-systems-1990`. All keys exist in `bibliography/references.bib`.

The Hubble named accident meets the primary-source rule. It also resolves to a registry entry at `docs/research/accidents/hubble-primary-mirror-1990.md`, and the chapter's mechanism agrees with that registry. The IPK is a named case rather than an accident; the current registry schema has no obvious home for it. That is acceptable for drafting, but the metadata label "Named cases" now mixes accidents and standards history. The release checklist should decide whether non-accident recurring cases need registry entries.

The standards citations are too sparse for the load they carry. `std:bipm-si2019` is used for current SI definitions, Kibble balance mass realisation, Josephson voltage, the second, kelvin realisation methods, ITS-90, and IPK verification history. Those are adjacent but not identical claims. Add BIPM current SI Brochure updated 2025, BIPM kilogram history or CGPM Resolution 1, a Kibble balance source, a CCT ITS-90 source, and a time-frequency source for the $10^{-16}$ claim.

`std:iso-iec-17025` supports the existence and high-level role of accreditation. It does not by itself support cost ranges, accreditation duration, surveillance cadence, or the claim that every downstream regulator will accept a certificate. Those need accreditation-body sources, ILAC material, or jurisdiction-specific examples.

Load-bearing claims without adequate citation include the epigraph's metrologist rule, "few dozen operational primary realisations," every calibration-service price range, typical recalibration intervals, kitchen-scale accuracy and drift assumptions, the "thousands of downstream measurements" claim, the GPS and NTP traceability examples, and all current-as-of-2026 institutional facts.

## F. Reader-path tagging

The main section tags are defensible. Calibration, standards hierarchy, traceability, drift, failure, and project are core. Cross-domain examples and validation versus verification are standard. The single mastery box on qualification is reasonable if it gains a citation or gets less industry-specific.

The exercise tags need revision after the exercise set is repaired. A missing simulation block should be `mastery` or `standard`, depending on tool burden. The derivation section is standard, which is correct. The failure-analysis section is core, which is correct because failure must close the mechanism under Q29.

The project is correctly core. It is the chapter's real proof of learning. To keep the core path honest, the project needs all required vocabulary in core sections. If GPS and smartphone time remain as suggested choices, the project should tell a core reader that a partially broken chain is an acceptable finding.

## G. Specific concrete fixes

1. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 4-7.

Current text: `\epigraph{A measurement that cannot be traced back to a defining constant is a private opinion expressed in the syntax of numbers.}{The working metrologist's rule, stated in many forms across calibration laboratories.}`

Proposed replacement: `\epigraph{A measurement result earns public meaning when its value and uncertainty can be related to a specified reference.}{A metrological rule in the vocabulary of the VIM and the NIST traceability policy.}`

2. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 13-17.

Current text: `Named cases: Hubble Space Telescope primary mirror (1990), revisited from chapter 2 as a test-instrument-as-failed-standard case; international prototype of the kilogram (1889--2019), revisited from chapter 2 as the artifact-standard divergence.`

Proposed replacement: `Named cases: Hubble Space Telescope primary mirror (1990), a verified named accident in the registry; international prototype of the kilogram (1889--2019), a standards-history case rather than an accident.`

3. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 31-41.

Current text: `\engterm{Calibration} is the operation that establishes a relationship between an instrument's indication and the value of the quantity it is intended to measure, by comparing the instrument against a reference of known accuracy.`

Proposed replacement: `\engterm{Calibration} is the operation that establishes a relation between an instrument's indication and quantity values provided by measurement standards, with uncertainties stated on both sides of the relation.`

4. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, line 43.

Current text: `The definition is precise but dense. We unpack it.`

Proposed replacement: `The definition has two steps.`

5. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 45-53.

Current text: `A calibration is, first of all, a comparison... an instrument that has been calibrated has not necessarily been adjusted.`

Proposed replacement: `A calibration begins as a comparison. The instrument produces an indication; the reference provides a value with stated uncertainty; the calibration records the relation between the two. Adjustment is a separate operation. It changes the instrument after calibration has shown what change is needed.`

6. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 55-63.

Current text: `The certificate names the instrument, the reference, the date, the operator, the conditions, the procedure, the measured indications, the corresponding reference values, the uncertainties, and a calibration interval after which the calibration is no longer asserted to hold. A reader who possesses an instrument with no calibration certificate possesses a useful object without a measurement chain.`

Proposed replacement: `The report should identify the instrument, the reference, the date, the conditions, the procedure, the indications, the corresponding reference values, and the uncertainties. A recalibration interval may appear on the certificate when required by the customer, regulator, or quality system. Without records of calibration and use, the owner has an instrument, but not enough evidence to claim traceability for a measurement result.`

7. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 65-72.

Current text: `A calibration is, third, a discipline that depends on a reference whose own calibration is known... a reference whose own calibration is unknown produces a calibration whose meaning is unknown.`

Proposed replacement: `A calibration also depends on the reference's documented status. The laboratory voltage source is calibrated against a transfer standard; the transfer standard is calibrated through a higher-level electrical standard; the primary realisation is tied to Josephson and quantum Hall effects and the SI constants. Each undocumented link adds an undocumented uncertainty to the result below it.`

8. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 74-83.

Current text: `\begin{archetype}[Interface] ... engineering quantities arise by magic. \end{archetype}`

Proposed replacement: `\begin{archetype}[Interface]
The interface archetype appears here as the calibration interface. An interface is a place where a physical quantity becomes a representation that another system can use. A calibration interface relates a mass, voltage, length, frequency, or temperature to an instrument indication, with uncertainty attached to the relation. If the interface is omitted, the account has not explained how the quantity became usable.
\end{archetype}`

9. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 112-124.

Current text: `A measurement standard is a physical realisation of a defined value (or, since 2019, of a defined relationship) that other instruments can be calibrated against.`

Proposed replacement: `A \engterm{measurement standard} is a realisation of the definition of a quantity, with a stated value and measurement uncertainty, used as a reference. Some standards are artifacts, some are instruments or systems, and some are realised through quantum or thermodynamic effects.`

10. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 126-148.

Current text: `Examples of primary realisations as of 2026:` followed by the six-item list.

Proposed replacement: `Examples of primary realisations, current for the post-2019 SI, include Kibble balances and silicon-sphere XRCD methods for mass, laser interferometry tied to the second for length, cesium fountain clocks for the second, Josephson voltage standards for voltage, quantum Hall resistance standards for resistance, and several primary thermometry methods for the kelvin. Each example needs its own source: the current BIPM SI Brochure for definitions, a time-frequency source for cesium fountain uncertainties, a Kibble-balance source for mass realisation, and a CCT ITS-90 or kelvin mise-en-pratique source for thermometry.`

11. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 150-154.

Current text: `Realising a primary standard is not a routine laboratory operation... rests on these few dozen operational primary realisations.`

Proposed replacement: `Primary realisation is specialised work. National metrology institutes and designated institutes maintain selected realisations, compare them internationally, and publish calibration and measurement capabilities. The dissemination system rests on those realisations, their comparisons, and the documented uncertainty budgets that connect them to working laboratories.`

12. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 158-171.

Current text: `A \engterm{secondary standard} is a standard calibrated by direct comparison against a primary standard, used to disseminate the unit.`

Proposed replacement: `A \engterm{secondary standard} is a standard whose value is established by calibration with respect to a primary standard or another higher-order reference for the same quantity. It disseminates the unit through a documented calibration chain rather than by definitional authority.`

13. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 189-194.

Current text: `The hierarchy is concrete: every chain has between three and five links.`

Proposed replacement: `A simple teaching chain has three to five visible links, but real chains vary. A user may have a short chain through a direct NMI calibration, or a longer chain through accredited laboratories, reference standards, transfer standards, and internal checks.`

14. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 221-249.

Current text: the institutional list under "Who maintains the chain."

Proposed replacement: revise the NMI bullet to read `National metrology institutes and designated institutes. NIST, NPL, PTB, NRC, NMIJ, NIM, VNIIM, CSIR-NPLI, and other bodies operate national or designated metrology functions. Some countries use more than one designated institute for different fields. These institutes maintain realisations, participate in comparisons, and issue calibration certificates within published scopes.` Revise the accredited-laboratory bullet to read `Accredited calibration laboratories, assessed against ISO/IEC 17025 by recognised accreditation bodies. These laboratories disseminate calibration services to industry and research within their accredited scopes.`

15. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 253-269.

Current text: `A measurement made in a German plant against a PTB-traceable calibration must be acceptable to a Brazilian regulator... as if it had been issued domestically.`

Proposed replacement: `A manufacturer wants a calibration certificate issued under one national metrology system to be intelligible and acceptable in another. The CIPM MRA supports that by recognising NMI standards, calibration certificates, and published calibration and measurement capabilities through comparisons, quality systems, and peer review. Legal or regulatory acceptance still depends on the regulator, the accreditation scope, and the requirement being applied.`

16. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 282-289.

Current text: `An ISO/IEC 17025 accreditation is not free... typically four years... surveillance audits in between...`

Proposed replacement: `ISO/IEC 17025 accreditation has direct and recurring cost: application, assessment, corrective action, proficiency testing, documentation, and surveillance. Assessment cycles are set by accreditation bodies, so the chapter should give named examples rather than a universal period. For example, UKAS uses annual surveillance with periodic full reassessment; other bodies use different cycles.`

17. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 291-295.

Current text: `A reader who buys a calibration service from a non-accredited laboratory has a certificate of unverified value.`

Proposed replacement: `A reader who buys a calibration service outside an accredited scope must inspect the evidence directly: method, reference standards, uncertainty budget, competence, and traceability statement. Accreditation packages that evidence in a recognised form; it does not replace the user's duty to read the certificate.`

18. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 299-302.

Current text: `These three words, plus a fourth (qualification) that we will not take up here, are routinely confused in working engineering. The international vocabulary of metrology and the major quality-system standards distinguish them sharply \cite{std:jcgm-vim}.`

Proposed replacement: `Working engineering separates calibration, validation, and verification because each answers a different audit question. The vocabulary comes from VIM and quality-system standards; cite VIM for calibration and verification, and add an ISO 9000 or sector-specific source if validation and qualification are treated here.`

19. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 344-354.

Current text: the mastery box on qualification.

Proposed replacement: keep the box, but add a source and tighten the closing sentence: `Qualification has substages such as installation qualification, operational qualification, and performance qualification in pharmaceutical and life-science practice. The structure resembles validation and verification, but the governing vocabulary is sector-specific. A reader in a regulated industry learns the local standard and procedure before using the generic terms.`

20. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 415-423.

Current text: `A typical interval for a working laboratory instrument is one year; for a critical instrument in a regulated environment, six months...`

Proposed replacement: `Many laboratories begin with a manufacturer recommendation, customer requirement, regulatory requirement, or local default interval, then adjust the interval using calibration history and risk. The chapter should give sourced examples only by instrument class and jurisdiction. The general rule is drift risk versus measurement stakes, not a universal calendar interval.`

21. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 443-449.

Current text: the four calibration price ranges.

Proposed replacement: `Calibration costs vary by scope, accredited status, points measured, turnaround, and on-site work. Replace the generic price list with a sourced 2026 table from named providers or accreditation bodies, or mark the values as illustrative and move the live prices to a companion note.`

22. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 470-499.

Current text: the kitchen-scale estimation answer.

Proposed replacement: `A working estimate starts from the user's tolerance, not from the scale's display resolution. If the application allows $\pm 5 \,\si{\gram}$ and the scale repeats within about $\pm 1 \,\si{\gram}$ under a local check, the immediate risk is small. A yearly check with two or three known masses is usually more defensible than pretending the household scale has a formal five-year recalibration interval. If the check shows a bias near the tolerance, the scale is no longer fit for that use. If the application requires $\pm 1 \,\si{\gram}$, the tolerance is the same size as the scale's likely repeatability, and the correct engineering answer is a better instrument or a lower-stakes measurement.`

23. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 512-528.

Current text: the Josephson voltage subsection.

Proposed replacement: keep the equation, but replace `with fractional uncertainty around $10^{-9}$ to $10^{-10}$` with `with uncertainty set by the realised system, comparison method, and uncertainty budget. Add a voltage-standards source if a numerical uncertainty is retained.`

24. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 532-550.

Current text: `The kilogram, since 2019, is realised through the Kibble balance... operated at NIST, NPL, NRC, the BIPM, and a handful of other national institutes.`

Proposed replacement: `The kilogram, since 2019, is realised through methods tied to the fixed value of the Planck constant, including Kibble balances and silicon-sphere XRCD measurements. A Kibble balance compares mechanical and electrical power; its voltage and resistance measurements connect to Josephson and quantum Hall effects. Name only institutes supported by a current source, or write "several national metrology institutes and the BIPM" without a list.`

25. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 604-614.

Current text: `ITS-90, a practical scale defined by interpolation between sixteen fixed points...`

Proposed replacement: `For working laboratories, the kelvin is often disseminated through the International Temperature Scale of 1990 (ITS-90), a practical scale defined by fixed points, interpolation instruments, and interpolation equations over specified ranges. Its fixed points include cryogenic points, the triple point of water, the melting point of gallium, and the freezing points of indium, tin, zinc, aluminium, silver, gold, and copper. Add a BIPM CCT ITS-90 guide citation here.`

26. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 633-655.

Current text: the IPK divergence paragraph.

Proposed replacement: `The international prototype of the kilogram (IPK) was the world's mass standard from 1889 until the revised SI took effect on 20 May 2019. BIPM records divergence among prototypes by the second verification in 1946 and a median difference of about $25 \,\si{\micro\gram}$ for the original prototypes in the 1989--1991 verification. Larger century-scale figures for official copies need a separate source. The technical lesson is that an artifact definition cannot distinguish unit drift from artifact drift using artifacts alone.`

27. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 657-683.

Current text: the Hubble subsection.

Proposed replacement: use the registry short form with less rhetoric: `The Hubble Space Telescope launched in April 1990 with a primary mirror figured to the wrong shape. The NASA Optical Systems Board of Investigation traced the error to the reflective null corrector used during polishing: a field lens was mispositioned by about $1.3 \,\si{\milli\meter}$ along the optical axis, and auxiliary tests that showed the discrepancy were discounted \cite{acc:nasa-hubble-optical-systems-1990}. The missing barrier was independent verification of the test instrument before it became the authoritative reference.`

28. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 685-717.

Current text: the drifting transfer standards subsection.

Proposed replacement: introduce it as generic unless a named case is added: `A generic but common failure begins when a laboratory reference standard drifts undetected between external calibrations. Every working instrument calibrated against it inherits part of the bias. If the next external calibration reveals the problem, the laboratory must assess affected certificates, notify customers where required, and decide whether corrected results or recalls are necessary. Add a real recall or standards source if the "thousands of downstream measurements" claim remains.`

29. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 748-755.

Current text: the smartphone clock and GPS project options.

Proposed replacement: `A smartphone clock reading. Trace as far as the device and network documentation allow: operating-system time service, cellular or NTP source, server stratum or carrier time source, and the reference clock above it. Expect gaps.` Replace the GPS bullet with `A GPS position reading. Trace the timing chain, satellite ephemeris source, receiver assumptions, and geodetic reference frame. Treat this as a gap-finding exercise rather than a clean calibration chain.`

30. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 808-814.

Current text: the exercise preface.

Proposed replacement: `The exercises must train calculation, derivation, estimation, simulation, design, diagnosis, failure analysis, and judgment. The present draft needs three added exercises to meet the target of 30 and to include simulation. Calculation and derivation problems have full solutions; open-ended problems have rubrics or reference write-ups.`

31. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 837-844.

Current text: the platinum resistance thermometer exercise.

Proposed replacement: `A platinum resistance thermometer is calibrated at the triple point of water and the melting point of gallium. For the narrow interval between those points, write a local linear interpolation in the resistance ratio $W(T)=R(T)/R(273.16\,\si{\kelvin})$. Then explain why ITS-90 uses specified interpolation functions and additional fixed points rather than a single linear rule when the range extends toward $200 \,\si{\degreeCelsius}$.`

32. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 846-852.

Current text: the voltage-standard drift exercise.

Proposed replacement: `A working laboratory's secondary voltage standard is rated at $10.000\,000 \,\si{\volt}$ with a drift limit of $\pm 0.5 \,\si{\micro\volt}$ per year. It was last calibrated $24$ months ago. Compute the worst-case drift allowance, then compute the standard uncertainty if the drift is modelled as uniformly distributed within that allowance.`

33. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 920-928.

Current text: the worldwide calibration certificate estimation exercise.

Proposed replacement: `Estimate the number of calibration certificates issued per year in one country of your choice. Use a sourced count of accredited calibration laboratories if available, estimate certificates per laboratory per year, and state what the estimate excludes: internal checks, non-accredited calibrations, manufacturer calibrations, and NMI services.`

34. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 930-935.

Current text: the laser distance meter estimation exercise.

Proposed replacement: `Estimate the length at which a fractional frequency uncertainty of $10^{-7}$ would correspond to a length uncertainty of $1 \,\si{\milli\meter}$ in an ideal time-of-flight distance meter. Then name at least three real error sources that dominate before that theoretical limit in a handheld instrument.`

35. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, after line 952.

Current text: no simulation subsection.

Proposed replacement: insert:

```
\subsection*{Simulation}\pathtag{standard}

\begin{exercise}
Simulate an instrument whose bias drifts linearly at rate $d$ and whose readings include Gaussian random variation with standard deviation $\sigma$. For several recalibration intervals, estimate the probability that the instrument exceeds tolerance before the next calibration.
\end{exercise}

\begin{exercise}
Simulate a five-link traceability chain in which each link contributes an independent standard uncertainty. Compare equal-link uncertainties with a chain dominated by one weak link, and plot the combined uncertainty in each case.
\end{exercise}

\begin{exercise}
Build a simple cost model for recalibration interval choice. Include calibration cost, downtime cost, and an estimated cost for discovering an out-of-tolerance condition late. Identify the interval that minimises expected cost under your assumptions.
\end{exercise}
```

36. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 955-964.

Current text: the kitchen-scale design exercise using coins and sealed packages.

Proposed replacement: `Design a local verification procedure for a household kitchen scale using one or more low-stakes references: a calibration mass with stated tolerance, coins whose official mass and wear condition are considered, or a sealed package whose labelled net mass is treated only as a rough check. State why this is a verification check rather than an accredited calibration.`

37. File: `volumes/01-quantity/ch03-calibration-and-traceability/chapter.tex`, lines 1031-1036.

Current text: `The pre-2019 international prototype of the kilogram, as the artifact-based mass definition, had no external check.`

Proposed replacement: `The pre-2019 international prototype of the kilogram, as the artifact-based mass definition, had no external standard with equal definitional authority. Describe how the post-2019 SI redefinition changes that problem, and identify what new failure modes Kibble-balance and XRCD realisations introduce that the IPK did not have.`

## H. Structural risks for the larger project

1. The traceability policy needs a project-wide wording rule. Chapters should reserve "metrological traceability" for measurement results and use different wording for instruments, certificates, laboratories, and services. Otherwise the book will teach the common shorthand while claiming to teach the discipline.

2. The bibliography schema needs finer standards entries. One BIPM SI entry cannot carry every current SI, Kibble balance, ITS-90, CIPM MRA, and kilogram-history claim. Before reviewing more metrology-heavy chapters, add source slots for current standards pages, mises en pratique, CCT guides, accreditation body examples, and standards-history pages.

3. The exercise architecture needs a mechanical target check. This chapter says 30 exercises and supplies 27, with no simulation. A release check should count exercises by subsection and compare them against `\chapmeta`, Q16, and the dossier before review. Reviewers should spend judgment on quality, not on recounting exercise blocks by hand.
