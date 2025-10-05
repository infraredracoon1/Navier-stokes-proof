import numpy as np
from numpy.fft import rfftn, irfftn
from .constants import nu, kappa_NS, lambda_NS

def simulate_enstrophy_decay(nx=128, steps=1000, dt=1e-3):
    """Simple spectral solver for ∂t u = νΔu - nonlinear(u)."""
    x = np.linspace(0, 2*np.pi, nx, endpoint=False)
    k = np.fft.rfftfreq(nx, 1/nx)
    u = np.sin(x) + 0.5*np.sin(3*x)
    u_hat = rfftn(u)
    enstrophy = []
    for n in range(steps):
        lap = -(k**2)
        u_hat *= np.exp(nu*lap*dt)
        u = irfftn(u_hat)
        enstrophy.append(np.sum((np.gradient(u)**2)))
    return np.array(enstrophy)
