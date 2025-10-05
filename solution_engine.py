# uam/engines/solution_engine.py
import numpy as np
from scipy.integrate import solve_ivp
from .constants import C1, C2, nu

def vorticity_ode(t, y):
    """BKM-inspired differential inequality dy/dt = A*y^2 - C2*y^3"""
    A = C1 + nu
    return A * y**2 - C2 * y**3

def integrate_vorticity(y0=1.0, tmax=1000.0, nsteps=10000):
    """Integrate the vorticity envelope inequality."""
    t_span = (0, tmax)
    t_eval = np.linspace(0, tmax, nsteps)
    sol = solve_ivp(vorticity_ode, t_span, [y0], t_eval=t_eval)
    return t_eval, sol.y[0]

def bkm_integral(y):
    """Approximate ∫ ||ω||_∞ dt."""
    return np.trapz(y)
