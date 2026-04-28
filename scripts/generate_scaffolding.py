#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""
Engineering: scaffolding generator.

Generates the 12 _volume.tex volume-openers and the 174 chapter shell files
under volumes/. Re-runnable; overwrites existing shells. The chapter outline
is canonical here in BOOKS; per-chapter and per-volume metadata (half-life,
archetypes, project, exercise count) is parsed at runtime from the dossiers
under docs/research/<NN>-<slug>/_volume.md and docs/research/<NN>-<slug>/
ch<MM>-<slug>.md.

Layout:
    volumes/
        NN-slug/
            _volume.tex
            chMM-chslug/
                chapter.tex

Each chapter lives in its own folder so it can accumulate figures, code,
datasets, exercise solutions, and reviewer logs alongside the prose.

Use:  uv run scripts/generate_scaffolding.py
   or: ./scripts/generate_scaffolding.py    (the shebang invokes uv run)
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Each volume: (num, slug, name, tagline, scope, [(ch_num, slug, title, approx_pp, [sections])])
BOOKS = []

BOOKS.append((
    1, "quantity", "Quantity",
    "Reality is measurable",
    "We teach the reader to convert reality into numbers and to know what those numbers mean. Measurement, units, error, calibration, dimensional analysis, and the statistics every working engineer needs.",
    [
        (1, "why-we-measure", "Why we measure", 60, [
            "What measurement is for",
            "The impossibility of unmeasured engineering",
            "Estimation, error, precision, accuracy: the orienting vocabulary",
            "Measurement crises: Mars Climate Orbiter, Air Canada Flight 143, Ariane 5",
            "The measurement habit",
            "Failure: the metric vs.\\ imperial fault line",
        ]),
        (2, "units-and-dimensions", "Units and dimensions", 70, [
            "SI base units",
            "Derived units",
            "Conversion and the discipline of carrying units",
            "Dimensional analysis as debugging",
            "Dimensional homogeneity and the Buckingham pi theorem",
            "Failure: unit errors that cost money or lives",
        ]),
        (3, "calibration-and-traceability", "Calibration and traceability", 80, [
            "What a calibration is",
            "Primary, secondary, working standards",
            "The traceability chain and NIST (and BIPM)",
            "Calibration vs validation vs verification",
            "Drift, recalibration intervals, the cost of calibration",
            "Cross-domain examples: voltage, mass, length, frequency, temperature",
            "Failure: when the standard itself was wrong",
        ]),
        (4, "error-and-uncertainty", "Error and uncertainty", 100, [
            "Random vs systematic error",
            "Distribution of error: Gaussian, uniform, asymmetric",
            "Propagation of uncertainty: linear and Monte Carlo",
            "The central limit theorem in practice",
            "Significant figures, rounding, reporting",
            "Confidence intervals as engineering tools",
            "The cost of a smaller error bar",
            "Failure: error bars that were politically chosen",
        ]),
        (5, "sensors-and-instruments", "Sensors and instruments", 90, [
            "What a sensor is",
            "Transducer principles: thermal, electrical, optical, mechanical, chemical, magnetic",
            "Sensor specifications: accuracy, precision, resolution, range, drift, hysteresis",
            "Choosing the right sensor",
            "Common instruments: multimeter, oscilloscope, micrometer, scale, microscope, sensor arrays",
            "Failure: when the sensor lies, and why it usually lies in the same direction",
        ]),
        (6, "time-frequency-signals", "Time, frequency, and signals", 80, [
            "Time as the most precisely measured quantity",
            "Clocks: pendulum, quartz, atomic, optical",
            "Frequency, period, phase",
            "Sampling and aliasing (Nyquist informally)",
            "Time-frequency duality preview",
            "GPS as a measurement system",
            "Failure: clock drift and the Patriot missile",
        ]),
        (7, "length-area-volume-mass", "Length, area, volume, mass", 70, [
            "Length: ruler to interferometer",
            "Area, volume, density",
            "Mass: balance, scale, recoil mass spectrometer",
            "Specialised quantities: viscosity, hardness, surface roughness",
            "Cross-checking: independent measurements of the same quantity",
            "Failure: when the ruler was wrong (Hubble's primary mirror)",
        ]),
        (8, "statistics-for-engineers", "Statistics for engineers", 90, [
            "Summary statistics: mean, median, mode, variance, IQR",
            "Distributions: normal, log-normal, Weibull, Poisson, exponential",
            "Hypothesis testing in engineering context",
            "Confidence vs prediction intervals",
            "Bayesian intuition for the practitioner",
            "Sample size and statistical power",
            "P-hacking, garden of forking paths, and what to refuse",
            "Failure: replication crises across engineering disciplines",
        ]),
        (9, "discipline-of-estimation", "The discipline of estimation", 80, [
            "Order-of-magnitude reasoning",
            "Fermi problems",
            "Estimation before calculation: a habit",
            "Sanity-checking calculated results",
            "Estimation under deep uncertainty",
            "The estimation environment introduced",
            "Failure: estimates that were never sanity-checked",
            "Estimation as a moral discipline",
        ]),
    ]
))

BOOKS.append((
    2, "form", "Form",
    "Mathematics as the language of engineering",
    "We teach mathematics for engineers: usable power, not disciplinary completeness. The reader leaves able to differentiate, integrate, solve linear systems, set up and solve ODEs and the simpler PDEs, reason probabilistically, optimise under constraint, and translate a real problem into a model.",
    [
        (1, "algebra-and-proof", "Algebra and proof discipline", 80, [
            "Algebraic identities and manipulations",
            "Inequalities",
            "What a proof is, what it costs, why engineers occasionally need them",
            "Induction",
            "Functions, sets, mappings",
            "Notation discipline: how engineers should write mathematics",
            "Failure: notation collapse and the cost of imprecision",
        ]),
        (2, "functions-and-graphs", "Functions and graphs", 80, [
            "Functions as mappings",
            "Polynomials, rational functions",
            "Exponentials and logarithms",
            "Trigonometric functions",
            "Inverse functions",
            "Reading a graph: shape, slope, asymptote, scale",
            "Failure: log-scale traps and linear extrapolation",
        ]),
        (3, "trigonometry-complex-phasors", "Trigonometry, complex numbers, phasors", 90, [
            "Right triangles, the unit circle, identities",
            "Complex numbers as ordered pairs",
            "Euler's identity, polar form",
            "Phasors as the engineer's complex-number tool",
            "Rotations in 2D",
            "Spherical and cylindrical coordinates preview",
            "Failure: phase wrap-around in real measurements",
            "Worked examples: AC circuit, rotating machinery, wave addition",
        ]),
        (4, "sequences-series-limits", "Sequences, series, limits", 80, [
            "Sequences and their behaviour at infinity",
            "Series: geometric, harmonic, alternating",
            "Convergence tests engineers actually use",
            "Power series, Taylor series",
            "Limits: epsilon-delta informally; engineering use",
            "Failure: divergent series that look convergent",
            "Worked examples: small-angle approximations, perturbation expansions",
        ]),
        (5, "differentiation", "Differentiation", 110, [
            "The derivative as rate",
            "Rules: product, chain, quotient, implicit",
            "Higher-order derivatives",
            "Local linearisation",
            "Mean value theorem and L'H\\^opital",
            "Optimisation of one variable",
            "Numerical differentiation, why it is hard",
            "Failure: discontinuities, kinks, derivatives that do not exist",
            "Worked examples across domains",
        ]),
        (6, "integration", "Integration", 110, [
            "The integral as accumulation",
            "Fundamental theorem of calculus",
            "Techniques: substitution, parts, partial fractions",
            "Improper integrals",
            "Numerical integration: trapezoidal, Simpson, Gauss",
            "Multiple integrals preview",
            "Convolution introduced",
            "Failure: when an integral does not exist or does not converge",
            "Worked examples: centre of mass, moment of inertia, work, expectation",
        ]),
        (7, "odes", "Differential equations: ODEs", 120, [
            "What an ODE is, where it comes from",
            "First-order linear ODEs",
            "Separable equations",
            "Second-order linear with constant coefficients",
            "Forced response: resonance, beating",
            "Systems of ODEs",
            "Phase-plane analysis",
            "Numerical ODE solvers: Euler, RK4, stiffness",
            "Failure: numerical instability and the stiffness trap",
            "Worked examples: RC circuit, pendulum, predator-prey, drug kinetics",
        ]),
        (8, "vectors-and-vector-calculus", "Vectors and vector calculus", 100, [
            "Vectors as algebraic and geometric objects",
            "Dot and cross products",
            "Coordinate systems and transformations",
            "Curves: parametrisation, arc length, curvature",
            "Surfaces: parametrisation, normals, area",
            "Gradient, divergence, curl",
            "Stokes, Gauss, Green: the three integral theorems",
            "Failure: orientation errors and the sign-of-the-normal problem",
        ]),
        (9, "linear-algebra", "Linear algebra", 110, [
            "Vector spaces",
            "Matrices as linear maps",
            "Solving linear systems: Gaussian elimination, LU, QR",
            "Determinants",
            "Inner products, norms, orthogonality",
            "Projection, least squares",
            "Conditioning and numerical sensitivity",
            "Failure: ill-conditioned systems and what to refuse to solve",
        ]),
        (10, "eigenvalues-and-decompositions", "Eigenvalues and decompositions", 110, [
            "Eigenvalues and eigenvectors",
            "Diagonalisation",
            "SVD",
            "Spectral methods, low-rank approximation",
            "Markov chains and stochastic matrices",
            "Power iteration and PageRank as worked example",
            "Failure: when the matrix has no real eigenvectors and the engineer panics",
            "Worked examples: PCA, modal analysis, image compression",
        ]),
        (11, "multivariable-calculus", "Multivariable calculus", 100, [
            "Functions of many variables",
            "Partial derivatives, gradients",
            "Critical points: maxima, minima, saddles",
            "Lagrange multipliers",
            "Constrained optimisation preview",
            "Multiple integrals",
            "Change of variables, Jacobians",
            "Failure: the high-dimensional space and our intuition's collapse",
        ]),
        (12, "pdes", "Partial differential equations", 120, [
            "Why distributed phenomena need PDEs",
            "The heat equation",
            "The wave equation",
            "Laplace's equation",
            "Separation of variables, Fourier series introduction",
            "Boundary and initial conditions: the engineer's craft",
            "Numerical PDEs: finite difference, finite element preview",
            "Failure: ill-posed problems and the cost of bad boundary conditions",
        ]),
        (13, "probability", "Probability theory", 100, [
            "Sample spaces and events",
            "Conditional probability, Bayes",
            "Random variables, expectation, variance",
            "Common distributions: discrete and continuous",
            "Joint distributions, independence, correlation",
            "Limit theorems: LLN, CLT",
            "Stochastic processes preview",
            "Failure: independence assumed where there was none",
        ]),
        (14, "statistical-inference", "Statistical inference", 100, [
            "Estimation: point and interval",
            "Hypothesis testing as decision theory",
            "Likelihood and maximum likelihood",
            "Bayesian inference",
            "Regression: linear, logistic, regularised",
            "Cross-validation, hold-out, the danger of looking at test data",
            "Failure: p-hacking, multiple comparisons, the replication crisis revisited",
        ]),
        (15, "optimisation", "Optimisation", 110, [
            "What an optimisation problem is",
            "Convex optimisation",
            "Linear and quadratic programming",
            "Lagrangian duality",
            "Gradient methods, Newton's method",
            "Stochastic optimisation, SGD",
            "Integer and combinatorial optimisation preview",
            "Failure: local minima, ill-posed objectives, optimisation theatre",
        ]),
        (16, "numerical-methods", "Numerical methods", 110, [
            "Floating-point arithmetic",
            "Error: truncation, round-off, conditioning",
            "Root-finding: bisection, Newton, secant",
            "Numerical linear algebra revisited",
            "Numerical integration revisited",
            "Numerical ODE/PDE solvers",
            "Reproducibility: deterministic floating-point, exact-arithmetic alternatives",
            "Failure: famous numerical failures",
        ]),
        (17, "discrete-mathematics", "Discrete mathematics, graphs, combinatorics", 100, [
            "Counting, permutations, combinations",
            "Graph theory: nodes, edges, walks, paths",
            "Algorithmic graph problems: shortest path, MST, matching",
            "Boolean algebra and logic",
            "Asymptotic notation",
            "Recurrences and generating functions",
            "Number theory engineers actually use",
            "Failure: combinatorial explosion in design spaces",
        ]),
        (18, "mathematical-modelling", "Mathematical modelling: real problem to math", 100, [
            "What modelling is",
            "Choosing what to keep and what to throw away",
            "Identification and validation",
            "Parameter estimation",
            "Model uncertainty and structural error",
            "Worked example: from a measurement notebook to a model and back",
            "Worked example: a biological system, a financial system, a structural system",
            "Failure: models that fooled their builders",
        ]),
    ]
))

BOOKS.append((
    3, "force", "Force",
    "The grammar of why things move and don't",
    "We point Volume II's mathematics at the mechanical world: statics, dynamics, mechanics of deformable solids, fluid mechanics through compressible flow.",
    [
        (1, "forces-and-fbd", "Forces and free-body diagrams", 90, [
            "Force as a vector",
            "Newton's laws as observations",
            "Free-body diagrams: the discipline",
            "Constraints: rolling, pinning, fixing",
            "Friction",
            "Worked examples: a ladder, a truss joint, a hanging mass",
            "Failure: free-body diagrams that hid the real load path",
        ]),
        (2, "statics-of-rigid-bodies", "Statics of rigid bodies", 100, [
            "Equilibrium conditions",
            "Trusses: method of joints, method of sections",
            "Frames and machines",
            "Distributed loads",
            "Centroids and moments of area",
            "Internal forces: shear, moment, axial",
            "Worked examples: bridge truss, crane",
            "Failure: pin connections, bolted joints, missed load paths",
        ]),
        (3, "stress-and-strain", "Stress and strain", 120, [
            "Internal forces become stresses",
            "Normal and shear stress",
            "Strain: small deformation theory",
            "Hooke's law and elastic constants",
            "Stress transformation, Mohr's circle",
            "Yield and failure criteria (Tresca, von Mises)",
            "Material non-linearity, plasticity preview",
            "Stress concentration",
            "Failure: where parts actually break and why",
        ]),
        (4, "dynamics-and-newtons-laws", "Dynamics: kinematics and Newton's laws", 100, [
            "Position, velocity, acceleration in 1D, 2D, 3D",
            "Rotational kinematics",
            "Newton's second law applied",
            "Work-energy theorem",
            "Impulse-momentum",
            "Conservation of momentum",
            "Worked examples: projectile, oscillating cart, spinning top",
            "Failure: rotating machinery imbalance",
        ]),
        (5, "energy-methods", "Energy methods", 90, [
            "Energy as a unifying currency",
            "Conservation of energy in mechanics",
            "Lagrangian mechanics introduced",
            "Generalised coordinates and constraints",
            "Hamilton's principle",
            "Worked examples: pendulum, double pendulum, sliding bead",
            "Failure: missing degrees of freedom in dynamic analysis",
        ]),
        (6, "vibrations", "Vibrations", 110, [
            "Single-degree-of-freedom oscillators",
            "Damped vibration",
            "Forced response and resonance",
            "Multi-DOF systems and modal analysis",
            "Continuous systems (strings, beams)",
            "Random vibration",
            "Vibration measurement and signature analysis",
            "Failure: Tacoma Narrows, Millennium Bridge, machinery resonance",
        ]),
        (7, "acoustics", "Acoustics: waves in solids and fluids", 100, [
            "The wave equation in fluids",
            "The wave equation in solids: longitudinal and shear",
            "Reflection, refraction, transmission at interfaces",
            "Sound propagation in air, water, ground",
            "Resonance, room acoustics, modal density",
            "Ultrasonic and infrasonic engineering",
            "Noise control: sources, paths, receivers",
            "Failure: acoustic-induced fatigue, sonic boom, rotating-machinery noise",
            "Worked examples: speaker, sonar, NDT",
        ]),
        (8, "beams-columns-frames", "Beams, columns, frames", 120, [
            "Bending: Euler-Bernoulli theory",
            "Beam deflection",
            "Combined loading",
            "Buckling: Euler's formula and beyond",
            "Frames: indeterminate structures",
            "Energy methods for structures",
            "Code-based design preview",
            "Failure: column buckling, beam fatigue, joint detail failures",
        ]),
        (9, "plates-shells-solid-mechanics", "Plates, shells, solid mechanics", 120, [
            "Plate theory",
            "Shell structures",
            "Three-dimensional stress states",
            "Anisotropy preview",
            "Finite-element method introduced",
            "Mesh quality and the engineer's responsibility",
            "Verification, validation, and uncertainty quantification in FEM",
            "Failure: when FEM lies, and why beginners trust it anyway",
        ]),
        (10, "fluid-statics", "Fluid statics", 80, [
            "Pressure as a scalar field",
            "Hydrostatic pressure",
            "Manometers",
            "Forces on submerged surfaces",
            "Buoyancy and stability of floating bodies",
            "Pressure in the atmosphere",
            "Failure: dam breaches and floating instability",
        ]),
        (11, "fluid-dynamics-inviscid", "Fluid dynamics: inviscid", 110, [
            "Continuity equation",
            "Momentum equation (Euler)",
            "Bernoulli's equation",
            "Streamlines, streaklines, pathlines",
            "Vorticity and circulation",
            "Potential flow",
            "Worked examples: flow over an airfoil, nozzle flow, dam spillway",
            "Failure: where Bernoulli does not apply, and why students misuse it",
        ]),
        (12, "viscous-flow-boundary-layers", "Viscous flow, boundary layers", 110, [
            "Newton's law of viscosity",
            "Navier-Stokes equations",
            "Pipe flow: laminar and turbulent",
            "Boundary layers",
            "Drag, lift, and the dimensionless numbers",
            "Turbulence: the unfinished problem",
            "Computational fluid dynamics introduced",
            "Failure: separation, stall, and unexpected drag",
        ]),
        (13, "compressible-flow-aerodynamics", "Compressible flow, aerodynamics", 110, [
            "Speed of sound",
            "Mach number, regimes",
            "Isentropic flow",
            "Normal and oblique shocks",
            "Nozzles, diffusers",
            "Subsonic, transonic, supersonic, hypersonic aerodynamics",
            "Heating in high-speed flow preview",
            "Failure: shock-induced failures, transonic-buzz wing failures",
        ]),
    ]
))

BOOKS.append((
    4, "energy", "Energy",
    "The conserved currency of physics",
    "We extend Volume III's mechanical energy through thermodynamics, heat transfer, electromagnetism, optics, and the quantum effects engineers actually use.",
    [
        (1, "three-laws-of-thermodynamics", "The three laws of thermodynamics", 120, [
            "Energy as accounting",
            "First law: closed and open systems",
            "Second law: entropy and direction",
            "Third law",
            "State functions vs path functions",
            "Internal energy, enthalpy, free energies",
            "Worked examples: gas compression, mixing, phase change",
            "Failure: perpetual motion machines and how to recognise them in proposals",
        ]),
        (2, "equations-of-state-phase-changes", "Equations of state, phase changes", 100, [
            "Ideal gas",
            "Real-gas equations",
            "Liquids and solids: incompressibility approximation",
            "Phase diagrams: PVT, T-S, h-s",
            "Saturation states and quality",
            "Properties tables and software",
            "Worked examples: steam table use, refrigerant cycle",
            "Failure: cavitation, water-hammer, BLEVE",
        ]),
        (3, "heat-engines-refrigerators", "Heat engines and refrigerators", 100, [
            "Carnot cycle as the reference",
            "Rankine cycle",
            "Brayton cycle",
            "Otto, Diesel, Atkinson cycles",
            "Refrigeration cycles",
            "Combined cycles, cogeneration, trigeneration",
            "Failure: efficiency claims that violated the second law",
        ]),
        (4, "entropy-and-arrow-of-time", "Entropy and the arrow of time", 100, [
            "Microscopic interpretation: Boltzmann",
            "Statistical mechanics for engineers",
            "Entropy in chemical and biological systems",
            "Information entropy preview",
            "Free energy and equilibrium",
            "The arrow of time and the second law as observation",
            "Failure: statistical fluctuations vs systematic violations",
        ]),
        (5, "conduction-convection-radiation", "Conduction, convection, radiation", 120, [
            "Fourier's law of conduction",
            "Steady and transient conduction",
            "Convection: free and forced",
            "Radiation: Stefan-Boltzmann, view factors",
            "Combined heat transfer",
            "Worked examples: insulated pipe, electronics cooling, building heat loss",
            "Failure: thermal runaway and where it actually happens",
        ]),
        (6, "heat-exchangers-thermal-systems", "Heat exchangers and thermal systems", 110, [
            "Heat exchanger types",
            "LMTD method",
            "NTU-effectiveness method",
            "Pressure drop and pumping power",
            "Thermal energy storage",
            "District heating and cooling",
            "Failure: fouling, corrosion, tube leaks",
        ]),
        (7, "mass-transfer", "Mass transfer and separation processes", 110, [
            "Diffusion: Fick's laws and binary diffusion",
            "Convective mass transfer and the heat-mass transfer analogy",
            "Mass-transfer coefficients in design",
            "Distillation: trays, packing, HETP, McCabe-Thiele",
            "Absorption, extraction, adsorption",
            "Membrane processes: RO, UF, MF, gas separation",
            "Drying, crystallisation, leaching",
            "Failure: separation breakthroughs, fouling, channelling, equilibrium-stage failures",
        ]),
        (8, "electromagnetism-maxwell", "Electromagnetism: Maxwell's equations as four observations", 120, [
            "Charge, current, fields",
            "Gauss's law",
            "No magnetic monopoles",
            "Faraday's law",
            "Amp\\`ere-Maxwell law",
            "Electromagnetic energy and Poynting vector",
            "Boundary conditions and material laws",
            "Worked examples: solenoid, parallel plate, coaxial cable",
            "Failure: ground loops, induced EMI, lightning",
        ]),
        (9, "circuits", "Circuits: KVL, KCL, impedance", 110, [
            "Lumped-parameter circuits",
            "KVL and KCL",
            "Resistive networks: Th\\'evenin, Norton, superposition",
            "Capacitors and inductors",
            "Transient response: RC, RL, RLC",
            "AC steady-state and impedance",
            "Power: real, reactive, apparent",
            "Three-phase introduction",
        ]),
        (10, "em-waves-antennas", "Electromagnetic waves and antennas", 100, [
            "Wave equation from Maxwell",
            "Plane waves, polarisation",
            "Reflection, refraction",
            "Transmission lines",
            "Waveguides",
            "Antennas: dipole, loop, array introduced",
            "Failure: impedance mismatch, standing waves, RF heating",
        ]),
        (11, "optics", "Optics", 110, [
            "Geometric optics: lenses, mirrors",
            "Aberrations",
            "Wave optics: interference, diffraction",
            "Coherence and lasers preview",
            "Imaging systems: cameras, microscopes, telescopes",
            "Optical fibres",
            "Failure: aberrations that ruined missions",
        ]),
        (12, "quantum-effects-engineers-use", "Engineering quantum mechanics", 80, [
            "Why classical physics is not enough at the device scale",
            "Photon, electron, semiconductor",
            "LED, laser, photovoltaic",
            "The transistor as a quantum device",
            "MRI, electron microscopy, X-ray",
            "Failure: quantum-noise floors and the limits of classical design",
        ]),
        (13, "plasma-physics", "Plasma physics for engineers", 90, [
            "What plasma is: ionisation, Debye length, plasma frequency",
            "Magnetised plasmas: cyclotron motion, drifts",
            "Fluid models of plasma: MHD",
            "Plasma diagnostics",
            "Industrial plasmas: etching, CVD, lighting, propulsion",
            "Fusion engineering: tokamaks, stellarators, inertial confinement",
            "Failure: plasma instabilities, disruption, sputtering",
        ]),
        (14, "energy-systems-integration", "Energy systems integration", 110, [
            "The grid: generation, transmission, distribution",
            "Power generation: thermal, hydro, wind, solar, nuclear, geothermal",
            "Energy storage: batteries, pumped hydro, thermal, hydrogen",
            "Demand-side management and grid control",
            "Off-grid and microgrid systems",
            "The energy transition",
            "Failure: grid blackouts, runaway batteries, generation outages",
        ]),
    ]
))

BOOKS.append((
    5, "matter", "Matter",
    "What things are made of, and why it matters",
    "We cover atoms and bonds, chemistry, the four materials classes, degradation, materials selection, and the manufacturing-driven side of properties.",
    [
        (1, "atoms-bonds-periodic-table", "Atoms, bonds, periodic table", 80, [
            "Atomic structure",
            "The periodic table read engineering-first",
            "Bonding: ionic, covalent, metallic, secondary",
            "Crystals: lattices, defects, grains",
            "Amorphous solids",
            "Why bonding determines properties",
            "Failure: bond-level origins of brittleness, ductility, conductivity",
        ]),
        (2, "reactions-and-equilibria", "Reactions and equilibria", 90, [
            "Stoichiometry refresher",
            "Reaction rates and Arrhenius",
            "Chemical equilibrium and Le Chatelier",
            "Acid-base, redox, complexation",
            "Free energy revisited",
            "Catalysis",
            "Failure: runaway reactions and what triggers them",
        ]),
        (3, "solutions-electrochemistry-batteries", "Solutions, electrochemistry, batteries", 100, [
            "Solutions and concentration",
            "Electrochemical cells",
            "Electrode potentials",
            "Electrolysis",
            "Battery chemistries: lead-acid, NiCd, NiMH, Li-ion, LiFePO4, sodium, flow",
            "Fuel cells",
            "Failure: thermal runaway in Li-ion, dendrite formation, Galaxy Note 7, Boeing 787",
        ]),
        (4, "phase-diagrams", "Phase diagrams", 90, [
            "Single-component phase diagrams",
            "Binary diagrams",
            "Ternary diagrams",
            "Lever rule",
            "Eutectics, peritectics",
            "Phase transformations and TTT diagrams",
            "Worked example: Fe-C diagram and steel heat treatment",
            "Failure: improper heat treatment and brittle parts",
        ]),
        (5, "metals-and-alloys", "Metals and alloys", 110, [
            "Crystal structures of metals",
            "Plastic deformation, dislocations",
            "Strengthening mechanisms",
            "Steels and cast irons",
            "Aluminium alloys",
            "Copper, titanium, magnesium, nickel-based superalloys",
            "Welding and joining metals",
            "Failure: weld failures, hydrogen embrittlement, stress-corrosion cracking",
        ]),
        (6, "polymers", "Polymers", 110, [
            "Polymer chemistry: chains, crosslinks, networks",
            "Thermoplastics vs thermosets vs elastomers",
            "Glass transition and viscoelasticity",
            "Common engineering polymers: PE, PP, PS, ABS, PC, PEEK, PTFE",
            "Polymer processing: extrusion, injection moulding, additive manufacturing",
            "Polymer degradation and ageing",
            "Failure: creep, environmental cracking, photo-oxidation",
        ]),
        (7, "ceramics", "Ceramics", 100, [
            "Ceramic structure and bonding",
            "Mechanical behaviour: brittleness, Weibull statistics",
            "Glasses",
            "Refractories and high-temperature applications",
            "Concrete: the most-used engineered material",
            "Electronic ceramics: piezoelectrics, ferroelectrics",
            "Failure: brittle fracture, thermal shock, concrete spalling",
        ]),
        (8, "composites", "Composites", 100, [
            "Composite types: fibre-reinforced, particulate, laminate",
            "Rule of mixtures",
            "Anisotropy and lay-up design",
            "Carbon fibre, glass fibre, aramid",
            "Manufacturing: hand lay-up, autoclave, RTM, automated fibre placement",
            "Sandwich structures",
            "Failure: delamination, impact damage, fatigue in composites",
        ]),
        (9, "corrosion-and-degradation", "Corrosion and degradation", 100, [
            "Corrosion mechanisms: galvanic, pitting, crevice, intergranular",
            "Stress-corrosion cracking",
            "Protection: coatings, cathodic protection, alloy choice, design",
            "Wear: abrasive, adhesive, erosive",
            "Radiation damage",
            "Polymer ageing revisited",
            "Failure: corrosion-driven catastrophic failures",
        ]),
        (10, "materials-selection", "Materials selection", 100, [
            "The Ashby method introduced",
            "Property charts",
            "Performance indices",
            "Constraints and objectives",
            "Multi-objective trade-offs",
            "Cost, manufacturability, availability, sustainability as constraints",
            "Failure: materials decisions made on price alone",
        ]),
        (11, "manufacturing-driven-properties", "Manufacturing-driven materials properties", 110, [
            "Why how it was made matters as much as what it is",
            "Forging, casting, rolling: residual stresses",
            "Heat-affected zone in welding",
            "Surface treatments: case hardening, shot peening, anodising",
            "Additive manufacturing: anisotropy, porosity, residual stress",
            "Quality control: NDT methods",
            "Failure: as-manufactured vs as-designed: when the gap killed people",
        ]),
        (12, "combustion-explosives-energetic-materials", "Combustion, explosives, energetic materials", 80, [
            "Combustion thermochemistry",
            "Flame structure and propagation",
            "Detonation vs deflagration",
            "Engineering explosives and propellants overview",
            "Pyrotechnics and energetic materials in industry",
            "Failure: dust explosions, BLEVE, chain reactions",
        ]),
    ]
))

BOOKS.append((
    6, "life", "Life",
    "Engineering's encounter with self-organising matter",
    "We treat living systems as engineered objects: bounded, layered, controlled, error-correcting, evolving, failure-prone.",
    [
        (1, "cells-structure-function", "Cells: structure and function", 90, [
            "The cell as engineered object",
            "Membranes, organelles, cytoskeleton",
            "Prokaryotic vs eukaryotic",
            "The cell as control loop",
            "Worked examples: red blood cell, neuron, plant cell, bacterium",
            "Failure: how cells die (apoptosis, necrosis, senescence)",
            "Cross-domain analogy: cell membrane as engineered interface",
        ]),
        (2, "metabolism-and-bioenergetics", "Metabolism and bioenergetics", 100, [
            "ATP as the universal currency",
            "Glycolysis, TCA, oxidative phosphorylation",
            "Photosynthesis",
            "Metabolic flux analysis",
            "Free-energy balances in cells",
            "Worked examples: muscle contraction, fermentation, photosynthesis efficiency",
            "Failure: metabolic disease, thermodynamic limits violated by hype",
        ]),
        (3, "genetics-transcription-translation", "Genetics, transcription, translation", 110, [
            "DNA as digital storage",
            "The central dogma engineering-first",
            "Gene expression and regulation",
            "The genetic code as a designed-by-evolution mapping",
            "Mutation, repair, and error rates",
            "Modern sequencing technology overview",
            "Failure: replication errors, cancer, hereditary disease",
        ]),
        (4, "proteins-as-machines", "Proteins as machines", 100, [
            "Amino acids and primary structure",
            "Protein folding",
            "Enzymes as catalysts",
            "Allosteric regulation",
            "Motor proteins (myosin, kinesin, dynein)",
            "Membrane proteins, ion channels, pumps",
            "Failure: misfolding diseases (Alzheimer's, prion diseases, sickle cell)",
        ]),
        (5, "tissue-and-organ-engineering", "Tissue and organ engineering", 110, [
            "The hierarchy: cells, tissues, organs, systems",
            "Extracellular matrix",
            "Tissue mechanics",
            "Vascularisation as design constraint",
            "Scaffolds and 3D-printed tissue",
            "Stem cells, organoids",
            "Failure: rejection, vascularisation failure, tissue death",
        ]),
        (6, "biomechanics", "Biomechanics", 110, [
            "Bones, joints, muscles as structures",
            "Locomotion: gait, swimming, flight",
            "Cardiovascular biomechanics",
            "Respiratory biomechanics",
            "Cell mechanics: forces a cell exerts and feels",
            "Soft-tissue constitutive models",
            "Failure: musculoskeletal injury, orthopaedic implant failure",
        ]),
        (7, "nervous-and-immune-systems", "Nervous and immune systems as control systems", 100, [
            "Neurons as devices",
            "Action potentials and signal propagation",
            "Synapses, networks",
            "The nervous system as distributed control",
            "The immune system: recognition, response, memory",
            "Adaptive vs innate immunity engineering-first",
            "Failure: autoimmune disease, infection, immunodeficiency",
        ]),
        (8, "population-ecology-epidemiology", "Population biology, ecology, epidemiology", 90, [
            "Population dynamics: growth, carrying capacity",
            "Predator-prey models",
            "SIR/SEIR epidemic models",
            "Ecosystems as networks",
            "Antibiotic resistance, evolution of resistance",
            "Conservation biology engineering-first",
            "Failure: ecosystem collapse, pandemic propagation, COVID-19 modelling lessons",
        ]),
        (9, "synthetic-biology-metabolic-engineering", "Synthetic biology and metabolic engineering", 110, [
            "What synthetic biology is",
            "Standard parts: BioBricks, the iGEM tradition",
            "Genetic circuits: switches, oscillators, logic",
            "Metabolic engineering: redirecting cellular flux",
            "CRISPR and gene editing engineering-first",
            "Directed evolution as design tool",
            "Containment and biosafety levels",
            "Failure: gene-edit off-target effects, gain-of-function risks, dual-use bio",
        ]),
        (10, "bioreactors-and-biomanufacturing", "Bioreactors and biomanufacturing", 100, [
            "Bioreactor types",
            "Mass and heat balances in bioreactors",
            "Aeration, mixing, scale-up",
            "Sterile process design",
            "Cell-culture vs microbial vs plant systems",
            "Downstream processing",
            "Worked example: insulin manufacture",
            "Failure: contamination, scale-up loss, batch failures",
        ]),
        (11, "bioinformatics", "Bioinformatics: sequence, structure, omics", 100, [
            "Sequence data: alphabets, alignment, search",
            "Sequence-to-structure: prediction, AlphaFold and beyond",
            "Genomics and variant calling",
            "Transcriptomics and single-cell RNA-seq",
            "Proteomics, metabolomics, lipidomics, fluxomics",
            "Phylogenetics and evolutionary engineering",
            "ML for biology: graph networks, foundation models",
            "Failure: data leakage in biological ML, batch effects, overfit-to-cohort",
        ]),
        (12, "biocompatibility-and-medical-devices", "Biocompatibility and medical devices", 90, [
            "What biocompatibility means in practice",
            "Material-tissue interactions",
            "Implant failure modes",
            "Drug-device combinations",
            "Sterilisation and packaging",
            "Regulatory framework (FDA, EMA) for medical devices",
            "Failure: Therac-25 (software), Bjork-Shiley heart valve, hip implants",
        ]),
        (13, "living-engineering-anatomical-compiler", "Living engineering: regenerative medicine, the anatomical compiler", 90, [
            "Regenerative medicine: state of the art",
            "Bioelectric morphogenesis (Levin's programme)",
            "The anatomical compiler concept",
            "Engineering challenges in morphogenetic control",
            "Long-horizon framing: what it would mean to compile anatomy",
            "Failure: morphogenetic interventions that did not work, and what they teach",
            "Closing: living matter as the next engineering frontier",
        ]),
    ]
))

BOOKS.append((
    7, "information", "Information",
    "Structure, representation, control, and constraint",
    "We cover logic, algorithms, software, hardware, data, communication, networks, and machine learning, treated as engineering.",
    [
        (1, "logic-sets-formal-languages", "Logic, sets, formal languages", 80, [
            "Propositional and predicate logic",
            "Sets, relations, functions",
            "Formal languages and grammars",
            "Computability: Turing machines, the halting problem",
            "Logic in engineering: requirements as predicates",
            "Failure: ambiguous specifications and their cost",
        ]),
        (2, "number-representations", "Number representations, arithmetic, precision", 80, [
            "Integer representations",
            "IEEE 754 floating-point",
            "Fixed-point arithmetic",
            "Numerical precision in practice",
            "Reproducibility of floating-point computation",
            "Failure: Patriot missile clock drift, Ariane 5 conversion, Pentium FDIV",
        ]),
        (3, "algorithms-and-complexity", "Algorithms and complexity", 110, [
            "What an algorithm is",
            "Time and space complexity",
            "Sorting and searching as canonical examples",
            "Greedy, divide-and-conquer, dynamic programming",
            "Graph algorithms",
            "NP-completeness, intractability",
            "Approximation and randomisation",
            "Failure: $O(n^2)$ algorithms in production at scale",
        ]),
        (4, "data-structures", "Data structures", 110, [
            "Arrays, lists, stacks, queues",
            "Hash tables",
            "Trees: BST, balanced trees, B-trees",
            "Heaps, priority queues",
            "Graphs in memory",
            "Persistent and immutable structures",
            "Cache-aware data layout",
            "Failure: hash collisions weaponised, structural sharing pitfalls",
        ]),
        (5, "programming-languages-paradigms", "Programming languages and paradigms", 120, [
            "Imperative, functional, declarative paradigms",
            "Type systems",
            "Memory management: manual, RAII, GC, ownership",
            "Concurrency primitives at the language level",
            "Metaprogramming and macros",
            "Comparing C, Python, Rust, Lisp, Haskell engineering-first",
            "Failure: type errors, null-pointer dereferences, the undefined-behaviour cost",
        ]),
        (6, "operating-systems", "Operating systems", 110, [
            "What an OS does",
            "Processes, threads, scheduling",
            "Memory: virtual memory, paging",
            "Filesystems",
            "I/O, drivers, interrupts",
            "Containers, virtualisation",
            "Real-time operating systems",
            "Failure: thrashing, priority inversion, deadlocks; Mars Pathfinder",
        ]),
        (7, "computer-architecture", "Computer architecture", 120, [
            "Digital logic refresher",
            "ISAs and the engineer's view",
            "Pipelining, hazards",
            "Caches and memory hierarchy",
            "Branch prediction, speculation",
            "SIMD, vector machines, GPUs",
            "Multicore, NUMA",
            "Failure: Spectre, Meltdown, side channels",
        ]),
        (8, "compilers-and-interpreters", "Compilers and interpreters", 100, [
            "Lexing and parsing",
            "ASTs and intermediate representations",
            "Type checking and analysis",
            "Code generation and optimisation passes",
            "Just-in-time compilation",
            "The compiler as design tool: DSLs",
            "Failure: undefined-behaviour optimisations, ICEs, generated-code bugs",
        ]),
        (9, "databases", "Databases", 100, [
            "Relational model",
            "SQL engineering-first",
            "Indexes and query plans",
            "Transactions, ACID, isolation levels",
            "NoSQL: key-value, document, columnar, graph",
            "Replication and consensus preview",
            "Failure: silent data corruption, lost updates, isolation-level confusion",
        ]),
        (10, "networks-and-protocols", "Networks and protocols", 110, [
            "Layered architecture",
            "Physical and link layer",
            "IP routing",
            "TCP, UDP, QUIC",
            "DNS",
            "HTTP, TLS",
            "BGP and the inter-domain routing problem",
            "Failure: BGP misconfigurations, DNS outages, head-of-line blocking",
        ]),
        (11, "distributed-systems", "Distributed systems", 120, [
            "Why distributed is hard: partial failure",
            "The CAP theorem and its descendants",
            "Consistency models",
            "Consensus: Paxos, Raft",
            "Replication, sharding",
            "Distributed transactions",
            "Microservices and service meshes",
            "Failure: split-brain, Knight Capital, AWS S3 2017 outage",
        ]),
        (12, "cryptography-and-security", "Cryptography and security", 110, [
            "Threat models",
            "Symmetric cryptography",
            "Public-key cryptography",
            "Hash functions, MACs, digital signatures",
            "Authentication, key exchange, TLS internals",
            "Application security: injection, auth, supply chain",
            "Side channels and physical attacks",
            "Failure: Heartbleed, Equifax, SolarWinds, Log4Shell",
        ]),
        (13, "information-theory", "Information theory", 100, [
            "Shannon entropy",
            "Source coding",
            "Channel capacity",
            "Error-correcting codes",
            "Mutual information and Kullback-Leibler divergence",
            "Information theory in physics, biology, ML",
            "Failure: codes pushed beyond Shannon limit; AI claims violating information conservation",
        ]),
        (14, "quantum-computing", "Quantum information and quantum computing", 100, [
            "Qubits and quantum gates",
            "Quantum entanglement and Bell inequalities",
            "Quantum algorithms: Shor, Grover, VQE",
            "Quantum error correction",
            "Quantum-classical hybrid: variational methods",
            "Quantum computing platforms: trapped ions, transmons, photonics, neutral atoms",
            "Post-quantum cryptography",
            "Failure: decoherence, quantum noise, current limits as of 2026",
            "Reality check: where quantum computing actually delivers",
        ]),
        (15, "signal-processing", "Signal processing", 110, [
            "Continuous- and discrete-time signals",
            "Fourier analysis",
            "Sampling and reconstruction revisited from Volume I",
            "Filters: FIR, IIR, design",
            "Time-frequency analysis",
            "Compression: DCT, wavelets",
            "Modern audio, image, video coding overview",
            "Failure: aliasing, ringing, lossy-compression artifacts in safety-critical systems",
        ]),
        (16, "control-of-digital-systems", "Control of digital systems", 100, [
            "The discrete-time control problem",
            "$z$-transform",
            "Digital control law design",
            "Sample-rate selection and aliasing in control",
            "Real-time scheduling and jitter",
            "Networked control",
            "Failure: networked-control failures (industrial control system attacks, Stuxnet)",
        ]),
        (17, "machine-learning-fundamentals", "Machine learning fundamentals", 120, [
            "The setup: data, model, loss",
            "Supervised learning: regression, classification",
            "Unsupervised learning: clustering, dimensionality reduction",
            "Generalisation: bias-variance, regularisation",
            "Cross-validation revisited",
            "Decision trees, ensembles",
            "Probabilistic graphical models",
            "Failure: overfitting, distribution shift, data leakage",
        ]),
        (18, "modern-ai", "Modern AI: deep learning, transformers, LLMs", 110, [
            "Neural networks: from perceptron to MLP",
            "Backpropagation",
            "Convolutional and recurrent architectures",
            "Attention and the transformer",
            "Pretraining, fine-tuning, RLHF",
            "LLMs: capabilities and limits engineering-first",
            "Multimodal models",
            "Failure: hallucination, jailbreaks, distributional cliffs, evaluation games (current as of 2026)",
        ]),
        (19, "software-engineering-as-discipline", "Software engineering as discipline", 110, [
            "What software engineering is",
            "Version control and change discipline",
            "Testing: unit, integration, property, fuzz",
            "Code review",
            "CI/CD",
            "Deployment, observability, incident response",
            "Software architecture: monoliths, services, modular design",
            "Failure: production incidents that started as PR comments dismissed",
        ]),
    ]
))

BOOKS.append((
    8, "machines", "Machines",
    "Model becomes machine",
    "We turn the mathematics, physics, materials, and computing of Volumes I-VII into artifact: mechanism, manufacturing, electronics, sensors, robotics, mechatronic integration.",
    [
        (1, "mechanisms-linkages-cams-gears", "Mechanisms: linkages, cams, gears", 120, [
            "Degrees of freedom, mobility",
            "Four-bar and other planar linkages",
            "Cams and followers",
            "Gears: spur, helical, bevel, worm",
            "Gear trains, ratios, efficiency",
            "Synthesis: designing for a desired motion",
            "Worked examples: bicycle drivetrain, watch escapement, robotic arm",
            "Failure: gear-tooth fatigue, backlash, linkage jam",
        ]),
        (2, "bearings-lubrication-tribology", "Bearings, lubrication, tribology", 100, [
            "Friction, the engineering view",
            "Plain and rolling bearings",
            "Lubrication regimes: boundary, mixed, hydrodynamic, EHL",
            "Lubricant chemistry",
            "Wear and life calculations",
            "Seals and gaskets",
            "Failure: lubrication failures, premature bearing death",
        ]),
        (3, "machine-elements-fasteners-springs-joints", "Machine elements: fasteners, springs, joints", 120, [
            "Bolted joints: preload, friction, fatigue",
            "Welded joints",
            "Adhesive joints",
            "Springs: helical, leaf, Belleville, gas",
            "Shaft design and keyways",
            "Couplings and clutches",
            "Failure: bolt-loosening accidents, weld-failure aviation, joint creep",
        ]),
        (4, "fatigue-and-wear-design", "Machine design under fatigue and wear", 140, [
            "Fatigue revisited at design depth",
            "S-N curves, design factors, safe-life vs damage-tolerant",
            "Fracture mechanics for design",
            "Wear-driven design margins",
            "Reliability-based design",
            "Service-life prediction",
            "Worked example: aircraft, automotive, infrastructure components",
            "Failure: design factors too low or too high; Comet, Aloha, fatigue inspections",
        ]),
        (5, "cad-and-engineering-drawing", "CAD and engineering drawing", 110, [
            "Engineering drawing as communication",
            "Tolerance: dimensional, geometric (GD\\&T)",
            "Surface finish",
            "Parametric CAD: features, constraints",
            "Assembly and motion",
            "PLM and BOM",
            "Drawing for manufacture",
            "Failure: tolerance-stack errors, drawing ambiguity, unit-system clash",
        ]),
        (6, "manufacturing-machining-casting-forming", "Manufacturing: machining, casting, forming", 140, [
            "Manufacturing as constrained optimisation",
            "Machining: turning, milling, drilling, grinding",
            "Casting: sand, investment, die",
            "Forming: forging, rolling, drawing, extrusion",
            "Sheet-metal processes",
            "Joining: welding, brazing, soldering, mechanical",
            "Surface treatments",
            "Failure: process variability, tooling wear, hidden defects",
        ]),
        (7, "additive-manufacturing", "Additive manufacturing", 110, [
            "What additive is and is not",
            "Polymer printing: FDM, SLA, MJF",
            "Metal printing: SLM, EBM, DED",
            "Process-property relationship",
            "Design for additive: lattices, internal structures",
            "Hybrid manufacturing",
            "Industrial qualification of additive parts",
            "Failure: anisotropy, porosity, residual stress, warping",
        ]),
        (8, "analog-electronics", "Analog electronics", 140, [
            "Op-amps as building blocks",
            "Filters: passive and active",
            "Amplifiers: small-signal, power, RF",
            "Oscillators",
            "Power conversion: linear, switching",
            "Noise: sources, characterisation, mitigation",
            "PCB design for analog",
            "Failure: ground loops, oscillation in unwanted feedback paths, layout-induced noise",
        ]),
        (9, "power-electronics", "Power electronics: drives, inverters, grid-tie", 120, [
            "Switched-mode power conversion",
            "DC-DC converters: buck, boost, buck-boost, isolated topologies",
            "Inverters: single-phase, three-phase, multilevel",
            "Rectifiers and power-factor correction",
            "Motor drives: BLDC, induction, synchronous, field-oriented control",
            "Battery management systems and EV powertrains",
            "Grid-tied power electronics: PV inverters, STATCOMs, HVDC",
            "Failure: thermal, EMI, switching transients, capacitor end-of-life",
        ]),
        (10, "digital-electronics-embedded", "Digital electronics, embedded systems", 140, [
            "Logic families and timing",
            "Microcontrollers vs microprocessors vs FPGAs",
            "Embedded firmware: real-time considerations",
            "Communication buses: I$^2$C, SPI, UART, CAN, USB, Ethernet",
            "Power management in embedded",
            "PCB design for digital and mixed-signal",
            "EMC and certification preview",
            "Failure: brownouts, ESD damage, undocumented errata",
        ]),
        (11, "sensors-and-actuators", "Sensors and actuators", 130, [
            "Sensor families revisited at design depth",
            "Calibration in the system context",
            "Sensor fusion preview",
            "Actuators: motors (DC, BLDC, stepper, servo)",
            "Hydraulic and pneumatic actuators",
            "Piezoelectric and shape-memory actuators",
            "Driver electronics for actuators",
            "Failure: sensor drift unaccounted for; actuator stalls and runaway",
        ]),
        (12, "mems-microsystems", "MEMS and microsystems", 100, [
            "What MEMS are and why scaling matters",
            "MEMS fabrication: bulk, surface, LIGA",
            "MEMS sensors: accelerometer, gyroscope, pressure, microphone",
            "MEMS actuators: comb drives, piezo, electrothermal",
            "RF MEMS and BAW/FBAR filters",
            "Microfluidics: lab-on-chip, droplet microfluidics, organ-on-chip",
            "Optical MEMS: DLP, MEMS mirrors, photonic integration",
            "Failure: stiction, charge-trapping, packaging-induced stress",
        ]),
        (13, "robotics", "Robotics", 140, [
            "Kinematics: forward and inverse",
            "Dynamics",
            "Trajectory planning",
            "Sensing for robots: vision, lidar, force",
            "Path planning",
            "Manipulation and grasping",
            "Mobile robotics: SLAM, navigation",
            "Failure: collisions, kinematic singularities, vision under adversarial conditions",
        ]),
        (14, "hydraulics-pneumatics-mechatronic-integration", "Hydraulics, pneumatics, mechatronic integration", 130, [
            "Fluid power fundamentals",
            "Hydraulic circuits, components, valves",
            "Pneumatic systems and applications",
            "Combined systems and selection",
            "Mechatronic integration: mechanical + electrical + digital",
            "System-level design for the full machine",
            "Documentation, commissioning, handover",
            "Failure: leak failures, contamination, integration interface failures",
        ]),
    ]
))

BOOKS.append((
    9, "systems", "Systems",
    "Many things working together without lying to themselves",
    "Feedback, control, signals, reliability, queueing, optimisation under uncertainty, multi-agent systems, infrastructure, cyber-physical systems, resilience, maintenance.",
    [
        (1, "modelling-dynamic-systems", "Modelling dynamic systems", 100, [
            "What a system is, what a model is",
            "Lumped vs distributed",
            "Linear vs nonlinear",
            "Time-invariant vs time-varying",
            "Block diagrams and signal-flow graphs",
            "System identification introduced",
            "Worked examples across mechanical, thermal, electrical, biological, social systems",
            "Failure: model misspecification at the foundation",
        ]),
        (2, "linear-control", "Linear control: transfer functions, Bode, Nyquist", 120, [
            "Plant, controller, feedback",
            "Transfer functions",
            "Stability: poles, root locus",
            "Bode plots",
            "Nyquist criterion",
            "PID design and tuning",
            "Lead-lag compensators",
            "Failure: gain margin and phase margin too low; resonance amplification",
        ]),
        (3, "state-space-modern-control", "State-space and modern control", 120, [
            "State-space representation",
            "Controllability and observability",
            "Pole placement",
            "LQR",
            "Observers and Kalman filtering preview",
            "LQG",
            "Discrete-time state-space",
            "Failure: unmodelled dynamics, observability loss in real systems",
        ]),
        (4, "nonlinear-and-robust-control", "Nonlinear and robust control", 110, [
            "Lyapunov stability",
            "Linearisation and its limits",
            "Sliding-mode control",
            "Backstepping introduction",
            "$H_\\infty$ control",
            "Robust control under uncertainty",
            "Saturation and anti-windup",
            "Failure: chattering in sliding mode, integrator wind-up, modelling-uncertainty surprises",
        ]),
        (5, "adaptive-and-learning-control", "Adaptive and learning control", 100, [
            "Why adaptive",
            "Model-reference adaptive control",
            "Self-tuning regulators",
            "Reinforcement-learning control engineering-first",
            "Safe RL: shields, constraint-respecting policies",
            "Failure: adaptation in the wrong direction; learning-induced instability",
            "Cross-references: Volume VII chapter 17 connection",
        ]),
        (6, "stochastic-systems-kalman", "Stochastic systems and Kalman filtering", 120, [
            "Random processes",
            "Linear Gaussian systems",
            "Kalman filter derivation engineering-first",
            "Extended and unscented Kalman filter",
            "Particle filters",
            "Sensor fusion",
            "Failure: filter divergence, mismatched noise covariance, the GPS-jamming problem",
        ]),
        (7, "reliability-theory", "Reliability theory", 110, [
            "Failure rate, MTBF, MTTR",
            "Bathtub curve",
            "Reliability functions and distributions",
            "Series, parallel, $k$-of-$n$ systems",
            "Fault-tree and event-tree analysis",
            "FMEA, FMECA",
            "Common-cause failure",
            "Failure: redundancy that did not help",
        ]),
        (8, "queueing-and-capacity", "Queueing theory and capacity planning", 100, [
            "Arrivals and service",
            "$M/M/1$, $M/M/c$, $M/G/1$",
            "Networks of queues",
            "Little's law in practice",
            "Capacity planning and queueing-theoretic sizing",
            "Worked examples: server farm, hospital ER, manufacturing line",
            "Failure: queues that became unstable; the cost of running too hot",
        ]),
        (9, "optimisation-in-operation", "Optimisation in operation", 100, [
            "LP/IP/MILP in operations",
            "Network flow problems",
            "Scheduling",
            "Inventory control",
            "Stochastic programming",
            "Robust optimisation",
            "Failure: optimised systems with no slack and the cost when reality bit",
        ]),
        (10, "project-management", "Engineering project management", 100, [
            "Projects as systems",
            "Work-breakdown structure and estimation",
            "Scheduling: PERT, CPM, critical chain, resource-constrained",
            "Risk management: registers, qualitative and quantitative analysis",
            "Stakeholder analysis and communication plans",
            "Earned-value management",
            "Programme and portfolio management",
            "Failure: schedule cynicism, scope creep, hidden dependencies, megaproject pathologies",
        ]),
        (11, "decision-under-uncertainty", "Decision-making under uncertainty", 110, [
            "Decision theory: utility, risk, regret",
            "Expected utility and its critics",
            "Markov decision processes",
            "Partially observable MDPs",
            "Multi-criteria decision-making",
            "Decision-making in real organisations",
            "Failure: anchoring, framing, motivated reasoning in engineering decisions",
        ]),
        (12, "multi-agent-and-game-theoretic", "Multi-agent and game-theoretic systems", 110, [
            "Game theory engineering-first",
            "Nash equilibria, dominant strategies",
            "Mechanism design and auctions",
            "Coordination and consensus in multi-agent systems",
            "Swarm intelligence and stigmergy: indirect coordination through environment",
            "Coupled-agent failure modes",
            "Failure: races to the bottom, tragedies of the commons in engineered systems",
        ]),
        (13, "network-systems", "Network systems", 120, [
            "Power grids: structure and dynamics",
            "Transport networks",
            "Communication networks revisited from Volume VII",
            "Water and gas networks",
            "Network resilience and graph properties",
            "Cascading failure in network systems",
            "Failure: 2003 North America blackout, 2012 India blackout, BGP cascades",
        ]),
        (14, "cyber-physical-systems", "Cyber-physical systems", 120, [
            "What CPS are",
            "Sensor-actuator-network-controller architectures",
            "Real-time and safety-critical CPS",
            "SCADA and ICS",
            "Industrial IoT",
            "Cyber-physical security (Stuxnet, water-utility attacks)",
            "Verification and validation of CPS",
            "Failure: the entire chapter is a failure section, with synthesis",
        ]),
        (15, "infrastructure-as-system", "Infrastructure as system", 110, [
            "Infrastructures as engineered systems",
            "Asset management at scale",
            "Lifecycle costs and total-cost-of-ownership",
            "Renewal vs replace decisions",
            "Coupled infrastructures and systemic risk",
            "The political economy of infrastructure",
            "Failure: aging infrastructure and the cost of deferred maintenance",
        ]),
        (16, "coupled-human-technical-systems", "Coupled human-technical systems", 110, [
            "The operator in the loop",
            "Human factors and ergonomics",
            "Automation surprises (Bainbridge's paradox)",
            "Levels of automation",
            "Mode confusion and shared control",
            "Trust calibration in automated systems",
            "Failure: Three Mile Island, Air France 447, Tesla Autopilot incidents",
        ]),
        (17, "resilience-and-antifragility", "Resilience and antifragility", 110, [
            "Resilience defined and operationalised",
            "Robustness vs resilience vs antifragility",
            "Bouncing back: recovery curves and capacity",
            "Slack, redundancy, modularity, diversity",
            "Stress testing and chaos engineering",
            "Resilience metrics",
            "Failure: resilience theatre, brittle systems that called themselves robust",
        ]),
        (18, "maintenance-observability-life-cycle", "Maintenance, observability, life-cycle", 120, [
            "Why maintenance is engineering's largest expense and least taught topic",
            "Maintenance strategies: corrective, preventive, predictive, prescriptive",
            "Condition monitoring",
            "Reliability-centred maintenance",
            "Observability: what to measure to manage",
            "Life-cycle costing revisited",
            "Decommissioning and end-of-life",
            "Failure: maintenance neglect as the root cause; the slow accident",
        ]),
        (19, "seeing-systems-whole", "Seeing systems whole", 120, [
            "Synthesis: what we have learned across the seventeen chapters",
            "Systems thinking practices: causal-loop diagrams, stock-and-flow models, archetype recognition",
            "The discipline of asking what the system optimises against",
            "Boundaries: where to cut, where to include",
            "Emergent behaviour",
            "The systems engineer as professional role",
            "Failure: when ``systems thinking'' became a slogan that hid the work",
            "Closing: handing the reader to Volume X",
        ]),
    ]
))

BOOKS.append((
    10, "failure", "Failure",
    "A real engineer is someone who knows how things die",
    "We make failure a first-class subject of study: mechanisms, statistical structure, organisational and political contexts, and the discipline of post-mortem.",
    [
        (1, "discipline-of-failure", "Failure as engineering subject", 80, [
            "Why failure deserves a volume",
            "The taxonomy of failure",
            "The Swiss-cheese model and its critics",
            "The HRO and resilience-engineering traditions",
            "Failure as data, not as shame",
            "The reader's posture: how to study failure without becoming useless",
            "Failure: failures of failure analysis",
        ]),
        (2, "fatigue-fracture-mechanics", "Fatigue, S-N curves, fracture mechanics", 120, [
            "Fatigue mechanism: nucleation, propagation, fracture",
            "S-N curves and their limits",
            "Variable amplitude, Miner's rule",
            "Linear-elastic fracture mechanics",
            "Elastic-plastic fracture mechanics",
            "Crack-growth analysis",
            "Inspection intervals and damage tolerance",
            "Case: de Havilland Comet, Aloha 243, Liberty Ships",
        ]),
        (3, "corrosion-wear-degradation", "Corrosion, wear, environmental degradation", 100, [
            "Corrosion failure mechanisms revisited at depth",
            "Environmental cracking",
            "Hydrogen embrittlement",
            "Wear in operating systems",
            "Bioenvironmental failure (medical implants, marine systems)",
            "Case: Mianus River Bridge, Erika, Boeing 707 oxygen-line corrosion",
        ]),
        (4, "instabilities-runaway-buckling-resonance", "Instabilities, runaway, buckling, resonance", 100, [
            "Buckling at depth",
            "Aeroelastic instability",
            "Thermal runaway",
            "Chemical runaway",
            "Mechanical resonance failures",
            "Numerical instability as engineering failure",
            "Case: Tacoma Narrows, Texas City refinery 2005, Therac-25 race condition, Lyon-Saint-Exup\\'ery station roof",
        ]),
        (5, "software-defects", "Software defects: types of bugs", 110, [
            "Why software fails differently from hardware",
            "Memory-safety bugs",
            "Logic and specification bugs",
            "Numerical bugs",
            "Concurrency bugs",
            "Time-related bugs",
            "Configuration and environment bugs",
            "Case: Mars Climate Orbiter, Knight Capital, GitHub 24-hour outage 2018",
        ]),
        (6, "concurrency-distributed-failure", "Concurrency and distributed failure", 110, [
            "The hard problem of partial failure",
            "Race conditions",
            "Deadlock, livelock, starvation",
            "Distributed-system failure modes",
            "Time, clocks, ordering, the missing common substrate",
            "Byzantine failure",
            "Case: Therac-25 (race), the 2017 AWS S3 outage, the 2020 Cloudflare outage",
        ]),
        (7, "cascading-failure-in-networks", "Cascading failure in networks", 110, [
            "Why networks cascade",
            "Power-grid cascades",
            "Financial-system cascades engineering-first",
            "Internet routing cascades",
            "Supply-chain cascades",
            "Models of cascading failure",
            "Case: 2003 North America blackout, 2008 financial crisis, 2021 Ever Given Suez blockage",
        ]),
        (8, "common-mode-failure", "Common-mode failure", 100, [
            "Why redundancy sometimes does not help",
            "Identifying common-mode dependencies",
            "Latent shared causes",
            "Cosmic rays, EMP, environmental common-mode",
            "Software in redundant systems",
            "Case: Three Mile Island common-mode loss, Boeing 737 MAX MCAS dual-channel collapse",
        ]),
        (9, "human-factors-operator-error", "Human factors and operator error", 100, [
            "The human as part of the system",
            "Skill-based, rule-based, knowledge-based behaviour (Rasmussen)",
            "Cognitive biases under stress",
            "Mode confusion and automation surprises revisited from Volume IX",
            "Crew resource management",
            "The myth of operator error and what it usually hides",
            "Case: Air France 447, Eastern 401, Tenerife",
        ]),
        (10, "organisational-failure", "Organisational failure", 120, [
            "Organisations as failure-producing systems",
            "Vaughan's normalisation of deviance",
            "Production pressure and safety drift",
            "Whistleblower dynamics",
            "The role of regulator capture",
            "Case in full depth: Challenger and Columbia, Boeing 737 MAX, Bhopal, Chernobyl",
        ]),
        (11, "regulatory-and-certification-failure", "Regulatory and certification failure", 110, [
            "Regulators and engineering",
            "Certification regimes: aviation, medical devices, nuclear, automotive",
            "Self-certification and its discontents",
            "Regulatory capture",
            "Case: Boeing 737 MAX certification, Therac-25 regulatory aftermath, Volkswagen diesel-emissions defeat device",
            "What the engineer owes the regulator and vice versa",
        ]),
        (12, "forensic-engineering", "Forensic engineering and accident investigation", 110, [
            "The role of the forensic engineer",
            "Evidence preservation",
            "Reconstruction methods",
            "Metallurgical, electrical, structural forensics",
            "Software forensics",
            "Reporting standards: NTSB, AAIB, BEA",
            "Legal and ethical pressures on forensic engineers",
            "Failure: when forensic engineering reached the wrong conclusion",
        ]),
        (13, "near-misses-and-weak-signals", "Near-misses and weak signals", 80, [
            "Why near-misses are the cheap data",
            "Reporting cultures: aviation ASRS, medical reporting",
            "Weak-signal recognition",
            "The HRO posture",
            "Anomaly detection from operational data",
            "Case: organisations that ignored weak signals; ATR-72 icing, Comair 5191",
        ]),
        (14, "maintenance-failure", "Maintenance failure: the slow accident", 80, [
            "Maintenance neglect as a leading failure cause",
            "Aging infrastructure",
            "Deferred-maintenance dynamics",
            "The political economy of maintenance",
            "Case: Genoa Morandi Bridge, Flint water crisis, ageing nuclear plants",
        ]),
        (15, "climate-ecological-planetary-failure", "Climate, ecological, planetary failure", 100, [
            "Engineering as ecological actor",
            "Pollution as engineered byproduct",
            "Climate change engineering-first",
            "Tipping points and irreversibility",
            "Engineering responses to ecological failure",
            "Case: the ozone-layer near-miss (and the success), CFC industry, lead in petrol, PFAS",
        ]),
        (16, "discipline-of-post-mortem", "Post-mortem as practice", 80, [
            "The post-mortem as engineering practice",
            "Blameless post-mortems",
            "The five-whys and its critics",
            "STAMP and other systemic methods",
            "Writing a post-mortem document",
            "The post-mortem habit at organisational scale",
            "Closing: handing the reader to Volume XI",
        ]),
    ]
))

BOOKS.append((
    11, "design", "Design",
    "Breakage becomes discipline",
    "We give the reader the practice of design under risk: requirements, concept, detail, simulation, prototype, test, review, certification, ethics, capstone.",
    [
        (1, "what-design-is", "What design is", 70, [
            "Design as the synthesis of constraint, want, knowledge, judgment",
            "The design process: stages and iterations",
            "The design space and how to navigate it",
            "Design as conversation with reality",
            "What design is not: gilded analysis, decoration, marketing",
            "Failure: design that did not start from need",
        ]),
        (2, "requirements-and-specification", "Requirements and specification", 100, [
            "Why requirements precede design",
            "Eliciting requirements",
            "Functional vs non-functional requirements",
            "Specifications: how precise is precise enough",
            "Requirements traceability",
            "Verification and validation distinguished",
            "Requirements as a conflict-management tool",
            "Failure: missed, ambiguous, or self-contradictory requirements",
        ]),
        (3, "user-research", "User research and human-centred design", 85, [
            "What user research is and what it is not",
            "Methods: interviews, contextual inquiry, ethnography",
            "Surveys, A/B testing, analytics, telemetry",
            "Personas, journey maps, jobs-to-be-done",
            "Accessibility and inclusive design as research practice",
            "Synthesis: insights to requirements",
            "Failure: research that asked the wrong questions; the wrong-user trap",
            "Worked examples: medical-device user research, industrial-control-room redesign",
        ]),
        (4, "conceptual-design-and-sketching", "Conceptual design and sketching", 80, [
            "Generation of alternatives",
            "Sketching as engineering tool",
            "Morphological analysis",
            "TRIZ engineering-first",
            "Concept selection: weighted matrix, Pugh chart",
            "First-pass cost and feasibility estimates",
            "Failure: premature commitment to a concept",
        ]),
        (5, "detailed-design-and-analysis", "Detailed design and analysis", 100, [
            "From concept to detail",
            "Tolerance budgets",
            "Stress analysis at design depth revisited",
            "Thermal, electromagnetic, fluid, control analysis",
            "Design rules of thumb across disciplines",
            "Engineering judgment: when calculation ends and judgment begins",
            "Documentation as part of design",
            "Failure: detailed design that hid load paths from the analyst",
        ]),
        (6, "simulation-and-digital-twins", "Simulation and digital twins", 110, [
            "Simulation as design tool",
            "Verification of simulation",
            "Validation against measurement",
            "Uncertainty quantification in simulation",
            "Multi-physics coupling",
            "Digital twins",
            "The cost and limit of simulation",
            "Failure: simulations that fooled their builders",
        ]),
        (7, "prototyping-and-iteration", "Prototyping and iteration", 90, [
            "Why prototype",
            "Prototype types: foam, functional, beta, MVP",
            "Prototype-driven learning",
            "Iteration cadence",
            "Knowing when to commit",
            "Pilot production and pre-production runs",
            "Failure: prototypes that became products without the work in between",
        ]),
        (8, "testing-and-validation", "Testing and validation", 110, [
            "Test-design as engineering discipline",
            "Functional, performance, environmental, life testing",
            "Statistical design of experiments",
            "Accelerated testing",
            "Software testing revisited from Volume VII",
            "Field testing and beta programmes",
            "Test-data management and reproducibility",
            "Failure: test plans that proved only what they were designed to prove",
        ]),
        (9, "design-reviews-certification-sign-off", "Design reviews, certification, sign-off", 80, [
            "The design review as engineering practice",
            "PDR, CDR, FDR",
            "Independent review and adversarial design",
            "Certification regimes revisited at design depth",
            "The signature: what an engineer commits when they sign",
            "Failure: rubber-stamp reviews and the legal aftermath",
        ]),
        (10, "manufacturability-maintainability-sustainability", "Manufacturability, maintainability, sustainability, accessibility", 90, [
            "Design for manufacture",
            "Design for assembly",
            "Design for maintenance",
            "Design for inspection",
            "Design for end-of-life",
            "Sustainable design",
            "Life-cycle analysis",
            "Failure: parts that could not be repaired, replaced, or recycled",
        ]),
        (11, "ethics-under-risk", "Ethics under risk and uncertainty", 80, [
            "Engineering ethics as practice, not aspiration",
            "Codes of ethics and what they actually do",
            "The duty to report and the duty to refuse",
            "Conflicts of interest",
            "Dual-use, surveillance, military: where the line is",
            "Whistleblowing",
            "Failure: ethical compromises that became technical disasters",
        ]),
        (12, "design-studios", "Design studios: integrated case studies", 100, [
            "Studio 1: a pump for a low-resource environment",
            "Studio 2: an autonomous mobile robot for a defined environment",
            "Studio 3: a small renewable energy installation",
            "Studio 4: a software-physical system with safety implications",
            "Failure: each studio includes its own failure mode analysis",
            "Reflection: what each studio teaches that the chapters could not",
        ]),
        (13, "the-capstone-problem", "The capstone problem", 70, [
            "The capstone framing",
            "The capstone brief: a real engineering problem at meaningful scale",
            "What the reader brings: every previous volume",
            "The capstone deliverable: a design pack reviewable by a panel",
            "What graduation looks like",
            "The reader's place after the book",
            "Closing: handing the reader to Volume XII",
        ]),
    ]
))

BOOKS.append((
    12, "civilization", "Civilization",
    "Discipline becomes civilization",
    "What the previous eleven volumes are for. Energy, water, transport, food, healthcare, cities, climate, planetary engineering, and the political economy of engineered life.",
    [
        (1, "engineering-at-civilization-scale", "Engineering at civilization scale", 90, [
            "What scale changes",
            "The unit of analysis: from artifact to infrastructure to system-of-systems",
            "Time horizons engineers have to learn",
            "The engineer as one of many actors",
            "The thesis revisited at civilization scale",
            "Failure: civilization-scale projects that did not understand they were civilization-scale",
        ]),
        (2, "energy-systems-for-a-planet", "Energy systems for a planet", 110, [
            "Global energy demand: history and projection",
            "The energy mix: where we are, where we go",
            "Decarbonisation pathways",
            "Storage at planetary scale",
            "Grids: continental and intercontinental",
            "Nuclear power and its institutional context",
            "Hydrogen, synthetic fuels, alternative carriers",
            "Failure: stranded-asset and just-transition issues",
        ]),
        (3, "water-supply-sanitation-climate", "Water: supply, sanitation, climate", 100, [
            "The water cycle as engineered domain",
            "Drinking-water supply at city scale",
            "Sanitation and wastewater",
            "Industrial water",
            "Agricultural water",
            "Water under climate change",
            "Failure: water failures (Flint, Cape Town day zero, Aral Sea, Jakarta sinking)",
        ]),
        (4, "transport-networks", "Transport networks", 110, [
            "Modal mix: road, rail, sea, air",
            "Urban transport networks",
            "Inter-city and freight networks",
            "Maritime and shipping",
            "Aviation",
            "Decarbonising transport",
            "Failure: car-centric urbanism and its costs",
        ]),
        (5, "food-agriculture-logistics", "Food: agriculture, logistics, security", 100, [
            "The agricultural system as engineered domain",
            "Soil, water, fertilisers, pesticides",
            "Mechanisation and precision agriculture",
            "Food processing, cold chain, logistics",
            "Food security and supply-chain resilience",
            "Alternative protein and emerging food systems",
            "Failure: food-system failures (Irish famine, the dust bowl, banana panic, 2008 food crisis)",
        ]),
        (6, "healthcare-systems", "Healthcare systems", 100, [
            "Healthcare as engineered system",
            "Hospital design and operation",
            "Medical-device infrastructure revisited from Volume VI",
            "Public-health engineering",
            "Pandemic engineering: surveillance, response, manufacturing",
            "Healthcare equity engineering-first",
            "Failure: healthcare-system failures (Walter Reed, Mid Staffordshire, COVID-19 logistics)",
        ]),
        (7, "buildings-cities-urbanism", "Buildings, cities, urbanism", 110, [
            "The building as engineered system",
            "Urban systems: streets, blocks, neighbourhoods, districts, cities",
            "Density, sprawl, and their engineering implications",
            "Climate-resilient cities",
            "Affordable-housing engineering",
            "The city as institution: planning, zoning, governance",
            "Failure: housing crises, urban-renewal disasters, planning failures",
        ]),
        (8, "communications-digital-infrastructure", "Communications and digital infrastructure", 100, [
            "Communications as civilization infrastructure",
            "Internet at planetary scale",
            "Submarine cables and the actual internet",
            "Cellular networks",
            "Satellites and orbital infrastructure",
            "Algorithmic governance: who controls flow",
            "Failure: undersea cable cuts, single-points of failure, BGP at planetary scale, content-moderation as engineering",
        ]),
        (9, "defence-security", "Defence and security as engineered systems", 100, [
            "Defence as engineered domain",
            "Defence-industrial supply chains and procurement",
            "Sensors, networks, and command-and-control",
            "Cyber defence at the state scale",
            "Critical-infrastructure defence",
            "Dual-use technology and export control",
            "Arms control and verification engineering",
            "Failure: defence-systems failures (Patriot timing, Bradley vehicle, F-35 ALIS)",
        ]),
        (10, "space-infrastructure", "Space infrastructure: orbital and planetary engineering", 100, [
            "Orbital mechanics for engineers",
            "Launch systems and propulsion",
            "Satellites: design, lifetime, end-of-life",
            "Constellation engineering: Starlink, Galileo, GPS, OneWeb",
            "Communications and earth observation",
            "Crewed spaceflight and space stations",
            "Mars and lunar engineering: Artemis, ISRU",
            "Space debris and orbital sustainability",
            "Failure: launch failures, in-orbit losses, mission failures",
        ]),
        (11, "climate-engineering-mitigation-adaptation", "Climate engineering, mitigation, adaptation", 120, [
            "Climate as engineered domain whether we want it or not",
            "Mitigation engineering: where the most leverage is",
            "Adaptation engineering",
            "Carbon dioxide removal: the menu",
            "Solar radiation management: governance and risk",
            "Climate engineering as international issue",
            "Failure: climate-policy failures and what engineers should learn from them",
        ]),
        (12, "planetary-boundaries-biosphere-engineering", "Planetary boundaries and biosphere engineering", 110, [
            "The planetary-boundaries framework",
            "Biogeochemical cycles as engineered domain",
            "Biodiversity and ecosystem services",
            "Soil at planetary scale",
            "Oceans",
            "Polar regions and cryosphere",
            "Engineering for biosphere health",
            "Failure: nutrient-cycle failures, fisheries collapse, ozone (the success), PFAS (the failure)",
        ]),
        (13, "political-economy-of-engineered-life", "The political economy of engineered life", 120, [
            "Who decides what gets built",
            "Who pays, who benefits, who is displaced",
            "The maintenance economy and its political invisibility",
            "Standards and standards-setting bodies",
            "Procurement and how it shapes engineering",
            "The engineering profession and its institutional reality",
            "Engineering-as-political: the case made in full",
            "Failure: engineering decisions that hid the politics; engineering decisions that were ambushed by the politics",
        ]),
        (14, "future-of-the-artificial", "The future of the artificial", 100, [
            "The artificial world as it stands",
            "The trajectories: techno-optimist, techno-pessimist, techno-realist",
            "What only the next generation will see",
            "What the engineer's child should learn",
            "The engineer in the world to come",
            "Closing the twelve volumes: the thesis returns",
            "The author's posture: what the reader keeps after the book",
            "The book ends; the work does not",
        ]),
    ]
))


# ---- Dossier metadata parsing ----
#
# The generator now enriches each chapter shell with editorial metadata
# (half-life, archetypes invoked, project brief, exercise count) parsed
# from the dossiers under docs/research/<NN>-<slug>/_volume.md (volume-level
# half-life, fallback archetype) and docs/research/<NN>-<slug>/ch<MM>-<slug>.md
# (per-chapter project, exercises, archetype overrides). This makes the
# dossiers the canonical source of per-chapter metadata and removes the
# source-of-truth drift the project diagnostic flagged.
#
# Parser tolerance:
# - Half-life is read from the volume-level header `Half-life of the contents:`
#   and applied to every chapter as a default. Per-chapter overrides can be
#   added by future passes if granularity is needed.
# - Archetype, Project, and Exercises are read from per-chapter blocks.
# - Two formats are supported in the dossiers: bold lines on separate lines
#   (Volume I style) and concatenated on one line (Volume III style).

import re

DOSSIER_DIR = ROOT / "docs" / "research"

HALF_LIFE_KEYWORDS = ["foundational", "fast-aging", "medium-life", "durable"]

# Volume-level overrides for cases where the dossier prose mixes terms and the
# automatic keyword lookup would pick the wrong dominant half-life.
VOLUME_HALF_LIFE_OVERRIDES = {
    7: "durable",       # mostly-durable foundations; modern-AI/security/networking are exceptions
    12: "medium-life",  # explicitly stated medium-life at volume scope
}

# Per-chapter half-life overrides: specific chapters whose half-life differs
# from the volume default. Drawn from the per-volume dossier prose.
# Coordinates updated for the Phase-0.6 expansion (174 chapters).
CHAPTER_HALF_LIFE_OVERRIDES = {
    (2, 16): "medium-life",   # Numerical methods (concrete tooling)
    (4, 13): "medium-life",   # Plasma physics (industrial applications evolve)
    (4, 14): "medium-life",   # Energy systems integration (mix dependent)
    (6, 9):  "medium-life",   # Synthetic biology
    (6, 10): "medium-life",   # Bioreactors and biomanufacturing
    (6, 11): "medium-life",   # Bioinformatics (tools and references move fast)
    (6, 13): "medium-life",   # Living engineering / anatomical compiler (speculative)
    (7, 10): "medium-life",   # Networks and protocols
    (7, 11): "medium-life",   # Distributed systems (specifics)
    (7, 12): "medium-life",   # Cryptography and security (current attacks)
    (7, 14): "fast-aging",    # Quantum information and quantum computing
    (7, 17): "medium-life",   # ML fundamentals (algorithms move)
    (7, 18): "fast-aging",    # Modern AI: deep learning, transformers, LLMs
    (8, 7):  "medium-life",   # Additive manufacturing
    (8, 9):  "medium-life",   # Power electronics (semiconductor evolution)
    (8, 10): "medium-life",   # Digital electronics, embedded
    (8, 12): "medium-life",   # MEMS and microsystems
    (8, 13): "medium-life",   # Robotics specifics
    (9, 14): "medium-life",   # Cyber-physical systems
    (9, 15): "medium-life",   # Infrastructure as system (specifics)
    (11, 6): "medium-life",   # Simulation and digital twins
    (12, 9): "medium-life",   # Defence and security as engineered systems
    (12, 10): "medium-life",  # Space infrastructure
}


def parse_volume_half_life(text):
    """Return the dominant half-life keyword from the dossier header. Falls back to TBD."""
    m = re.search(r"\*\*Half-life of the contents\*\*:\s*([^\n]+)", text)
    if not m:
        return "TBD"
    head = m.group(1).lower()
    for kw in HALF_LIFE_KEYWORDS:  # ordered: foundational > fast-aging > medium-life > durable
        if kw in head:
            return kw
    return "TBD"


def parse_one_chapter_md(path):
    """Parse a single chapter dossier file. Returns dict with archetypes, project, exercises."""
    if not path.exists():
        return None
    text = path.read_text()
    arch_m = re.search(r"\*\*Archetype[^*]*\*\*\s*:\s*([^\n*]+?)\s*(?:\*\*|\.|\n|$)", text)
    proj_m = re.search(r"\*\*Project\*\*\s*:\s*([^\n*]+?)\s*(?:\*\*|\n|$)", text)
    ex_m = re.search(r"\*\*Exercises?\*\*[^:]*:\s*~?(\d+)", text)
    return {
        "archetypes": arch_m.group(1).strip().rstrip(".") if arch_m else "TBD",
        "project": proj_m.group(1).strip().rstrip(".") if proj_m else "TBD",
        "exercises": int(ex_m.group(1)) if ex_m else 30,
    }


def parse_chapter_meta(volume_num, slug):
    """Return {ch_num: {"half_life", "archetypes", "project", "exercises"}}.

    Reads from the per-volume directory layout under docs/research/<NN>-<slug>/:
    a `_volume.md` for the volume-level half-life and a `chMM-chslug.md` per chapter.
    Falls back to defaults if a file is missing.
    """
    vol_dir = DOSSIER_DIR / f"{volume_num:02d}-{slug}"
    if not vol_dir.is_dir():
        return {}
    # Volume half-life: parse from _volume.md, then apply override if any.
    volume_md = vol_dir / "_volume.md"
    if volume_md.exists():
        vol_half_life = parse_volume_half_life(volume_md.read_text())
    else:
        vol_half_life = "TBD"
    vol_half_life = VOLUME_HALF_LIFE_OVERRIDES.get(volume_num, vol_half_life)

    out = {}
    # Per-chapter files: chMM-chslug.md.
    for chapter_md in sorted(vol_dir.glob("ch*-*.md")):
        m = re.match(r"ch(\d+)-", chapter_md.name)
        if not m:
            continue
        ch_num = int(m.group(1))
        meta = parse_one_chapter_md(chapter_md) or {}
        ch_half_life = CHAPTER_HALF_LIFE_OVERRIDES.get((volume_num, ch_num), vol_half_life)
        out[ch_num] = {
            "half_life": ch_half_life,
            "archetypes": meta.get("archetypes", "TBD"),
            "project": meta.get("project", "TBD"),
            "exercises": meta.get("exercises", 30),
        }
    return out


# ---- Generation ----

def write_book_opener(num, slug, name, tagline, scope):
    vol_dir = ROOT / "volumes" / f"{num:02d}-{slug}"
    vol_dir.mkdir(parents=True, exist_ok=True)
    path = vol_dir / "_volume.tex"
    content = f"""% Volume {num}: {name}
% Opener: tagline + scope. Sits immediately after the \\part{{}} declaration.

\\vspace*{{1.5cm}}
\\begin{{center}}
\\itshape\\large
{tagline}
\\end{{center}}
\\vspace{{0.5cm}}

\\noindent
{scope}

\\TODO{{Volume {num} opener prose to be written. The opener carries roughly 5--10 pp: scope, arc, what the reader brings into this volume from previous volumes, what the reader will be able to do at the end of this volume, and a brief statement of which problem archetypes this volume introduces or revisits.}}

\\vspace{{1cm}}
"""
    path.write_text(content)
    return path


def write_chapter(book_num, book_slug, ch_num, ch_slug, title, pages, sections, meta=None):
    """Render one chapter shell. `meta` is the parsed dossier metadata for this chapter; if None or missing, fall back to TBD/defaults."""
    ch_dir = ROOT / "volumes" / f"{book_num:02d}-{book_slug}" / f"ch{ch_num:02d}-{ch_slug}"
    ch_dir.mkdir(parents=True, exist_ok=True)
    path = ch_dir / "chapter.tex"
    sec_lines = []
    for sec in sections:
        sec_lines.append(f"\\section{{{sec}}}\n\\TODO{{Section prose.}}\n")
    sec_block = "\n".join(sec_lines)

    # Pull metadata from the dossier (parsed). Fall back gracefully.
    meta = meta or {}
    half_life = meta.get("half_life", "TBD")
    archetypes = meta.get("archetypes", "TBD")
    project = meta.get("project", "TBD")
    exercises = meta.get("exercises", 30)

    chapmeta = (
        f"Half-life: {half_life}. "
        f"Archetypes: {archetypes}. "
        f"Exercise target: {exercises}. "
        f"Project track: TBD (physical, simulation, household, or hybrid)."
    )
    project_note = project if project != "TBD" else "Chapter project: a small applied task the reader can complete in a few hours to a few days."
    exercise_note = (
        f"Approximately {exercises} exercises across calculation, derivation, "
        f"estimation, simulation, design, and judgement."
    )

    content = f"""\\chapter{{{title}}}
\\label{{vol{book_num:02d}:ch{ch_num:02d}}}

\\epigraph{{}}{{}}

\\chapmeta{{{chapmeta}}}

\\noindent
\\TODO{{Volume {book_num}, Chapter {ch_num}. Approx {pages} pp.}}

{sec_block}

\\section{{Project}}
\\TODO{{{project_note}}}

\\section{{Exercises}}
\\TODO{{{exercise_note}}}
"""
    path.write_text(content)
    return path


def main():
    n_chapters = 0
    n_meta_hits = 0
    for num, slug, name, tagline, scope, chapters in BOOKS:
        write_book_opener(num, slug, name, tagline, scope)
        meta = parse_chapter_meta(num, slug)
        for (ch_num, ch_slug, title, pages, sections) in chapters:
            ch_meta = meta.get(ch_num)
            if ch_meta:
                n_meta_hits += 1
            write_chapter(num, slug, ch_num, ch_slug, title, pages, sections, ch_meta)
            n_chapters += 1
    print(f"wrote {len(BOOKS)} _volume.tex openers")
    print(f"wrote {n_chapters} chapter shells (each in its own folder)")
    print(f"dossier metadata applied to {n_meta_hits}/{n_chapters} chapters")


if __name__ == "__main__":
    main()
