# Volume 1 Chapter 6 review: Time, frequency, and signals

**Resolved: 2026-04-29.** All G1-G31 fixes applied to `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex` and `bibliography/references.bib`. The voice items (B1-B11) were applied at the same time. The clock-family table now carries `\label{tab:vol01-ch06-clock-families}` and the prose uses `Table~\ref{...}`. The mains paragraph is jurisdiction-qualified, the wagon-wheel arithmetic is corrected ($88.5^{\circ}$ per frame at $24 \,\si{\hertz}$), the GPS error-source magnitudes are rewritten with citations to GPS.gov and the GPS SPS Performance Standard, the forward references are corrected (Volume II for calculus, force/energy volumes for waves, Volume VII Chapter 15 for DSP), the project safety constraints rule out direct mains-voltage work and require certified isolation, the square-wave Fourier exercise now uses sine basis with explicit Gibbs-overshoot framing, and the laptop oscillator exercise distinguishes sample-clock fractional error from cumulative timing error. New bibliography entries: `web:bipm-circular-t`, `web:bipm-cgpm2022-utc`, `web:nist-leap-seconds`, `web:usno-gps-time`, `web:gpsgov-accuracy`, `std:gps-sps-2020`. Build verified: `make distclean && make strict` produces a 693-page `main.pdf`; `make check`, `make audit-docs`, `make accidents`, and `make exercise-counts` all PASS.

Draft review returned 2026-04-29.

Build-facing note: no obvious chapter-specific build breaker was found. `make check`, `make accidents`, and `make exercise-counts` pass. `make strict` also completes and writes `main.pdf`. The chapter-specific build warnings are layout warnings, not blockers: the clock-family table at lines 305-333 produces an overfull box and LaTeX changes the `h` float specifier to `ht`. The chapter has no `\cref`, `\autoref`, or `\ref` commands beyond its own `\label{vol01:ch06}`. It does have a hard-coded "Table 1" reference with no label, which is editorially brittle.

Sources checked for this review include the local chapter dossier, the Volume I dossier, the Volume I opener, the cited BibLaTeX entries `std:bipm-si2019`, `web:nist-cesium-fountain`, `web:nist-optical-clock`, `web:nist-kibble-balance`, and `acc:gao-patriot-1992`, the Patriot Dhahran registry entry, and official external pages from GAO, BIPM, NIST, USNO, and GPS.gov. External links checked: `https://www.gao.gov/products/imtec-92-26`, `https://www.bipm.org/en/publications/si-brochure`, `https://www.bipm.org/en/cgpm-2022/resolution-4`, `https://www.nist.gov/pml/time-and-frequency-division/time-realization/primary-standard-nist-f1`, `https://www.nist.gov/pml/time-and-frequency-division/time-realization/leap-seconds`, `https://maia.usno.navy.mil/information/eo-values`, `https://www.cnmoc.usff.navy.mil/our-commands/united-states-naval-observatory/precise-time-department/global-positioning-system/usno-gps-time-transfer/`, and `https://archive.gps.gov/systems/gps/performance/accuracy/`.

## A. Verdicts

Technical: blocked. Blockers: several load-bearing numerical claims are uncited or wrong, especially the GPS error-source magnitudes, the wagon-wheel aliasing example, and one Fourier exercise; the chapter also contains wrong forward references to later chapters.

Pedagogical: blocked. Blockers: the project asks many readers to make a 24-hour high-rate recording with an unsafe or underspecified mains-coupling path; several exercises are unanswerable or misleading as written.

Voice: approved-with-corrections. The prose is mostly in register, but the chapter still contains banned negate-first-then-pivot constructions, self-announcing topic sentences, and a few hyped or over-broad sentences that sound more confident than the evidence.

## B. Voice Review

We walk the chapter in order. The voice problem is local, not pervasive. Most paragraphs are clean, but the weak sentences appear at important hinges: the opening quantification of time precision, the sampling section, the GPS section, the Patriot section, and the exercise preface.

1. Lines 50-51: "This precision is not abstract."

Rule: `docs/voice.md`, negate-first-then-pivot construction and empty emphasis. The sentence rejects "abstract" before stating the engineering consequence.

Rewrite: "This precision sets engineering budgets."

2. Lines 149-151: "The reader should retain the working principle: when a quantity can be reduced to a time measurement, its accuracy floor is set by the clock, not by the original instrument."

Rule: `docs/voice.md`, bad pedagogical signposting and negate-first-then-pivot. The idea is useful, but the sentence tells the reader what to retain and then pivots through "not by."

Rewrite: "Working principle: reducing a quantity to a time measurement moves the accuracy floor to the clock and to the model that connects the clock to the original measurand."

3. Lines 455-457: "The mains-frequency record is a publicly available time signal that the reader can measure with simple equipment. The chapter project exploits this fact."

Rule: `docs/voice.md`, self-announcing topic sentence and overstatement. "Exploits this fact" is meta-commentary, and public grid-frequency data is not universal.

Rewrite: "In many synchronous grids, the mains waveform gives the reader a measurable frequency signal; where the grid operator publishes a reference record, the reader can compare a household measurement against an institutional one."

4. Lines 550-552: "Aliasing is the single most common pathology of digital signal acquisition, and the source of more chronic measurement errors than any other sampling mistake."

Rule: `docs/voice.md`, hyped claim and generic intensifier. "Single most common" is an empirical ranking with no source.

Rewrite: "Aliasing is a common pathology of digital signal acquisition because it can produce a clean-looking sampled record with the wrong frequency content."

5. Lines 644-647: "A sample rate well above the Nyquist requirement (which is only $100$ or $120 \,\si{\hertz}$) is therefore set not by the Nyquist condition but by the desired timing resolution of zero-crossing detection."

Rule: `docs/voice.md`, negate-first-then-pivot construction.

Rewrite: "The project therefore chooses a sample rate above the formal Nyquist minimum because zero-crossing timing, sample-clock quality, and front-end delay set the measurement budget."

6. Lines 780-785: "The full treatment of windowing, leakage, spectral estimation, filter design, and the relationship between time-domain and frequency-domain measurements is in Volume II Chapter 4 (calculus machinery), Volume IV Chapter 6 (signals as physical waves), and Volume VII Chapter 7 (digital signal processing as a working discipline)."

Rule: `docs/voice.md`, performative qualifier and meta-explanation tail. The sentence is also technically wrong because the chapter numbers do not match the outline.

Rewrite: "Later chapters take up the machinery this preview names: integration and series in Volume II, physical waves in the force and energy volumes, and digital signal processing in Volume VII Chapter 15."

7. Lines 789-795: "The Global Positioning System (GPS), and the broader \engterm{Global Navigation Satellite Systems (GNSS)} that include the European Galileo, the Russian GLONASS, and the Chinese BeiDou, are measurement systems whose primary product is time and whose secondary product is position. The reader who treats GPS as a navigation tool only has missed its working role in the engineering measurement chain."

Rule: `docs/voice.md`, mild scolding and overstatement. "Has missed" talks down to the reader.

Rewrite: "The Global Positioning System (GPS), and the broader \engterm{Global Navigation Satellite Systems (GNSS)} that include Galileo, GLONASS, and BeiDou, are timing systems that solve for position through time-of-flight measurements. Navigation is the visible service; time transfer is the measurement mechanism underneath it."

8. Lines 920-921: "Relativity is not academic in GPS; it is part of the operating budget."

Rule: `docs/voice.md`, negate-first-then-pivot construction. The sentence is memorable, but the banned construction carries the force.

Rewrite: "Relativity sits inside the GPS operating budget."

9. Lines 975-976: "The technical mechanism is worth narrating in detail because every step has an analogue in measurements the reader will make."

Rule: `docs/voice.md`, self-announcing topic sentence. The prose explains why it will explain.

Rewrite: "The mechanism is the same pattern the reader will see in long-running measurement chains: representation error, accumulation, threshold crossing, and late correction."

10. Lines 1083-1086: "Test the system at the longest expected continuous run, not only at the nominal operating duration. Drift is a long-time-scale failure mode; short-time-scale tests miss it entirely."

Rule: `docs/voice.md`, "not only" construction. The engineering point is correct.

Rewrite: "Test the system at the longest expected continuous run. Drift is a long-time-scale failure mode; a short qualification test can pass while the fielded system still fails."

11. Lines 1257-1261: "The exercises move from numerical period-frequency conversions to sampling, aliasing, GPS error budgets, and clock-drift failure analysis. Closed problems have full solutions; design and judgment problems have rubrics or reference write-ups. Exercises are tagged with their reader-path tier."

Rule: `docs/voice.md`, bad pedagogical signposting. The sentence leaks internal architecture into chapter prose.

Rewrite: "The exercises begin with period-frequency arithmetic and end with sampling diagnosis, GPS error budgets, and clock-drift failure analysis."

## C. Technical Review

The chapter has the right central mechanism: time is the best realised engineering quantity, frequency is inverse time, sampling converts continuous signals into discrete records, GPS is a timing system, and the Patriot case closes the loop by showing accumulated timing error at operational scale. The structure works. The present draft fails technical review because too many numbers are carried without source-tier support, and several numerical examples are wrong.

The build and structural checks pass. The chapter cites all five BibLaTeX keys it uses, and the Patriot accident resolves to a verified registry entry. The hard-coded "Table 1" should still become a labelled table. We found no undefined cross-reference commands because the chapter uses no `\cref`, `\autoref`, or `\ref` commands.

The SI definition of the second is correct. The value $9{,}192{,}631{,}770 \,\si{\hertz}$ matches the SI Brochure. The $10^{-16}$ caesium-fountain order and low $10^{-18}$ optical-clock order are defensible against NIST and BIPM sources. The conversion from $10^{-16}$ fractional uncertainty to about $3 \,\si{\nano\second}$ per year is correct: $3.16 \times 10^{7} \,\si{\second}$ per year times $10^{-16}$ gives $3.16 \times 10^{-9} \,\si{\second}$.

The paragraph at lines 42-48 overreaches. The kilogram, kelvin, and mechanical-length comparisons need tier-appropriate sources and sharper wording. "Routine practice" is too loose, and the kelvin can be realised at different uncertainty levels depending on range and method. The claim that no other SI unit is realised with comparable fractional precision is directionally right, but it should cite BIPM or NIST mise-en-pratique material rather than a general NIST Kibble-balance page.

Lines 56-61 contain a wrong SI-constant claim. The sentence says every 2019 SI defining constant except the elementary charge and the Boltzmann constant has the second built into it through the hertz. That is not correct. The Avogadro constant has unit $\si{\per\mole}$ and does not contain the second. The elementary charge has unit $\si{\coulomb} = \si{\ampere\second}$, and the Boltzmann constant has unit $\si{\joule\per\kelvin}$, so both contain the second dimensionally through derived units. The safe claim is narrower: several practical realisations of length, voltage, and mass borrow frequency measurement, but the seven defining constants do not all have the same relation to the second.

The TAI, UTC, and GPS offsets are mostly correct as of 2026: TAI-UTC is $37 \,\si{\second}$, GPS-UTC is $18 \,\si{\second}$, and GPS time is $19 \,\si{\second}$ behind TAI. The leap-second phase-out wording is imprecise. CGPM Resolution 4 of 2022 did not simply "phase out leap seconds"; it decided that the maximum allowed UT1-UTC difference will be increased in or before 2035 and requested an implementation plan. The chapter should cite that resolution and NIST or USNO current leap-second tables.

The pendulum equation is dimensionally correct. The line "For small swings the formula is accurate to about $1\,\%$" needs an amplitude. The small-angle period error is approximately $\theta_0^2/16$ for amplitude $\theta_0$ in radians, so 1 percent error corresponds to roughly $0.4$ rad, about $23^\circ$. A serious reader will not know whether "small" means $5^\circ$, $10^\circ$, or $25^\circ$.

The clock-family catalogue is useful but under-sourced. Quartz, TCXO, OCXO, caesium beam, CSAC, and optical-clock performance bands should cite either a handbook, a standards source, or representative datasheets. The CSAC claim, $10^{-10}$ to $10^{-11}$ over months, and "a few thousand US dollars per unit, current as of 2026" are fast-aging commercial claims and need dated source support. The optical-clock "kilowatts" claim and "within the next decade" redefinition claim are plausible but need CCTF or BIPM support.

The period, frequency, angular-frequency, and phase equations check dimensionally. The phase-delay example is correct if $\Delta\varphi$ is treated as a lag magnitude. The exercise at lines 1301-1307 asks the reader to handle the sign convention, which is appropriate.

The mains-frequency paragraph is too broad. The normal and disturbance tolerances differ by synchronous area and regulatory code. A global sentence that gives $\pm 0.1 \,\si{\hertz}$ and $\pm 0.5 \,\si{\hertz}$ needs to name the grid or become an example. The integrated-time-error claim also needs jurisdictional qualification, since some regions have changed or suspended time-error correction practices.

The Nyquist condition and the 50 Hz sampled at 30 Hz alias example are correct. The wagon-wheel example is not. A wheel turning at $180 \,\si{\degree\per\second}$ advances only $7.5^\circ$ per frame at $24 \,\si{\hertz}$, not near a $90^\circ$ spoke-pattern repeat. The line multiplying $360^\circ \cdot 24$ is dimensionally disconnected from the stated wheel speed. This example must be replaced.

The anti-aliasing filter rule at lines 587-593 is unsafe as a general design rule. Sampling at four to ten times the highest frequency of interest is a useful oversampling heuristic, but setting the analog filter corner "at or below twice the highest frequency of interest" can place the corner at the Nyquist frequency when $f_s = 4 f_\text{max}$, leaving no transition band. The design rule should say to pass the highest frequency of interest with acceptable ripple and meet the required stopband attenuation by the Nyquist frequency.

The quantisation arithmetic is correct for the usual ideal ADC model: $5/2^{16} = 76.3 \,\si{\micro\volt}$ and $5/2^{12} = 1.22 \,\si{\milli\volt}$. The $q/\sqrt{12}$ statement is correct under the stated many-level assumption.

The estimation block is directionally good but mixes three error budgets. The sample rate needed for Nyquist is distinct from the sample rate needed for zero-crossing interpolation, and both are distinct from the recording-device sample-clock accuracy. A $10 \,\si{\kilo\hertz}$ sample rate is reasonable, but a naive FFT over a one-minute record has bin spacing $1/60 \,\si{\hertz} = 16.7 \,\si{\milli\hertz}$, so it cannot report $1 \,\si{\milli\hertz}$ resolution without interpolation, phase fitting, or a model-based estimator. The chapter later tells the reader that FFT peak detection suffices; that is incomplete.

The DFT preview needs one precision sentence: for real sampled signals, bins above $N/2$ represent negative frequencies or mirrored positive-frequency content. As written, "X[k] is the complex amplitude at $k f_s/N$" is acceptable for a first pass but incomplete enough to confuse the same aliasing lesson the chapter is teaching.

The GPS section needs the largest technical correction. The core pseudorange calculation is correct: $1 \,\si{\nano\second}$ times $c$ is $0.2998 \,\si{\meter}$. The relativistic correction numbers, $45$, $7$, and $38 \,\si{\micro\second}$ per day and about $11 \,\si{\kilo\meter}$ per day, are standard and numerically correct. The error-source magnitudes are the problem. The chapter gives ionospheric delay as $1$ to $10 \,\si{\nano\second}$ and tropospheric delay as $30 \,\si{\nano\second}$ at zenith. These are not good working numbers. L1 ionospheric delay is commonly several metres to tens of metres before correction, roughly tens of nanoseconds. Zenith tropospheric delay is closer to about $2.3$ to $2.6 \,\si{\meter}$, roughly $8$ to $9 \,\si{\nano\second}$, with a much larger slant delay at low elevation. The chapter should cite a GNSS text, the GPS SPS Performance Standard, or an IGS source.

The consumer GPS accuracy claim, "about $3 \,\si{\meter}$ ($95\,\%$ confidence)" for a single-frequency receiver, is optimistic unless the receiver class and environment are specified. GPS.gov gives smartphone open-sky accuracy around $4.9 \,\si{\meter}$ radius and a government signal-in-space commitment distinct from user accuracy. A safer sentence distinguishes signal-in-space, smartphone open-sky, high-quality single-frequency receivers, and RTK.

The Patriot section aligns with the GAO report and the local registry. The casualty count, date, run time, $0.34 \,\si{\second}$ accumulated error, $24$-bit fixed-point representation, $1{,}676 \,\si{\meter\per\second}$ Scud speed, $570 \,\si{\meter}$ offset, and patch-arrival date are consistent with the cited GAO source and the registry. The accident source tier is correct.

Several exercises need correction. The square-wave exercise at lines 1330-1337 is wrong: the first three odd sine terms at a quarter-period produce about $1.10A$, not within $5\,\%$ of $A$, and the exercise gives amplitudes without phases after the chapter has taught a cosine-plus-phase representation. The laptop oscillator exercise at lines 1359-1365 needs to distinguish oscillator accuracy from sample-rate calibration. The 24-hour recording project and the one-second substation design exercise need a stronger timebase calibration path.

## D. Pedagogical Review

The chapter promises to build the habit of treating time as a measured quantity, then treating frequency, phase, sampling, GPS, and clock drift as engineering consequences of that habit. That promise is sound. The ordering works: clock families, periodic quantities, sampling, Fourier preview, GPS, failure, project, exercises. The failure section closes the mechanism well because Patriot is a direct timing-accumulation case rather than a decorative accident.

The chapter respects the working-engineer depth standard better than a science-undergraduate depth standard. It avoids full Fourier analysis and full relativity derivations, which is right for Volume I. The places where it slips are not over-depth; they are under-specified engineering claims. The reader gets confident numbers for GNSS delay, grid frequency tolerance, clock classes, and ADC adequacy without the source trail that would teach how engineers defend those numbers.

The exercise mix matches Q16 on paper. We counted 28 exercises, and `make exercise-counts` agrees with the chapmeta target. The set includes calculation, derivation, estimation, simulation, design, diagnosis, failure analysis, and judgment. The balance is good: five calculation, four derivation, four estimation, four simulation, three design, four diagnosis, two failure analysis, and two judgment. The problem is calibration, not taxonomy. Several exercises assume tools or facts not yet specified, and one exercise is mathematically false.

The project is the pedagogical blocker. Q55-ch06 asks for a 24-hour mains-frequency record at one-minute resolution or finer. The chapter turns that into a continuous 24-hour raw recording in places. A mono 16-bit $44{,}100 \,\si{\hertz}$ WAV file for 24 hours is about $7.6$ GB before metadata; stereo is twice that. A 24-hour slow-motion smartphone video is unrealistic for storage, heat, and battery. The project should instead ask the reader to log one short window per minute, or to run a low-rate zero-crossing logger that stores derived timestamps rather than raw audio or video.

The safety wording also needs tightening. "Low-voltage transformer providing galvanic isolation" can be read as permission to improvise a mains transformer coupling. The project should allow only optical coupling or a sealed, certified plug-in AC-output adapter whose low-voltage side is measured. No reader should wire anything to mains conductors in Volume I.

The estimation block is a good model in spirit. It estimates before calculation, identifies the difference between Nyquist and timing resolution, and points to sample-clock and front-end uncertainty. It needs one more step: the reader must learn that frequency accuracy is controlled by the recorder's sample clock, separately from the file timestamp or NTP-synchronised wall clock. The block should explicitly require sample-clock calibration or comparison against a reference.

The archetype invocations are defensible. Scaling recurs cleanly from Chapters 1 and 2. Interface recurs from Chapters 3 and 5 and is strong in GPS. The chapter also uses failure well through Patriot. It does not introduce a new archetype, which is correct.

## E. Citation Discipline

The citation count is too low for the density of numerical and institutional claims. Only five keys are cited in the chapter. The Patriot case is properly cited to `acc:gao-patriot-1992`, and the registry entry is present and verified. The SI epigraph is properly cited to BIPM. The NIST clock citations support some of the caesium and optical-clock claims.

The following load-bearing claims need citations or cuts:

Lines 42-48: kilogram, kelvin, and metre-scale realisation uncertainty comparisons.

Lines 52-61: commercial chip-scale atomic clock access, Josephson and Kibble-balance realisation claims, and the SI-defining-constant sentence.

Lines 103-124: TAI clock ensemble size, monthly BIPM computation, UTC leap-second rule, current TAI-UTC offset, last leap second, and 2035 UTC change. Cite BIPM Circular T, BIPM time metrology, CGPM Resolution 4, NIST leap-second page, or USNO tables.

Lines 127-131: GPS epoch and 18-second offset. Cite USNO GPS Time Transfer or GPS timing data.

Lines 178-186: Huygens, Shortt-Synchronome, and observatory-standard claims. These are historical claims and need `hist:` or `text:` support.

Lines 207-259 and 288-293: quartz, TCXO, OCXO, caesium beam, CSAC, optical-clock performance, price, power, and redefinition timeline. Use `text:`, `paper:`, `web:`, or datasheet-class sources.

Lines 441-453: grid-frequency geography, normal and disturbance tolerances, and time-error correction. These need grid-code or operator citations.

Lines 501-506: sample-rate ranges for audio, high-resolution audio, industrial control, lab acquisition, and video. Some are common, but the list reads as empirical practice and should cite standards or be softened.

Lines 574-593: anti-aliasing filter attenuation and design rule. Cite a signal-processing text.

Lines 856-902: GPS error-source magnitudes and user-accuracy claims. Cite GPS SPS Performance Standard, GPS.gov accuracy page, IGS material, and a GNSS text.

Lines 904-921: GPS relativistic corrections. Cite GPS SPS material or a standard relativity-in-GPS source.

Lines 923-952: WGS 84 frame, GPSDO accuracy, and infrastructure use. Cite the WGS 84 standard, USNO, GPS.gov, or timing-system sources.

Lines 1110-1143 and 1181-1199: project tool capability, smartphone slow-motion rates, oscillator accuracy, and operator data availability. These are practical claims that need either citations or companion-note treatment.

## F. Reader-Path Tagging

The section-level path tags are mostly defensible. The core path includes time precision, clock families, period-frequency-phase, sampling and aliasing, failure, project, calculation exercises, estimation exercises, diagnosis, and failure analysis. That gives a core reader the chapter spine.

The `standard` tag on the Fourier preview is right. It is useful working apparatus, but a core reader can finish the chapter without formal spectral analysis. The GPS section as a whole is currently tagged `standard`; that is defensible if the core promise is time, frequency, sampling, and drift. We would still move the pseudorange equation and the one-nanosecond-to-thirty-centimetres working number into a short core subsection or a core boxed principle, because GPS is the chapter's strongest time-as-distance example.

The simulation exercises are rightly tagged `mastery`. No mastery box is needed in the main prose; the chapter is already a preview-heavy chapter, and forcing Fourier or relativity into a mastery box would distract from the Volume I task. A mastery box would make sense only if the author wants to include the small-angle pendulum correction or the derivation of GPS relativistic offsets.

## G. Specific Concrete Fixes

1. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 42-48.

Current text: "No other SI unit is realised with comparable fractional precision. The kilogram, since the 2019 redefinition, is realised through the Planck constant at fractional uncertainties of order $10^{-8}$ \cite{web:nist-kibble-balance}; the kelvin is realised at order $10^{-6}$ in routine practice; mechanical lengths at the metre scale are routinely realised at $10^{-7}$. Time stands several orders of magnitude ahead."

Proposed replacement: "Few engineering quantities are realised with comparable fractional precision. National mass, temperature, and length realisations can be extraordinarily good, but their routine uncertainty budgets depend on the method, range, and laboratory. For the purpose of this chapter, the important fact is narrower: frequency standards reach fractional uncertainties small enough that many other measurements are tied back to time or frequency when the measurement chain allows it \cite{web:nist-cesium-fountain,web:nist-optical-clock}."

2. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 52-61.

Current text: "A working engineer in 2026 has access, through GPS and through commercial chip-scale atomic clocks, to a local time signal whose fractional accuracy beats any other quantity in the engineer's measurement chain. Time is the quantity to which other quantities are increasingly compared: length is realised through the speed of light times an interval; voltage through the Josephson constant and a frequency; mass through the Planck constant and a frequency. Every fundamental constant that appears in the 2019 SI definitions, except the elementary charge and the Boltzmann constant, has the second built into it through the hertz."

Proposed replacement: "A working engineer in 2026 often has access to a disciplined local time signal through GPS, network time service, or a dedicated oscillator. Time also enters other measurement chains: length is realised through the fixed speed of light and measured intervals; Josephson voltage standards connect voltage to frequency; Kibble balances connect mass to the Planck constant through electrical and mechanical power. The practical lesson is that time and frequency often provide the cleanest reference in the chain, even when the final measurand is length, voltage, mass, or position."

3. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 103-105.

Current text: "International Atomic Time (TAI) is the timescale formed from a weighted ensemble of about $400$ atomic clocks at national metrology laboratories, computed and published monthly by the BIPM."

Proposed replacement: "International Atomic Time (TAI) is the timescale formed from a weighted ensemble of hundreds of atomic clocks at national metrology laboratories, computed by the BIPM and reported through Circular T \cite{web:bipm-circular-t}."

4. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 121-125.

Current text: "The IERS has not announced a leap second since the end of 2016, and the international metrology community has approved a plan to phase out leap seconds by 2035. The reader writing software in 2026 should treat the leap-second mechanism as live but politically scheduled to disappear."

Proposed replacement: "The last leap second was inserted at the end of December 2016. As of 2026, the mechanism remains live; CGPM Resolution 4 of 2022 directs that the maximum allowed UT1-UTC difference be increased in or before 2035, which would end the present pattern of frequent leap-second insertions \cite{web:nist-leap-seconds,web:bipm-cgpm2022-utc}."

5. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 127-132.

Current text: "GPS time is the timescale broadcast by the GPS satellite constellation. GPS time has no leap seconds; it was set equal to UTC at midnight on 6 January 1980 and has run at the rate of TAI ever since. As of 2026, GPS time is $18 \,\si{\second}$ ahead of UTC and $19 \,\si{\second}$ behind TAI. The fixed offsets are a feature of the timescale, not an error."

Proposed replacement: "GPS time is the timescale broadcast by the GPS satellite constellation. Its epoch is 00:00 UTC on 6 January 1980, and it is not stepped for leap seconds. As of 2026, GPS time is $18 \,\si{\second}$ ahead of UTC and $19 \,\si{\second}$ behind TAI; the GPS navigation message carries the GPS-UTC offset so receivers can present UTC when required \cite{web:usno-gps-time}."

6. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 167-176.

Current text: "A pendulum's period is approximately ... For small swings the formula is accurate to about $1\,\%$; larger swings introduce a positive amplitude correction. A one-metre pendulum has a period close to $2 \,\si{\second}$, which makes the seconds pendulum a convenient construction."

Proposed replacement: "A pendulum's small-amplitude period is approximately
\[
T = 2\pi \sqrt{\frac{\ell}{g}},
\]
where $\ell$ is the effective length and $g$ is the local gravitational acceleration. The first amplitude correction is approximately $\theta_0^2/16$ for swing amplitude $\theta_0$ in radians, so a $10^\circ$ swing changes the period by about $0.2\,\%$ and a $23^\circ$ swing by about $1\,\%$. A one-metre pendulum has a period close to $2 \,\si{\second}$, which makes the seconds pendulum a convenient construction."

7. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 207-227.

Current text: the quartz oscillator performance paragraph and aging paragraph.

Proposed replacement: "Wristwatch-grade quartz oscillators are often specified in parts per million rather than parts in $10^{9}$; $10^{-6}$ corresponds to about $32 \,\si{\second}$ per year. Temperature-compensated crystal oscillators (TCXOs) and oven-controlled crystal oscillators (OCXOs) improve that figure by controlling the crystal's temperature environment, but the exact value is a datasheet claim, not a property of quartz in general. The quartz oscillator's error budget includes aging, temperature, mechanical stress, drive level, and load capacitance. A quartz reference that has been on a shelf for ten years should be treated as an oscillator with a history, not as a fresh datasheet value."

8. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 252-259.

Current text: "Chip-scale atomic clocks (CSACs), the smallest commercial atomic standards available in 2026. They use the coherent population trapping technique on a small rubidium vapour cell, fit on a circuit board, draw a fraction of a watt, and reach fractional accuracies of about $10^{-10}$ to $10^{-11}$ over months. They make atomic-grade timekeeping available outside the laboratory, at the price of a few thousand US dollars per unit, current as of 2026."

Proposed replacement: "Chip-scale atomic clocks (CSACs), the smallest commercial atomic standards available in 2026. They use coherent population trapping in a small alkali-vapour cell, fit on a circuit board, and draw far less power than rack-scale atomic standards. Their stability, drift, aging, power, and price are commercial specifications and should be read from current datasheets; the durable point is that CSACs trade ultimate accuracy for portable holdover time."

9. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 288-293.

Current text: "Optical clocks live in laboratory racks and consume kilowatts of support equipment in 2026, so they have not yet replaced caesium as the SI definition of the second. The international metrology community has identified candidate optical transitions and is preparing for a redefinition of the second in terms of one of them within the next decade."

Proposed replacement: "Optical clocks remain laboratory systems in 2026, with lasers, vacuum systems, frequency combs, and environmental controls that keep them outside ordinary field instrumentation. They have not yet replaced caesium as the SI definition of the second. The CCTF and national metrology laboratories are preparing the technical basis for a future optical redefinition; the schedule should be cited to current BIPM or CCTF material rather than stated as a fixed decade."

10. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 297-333.

Current text: the paragraph that references "(Table 1)" and the unlabelled table.

Proposed replacement: add `\label{tab:vol01-ch06-clock-families}` immediately after the caption and change the prose to: "The four clock families form a hierarchy of accuracy and an inverse hierarchy of cost, size, and accessibility (Table~\ref{tab:vol01-ch06-clock-families}). The figures are order-of-magnitude bands for first selection; a real design uses the current datasheet or metrology report."

11. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 441-453.

Current text: "In most of the world the alternating-current power grid runs at $50 \,\si{\hertz}$; in North America and parts of South America and Asia, $60 \,\si{\hertz}$. The grid frequency is regulated by the collective action of the generators connected to it, with operating tolerances typically held within $\pm 0.1 \,\si{\hertz}$ in normal operation and within $\pm 0.5 \,\si{\hertz}$ even during disturbances. Long-term, grid operators in many jurisdictions accumulate the deviation between the integrated grid frequency and the nominal frequency, and steer the grid frequency to bring the integrated time error back to zero, so a synchronous mains-driven clock keeps long-term time on the grid."

Proposed replacement: "Most synchronous AC grids operate at a nominal $50 \,\si{\hertz}$ or $60 \,\si{\hertz}$. The permitted frequency band, disturbance limits, and time-error correction practice are grid-code matters, not universal constants. In some synchronous areas the operator also tracks integrated time error and steers the frequency over longer periods; in others the practice has changed. The chapter project should therefore ask the reader to identify the rule for their own synchronous area before comparing a household record with a published reference."

12. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 550-552.

Current text: "Aliasing is the single most common pathology of digital signal acquisition, and the source of more chronic measurement errors than any other sampling mistake."

Proposed replacement: "Aliasing is a common pathology of digital signal acquisition because it produces a plausible low-frequency record from high-frequency content that the sampler failed to exclude."

13. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 562-572.

Current text: the wagon-wheel worked example.

Proposed replacement: "A second worked example, familiar from cinema: a four-spoke wheel has the same visual pattern every $90^{\circ}$. Filmed at $24 \,\si{\hertz}$, a wheel that advances $88.5^{\circ}$ per frame is physically rotating forward at $88.5^{\circ}\times 24 = 2{,}124 \,\si{\degree\per\second}$, or $5.9$ revolutions per second. Because each frame is only $1.5^{\circ}$ short of the next spoke-pattern repeat, the sampled image appears to drift backward by $1.5^{\circ}$ per frame, or $36 \,\si{\degree\per\second}$. The eye accepts the alias because the sampled image has lost the unwrapped rotation count."

14. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 587-593.

Current text: "A working rule for engineering data acquisition: sample at four to ten times the highest frequency of interest, with an analog anti-aliasing filter whose corner frequency is at or below twice the highest frequency of interest. The factor of two over the formal Nyquist requirement gives margin against filter rolloff, phase noise on the sample clock, and spectral leakage when the samples are processed."

Proposed replacement: "A working rule for engineering data acquisition: choose the highest frequency of interest, choose the largest out-of-band signal that must be rejected, and then choose a sample rate and analog filter together. Oversampling by a factor of four to ten gives room for a transition band. The anti-aliasing filter should pass the signal band with acceptable amplitude and phase error and provide the required stopband attenuation by the Nyquist frequency, $f_s/2$."

15. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 644-653.

Current text: "A sample rate well above the Nyquist requirement ... falls back onto sample-clock quality and the analog front end's group delay."

Proposed replacement: "The project therefore chooses a sample rate above the formal Nyquist minimum because zero-crossing timing, sample-clock quality, and front-end delay set the measurement budget. With $f_s = 10 \,\si{\kilo\hertz}$, each sample is $100 \,\si{\micro\second}$. Linear interpolation between sign-change samples can improve the crossing estimate when the waveform is clean and the front-end delay is stable. Over a $60 \,\si{\second}$ window, the remaining uncertainty should be checked against the sample clock's fractional frequency error."

16. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 706-716.

Current text: the DFT definition paragraph.

Proposed replacement: "A digital recording is a finite sequence of samples, $x[0], x[1], \ldots, x[N-1]$, taken at sample rate $f_s$ over duration $N T_s$. The \engterm{discrete Fourier transform (DFT)} turns this finite sequence into $N$ complex coefficients. The bin spacing is $\Delta f = f_s/N = 1/(N T_s)$, the inverse of the recording duration. For real-valued records, bins above $N/2$ represent the negative-frequency side of the spectrum, mirrored in the usual one-sided magnitude plot."

17. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 765-778.

Current text: "Either time-domain zero-crossing detection or frequency-domain peak detection suffices ... comparable uncertainty when implemented carefully."

Proposed replacement: "The chapter project does not require formal Fourier analysis. It requires the reader to estimate the average frequency of a slowly varying near-$50 \,\si{\hertz}$ or near-$60 \,\si{\hertz}$ signal in one-minute windows. Time-domain zero-crossing detection is the cleanest route. A frequency-domain route can also work, but a one-minute FFT has bin spacing $16.7 \,\si{\milli\hertz}$, so millihertz resolution requires peak interpolation, phase tracking, or a fitted sinusoid rather than selecting the largest raw FFT bin."

18. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 780-785.

Current text: "The full treatment of windowing, leakage, spectral estimation, filter design, and the relationship between time-domain and frequency-domain measurements is in Volume II Chapter 4 (calculus machinery), Volume IV Chapter 6 (signals as physical waves), and Volume VII Chapter 7 (digital signal processing as a working discipline)."

Proposed replacement: "Later chapters take up the machinery this preview names: integration and series in Volume II, physical waves in the force and energy volumes, and digital signal processing in Volume VII Chapter 15."

19. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 856-893.

Current text: the `\begin{itemize}` block beginning with `\item \engterm{Ionospheric delay}` and ending with `\item \engterm{Receiver noise}`.

Proposed replacement:

```
\begin{itemize}[leftmargin=*]
  \item \engterm{Ionospheric delay}. For single-frequency L1 receivers,
    the uncorrected first-order ionospheric delay is commonly several
    metres to tens of metres, with larger excursions during ionospheric
    storms. Broadcast models reduce but do not remove it; dual-frequency
    receivers remove the first-order term by comparing delays at two
    carrier frequencies.
  \item \engterm{Tropospheric delay}. The neutral atmosphere contributes
    a zenith path delay of about $2.3$ to $2.6 \,\si{\meter}$, roughly
    $8$ to $9 \,\si{\nano\second}$, and a larger slant delay at low
    elevation angles through the mapping function.
  \item \engterm{Multipath}. Reflected signals corrupt the code and
    carrier measurements and can produce metre-scale errors in dense
    environments.
  \item \engterm{Satellite clock and ephemeris error}. Broadcast products
    leave residual range errors; precise products from analysis centres
    reduce orbit and clock errors for post-processed work.
  \item \engterm{Receiver noise and observable choice}. Code-phase noise
    is much larger than carrier-phase noise; carrier-phase positioning
    also has ambiguity-resolution requirements.
\end{itemize}
```

20. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 895-902.

Current text: "A consumer-grade GPS receiver in good open-sky conditions, current as of 2026, reaches horizontal accuracy of about $3 \,\si{\meter}$ ($95\,\%$ confidence) under nominal conditions, with worse performance in urban canyons or under foliage. Differential GPS (DGPS) and real-time kinematic (RTK) techniques use a reference station's measurements to correct for the common-mode errors (ionospheric, tropospheric, satellite clock and ephemeris); they reach sub-metre to centimetre accuracy under the right conditions."

Proposed replacement: "User accuracy depends on satellite geometry, signal-in-space error, atmosphere, multipath, receiver design, and processing. GPS.gov reports open-sky smartphone accuracy around a few metres and a government signal-in-space commitment that must not be confused with receiver accuracy. Differential and real-time kinematic methods use reference measurements and carrier-phase processing to move from metre-scale positioning toward sub-metre or centimetre-scale positioning when the environment, baseline, and ambiguity resolution support it \cite{web:gpsgov-accuracy,std:gps-sps-2020}."

21. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 904-921.

Current text: the GPS relativistic effects subsection.

Proposed replacement: keep the numerical values, add a citation, and replace the last sentence with: "Relativity sits inside the GPS operating budget: without these corrections, the timing error would map into position error at roughly $c \times 38 \,\si{\micro\second\per day} \approx 11 \,\si{\kilo\meter\per day}$ \cite{std:gps-sps-2020}."

22. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 940-952.

Current text: "GPS is the most widely used international time service ... GPSDOs at every infrastructure node where time synchronisation matters."

Proposed replacement: "GPS is a widely used time-transfer service. A fixed timing receiver can discipline a local oscillator to UTC(USNO) through the GPS signal, with the broadcast UTC offset specified in the GPS performance standard. GPS-disciplined oscillators are common in telecommunications, power-system measurement, scientific instrumentation, and distributed data acquisition; a real deployment still needs antenna siting, holdover design, interference monitoring, and an alternate timing plan for GPS loss."

23. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 1102-1127.

Current text: the project opening, track, and hazard text.

Proposed replacement: "The reader records or estimates the mains frequency at their location for a continuous twenty-four-hour period at one-minute resolution or finer, without any direct connection to mains-voltage conductors. The preferred track is optical: a photodiode or smartphone camera observes the flicker from a mains-powered lamp. The electrical track is allowed only with a sealed, certified plug-in AC-output adapter or other certified isolated low-voltage source; the reader does not open, modify, or wire mains equipment. If a safe isolated adapter is not already available, the optical track is mandatory."

24. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 1129-1143.

Current text: the project tools paragraph.

Proposed replacement: "Tools: a mains-powered LED or fluorescent lamp whose flicker is visible in a short test recording; a smartphone camera, photodiode circuit, or certified isolated low-voltage adapter; a recorder or logger; and software for zero-crossing detection, sinusoid fitting, or peak-frequency estimation. The durable requirement is a timestamped frequency estimate every minute. The reader may store derived zero-crossing times or one short record per minute instead of storing a continuous raw 24-hour audio or video file."

25. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 1147-1155.

Current text: "Plan the recording chain ... The sample rate must be well above the mains frequency and its flicker harmonics."

Proposed replacement: "Plan the measurement chain. Decide whether the record will be continuous raw data, short windows collected once per minute, or derived zero-crossing timestamps. Estimate storage, battery life, heat, and sample-clock accuracy before starting. The sample rate must be high enough for the estimator chosen, and the anti-aliasing or front-end bandwidth must be documented."

26. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 1174-1179.

Current text: "Analyse in one-minute windows ... by FFT peak detection on a windowed segment."

Proposed replacement: "Analyse in one-minute windows. For each segment, estimate frequency by zero-crossing detection with interpolation, by sinusoid fitting, or by an FFT method with peak interpolation or phase tracking. Do not report the largest raw FFT bin as a millihertz estimate; its spacing is $1/60 \,\si{\hertz}$ for a one-minute window."

27. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 1181-1189.

Current text: "Construct an uncertainty budget ... laptop or smartphone's own oscillator, typically $10^{-5}$ to $10^{-6}$ ..."

Proposed replacement: "Construct an uncertainty budget. List sample-clock fractional frequency error, estimator error, waveform distortion, noise, front-end delay variation, and any drift in the optical or audio coupling. If the sample clock is not disciplined to a known reference, estimate or measure its fractional error before claiming millihertz-level frequency accuracy. Propagate the components to a combined standard uncertainty per the rules of Chapter 4."

28. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 1330-1337.

Current text: "A square wave of fundamental frequency $f_{0}$ and amplitude $A$ has Fourier coefficients $a_{n} = (4A/\pi)/n$ at odd $n$ and zero at even $n$. Verify that the sum of the first three odd terms, evaluated at $t = 1/(4 f_{0})$ (a quarter-period), produces a value within $5\,\%$ of the square-wave amplitude $A$. (No calculus required; this is direct evaluation.)"

Proposed replacement: "A unit square wave with amplitude $A$ can be approximated by
\[
x_3(t)=\frac{4A}{\pi}\left[\sin(2\pi f_0 t)+\frac{1}{3}\sin(6\pi f_0 t)+\frac{1}{5}\sin(10\pi f_0 t)\right].
\]
Evaluate $x_3(t)$ at $t = 1/(4f_0)$ and compare it with $A$. Explain why the three-term approximation overshoots the plateau rather than landing within $5\,\%$."

29. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 1359-1365.

Current text: "A laptop's quartz oscillator has fractional accuracy $10^{-5}$. Estimate the cumulative timing error after a 24-hour recording. Compare to the 1-millihertz frequency-resolution requirement of the chapter project, and state whether the oscillator alone is the dominant uncertainty source."

Proposed replacement: "A recorder's sample clock has fractional frequency error $10^{-5}$. Estimate the apparent frequency error this produces when measuring a $50 \,\si{\hertz}$ signal, and compute the accumulated timing error over 24 hours. State what additional calibration would be needed before claiming $1 \,\si{\milli\hertz}$ standard uncertainty."

30. File: `volumes/01-quantity/ch06-time-frequency-signals/chapter.tex`, lines 1516-1522.

Current text: "Argue, in 200 to 300 words, whether GPS is or is not an acceptable time reference for an engineering system whose timing requirement is at the microsecond level. Take a position; defend it with at least one specific class of system (power-grid synchrophasors, financial trading, telecommunications backhaul, scientific instrumentation) where GPS is acceptable and one where it is not."

Proposed replacement: "Argue, in 200 to 300 words, when GPS is an acceptable time reference for an engineering system whose timing requirement is at the microsecond level. Take a position for one class of system where GPS timing is acceptable with proper antenna, holdover, and monitoring design, and one class where GPS alone is insufficient because jamming, spoofing, indoor operation, certification, or holdover requirements dominate."

31. File: `bibliography/references.bib`, lines near the `web:` section.

Current text: no entries for the official UTC, leap-second, GPS timing, or GPS performance sources used by the chapter.

Proposed replacement:

```
@misc{web:bipm-circular-t,
  author       = {{Bureau International des Poids et Mesures}},
  title        = {Circular T},
  howpublished = {\url{https://www.bipm.org/en/time-ftp/circular-t}},
  year         = {2026},
  note         = {Monthly publication of UTC and TAI time-scale information; last accessed 2026}
}

@misc{web:bipm-cgpm2022-utc,
  author       = {{General Conference on Weights and Measures}},
  title        = {Resolution 4 of the 27th CGPM (2022): On the Use and Future Development of UTC},
  howpublished = {\url{https://www.bipm.org/en/cgpm-2022/resolution-4}},
  year         = {2022},
  note         = {Decision to increase the maximum value for UT1-UTC in or before 2035}
}

@misc{web:nist-leap-seconds,
  author       = {{National Institute of Standards and Technology}},
  title        = {Leap Second and UT1-UTC Information},
  howpublished = {\url{https://www.nist.gov/pml/time-and-frequency-division/time-realization/leap-seconds}},
  year         = {2026},
  note         = {Current leap-second and DUT1 information; last accessed 2026}
}

@misc{web:usno-gps-time,
  author       = {{United States Naval Observatory}},
  title        = {USNO GPS Time Transfer},
  howpublished = {\url{https://www.cnmoc.usff.navy.mil/our-commands/united-states-naval-observatory/precise-time-department/global-positioning-system/usno-gps-time-transfer/}},
  year         = {2026},
  note         = {GPS time, UTC offset, satellite clocks, and GPS time steering; last accessed 2026}
}

@misc{web:gpsgov-accuracy,
  author       = {{National Coordination Office for Space-Based Positioning, Navigation, and Timing}},
  title        = {GPS Accuracy},
  howpublished = {\url{https://archive.gps.gov/systems/gps/performance/accuracy/}},
  year         = {2022},
  note         = {GPS.gov overview of user accuracy and signal-in-space accuracy}
}

@manual{std:gps-sps-2020,
  author       = {{U.S. Department of Defense}},
  title        = {Global Positioning System Standard Positioning Service Performance Standard},
  edition      = {5th},
  year         = {2020},
  note         = {Defines GPS SPS performance commitments, including UTC offset error and position-domain accuracy}
}
```

## H. Structural Risks For The Larger Project

1. The citation policy lacks a clear lane for fast-aging commercial specifications. This chapter needs current CSAC price, oscillator performance, smartphone slow-motion capability, audio-interface behaviour, and GPS receiver accuracy. The policy has `web:` and `data:`, but the review process needs a standard pattern for "representative datasheet, current as of YYYY" and a rule for moving commercial specifics to companion notes.

2. The dossier and outline do not protect forward references. This chapter points to Volume II Chapter 4 for Fourier proof, Volume IV Chapter 6 for waves, and Volume VII Chapter 7 for digital signal processing. All three are wrong against the current tree. The release checklist needs a forward-reference audit that checks named volume and chapter numbers against `docs/research` and `volumes`.

3. The project architecture needs a tractability and hazard pass before prose drafting. Q55 gives the right artifact, but the chapter turns it into a 24-hour raw recording and leaves the electrical coupling path too open. Every project brief should have a preflight line for storage, battery, data volume, tool access, and "what the reader must never wire or open."
