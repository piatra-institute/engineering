---
name: Volkswagen diesel emissions defeat device
year: 2015
domain: software
primary_source: acc:epa-vw-nov-2015
secondary_sources: [acc:doj-vw-2017]
short_form: Volkswagen Group equipped approximately 11 million model-year 2009-2015 light-duty diesel vehicles worldwide with engine-control software that detected the conditions of certified emissions tests and switched the vehicle's emissions-control system into a compliant calibration only during testing; under ordinary driving the same vehicles emitted nitrogen oxides at up to forty times the regulatory limit.
status: verified
---

# Volkswagen diesel emissions defeat device, 2015

## Date(s) and location

The technical defeat-device behaviour was present from approximately model year 2009 onward in light-duty diesel vehicles produced by Volkswagen Group (Volkswagen, Audi, Porsche, SEAT, and \v{S}koda brands). Independent on-road emissions testing at West Virginia University in May 2014 produced the first quantitative public evidence of the discrepancy between certified and on-road emissions. The U.S.\ Environmental Protection Agency issued the Notice of Violation on 18 September 2015. Subsequent regulatory and legal proceedings unfolded across the United States, the European Union, and other jurisdictions through 2017 and beyond.

## Technical mechanism

The EPA Notice of Violation \cite{acc:epa-vw-nov-2015} found that Volkswagen had installed an "auxiliary emission control device" (in EPA's regulatory language) in model-year 2009-2015 light-duty diesel vehicles equipped with 2.0-litre TDI engines, with separate findings for 3.0-litre engines following in November 2015. The device was a software function within the engine-control unit (ECU) that detected the operating profile of the EPA's certified emissions test cycles, primarily the FTP-75 dynamometer schedule, by combining inputs including steering wheel angle, vehicle speed profile, engine duration, and barometric pressure.

When the software detected that the vehicle was on a certified test cycle, it activated a "dyno calibration" of the emissions-control system: the lean-NOx trap (LNT) or the selective catalytic reduction (SCR) system operated in a regime that brought NOx emissions within the regulatory limits. When the software did not detect a certified test, it switched to a "road calibration" in which the same hardware operated at substantially higher NOx output to preserve fuel economy, drivability, or component-life characteristics. Under road conditions, NOx emissions reached up to approximately forty times the U.S.\ regulatory limit \cite{acc:epa-vw-nov-2015, acc:doj-vw-2017}.

The defeat device was discovered through on-road portable-emissions-measurement-system (PEMS) testing by researchers at West Virginia University's Center for Alternative Fuels, Engines, and Emissions, working under contract with the International Council on Clean Transportation (ICCT). The discrepancy between dyno-test and on-road measurements was the diagnostic signature; subsequent regulatory investigation by the EPA and the California Air Resources Board (CARB) confirmed the software mechanism through code review and instrumented testing.

## Organisational / regulatory mechanism

The U.S.\ Department of Justice's January 2017 announcement of Volkswagen's criminal plea \cite{acc:doj-vw-2017} documents the organisational mechanism in considerable detail. The defeat-device software was developed within Volkswagen's engine-development organisation in Wolfsburg, Germany, beginning in approximately 2006 to address an engineering tradeoff: meeting the U.S.\ EPA Tier 2 Bin 5 NOx limit while preserving the fuel-economy and drivability characteristics Volkswagen had marketed to its U.S.\ customers. Internal communications cited in the DOJ filings indicate awareness within multiple levels of the engineering and management chain that the software was designed to detect and behave differently during certification testing.

The U.S.\ legal resolution included a \$4.3 billion criminal and civil penalty in January 2017, separate civil settlements with U.S.\ vehicle owners totalling approximately \$15 billion, and individual criminal charges against several Volkswagen engineers and managers. European, Asian, and other jurisdictions pursued separate regulatory and legal proceedings.

The case is canonical in regulatory engineering for two reasons. First, it demonstrates the failure mode of certification testing under conditions distinguishable from operational conditions: any test whose conditions a system can detect can be defeated by a system that adapts its behaviour to the test. Second, it demonstrates the role of independent verification: the discrepancy was discovered not by the certifying regulator but by independent on-road testing, and only after the discrepancy reached public attention did the regulatory machinery investigate.

## Lessons by scale

- Volume I, Chapter 4 ("Error and uncertainty"): the chronic-class case of an uncertainty figure (or, equivalently, a reported emissions value) chosen for institutional convenience rather than derived from operational evidence; the certified emissions are smaller than the underlying real-world data supports.
- Volume IV, Chapter 14 ("Energy systems integration") or related: the engineering tradeoff between emissions, fuel economy, and component life that the defeat device was designed to evade.
- Volume VII (multiple chapters): the software-engineering aspects of the defeat-device implementation; software-as-defeat-mechanism in safety-and-regulatory-critical systems.
- Volume X, Chapter 6 ("Software defects, races, and undefined behaviour" or similar) and Chapter 12 ("Regulation, certification, accreditation"): canonical case of intentional defeat of regulatory testing by software design; the resulting evolution of on-road testing requirements.
- Volume X, Chapter 11 ("Forensic engineering and root-cause analysis"): the forensic role of independent on-road testing in surfacing the discrepancy.
- Volume XI, Chapter 11 ("Ethics under risk and uncertainty"): canonical engineering-ethics case for an industry-wide compliance failure executed through deliberate software design.
- Volume XII (civilization-scale engineering): the case as evidence of the limits of certification-based regulation and the policy response toward in-use compliance verification.

## Citation keys

- Primary: `acc:epa-vw-nov-2015`. EPA Notice of Violation, 18 September 2015. Establishes the regulatory finding of the defeat device, the affected vehicle population, and the mechanism in EPA's regulatory language.
- Secondary: `acc:doj-vw-2017`. DOJ press release of 11 January 2017 documenting the criminal plea and providing more detailed technical and organisational mechanism narrative drawn from the underlying DOJ filings.

## Short-form summaries

\textbf{One sentence}: Volkswagen Group equipped approximately 11 million model-year 2009-2015 light-duty diesel vehicles worldwide with engine-control software that detected the conditions of certified emissions tests and switched the vehicle's emissions-control system into a compliant calibration only during testing; under ordinary driving the same vehicles emitted nitrogen oxides at up to forty times the regulatory limit.

\textbf{Two sentences}: Volkswagen's diesel-emissions defeat device, present in 2009-2015 light-duty diesel vehicles, was an engine-control software function that detected the EPA's certified emissions test cycles and activated a compliant emissions-control calibration only during those tests. Independent on-road testing by researchers at West Virginia University surfaced the discrepancy in 2014; the EPA's Notice of Violation followed in September 2015, and the U.S.\ legal resolution included a \$4.3 billion criminal and civil penalty in January 2017.

\textbf{One paragraph}: Volkswagen Group equipped approximately 11 million model-year 2009-2015 light-duty diesel vehicles with engine-control software that detected when the vehicle was on the EPA's certified emissions test cycle (using inputs including steering-wheel angle, vehicle-speed profile, and barometric pressure) and switched the vehicle's lean-NOx-trap or selective-catalytic-reduction emissions-control system into a compliant calibration only during testing. Under ordinary on-road driving, NOx emissions reached up to approximately forty times the U.S.\ regulatory limit. The discrepancy was discovered through independent on-road portable-emissions-measurement-system testing by researchers at West Virginia University in 2014, working under contract with the International Council on Clean Transportation. The EPA issued its Notice of Violation on 18 September 2015. The U.S.\ Department of Justice resolution in January 2017 included a \$4.3 billion criminal and civil penalty plus individual criminal charges against several Volkswagen engineers and managers. The case is canonical in regulatory engineering as a defeat of certification testing by software designed to detect the conditions of the test, and as evidence for the role of independent on-road verification in surfacing such defeats.

## Provenance and verification

Sources consulted: U.S.\ EPA Notice of Violation issued 18 September 2015 (the primary regulatory finding); U.S.\ Department of Justice announcement of 11 January 2017 documenting the criminal plea and the underlying technical and organisational mechanisms; contemporaneous regulatory and academic literature on the West Virginia University on-road testing programme. The 11-million-vehicle global figure, the 40-times-NOx-limit road emission figure, and the \$4.3 billion penalty figure are taken from the EPA NOV and the DOJ announcement. The technical mechanism (test-cycle detection by ECU software with switched calibration) is documented in the EPA NOV and detailed further in the DOJ filings cited by the 2017 announcement. Verified: 2026-04-29.
