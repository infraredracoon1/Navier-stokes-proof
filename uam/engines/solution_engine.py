import numpy as np
from scipy.integrate import solve_ivp
from .constants import nu, C1, C2

def vorticity_ode(t, y):
    A = C1 + nu
    return A*y**2 - C2*y**3

def integrate_vorticity(y0=1.0, tmax=1000, nsteps=20000):
    t_span = (0, tmax)
    t_eval = np.linspace(0, tmax, nsteps)
    sol = solve_ivp(vorticity_ode, t_span, [y0], t_eval=t_eval)
    return t_eval, sol.y[0]

def bkm_integral(y, t):
    return np.trapz(y, t)
