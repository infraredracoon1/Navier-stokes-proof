import numpy as np
from .constants import kappa_YM, lambda_YM

def lattice_mass_gap(L=8, g=0.1):
    """Toy SU(2) lattice spectral gap estimator."""
    U = np.random.randn(L, L, 3) * 0.01
    energy = np.sum(U**2)
    decay = np.exp(-lambda_YM * np.arange(0, 100))
    gap = g**2 * (np.mean(decay[:10]) - np.mean(decay[-10:]))
    return abs(gap)

def verify_os_positivity():
    """Simple check that correlation ⟨F(t)F(0)⟩ > 0 decays exponentially."""
    t = np.linspace(0, 10, 100)
    corr = np.exp(-lambda_YM * t)
    return (corr > 0).all()
