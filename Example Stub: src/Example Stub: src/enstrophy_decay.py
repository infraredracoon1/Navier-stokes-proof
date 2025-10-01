import numpy as np, pandas as pd
from pathlib import Path

kappa = 1.0  # viscosity + alignment
Js = [6,8,10]
results = []

for j in Js:
    W0 = 10**(-j/2)  # arbitrary small IC
    t = np.linspace(0, 1, 200)
    W = W0 * np.exp(-kappa * (2**(2*j)) * t)
    half_life = np.interp(W0/2, W[::-1], t[::-1])
    results.append({"j": j, "half_life": half_life})

df = pd.DataFrame(results)
Path("results").mkdir(exist_ok=True)
df.to_csv("results/enstrophy.csv", index=False)
print("Enstrophy decay test complete -> results/enstrophy.csv")
