# Data assets for Vol VI Ch 10 (Bioreactors and biomanufacturing)

Four CSV files of order-of-magnitude working numbers, drawn from
standard bioprocess engineering references (Shuler-Kargi, Doran,
Stanbury et al.) and the public biopharma supply literature. The
numbers are working ranges for exercises and worked examples, not
release-grade design data.

- `yield_coefficients.csv`: biomass yield $Y_{X/S}$ and product
  yield $Y_{P/S}$ for representative organism / substrate / product
  combinations.
- `kla_by_reactor_scale.csv`: typical $k_L a$ values by reactor type
  and working volume across the laboratory-to-production range.
- `insulin_demand_by_region.csv`: order-of-magnitude annual insulin
  demand by world region (current as of mid-2020s public data).
- `batch_failure_modes.csv`: representative batch-rejection rates by
  failure mode for microbial and mammalian processes; used in the
  failure-section quantitative discussion.

Each CSV is small (tens of rows). Column units are stated in the
header row and in the relevant chapter prose.
