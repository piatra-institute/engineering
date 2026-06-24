"""Von Mises equivalent stress and safety factor from a stress tensor.

Given the six independent components of the Cauchy stress tensor, compute the
von Mises equivalent stress

    sigma_vm = sqrt( 0.5[(sxx-syy)^2 + (syy-szz)^2 + (szz-sxx)^2]
                     + 3(txy^2 + tyz^2 + tzx^2) )

and the safety factor against a given yield stress. The plane-stress
specialisation reduces to sigma_vm = sqrt(s1^2 - s1 s2 + s2^2) in principal
stresses. Run with: python von_mises.py
"""

import math


def von_mises(sxx, syy, szz, txy, tyz, tzx):
    return math.sqrt(
        0.5 * ((sxx - syy) ** 2 + (syy - szz) ** 2 + (szz - sxx) ** 2)
        + 3.0 * (txy**2 + tyz**2 + tzx**2)
    )


def von_mises_plane(s1, s2):
    return math.sqrt(s1**2 - s1 * s2 + s2**2)


def safety_factor(sigma_vm, sigma_Y):
    return sigma_Y / sigma_vm


if __name__ == "__main__":
    # Thin cylinder hoop/axial state: hoop=125 MPa, axial=62.5 MPa, radial~0.
    hoop, axial = 125e6, 62.5e6
    vm = von_mises(hoop, axial, 0.0, 0.0, 0.0, 0.0)
    print(f"von Mises (cylinder wall) = {vm/1e6:.1f} MPa")
    print(f"plane-stress check        = "
          f"{von_mises_plane(hoop, axial)/1e6:.1f} MPa")
    sigma_Y = 250e6
    print(f"safety factor vs yield    = {safety_factor(vm, sigma_Y):.2f}")
    # Uniaxial check: von Mises of a pure uniaxial state equals that stress.
    print(f"uniaxial check: vm(100,0,0,...) = "
          f"{von_mises(100e6,0,0,0,0,0)/1e6:.1f} MPa (expect 100)")
