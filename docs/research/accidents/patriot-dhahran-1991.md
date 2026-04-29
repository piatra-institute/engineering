---
name: Patriot missile system, Dhahran
year: 1991
domain: software
primary_source: acc:gao-patriot-1992
secondary_sources: []
short_form: A US Army Patriot missile battery at Dhahran, Saudi Arabia, failed to intercept an incoming Iraqi Scud missile on 25 February 1991, killing 28 US service members and wounding approximately 100 others; the GAO investigation traced the failure to a software-clock arithmetic error that accumulated to approximately $0.34 \,\si{\second}$ over $100 \,\si{\hour}$ of continuous operation, large enough that the Patriot's range gate computed the Scud's predicted position outside the search window and the system did not engage.
status: verified
---

# Patriot missile system, Dhahran, 1991

## Date(s) and location

The incident occurred at the US Army Patriot missile battery at Dhahran, Saudi Arabia, on 25 February 1991, during the Gulf War. An Iraqi Scud missile struck a US Army barracks at approximately 20:35 local time. The Patriot battery did not engage the incoming missile. Twenty-eight US service members died and approximately one hundred were wounded. The Patriot battery had been continuously operating for approximately one hundred hours at the time of the incident.

## Technical mechanism

The U.S.\ General Accounting Office (now Government Accountability Office) investigated the incident under congressional request and issued report GAO/IMTEC-92-26 in February 1992 \cite{acc:gao-patriot-1992}. The GAO identified the cause as a software-clock arithmetic error in the Patriot's range-gate prediction.

The Patriot's tracking software represented elapsed time as the number of tenths of a second since the system was started, stored as an integer counter and converted to seconds as a real number when needed. The conversion used a $24$-bit fixed-point representation of the constant $1/10$. The exact decimal $0.1$ has no exact binary representation; the $24$-bit truncation introduced a small per-conversion error of approximately $9.5 \times 10^{-8}$ in the converted seconds value. The error accumulated linearly with the integer counter.

After approximately $100 \,\si{\hour}$ of continuous operation, the integer counter had reached approximately $3.6 \times 10^{6}$, and the cumulative conversion error had reached approximately $0.34 \,\si{\second}$. The Patriot's range-gate calculation used the converted time to predict where an incoming target would be at the next radar look. A target moving at the Scud's speed of approximately $1{,}676 \,\si{\meter\per\second}$ over $0.34 \,\si{\second}$ travels approximately $570 \,\si{\meter}$. The Patriot's predicted position was therefore offset from the actual position by roughly $570 \,\si{\meter}$, larger than the range gate, and the system reported "no track" rather than engaging \cite{acc:gao-patriot-1992}.

A software patch correcting the conversion error had been developed and was being distributed to Patriot batteries at the time of the Dhahran incident. The Dhahran battery's patch arrived on 26 February 1991, the day after the incident.

## Organisational / regulatory mechanism

The GAO report identified contributing institutional factors beyond the technical error \cite{acc:gao-patriot-1992}. Patriot batteries were not designed to operate continuously for one hundred hours; the operational concept assumed periodic restarts that would reset the time counter. Field operators in the Gulf War deployment had been instructed to keep the systems running continuously to maintain readiness. The accumulated-error effect had been observed in field tests and reported through the chain, but the patch and the operational-restart guidance moved through different distribution channels and arrived at field units inconsistently.

The Patriot case became canonical in software-engineering education for several reasons. It is one of the clearest documented examples of a numerical-precision software error producing a directly attributable loss of life. It illustrates the failure mode of accumulated arithmetic error in long-running continuous operation, a category that recurs in flight-control software, navigation systems, and physical-process control. It also illustrates the institutional pattern in which a technical patch and an operational workaround are distributed through different channels with no synchronisation, so a battery in the field may have one without the other.

Subsequent regulatory and procurement response included revised testing requirements for long-running mission-critical software, formal guidance on numerical precision in real-time control systems, and changes to the way patches and operational guidance are jointly distributed to deployed military hardware.

## Lessons by scale

- Volume I, Chapter 6 ("Time, frequency, and signals"): canonical case of clock drift in a software-mediated measurement chain; the lesson that accumulated arithmetic error in long-running continuous operation must be analysed against the operational concept of the system.
- Volume VII, Chapter 2 ("Number representations, arithmetic, precision"): canonical case of fixed-point numerical-precision error reaching field deployment.
- Volume VII, Chapter 19 ("Software engineering as discipline"): the patch-distribution mechanism and the gap between patch availability and field deployment.
- Volume IX, Chapter 14 ("Cyber-physical systems"): the interaction between software arithmetic and the physical performance envelope of the Patriot's range gate.
- Volume X (multiple chapters): canonical case of software-induced loss of life with a clearly attributable numerical mechanism.
- Volume X, Chapter 9 ("Human factors and operator error"): the operational decision to run the systems continuously contrary to the design's restart assumption.

## Citation keys

- Primary: `acc:gao-patriot-1992`. U.S.\ General Accounting Office, Information Management and Technology Division, "Patriot Missile Defense: Software Problem Led to System Failure at Dhahran, Saudi Arabia," GAO/IMTEC-92-26, February 1992.

## Short-form summaries

\textbf{One sentence}: A US Army Patriot missile battery at Dhahran, Saudi Arabia, failed to intercept an incoming Iraqi Scud missile on 25 February 1991, killing 28 US service members and wounding approximately 100 others; the GAO investigation traced the failure to a software-clock arithmetic error that accumulated to approximately $0.34 \,\si{\second}$ over $100 \,\si{\hour}$ of continuous operation, large enough that the Patriot's range gate computed the Scud's predicted position outside the search window and the system did not engage.

\textbf{Two sentences}: The Patriot battery's tracking software represented elapsed time as integer tenths of a second and converted to real seconds using a $24$-bit truncation of $1/10$, accumulating a per-conversion error of about $9.5 \times 10^{-8}$ that reached $0.34 \,\si{\second}$ after $100 \,\si{\hour}$ of continuous operation. At the Scud's speed, this time offset corresponded to a predicted-position error of about $570 \,\si{\meter}$, beyond the Patriot's range gate, and the system did not engage; a software patch correcting the error arrived at the Dhahran battery the day after the incident.

\textbf{One paragraph}: On 25 February 1991, a US Army Patriot missile battery at Dhahran, Saudi Arabia, failed to intercept an incoming Iraqi Scud missile that struck a US Army barracks; 28 service members died and approximately 100 were wounded. The GAO investigation (report IMTEC-92-26, February 1992) identified the cause as a software-clock arithmetic error. The Patriot's tracking software stored elapsed time as integer tenths of a second and converted to real seconds using a $24$-bit fixed-point representation of $1/10$. The exact decimal $0.1$ has no exact binary representation; the truncation introduced a per-conversion error of about $9.5 \times 10^{-8}$ that accumulated linearly with the counter. After approximately $100 \,\si{\hour}$ of continuous operation, the cumulative error had reached about $0.34 \,\si{\second}$. The Patriot's range-gate prediction used the converted time to forecast the Scud's position at the next radar look; at the Scud's speed of about $1{,}676 \,\si{\meter\per\second}$, the time offset corresponded to a predicted-position error of about $570 \,\si{\meter}$, larger than the range gate. The system reported "no track" and did not engage. A software patch correcting the conversion arrived at the Dhahran battery the day after the incident; Patriot batteries had been operated continuously contrary to the design's restart assumption, and the patch and the operational-restart guidance had moved through different distribution channels.

## Provenance and verification

Sources consulted: U.S.\ General Accounting Office, "Patriot Missile Defense: Software Problem Led to System Failure at Dhahran, Saudi Arabia," GAO/IMTEC-92-26, February 1992 (the primary source). The $0.34 \,\si{\second}$ accumulated error figure, the $24$-bit fixed-point representation, the $100 \,\si{\hour}$ operating time, the casualty counts, and the patch-arrival date all come from the GAO report. The Scud speed and the resulting predicted-position offset are derived from the GAO report's figures. Verified: 2026-04-29.
