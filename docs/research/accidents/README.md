# Named-cases registry

This directory holds the project's canonical record of named engineering accidents. Every chapter that mentions a named accident must resolve to an entry here, and the chapter's mechanism description must align with the entry's `## Technical mechanism` section or quote one of the entry's short-form summaries verbatim.

The registry's discipline is documented at:

- `SCHEMA.md`: the format every entry takes.
- `../citation-policy.md`: source-tier rules and the closest-equivalent-to-primary clause.
- `../reviewer-guide.md`: the technical reviewer's registry-check obligations (items 24-27).

The `make accidents` target verifies that every `\cite{acc:*}` key in chapter prose has a matching entry here.

## Entries

Sorted by domain, then by year. Status: V = verified, P = provisional, X = placeholder.

### Aerospace

| Status | Year | Name | Primary source |
|---|---|---|---|
| V | 1954 | [de Havilland Comet](comet-1954.md) | `acc:cohen-comet-report-1955` |
| V | 1972 | [Eastern Air Lines Flight 401](eastern-401-1972.md) | `acc:ntsb-aar73-14` |
| V | 1977 | [Tenerife airport disaster](tenerife-1977.md) | `acc:ciaiac-tenerife-1978` |
| V | 1994 | [American Eagle Flight 4184 (Roselawn ATR-72 icing)](american-eagle-4184-1994.md) | `acc:ntsb-aar96-01` |
| V | 2006 | [Comair Flight 5191](comair-5191-2006.md) | `acc:ntsb-aar07-05` |
| V | 1983 | [Air Canada Flight 143](air-canada-143-1983.md) | `acc:lockwood-gimli1985` |
| V | 1986 | [Space Shuttle Challenger](challenger-1986.md) | `acc:nasa-challenger` |
| V | 1988 | [Aloha Airlines Flight 243](aloha-airlines-243-1988.md) | `acc:ntsb-aar94-04` |
| V | 1990 | [Hubble Space Telescope primary mirror](hubble-primary-mirror-1990.md) | `acc:nasa-hubble-optical-systems-1990` |
| V | 1996 | [Ariane 5 Flight 501](ariane-501-1996.md) | `acc:ariane501-ifr` |
| V | 1999 | [Mars Climate Orbiter](mars-climate-orbiter-1999.md) | `acc:nasa-mco-mib` |
| V | 2003 | [Space Shuttle Columbia](columbia-2003.md) | `acc:caib-columbia` |
| V | 1997 | [Mars Pathfinder priority inversion](mars-pathfinder-1997.md) | `paper:jones-pathfinder-1997` |
| V | 2009 | [Air France Flight 447](air-france-447-2009.md) | `acc:bea-af447` |
| V | 2013 | [Boeing 787 lithium-ion battery incidents](boeing-787-battery-2013.md) | `acc:ntsb-aar14-01-787-battery` |
| V | 2018-2019 | [Boeing 737 MAX MCAS](boeing-737-max-mcas-2018-2019.md) | closest-equivalent: `acc:house-737max-2020` |

### Civil

| Status | Year | Name | Primary source |
|---|---|---|---|
| V | 1940 | [Tacoma Narrows Bridge](tacoma-narrows-1940.md) | `acc:tacoma-narrows-1941` |
| V | 1981 | [Hyatt Regency walkway collapse](hyatt-regency-1981.md) | `acc:nbs-hyatt-1982` |
| V | 2000 | [London Millennium Footbridge](millennium-bridge-2000.md) | `acc:dallard-millennium-2001` |
| P | 2017 | [Grenfell Tower fire](grenfell-tower-2017.md) | `acc:grenfell-inquiry-2024` |
| P | 2018 | [Cape Town Day Zero water crisis](cape-town-day-zero-2018.md) | `acc:csir-capetown-2018` |
| V | 2018 | [Genoa Morandi Bridge](genoa-morandi-bridge-2018.md) | `acc:mit-morandi-2018` |

### Process

| Status | Year | Name | Primary source |
|---|---|---|---|
| P | 1984 | [Bhopal disaster](bhopal-1984.md) | `acc:icmr-bhopal-2004` |
| V | 2005 | [BP Texas City refinery explosion](bp-texas-city-2005.md) | `acc:csb-bp-texas-city-2007` |
| V | 2008 | [Imperial Sugar refinery dust explosion](imperial-sugar-2008.md) | `acc:csb-imperial-sugar-2009` |

### Power

| Status | Year | Name | Primary source |
|---|---|---|---|
| V | 1979 | [Three Mile Island](three-mile-island-1979.md) | `acc:kemeny-tmi-1979` |
| V | 1986 | [Chernobyl](chernobyl-1986.md) | `acc:iaea-insag7-1992` |
| P | 2011 | [Fukushima Daiichi nuclear accident](fukushima-daiichi-2011.md) | `acc:tepco-fukushima-2012` |
| P | 2021 | [Texas February 2021 grid failure](texas-grid-2021.md) | `acc:ferc-nerc-texas-2021` |

### Environmental

| Status | Year | Name | Primary source |
|---|---|---|---|
| V | 2014-2019 | [Flint water crisis](flint-water-crisis-2014-2019.md) | `acc:fwatf-2016` |

### Medical

| Status | Year | Name | Primary source |
|---|---|---|---|
| V | 1985-1987 | [Therac-25](therac-25-1985-1987.md) | closest-equivalent: `paper:leveson-turner1993` |
| P | 2005-2009 | [Mid Staffordshire NHS failure](mid-staffordshire-2005-2009.md) | `acc:francis-mid-staffs-2013` |

### Software

| Status | Year | Name | Primary source |
|---|---|---|---|
| V | 1991 | [Patriot missile system, Dhahran](patriot-dhahran-1991.md) | `acc:gao-patriot-1992` |
| V | 1994 | [Pentium FDIV bug](pentium-fdiv-1994.md) | `paper:coe-tang-pratt-1995` |
| P | 2010-2020 | [F-35 ALIS programme](f35-alis-2010-2020.md) | `acc:gao-f35-alis-2020` |
| V | 2015 | [Volkswagen diesel emissions defeat device](volkswagen-diesel-defeat-2015.md) | `acc:epa-vw-nov-2015` |
| P | 1999/2019 | [GPS week-number rollover](gps-week-rollover-1999-2019.md) | `web:gpsgov-week-rollover-2019` |

### Metrology

| Status | Year | Name | Primary source |
|---|---|---|---|
| V | 1889-2019 | [IPK mass drift (international prototype of the kilogram)](ipk-mass-drift-1889-2019.md) | `paper:girard-ipk-1994` |

## Counts

- Aerospace: 16
- Civil: 6
- Process: 3
- Power: 4
- Environmental: 1
- Medical: 2
- Software: 5
- Metrology: 1
- **Total: 38**

## Pending entries

Accumulate as chapters cite them. Listed here for forward planning, not as commitment:

- Civil: Tay Bridge (1879), Citicorp Tower (1978-1979, averted), Aberfan (1966), Vajont Dam (1963).
- Process: Flixborough (1974), Buncefield (2005), Deepwater Horizon (2010).
- Power: Northeast blackout (2003).
- Software: Knight Capital (2012).

The schema and citation policy govern future additions. New entries are added in the appropriate domain section above when their primary or closest-equivalent source has been confirmed and the body sections are filled.
