---
name: Mars Climate Orbiter
year: 1999
domain: aerospace
primary_source: acc:nasa-mco-mib
secondary_sources: []
short_form: NASA's Mars Climate Orbiter was lost on 23 September 1999 when ground software supplied small-forces impulse data in pound-force seconds while the navigation interface required newton seconds, producing a cumulative trajectory error that brought the spacecraft into the Martian atmosphere during orbital insertion.
status: verified
---

# Mars Climate Orbiter, 1999

## Date(s) and location

The Mars Climate Orbiter was launched on 11 December 1998 and arrived at Mars on 23 September 1999. The spacecraft was lost during the Mars orbital-insertion burn at approximately 09:01 UTC on 23 September 1999, at the planet Mars.

## Technical mechanism

The Mishap Investigation Board found that the ground software programme `SM_FORCES` produced thruster-generated change-in-velocity data using thruster performance values in English units (pound-force seconds). The interface specification with the navigation team's `AMD` file required impulse data in metric units (newton seconds). The conversion factor of approximately $4.45$ between the two never appeared in any handoff. Over months of cruise, the small per-burn impulse error accumulated through angular-momentum-desaturation manoeuvres and trajectory-correction manoeuvres into a cumulative trajectory deflection. At Mars arrival, the spacecraft's actual closest approach was approximately $57 \,\si{\kilo\meter}$ above the Martian surface, well below the planned $193 \,\si{\kilo\meter}$ closest approach and below the spacecraft's atmospheric-survival altitude. The spacecraft entered the Martian atmosphere and was destroyed \cite{acc:nasa-mco-mib}.

The technical failure sat at the interface between contractor data and the navigation model. Each side of the interface was internally consistent. The interface document specified metric units. The producing software did not enforce the specification, and the consuming software did not verify it.

## Organisational / regulatory mechanism

The Mishap Investigation Board's recommendations centred on missing barriers rather than on individual error. The board found inadequate verification of unit consistency across the contractor (Lockheed Martin Astronautics) and operator (Jet Propulsion Laboratory) interface, inadequate review of small-forces data delivered between the two organisations, inadequate testing against flight data during cruise, and inadequate independent review of the trajectory-correction manoeuvre process. The board specifically did not blame any individual; the board's framing was that the process should not have allowed the error to reach Mars, and that several places existed where audit, review, or test would have caught the discrepancy \cite{acc:nasa-mco-mib}.

## Lessons by scale

- Volume I, Chapter 1 ("Why we measure"): the chronic measurement-failure pattern of unit confusion at an unaudited interface.
- Volume I, Chapter 2 ("Units and dimensions"): the interface-as-place-where-units-cross discipline.
- Volume IX, Chapter 14 ("Cyber-physical systems"): the interface between two software systems delivering quantities to one another.
- Volume X, Chapter 9 ("Human factors and operator error"): the absence of a unit-handoff-audit step that the operations workflow could have included.
- Volume X, Chapter 11 ("Forensic engineering and root-cause analysis"): the MIB report itself as a model of contemporary aerospace forensic engineering.

## Citation keys

- Primary: `acc:nasa-mco-mib`. NASA Mars Climate Orbiter Mishap Investigation Board Phase I Report, 10 November 1999.

## Short-form summaries

\textbf{One sentence}: NASA's Mars Climate Orbiter was lost on 23 September 1999 when ground software supplied small-forces impulse data in pound-force seconds while the navigation interface required newton seconds, producing a cumulative trajectory error that brought the spacecraft into the Martian atmosphere during orbital insertion.

\textbf{Two sentences}: The Mars Climate Orbiter was destroyed during Mars orbital insertion on 23 September 1999 because ground software at Lockheed Martin produced impulse data in pound-force seconds while the navigation software at JPL required newton seconds. The conversion factor was missing from the interface, the small per-burn error accumulated over months of cruise, and the spacecraft's closest approach to Mars was below atmospheric-survival altitude.

\textbf{One paragraph}: NASA's Mars Climate Orbiter was lost on 23 September 1999 during Mars orbital insertion. The Mishap Investigation Board found that the ground software `SM_FORCES`, used to compute thruster-generated change in velocity, used English units (pound-force seconds), while the navigation interface required metric units (newton seconds). The conversion factor of about $4.45$ never appeared in any handoff between Lockheed Martin Astronautics and the Jet Propulsion Laboratory. The small per-burn error accumulated over months of cruise into a trajectory deflection. At Mars arrival, the spacecraft's closest approach was approximately $57 \,\si{\kilo\meter}$ above the surface, below atmospheric-survival altitude. The board's recommendations centred on missing verification, audit, and test barriers rather than on individual error.

## Provenance and verification

Sources consulted: NASA Mars Climate Orbiter Mishap Investigation Board Phase I Report (10 November 1999); ESA and JPL public summaries of the mishap. The technical mechanism, conversion factor, dates, and closest-approach figures are taken from the MIB report. No independent secondary investigation has produced a different mechanism narrative. Verified: 2026-04-28.
