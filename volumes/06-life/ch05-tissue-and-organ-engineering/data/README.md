# Data assets for Vol VI Ch 5 (Tissue and organ engineering)

Four CSV files. Each is small (tens of rows), self-documenting through
its header, and sourced from the chapter's bibliography. Numbers are
representative of the working ranges in the field and carry their
year of currency in the file or the cited source. They are intended
as the working dataset for the chapter's exercises and as a
reproducible reference for the table-form numerical claims in the
prose.

- `tissue_mechanical_properties.csv` (10 tissues): Young's modulus,
  ultimate tensile strength, strain at failure, and reference. The
  ranges span five orders of magnitude in modulus from brain to
  cortical bone.
- `oxygen_diffusion_coefficients.csv`: oxygen diffusion coefficient
  in water, plasma, and various tissues, plus oxygen consumption
  rates by tissue. Used in the Krogh-cylinder and slab-diffusion
  worked examples.
- `scaffold_materials.csv`: properties of PLA, PLGA, PCL, alginate,
  and decellularised matrix; modulus, degradation half-life,
  approximate cost per gram for medical-grade material (current as
  of 2024), and a notes field.
- `ipsc_reprogramming_efficiency.csv`: reprogramming efficiency by
  method (retroviral, lentiviral, episomal, Sendai virus, mRNA,
  small-molecule), with cell-source and integration-vs-non-integration
  status. Used in the cell-source discussion and in the Yamanaka
  reprogramming exercise.
