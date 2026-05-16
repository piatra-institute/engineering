---
name: GPS week-number rollover events
year: 1999-2019
domain: software
primary_source: web:gpsgov-week-rollover-2019
secondary_sources: [web:dhs-cisa-gps-rollover-2019, web:nist-gps-week-rollover-2019]
short_form: The GPS Coarse/Acquisition navigation message represented the week number in 10 bits, which rolled over from 1023 to 0 on 21 August 1999 and again on 6 April 2019; receivers that did not implement a correct rollover-handling rule reported dates roughly 19.7 years in the past, producing time-output errors that propagated into systems using GPS for time transfer.
status: provisional
---

# GPS week-number rollover events, 1999 and 2019

## Date(s) and location

The GPS week-number counter, broadcast in the legacy Coarse/Acquisition (C/A) navigation message as a 10-bit field, completes a rollover every $2^{10} = 1024$ weeks (approximately 19.7 years). Rollovers occurred at the end of 21 August 1999 and at the end of 6 April 2019. The events were global: any receiver decoding the legacy 10-bit field was affected. The newer Civil Navigation (CNAV) message uses a 13-bit week-number field and does not roll over until 2137; receivers using only legacy C/A remain subject to rollover. Equipment classes most affected included older fixed timing receivers in critical infrastructure, embedded receivers in industrial and military equipment, and consumer devices whose firmware had not been updated.

## Technical mechanism

The GPS week-number field is broadcast modulo $2^{10}$. The receiver must reconstruct the absolute week from the modular broadcast value and a known reference epoch. Receivers implement reconstruction in firmware: typical strategies hold a pivot date (the receiver's compile date or last firmware-update date) and assume that any week-number value mapping to a date earlier than the pivot belongs to the next rollover. A receiver whose pivot is set inappropriately or whose pivot logic is incorrect computes a date that may be in error by an integer multiple of 1024 weeks, that is, approximately 19.7 years (\cite{web:gpsgov-week-rollover-2019}, \cite{web:dhs-cisa-gps-rollover-2019}).

Effects observed at the 2019 rollover included receivers reporting calendar dates in 1999, time-transfer outputs offset by integer multiples of 1024 weeks, and disciplined-oscillator systems whose UTC steering inputs became inconsistent across receivers in the same installation. The pseudorange and position outputs of a navigation-only receiver are not directly affected by the week-number error because the within-week time-of-week field is used for ranging; the date and the integer-week timestamp are affected. Systems that consume GPS for time transfer or for time stamping are therefore exposed even when the position service appears nominal (\cite{web:nist-gps-week-rollover-2019}).

CISA and the U.S.\ Department of Homeland Security issued advisories before and after both rollovers identifying vulnerable equipment classes and recommending firmware updates, manufacturer contact, or planned downtime windows. NIST published guidance and held public information sessions before the 2019 event. The rollover events did not cause a single high-profile loss-of-life accident in the public record, but they produced documented timing-system outages and erroneous time stamps in a long tail of installations whose firmware-update path had lapsed (\cite{web:dhs-cisa-gps-rollover-2019}).

## Organisational / regulatory mechanism

Two organisational mechanisms recur in the rollover record. First, equipment-fielding cycles in industrial, military, and infrastructure deployments are longer than the rollover period, so a receiver installed early in one epoch may still be operating at the next rollover with no firmware update having reached it. Second, the rollover-handling logic depends on a pivot date set at manufacture or at last update; an operator who does not refresh the pivot inherits the manufacturer's assumed deployment horizon, which may be shorter than the actual deployment.

Subsequent procurement and operational responses included requirements to record the GPS-receiver firmware version and last-update date in installation logs, periodic firmware-update obligations for time-critical receivers, parallel operation of CNAV-capable receivers in critical timing applications, and explicit holdover and alternate-source plans for the rollover dates (\cite{web:dhs-cisa-gps-rollover-2019}, \cite{web:nist-gps-week-rollover-2019}).

## Lessons by scale

- Volume I, Chapter 6 ("Time, frequency, and signals"): canonical case of a finite-width counter rolling over inside a time-transfer chain; the lesson that a time service depends on more than the broadcast signal, including the receiver firmware's reconstruction rule and its last-update date.
- Volume VII, Chapter 2 ("Number representations, arithmetic, precision"): canonical case of modular-counter design without a documented rollover-handling contract.
- Volume IX (timing and synchronisation chapters): the discipline of parallel timing sources and explicit holdover plans.
- Volume X (multiple chapters): the institutional pattern in which a manufacturer's pivot assumption becomes the operator's silent dependency.

## Citation keys

- Primary: `web:gpsgov-week-rollover-2019`. GPS.gov operational advisory and background pages on the 1024-week rollover, U.S.\ Space Force, 2019.
- Secondary: `web:dhs-cisa-gps-rollover-2019`. U.S.\ Department of Homeland Security, Cybersecurity and Infrastructure Security Agency advisory on GPS week-number rollover, 2019.
- Secondary: `web:nist-gps-week-rollover-2019`. NIST Time and Frequency Division, public guidance and webinar materials on the GPS week-number rollover, 2019.

## Short-form summaries

\textbf{One sentence}: The GPS C/A navigation message broadcast the week number in 10 bits, which rolls over every 1024 weeks; rollovers on 21 August 1999 and 6 April 2019 produced incorrect dates and time stamps in receivers whose firmware lacked an up-to-date pivot for the rollover-handling rule.

\textbf{Two sentences}: The legacy GPS week-number field is 10 bits wide and rolls over every $2^{10} = 1024$ weeks (about 19.7 years), so receivers must reconstruct the absolute week from a pivot date set at manufacture or last firmware update. Rollovers on 21 August 1999 and 6 April 2019 produced documented timing-system outages and erroneous time stamps in receivers whose pivots had lapsed, exposing time-transfer applications that depended on GPS without an alternate source or a recent firmware update.

\textbf{One paragraph}: The GPS Coarse/Acquisition navigation message represents the week number in a 10-bit field, so the broadcast value wraps from 1023 to 0 every 1024 weeks, approximately 19.7 years. A receiver reconstructs the absolute week by combining the broadcast value with a pivot date held in firmware, typically the compile date or the last firmware-update date; a receiver whose pivot has not been refreshed before a rollover may compute a date that is an integer multiple of 1024 weeks too early. Rollovers occurred at the end of 21 August 1999 and 6 April 2019. The 2019 rollover prompted CISA and NIST advisories, identified vulnerable equipment classes in industrial, military, and infrastructure deployments, and produced documented timing-system outages and erroneous time stamps in installations whose firmware-update path had lapsed. The position service of a navigation-only receiver is not directly affected because the within-week time-of-week field carries the ranging information; time-transfer and time-stamp applications are exposed even when position outputs appear nominal. The newer CNAV message uses a 13-bit week field that does not roll over until 2137.

## Provenance and verification

Sources consulted: GPS.gov pages on the GPS week-number rollover (U.S.\ Space Force, 2019, accessed for the technical mechanism and the manufacturer-pivot reconstruction rule); CISA advisory on GPS week-number rollover (DHS/CISA, 2019, accessed for vulnerable-equipment-class guidance); NIST Time and Frequency Division materials on the rollover (2019, accessed for the time-transfer impact and the recommended preparation). The 10-bit and 13-bit field widths, the 1024-week period, and the 1999 and 2019 dates are confirmed across all three sources. Status: provisional, last reviewed 2026-05-16.
