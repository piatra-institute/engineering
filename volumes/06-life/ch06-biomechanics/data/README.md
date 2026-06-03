# Data assets for Vol VI Ch 6 (Biomechanics)

Five CSV files supporting the chapter's worked examples and exercises.
Each row has source attribution in the `reference` column; the
chapter's bibliography lists the primary entries.

- `bone_mechanical_properties.csv`: Young's modulus, ultimate strength,
  ultimate strain, density, and loading direction for cortical and
  trabecular bone at the femoral mid-shaft, tibial mid-shaft, femoral
  neck, vertebral body, proximal tibia, calcaneus, and craniofacial
  bone. Primary sources Reilly and Burstein 1975-1976 and Hayes 1991.
- `muscle_fibre_properties.csv`: specific tension, maximum shortening
  velocity, fatigue resistance, recruitment threshold, and typical use
  for type I, IIa, and IIb / IIx skeletal fibres plus cardiac and
  smooth muscle. Also includes physiological cross-section areas for
  five named human muscles. Primary sources Bottinelli 1996, Bers
  2002, Wickiewicz 1983.
- `lung_function_reference.csv`: FVC, FEV$_1$, FEV$_1$/FVC, TLC, RV,
  FRC by age (20-80) and sex for a $175$-cm male and $165$-cm female
  reference. Values are GLI 2012 white reference equation predictions,
  used as the comparator in the spirometry exercise and in the lung
  compliance estimate.
- `cardiac_pv_samples.csv`: twenty-two samples around a normal left
  ventricular pressure-volume loop, one full cardiac cycle, with the
  four phases (filling, isovolumetric contraction, ejection,
  isovolumetric relaxation) labelled. Values are typical of a healthy
  adult at rest (heart rate $70$ bpm, EDV $120\,\text{mL}$, ESV
  $50\,\text{mL}$).
- `soft_tissue_uniaxial.csv`: stretch lambda and first-Piola stress for
  arterial wall, tendon, dorsal skin, and articular cartilage. Used to
  fit Mooney-Rivlin and Ogden constitutive models in the simulation
  exercise. Primary sources Holzapfel 2000, Maganaris 2002, Mow 1980.

All files are UTF-8 with header row. Units are in column names.
