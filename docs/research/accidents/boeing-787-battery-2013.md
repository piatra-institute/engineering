---
name: Boeing 787 lithium-ion battery incidents
year: 2013
domain: aerospace
primary_source: acc:ntsb-aar14-01-787-battery
secondary_sources: []
short_form: A lithium-ion auxiliary-power-unit battery aboard a Japan Airlines Boeing 787-8 caught fire at the gate at Boston Logan on 7 January 2013; cell-to-cell thermal propagation from a short circuit in one cell consumed the eight-cell pack and led the FAA to ground the global 787 fleet for three months.
status: verified
---

# Boeing 787 lithium-ion battery incidents, 2013

## Date(s) and location

7 January 2013, Boston Logan International Airport, Massachusetts. The aircraft, a Japan Airlines Boeing 787-8 registered JA829J, had just completed a scheduled passenger flight from Tokyo Narita and was parked at gate E20 when smoke and fire were observed from the aft electronic-equipment bay (NTSB AIR-14/01, pp.~1--2). A second 787, an All Nippon Airways aircraft, made an emergency descent and landing at Takamatsu, Japan, on 16 January 2013 following an in-flight battery event of the same class; the FAA grounded the global 787 fleet on the same day, lifting the grounding on 19 April 2013 after Boeing redesigned the battery enclosure (NTSB AIR-14/01, pp.~2, 60).

## Technical mechanism

The battery was a $32\,\text{V}$, $75\,\text{Ah}$ lithium-ion auxiliary-power-unit pack of eight cobalt-oxide cells (LiCoO$_2$ cathode, graphite anode) in series, manufactured by GS Yuasa with a battery-management unit by Securaplane (NTSB AIR-14/01, pp.~9--12). An internal short circuit developed within cell~5 of the pack, identified post-event by tear-down as having initiated near a defect in the jelly-roll structure of the electrode assembly (NTSB AIR-14/01, pp.~71--75). The short produced localised joule heating sufficient to drive the cell into thermal runaway: the cathode released oxygen above approximately $180\,\degC$, the electrolyte (a lithium-salt solution in carbonate solvents) decomposed and ignited, and the cell vented hot gas and electrolyte at temperatures in excess of $600\,\degC$ (NTSB AIR-14/01, p.~75). Heat transfer to adjacent cells through the conductive nickel-plated steel can and the shared electrolyte mist drove cell~6, then cells~3 and~7, into thermal runaway in succession; the cascade is the phenomenon now called cell-to-cell propagation. The battery enclosure was not designed to contain the thermal-runaway event, and pressurised gases and electrolyte mist escaped into the electronic-equipment bay (NTSB AIR-14/01, pp.~98--104). The investigation found that the design certification had not adequately tested for cell-to-cell propagation and had assumed thermal-runaway events would be confined to a single cell.

## Organisational / regulatory mechanism

The FAA had granted a special condition for the use of large-format lithium-ion batteries on a Part~25 transport aircraft in 2007 (special condition 25-359-SC), the first such certification (NTSB AIR-14/01, p.~111). The certification testing required by the special condition included single-cell thermal-runaway initiation but did not require demonstration that the enclosure could contain a propagated multi-cell event. The investigation found that the certification's assumed initiating-event probability ($10^{-9}$ per flight hour) was not supported by the in-service experience accumulated between entry-into-service (October 2011) and the Boston event (January 2013), which yielded two thermal-runaway events in approximately $52{,}000$ flight hours (NTSB AIR-14/01, pp.~117--120). Boeing's redesigned battery, certified in April 2013, encloses the cell pack in a steel containment vessel vented to outside the pressure hull, accepting that propagation may occur and constraining its consequences rather than preventing it.

## Lessons by scale

- Vol V, Ch 3 (solutions, electrochemistry, batteries): cell-to-cell thermal propagation as the failure mode whose mitigation set the post-2013 design template for transport-aircraft lithium-ion installations; certification probability assumptions checked against in-service experience.
- Vol V, Ch 9 (corrosion and degradation): internal short-circuit initiation as an example of latent manufacturing defect under load.
- Vol IX (machines and systems, future): system-level mitigation through enclosure design when the lower-level failure mode cannot be eliminated.
- Vol X (failure case studies, future): probabilistic certification arguments and the in-service feedback loop.

## Citation keys

- `acc:ntsb-aar14-01-787-battery`: primary; NTSB Aircraft Incident Report AIR-14/01, 2014.

## Short-form summaries

One sentence:

> A lithium-ion auxiliary-power-unit battery aboard a Japan Airlines Boeing 787 caught fire at the gate at Boston Logan on 7 January 2013, and the FAA grounded the global 787 fleet for three months while Boeing redesigned the battery enclosure to contain cell-to-cell thermal propagation.

Two sentences:

> An internal short circuit in one cell of the 787's eight-cell lithium-ion auxiliary-power-unit battery drove that cell into thermal runaway, and the released heat propagated cell by cell through the pack. The certification special condition had assumed runaway would be confined to a single cell; the in-service experience showed it would not, and the post-2013 design encloses the pack in a steel vessel vented overboard rather than attempting to prevent propagation.

One paragraph:

> On 7 January 2013 a Boeing 787-8 parked at Boston Logan suffered a lithium-ion battery fire in its aft electronic-equipment bay; an in-flight event on 16 January aboard a second 787 produced an emergency landing in Japan, and the FAA grounded the global fleet for three months. The NTSB investigation traced the initiating event to an internal short circuit in cell~5 of the eight-cell, $32\,\text{V}$ pack, which drove that cell into thermal runaway. The released heat propagated to adjacent cells through the conductive cell cans and the vented electrolyte mist, consuming the pack and damaging the enclosure. The FAA's 2007 special condition for large-format lithium-ion certification on transport aircraft had required single-cell thermal-runaway containment but had not required demonstration of multi-cell propagation containment; the in-service event rate exceeded the certification assumption by several orders of magnitude. Boeing's redesigned battery, certified in April 2013, accepts that propagation may occur and confines its consequences via a steel containment vessel vented overboard.

## Provenance and verification

Sources consulted: NTSB Aircraft Incident Report NTSB/AIR-14/01, ``Auxiliary Power Unit Battery Fire, Japan Airlines Boeing 787-8, JA829J, Boston, Massachusetts, January 7, 2013'' (issued 2014), in particular the executive summary (pp.~xi--xv), the battery description (pp.~9--12), the cell-tear-down findings (pp.~71--75), the propagation analysis (pp.~98--104), and the certification and probability discussion (pp.~111--120). Page pins above refer to this report.

Verified: 2026-05-13.
