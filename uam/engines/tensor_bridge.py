import numpy as np

def vortex_to_gauge(omega):
    """Convert antisymmetric ω_ij tensor to gauge-like F_μν."""
    F = omega - omega.T
    return F

def gauge_to_vortex(F):
    """Inverse projection."""
    return 0.5 * (F - F.T)
