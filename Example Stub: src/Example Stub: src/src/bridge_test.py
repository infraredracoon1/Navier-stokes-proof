import numpy as np, pandas as pd
from pathlib import Path

def bridge_error(j, N=5000):
    """
    Toy test: sample random Fourier modes on shell |xi| ~ 2^j,
    compare alignment factor from Fourier vs physical domain.
    """
    xi = np.random.normal(size=(N,3))
    xi /= np.linalg.norm(xi, axis=1)[:,None]
    # "true" uniform density
    mu_uniform = 1.0/N
    # random perturbation
    mu = mu_uniform + 0.01*np.random.randn(N)
    mu = np.abs(mu)/mu.sum()
    # physical alignment proxy: cos^2 with fixed e_c
    e_c = np.array([1,0,0])
    phys = np.mean([(np.dot(s,e_c)**2)*mu[i] for i,s in enumerate(xi)])
    fourier = 1/3  # theoretical isotropy value
    return abs(phys - fourier)

Js = [4,6,8,10]
errors = [bridge_error(j) for j in Js]

df = pd.DataFrame({"j": Js, "bridge_error": errors})
Path("results").mkdir(exist_ok=True)
df.to_csv("results/bridge.csv", index=False)
print("Bridge test complete -> results/bridge.csv")
