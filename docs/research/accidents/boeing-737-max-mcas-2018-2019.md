---
name: Boeing 737 MAX MCAS
year: 2018-2019
domain: aerospace
primary_source: no single primary report; closest-equivalent: acc:house-737max-2020
secondary_sources: [acc:jatr-737max-2019, acc:knkt-lion-air-610-2019, acc:ecaa-et302-2022]
short_form: Two crashes of Boeing 737 MAX 8 aircraft (Lion Air Flight 610 on 29 October 2018 off Indonesia and Ethiopian Airlines Flight 302 on 10 March 2019 near Ethiopia) killed 346 people; the Maneuvering Characteristics Augmentation System (MCAS) commanded nose-down stabiliser trim from a single angle-of-attack sensor in a dual-AoA-sensor aircraft, and failure of that single sensor produced repeated automatic trim against the pilots, who lacked documentation, training, or annunciation of the system's existence sufficient to diagnose and recover.
status: verified
---

# Boeing 737 MAX MCAS, 2018-2019

## Date(s) and location

Lion Air Flight 610 (Boeing 737 MAX 8, registration PK-LQP) departed Jakarta Soekarno-Hatta at 06:20 local time on 29 October 2018 and crashed into the Java Sea twelve minutes after takeoff, killing all 189 occupants \cite{acc:knkt-lion-air-610-2019}. Ethiopian Airlines Flight 302 (Boeing 737 MAX 8, registration ET-AVJ) departed Addis Ababa at 08:38 local time on 10 March 2019 and crashed near Bishoftu six minutes after takeoff, killing all 157 occupants \cite{acc:ecaa-et302-2022}. The global fleet was grounded between 13 March 2019 (China) and 18 November 2020 (FAA return-to-service order); other regulators followed on varying schedules through 2021.

## Technical mechanism

The Maneuvering Characteristics Augmentation System (MCAS) was a flight-control law added to the 737 MAX to compensate for the pitch-up tendency introduced by the larger and more forward-mounted CFM LEAP-1B engines, which changed the aircraft's longitudinal aerodynamic characteristics relative to earlier 737 generations \cite{acc:house-737max-2020}. The Joint Authorities Technical Review (JATR) and the House Committee on Transportation and Infrastructure final report identified the design as taking input from only one of the aircraft's two angle-of-attack (AoA) vanes per flight, with the active vane alternating between flights \cite{acc:jatr-737max-2019,acc:house-737max-2020}. A failed or miscalibrated AoA vane therefore produced a false high-AoA signal with no cross-comparison against the second vane and no annunciation to the flight crew that the inputs disagreed (an AoA-disagree alert existed but was tied to an optional indicator and was inoperative on most delivered MAX aircraft, a fact Boeing did not disclose to operators or the FAA for over a year) \cite{acc:house-737max-2020}.

On detecting an apparent high AoA, MCAS commanded nose-down stabiliser trim at a rate of 0.27 degrees per second for up to 9.26 seconds; the command could repeat indefinitely after a five-second pause if the AoA signal remained high \cite{acc:house-737max-2020}. The cumulative trim authority exceeded the elevator's pitch-up authority. Both accident sequences show repeated MCAS activations driving stabiliser trim to the nose-down limit, the crews countering with manual electric trim, and the cycle repeating; on ET302, after the crew followed the runaway-stabiliser memory items and disabled electric trim, aerodynamic loads on the mis-trimmed stabiliser made manual wheel trim physically infeasible at the flight's airspeed \cite{acc:ecaa-et302-2022}.

## Organisational / regulatory mechanism

The House Committee report identified a sequence of organisational decisions that produced the design \cite{acc:house-737max-2020}. The 737 MAX was developed under cost and schedule pressure from the competitive response to the Airbus A320neo; a key commercial premise was that the MAX would require no simulator training for 737NG-rated pilots, which required certifying the type as a continuation of the 737 family. MCAS was developed late in the program, after wind-tunnel testing identified the aerodynamic issue, and its authority was expanded during development without the system safety assessment being rerun against the expanded authority \cite{acc:jatr-737max-2019}. Boeing's organisation designation authorisation (ODA) arrangement with the FAA delegated significant certification work to Boeing employees; the House report identified gaps in FAA oversight of those delegations, particularly around the system safety assessment of MCAS and the human-factors analysis of MCAS failure modes \cite{acc:house-737max-2020}.

The single-AoA-sensor architecture for a function with the demonstrated authority of MCAS was inconsistent with prevailing certification expectations for high-criticality flight controls; the JATR report identified this as a finding of the technical review \cite{acc:jatr-737max-2019}. MCAS was not documented in the pilot manuals provided to airlines (a deliberate decision tied to the no-additional-training commercial premise), and an existing AoA-disagree alert that could have warned crews of the underlying sensor disagreement was rendered inoperative on most aircraft by a software issue Boeing identified in 2017 and did not disclose to the FAA until after the Lion Air crash \cite{acc:house-737max-2020}.

## Lessons by scale

- Volume IX, Chapter 14 ("Systems engineering process") and Volume IX more broadly: the gap between MCAS as documented in the system safety assessment and MCAS as built.
- Volume X, Chapter 8 ("Common-mode failure"): canonical case of dual-channel architecture defeated by single-channel input; failure of one AoA vane took down both flights despite the aircraft having two vanes.
- Volume X, Chapter 9 ("Human factors and operator error"): system whose existence was withheld from operators, whose annunciation was suppressed, and whose failure mode was not in the training corpus.
- Volume X, Chapter 10 ("Organisational failure"): commercial pressure (no-simulator-training requirement) shaping a technical design through chains of accommodation.
- Volume X, Chapter 11 ("Regulatory and certification failure"): ODA delegation gaps; FAA's reliance on Boeing-employed authorised representatives for the MCAS safety assessment.
- Volume X, Chapter 13 ("Near-misses and weak signals"): the Lion Air Flight 043 incident on the previous day (29 October 2018, prior flight of the same airframe) exhibited the same MCAS behaviour; the off-duty pilot in the jumpseat diagnosed and resolved the issue, the event was not escalated as the warning it was.

## Citation keys

- Closest-equivalent: `acc:house-737max-2020`. House Committee on Transportation and Infrastructure, "The Design, Development \& Certification of the Boeing 737 MAX," U.S.\ House of Representatives, September 2020.
- Secondary: `acc:jatr-737max-2019`. Joint Authorities Technical Review, "Boeing 737 MAX Flight Control System: Observations, Findings, and Recommendations," October 2019.
- Secondary: `acc:knkt-lion-air-610-2019`. Komite Nasional Keselamatan Transportasi (Indonesia), "Aircraft Accident Investigation Report: PT.\ Lion Mentari Airlines Boeing 737-8 (MAX); PK-LQP," KNKT.18.10.35.04, October 2019.
- Secondary: `acc:ecaa-et302-2022`. Ethiopian Civil Aviation Authority, "Aircraft Accident Investigation Bureau Final Investigation Report on Accident to Ethiopian Airlines Group B737-8 (MAX) Registered ET-AVJ," December 2022.

## Short-form summaries

\textbf{One sentence}: Two crashes of Boeing 737 MAX 8 aircraft (Lion Air Flight 610 on 29 October 2018 off Indonesia and Ethiopian Airlines Flight 302 on 10 March 2019 near Ethiopia) killed 346 people; the Maneuvering Characteristics Augmentation System (MCAS) commanded nose-down stabiliser trim from a single angle-of-attack sensor in a dual-AoA-sensor aircraft, and failure of that single sensor produced repeated automatic trim against the pilots.

\textbf{Two sentences}: MCAS, a flight-control law added to the 737 MAX to compensate for an aerodynamic pitch-up tendency from larger forward-mounted engines, took input from only one angle-of-attack vane per flight despite the aircraft having two vanes; a single failed vane could drive repeated nose-down trim commands of significant authority. On Lion Air 610 and Ethiopian 302, that single-channel input failed, MCAS repeatedly trimmed against the crews, and the crews lacked documentation, training, or annunciation of the system's existence sufficient to diagnose and recover.

\textbf{One paragraph}: The 737 MAX accidents are a canonical case of dual-channel architecture defeated by single-channel input. MCAS, developed to compensate for the changed pitch behaviour introduced by the LEAP-1B engines, was given enough authority to drive the stabiliser to its nose-down limit, but its activation logic took input from only one of the aircraft's two AoA vanes (alternating per flight). A failed AoA vane therefore produced repeated MCAS trim commands with no cross-comparison and no crew annunciation; an AoA-disagree alert that could have warned of sensor disagreement was inoperative on most delivered aircraft, a fact Boeing did not disclose to the FAA for over a year. The organisational mechanism centred on a commercial premise that the MAX would require no simulator training for 737NG-rated pilots, a premise that shaped what could be documented to operators and what could appear in training; the regulatory mechanism centred on FAA delegation arrangements that left the MCAS safety assessment and human-factors analysis substantially to Boeing-employed authorised representatives.

## Provenance and verification

Sources consulted: House Committee on Transportation and Infrastructure, "The Design, Development \& Certification of the Boeing 737 MAX," September 2020 (closest-equivalent primary, used for the regulatory-mechanism narrative and the MCAS development sequence); Joint Authorities Technical Review final report, October 2019 (used for the single-AoA architecture finding and certification-process critique); KNKT Lion Air 610 final report, October 2019 (used for the Lion Air accident sequence and Lion Air Flight 043 precursor); Ethiopian Civil Aviation Authority final report, December 2022 (used for the Ethiopian 302 accident sequence and the manual-trim aerodynamic-load detail). No single primary investigation report exists because two national investigation authorities (KNKT and ECAA) produced reports on the two accidents and the House Committee report covers the design and certification across both; the closest-equivalent designation goes to the House Committee report as the most comprehensive single account of the underlying engineering and organisational mechanism. Verified: 2026-05-16.
