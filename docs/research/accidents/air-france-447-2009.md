---
name: Air France Flight 447
year: 2009
domain: aerospace
primary_source: acc:bea-af447
secondary_sources: []
short_form: Air France Flight 447, an Airbus A330-203 on a scheduled flight from Rio de Janeiro to Paris, crashed into the Atlantic on 1 June 2009 with the loss of all 228 people aboard; the BEA's investigation found that ice crystals at altitude obstructed all three of the aircraft's pitot tubes simultaneously, producing inconsistent airspeed indications, after which the autopilot disengaged and the flight crew, in cruise turbulence with conflicting cockpit information, allowed the aircraft to enter a stall from which they did not recover.
status: verified
---

# Air France Flight 447, 2009

## Date(s) and location

Air France Flight 447 was a scheduled passenger flight from Rio de Janeiro--Galeao International Airport to Paris--Charles de Gaulle Airport. The aircraft, an Airbus A330-203 registered F-GZCP, departed Rio at 22:29 UTC on 31 May 2009 and entered the radar gap over the equatorial Atlantic on 1 June 2009. The aircraft transmitted an Aircraft Communications Addressing and Reporting System (ACARS) message indicating multiple equipment failures at 02:10 UTC on 1 June. The aircraft impacted the Atlantic Ocean approximately three minutes later. All 228 people aboard (216 passengers and 12 crew) died. The flight recorders were recovered from the seabed in May 2011, almost two years after the accident, after extended search operations.

## Technical mechanism

The Bureau d'Enqu\^etes et d'Analyses pour la s\'ecurit\'e de l'aviation civile (BEA) issued the final report on 5 July 2012 \cite{acc:bea-af447}. The BEA identified the precipitating event as the temporary obstruction of the aircraft's three pitot probes by ice crystals at high altitude as the aircraft transited the Intertropical Convergence Zone. Airbus A330 aircraft had a known susceptibility to pitot-probe icing under specific high-altitude conditions; the issue had been discussed in earlier service bulletins, and a programme to replace the affected Thales AA model probes with a less susceptible Thales BA or Goodrich design was already underway across the global A330 fleet. F-GZCP had not yet had its pitot probes replaced.

The pitot obstruction lasted approximately one minute and produced inconsistent airspeed indications across the three probes. The aircraft's flight-control system recognised the inconsistency, transitioned the autopilot from normal-law operation to alternate law, disengaged the autothrust, and disengaged the autopilot. The flight crew assumed manual control of the aircraft in cruise turbulence with no reliable airspeed indication and with conflicting cockpit information.

The crew applied a sustained nose-up sidestick input that, combined with the loss of airspeed reference and the aircraft's transition out of normal-law protections, caused the aircraft to climb above its cruise altitude and enter a stall. The stall warning sounded repeatedly during the descent. The pitot probes recovered approximately one minute after the initial obstruction; valid airspeed indications were restored to the cockpit displays. The crew did not recognise the stalled state of the aircraft; the captain (who had been on rest break at the start of the event) returned to the cockpit but did not assume control. The aircraft descended in a deep stall at high angle of attack and high vertical descent rate from approximately $35{,}000 \,\text{ft}$ until impact.

The technical lesson for sensor and instrumentation engineering: three independent pitot probes shared a single environmental cause (high-altitude ice-crystal cloud) and failed simultaneously. Independence in design did not guarantee independence in failure. The BEA's recommendations included improved pitot-probe icing performance at altitude, improved cockpit handling of unreliable airspeed conditions, improved crew training for high-altitude upset recovery, and improved crew-resource-management procedures for unreliable airspeed events.

## Organisational / regulatory mechanism

The BEA's report identified contributing factors beyond the technical mechanism. Airbus A330 unreliable-airspeed events had been reported across the fleet for several years before AF447, and the aircraft manufacturer and the relevant national aviation authorities (DGAC, EASA, FAA) had been working through a service-bulletin programme to replace the affected pitot probes. The programme's pace was, in retrospect, not commensurate with the operational risk; replacement was ongoing rather than mandatory at the time of the accident. The crew's training in unreliable-airspeed handling and high-altitude manual flight had been documented in operations manuals, but the training did not match the actual cockpit experience the AF447 crew encountered. Crew-resource-management procedures for the captain returning to the cockpit during an in-flight emergency were not standardised across operators.

The case has become canonical in aviation safety for several reasons. It is the most-studied modern example of an unreliable-airspeed event leading to loss of control. It is also a canonical case in human-factors and crew-resource-management research, in autopilot-handoff design, and in high-altitude-stall-recovery training. Subsequent regulatory action included EASA airworthiness directives mandating the pitot replacement, revised crew-training requirements for unreliable airspeed and high-altitude upset, and changes to A330 autoflight handoff design.

## Lessons by scale

- Volume I, Chapter 1 ("Why we measure"): the failure of an unverified measurement to support a high-stakes decision under stress.
- Volume I, Chapter 5 ("Sensors and instruments"): canonical case of common-mode sensor failure, in which three nominally independent sensors fail simultaneously because they share an environmental cause; the lesson that sensor independence in design does not imply sensor independence in failure.
- Volume IX (control and stochastic systems): autopilot handoff to manual control under inconsistent measurement conditions; the design of fall-back control modes when the flight envelope's measurement basis is degraded.
- Volume X (multiple chapters): canonical case of human-factors failure under time pressure, conflicting cockpit information, and degraded automation.
- Volume X, Chapter 9 ("Human factors and operator error"): crew response to unreliable airspeed indications and high-altitude stall recovery.
- Volume XI, Chapter 9 ("Design reviews, certification, sign-off"): the regulatory programme's pacing relative to the underlying operational risk.

## Citation keys

- Primary: `acc:bea-af447`. Bureau d'Enqu\^etes et d'Analyses pour la s\'ecurit\'e de l'aviation civile, Final Report on the Accident on 1st June 2009 to the Airbus A330-203 registered F-GZCP operated by Air France flight AF 447 Rio de Janeiro--Paris, 5 July 2012.

## Short-form summaries

\textbf{One sentence}: Air France Flight 447, an Airbus A330-203 on a scheduled flight from Rio de Janeiro to Paris, crashed into the Atlantic on 1 June 2009 with the loss of all 228 people aboard; the BEA's investigation found that ice crystals at altitude obstructed all three of the aircraft's pitot tubes simultaneously, producing inconsistent airspeed indications, after which the autopilot disengaged and the flight crew, in cruise turbulence with conflicting cockpit information, allowed the aircraft to enter a stall from which they did not recover.

\textbf{Two sentences}: AF447's three pitot probes iced over simultaneously at high altitude on 1 June 2009 because they shared a single environmental cause, the aircraft's autopilot disengaged on inconsistent airspeed inputs, and the flight crew was left flying the aircraft in cruise turbulence without a reliable airspeed reference. The crew applied sustained nose-up control inputs and the aircraft entered a deep stall from $35{,}000 \,\text{ft}$ that they did not recognise or recover from before impact.

\textbf{One paragraph}: On 1 June 2009 Air France Flight 447, an Airbus A330-203 from Rio de Janeiro to Paris, crashed into the Atlantic with the loss of all 228 people aboard. The BEA's final report (2012) identified the precipitating event as the temporary obstruction of all three pitot probes by ice crystals at high altitude as the aircraft transited the Intertropical Convergence Zone. The pitot obstruction lasted about one minute, produced inconsistent airspeed indications, and triggered the autopilot to disengage and the flight-control system to transition out of normal-law protections. The crew assumed manual control with conflicting cockpit information; sustained nose-up sidestick inputs caused the aircraft to climb above its cruise altitude and enter a stall. The crew did not recognise the stalled state, and the aircraft descended in a deep stall at high angle of attack from $35{,}000 \,\text{ft}$ until impact. The case is canonical in sensor and instrumentation engineering as an example of common-mode sensor failure: three independent pitot probes shared a single environmental cause and failed simultaneously, breaking the assumption that design independence guarantees failure independence. Subsequent regulatory action included pitot replacement, revised unreliable-airspeed training, and changes to autoflight handoff design.

## Provenance and verification

Sources consulted: BEA Final Report on the Accident on 1st June 2009 to the Airbus A330-203 registered F-GZCP, 5 July 2012. Crew composition, aircraft registration, sequence of events, pitot probe model, and the BEA's recommendation list are taken from the report. The ACARS message timing, autopilot transition, and recovery-of-airspeed-indications timeline come from the report's chronology. Verified: 2026-04-29.
