"""Floating equilibrium and metacentric stability of a rectangular box.

For a homogeneous box of length L, beam B, and height D floating upright
in a fluid of density rho_f, with the box material at density rho_b:

    draft  T = (rho_b / rho_f) * D                  (equilibrium submersion)
    V_disp = L * B * T
    BM = I_wp / V_disp,  I_wp = L * B^3 / 12         (roll axis)
    KB = T / 2          (centre of buoyancy above keel)
    KG = D / 2          (centre of mass above keel, homogeneous box)
    GM = KB + BM - KG

A positive GM means the box is stable in small-angle roll. Run with:

    uv run volumes/03-force/ch10-fluid-statics/code/metacentre.py
"""


def box_stability(length, beam, height, rho_b, rho_f=1000.0):
    draft = (rho_b / rho_f) * height
    if draft >= height:
        return {"floats": False, "draft": draft}
    v_disp = length * beam * draft
    i_wp = length * beam ** 3 / 12.0
    bm = i_wp / v_disp
    kb = draft / 2.0
    kg = height / 2.0
    gm = kb + bm - kg
    return {
        "floats": True,
        "draft": draft,
        "freeboard": height - draft,
        "BM": bm,
        "KB": kb,
        "KG": kg,
        "GM": gm,
        "stable": gm > 0.0,
    }


if __name__ == "__main__":
    cases = [
        ("beamy barge", dict(length=10.0, beam=4.0, height=2.0, rho_b=500.0)),
        ("tall narrow hull", dict(length=10.0, beam=1.0, height=4.0, rho_b=500.0)),
    ]
    for name, kw in cases:
        r = box_stability(**kw)
        print(f"{name}:")
        if not r["floats"]:
            print(f"  sinks (required draft {r['draft']:.2f} m exceeds height)")
            continue
        print(f"  draft     = {r['draft']:.3f} m, freeboard = {r['freeboard']:.3f} m")
        print(f"  BM        = {r['BM']:.3f} m")
        print(f"  GM        = {r['GM']:.3f} m  -> {'STABLE' if r['stable'] else 'UNSTABLE'}")
        print()
