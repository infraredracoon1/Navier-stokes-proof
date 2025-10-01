import numpy as np
import pandas as pd
from pathlib import Path

N = 6000
# sample points on S^2
sigma = np.random.normal(size=(N,3))
sigma /= np.linalg.norm(sigma, axis=1)[:,None]

def kernel(s, t):
    cos_theta = np.dot(s, t)
    return 0.25/np.pi * (1 - cos_theta**2)

def apply_B(mu):
    out = np.zeros_like(mu)
    for i in range(N):
        out[i] = np.mean([kernel(sigma[i], sigma[j]) * mu[j] for j in range(N)])
    return out

# Initialize
mu = np.random.rand(N)
mu /= mu.sum()

errors = []
for k in range(10):
    mu = apply_B(mu)
    mu /= mu.sum()
    err = np.linalg.norm(mu - 1/N)
    errors.append(err)

df = pd.DataFrame({"k": range(10), "error": errors})
Path("results").mkdir(exist_ok=True)
df.to_csv("results/spectral_gap.csv", index=False)
print("Spectral gap test complete -> results/spectral_gap.csv")
