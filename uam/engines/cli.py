import argparse
from .solution_engine import integrate_vorticity, bkm_integral
from .fft_enstrophy import simulate_enstrophy_decay
from .yang_mills_engine import lattice_mass_gap
from .derivation_engine import derive_bkm_closure
from .referee_engine import run_checks

def main():
    parser = argparse.ArgumentParser(description="Run UAM Engines")
    parser.add_argument("--mode", choices=["ns", "ym", "all"], default="all")
    args = parser.parse_args()

    if args.mode in ("ns", "all"):
        print("=== Navier–Stokes Engine ===")
        t, y = integrate_vorticity()
        print("BKM Integral:", bkm_integral(y, t))
        run_checks(y)

    if args.mode in ("ym", "all"):
        print("=== Yang–Mills Engine ===")
        gap = lattice_mass_gap()
        print("Estimated Mass Gap:", gap)

    print("=== Symbolic Verification ===")
    print(derive_bkm_closure())
