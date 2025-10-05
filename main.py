from engines.solution_engine import integrate_vorticity, bkm_integral
from engines.referee_engine import run_checks
from engines.derivation_engine import derive_bkm_closure

print("=== Running UAM Engines ===")

t, y = integrate_vorticity(y0=1.0)
I = bkm_integral(y)
run_checks(y)

print("BKM Integral:", I)
print("Symbolic closure:", derive_bkm_closure())
