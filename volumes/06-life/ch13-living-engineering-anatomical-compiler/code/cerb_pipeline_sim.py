"""
cerb_pipeline_sim.py

Toy anatomical-compiler pipeline. Three stages:

  1. specification: dictionary describing target morphology at a coarse
     symbolic level (topology, polarity, scale, composition, function);
  2. translation: deterministic map from symbolic specification to a
     candidate bioelectric pattern (a numerical array on a 1D tissue);
  3. execution: simulated forward model in which a tissue 'reads' the
     pattern and produces an outcome morphology, with stochastic noise.

This file is illustrative only. It does not implement an actual
biological mechanism. Its purpose is to give Vol VI Ch 13 readers a
runnable scaffold for the chapter's project (a critique of the CERB
position paper) and the exercises that touch the compiler analogy.
"""

import numpy as np

# --- Stage 1: specification --------------------------------------------------

EXAMPLE_SPEC = {
    "topology": "linear",       # only linear vs branched supported here
    "polarity": "head_then_tail",
    "scale_mm": 1.0,
    "composition": {"head_fraction": 0.3, "trunk_fraction": 0.5,
                    "tail_fraction": 0.2},
}

# --- Stage 2: translation ----------------------------------------------------

def translate(spec, n=200):
    """Map a coarse spec to a bioelectric voltage pattern (mV)."""
    if spec["topology"] != "linear":
        raise NotImplementedError("only linear topology supported in toy model")
    head = spec["composition"]["head_fraction"]
    trunk = spec["composition"]["trunk_fraction"]
    n_head = int(n * head)
    n_trunk = int(n * trunk)
    n_tail = n - n_head - n_trunk
    V_head = np.full(n_head, -40.0)   # depolarised head region
    V_trunk = np.full(n_trunk, -55.0)
    V_tail = np.full(n_tail, -70.0)   # hyperpolarised tail region
    V = np.concatenate([V_head, V_trunk, V_tail])
    if spec["polarity"] == "tail_then_head":
        V = V[::-1]
    return V

# --- Stage 3: execution -------------------------------------------------------

def execute(V, rng=None, noise_mV=5.0):
    """Stochastic outcome morphology based on voltage thresholds."""
    if rng is None:
        rng = np.random.default_rng(0)
    Vn = V + rng.normal(0, noise_mV, size=V.shape)
    out = np.where(Vn > -50.0, "head", np.where(Vn < -65.0, "tail", "trunk"))
    return out

def score(outcome, spec):
    """Crude scoring: head-/trunk-/tail-fraction error vs spec."""
    n = len(outcome)
    head_frac = float(np.mean(outcome == "head"))
    trunk_frac = float(np.mean(outcome == "trunk"))
    tail_frac = float(np.mean(outcome == "tail"))
    target = spec["composition"]
    err = (
        abs(head_frac - target["head_fraction"])
        + abs(trunk_frac - target["trunk_fraction"])
        + abs(tail_frac - target["tail_fraction"])
    )
    return {
        "head_frac": head_frac,
        "trunk_frac": trunk_frac,
        "tail_frac": tail_frac,
        "L1_error": err,
    }

def main():
    rng = np.random.default_rng(0)
    V = translate(EXAMPLE_SPEC)
    print(f"Translated voltage pattern: range "
          f"[{V.min():.1f}, {V.max():.1f}] mV over {len(V)} cells")
    outcomes = []
    for trial in range(10):
        out = execute(V, rng=rng, noise_mV=5.0)
        outcomes.append(score(out, EXAMPLE_SPEC))
    errs = [o["L1_error"] for o in outcomes]
    print(f"L1 fraction error across 10 trials: "
          f"mean {np.mean(errs):.3f}, max {np.max(errs):.3f}")
    print("Sample outcome composition (first trial):", outcomes[0])

if __name__ == "__main__":
    main()
