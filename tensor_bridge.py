# uam/engines/tensor_bridge.py
import numpy as np

def vortex_to_gauge(vorticity_tensor):
    """Project a 3×3 antisymmetric tensor (ω_ij) to SU(2) gauge-like F_μν."""
    F = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            F[i,j] = vorticity_tensor[i,j] - vorticity_tensor[j,i]
    return F
