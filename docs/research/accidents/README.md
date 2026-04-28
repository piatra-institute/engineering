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
| V | 1986 | [Space Shuttle Challenger](challenger-1986.md) | `acc:nasa-challenger` |
| V | 1990 | [Hubble Space Telescope primary mirror](hubble-primary-mirror-1990.md) | `acc:nasa-hubble-optical-systems-1990` |
| V | 1996 | [Ariane 5 Flight 501](ariane-501-1996.md) | `acc:ariane501-ifr` |
| V | 1999 | [Mars Climate Orbiter](mars-climate-orbiter-1999.md) | `acc:nasa-mco-mib` |
| V | 2003 | [Space Shuttle Columbia](columbia-2003.md) | `acc:caib-columbia` |
| V | 1983 | [Air Canada Flight 143](air-canada-143-1983.md) | `acc:lockwood-gimli1985` |

### Civil

| Status | Year | Name | Primary source |
|---|---|---|---|
| V | 1940 | [Tacoma Narrows Bridge](tacoma-narrows-1940.md) | `acc:tacoma-narrows-1941` |
| V | 1981 | [Hyatt Regency walkway collapse](hyatt-regency-1981.md) | `acc:nbs-hyatt-1982` |

### Process

| Status | Year | Name | Primary source |
|---|---|---|---|
| P | 1984 | [Bhopal disaster](bhopal-1984.md) | `acc:icmr-bhopal-2004` |

### Power

| Status | Year | Name | Primary source |
|---|---|---|---|
| V | 1979 | [Three Mile Island](three-mile-island-1979.md) | `acc:kemeny-tmi-1979` |
| V | 1986 | [Chernobyl](chernobyl-1986.md) | `acc:iaea-insag7-1992` |

### Medical

| Status | Year | Name | Primary source |
|---|---|---|---|
| V | 1985-1987 | [Therac-25](therac-25-1985-1987.md) | closest-equivalent: `paper:leveson-turner1993` |

## Counts

- Aerospace: 6
- Civil: 2
- Process: 1
- Power: 2
- Medical: 1
- **Total: 12**

## Pending entries (~18-20)

Accumulate as chapters cite them. Listed here for forward planning, not as commitment:

- Aerospace: Aloha 243 (1988), Air France 447 (2009), Boeing 737 MAX (2018-2019).
- Civil: Tay Bridge (1879), Citicorp Tower (1978-1979, averted), Genoa Morandi (2018), Aberfan (1966), Vajont Dam (1963).
- Process: Texas City refinery (2005), Flixborough (1974), Buncefield (2005), Deepwater Horizon (2010).
- Power: Fukushima (2011), Northeast blackout (2003), Texas grid failure (2021).
- Software: Patriot timing bug at Dhahran (1991), Knight Capital (2012), Volkswagen diesel-defeat (2015).

The schema and citation policy govern future additions. New entries are added in the appropriate domain section above when their primary or closest-equivalent source has been confirmed and the body sections are filled.
