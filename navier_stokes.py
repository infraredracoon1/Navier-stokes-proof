import numpy as np
def biot_savart_k(x):
    r = np.linalg.norm(x)
    if r == 0: return np.zeros(3)
    return np.cross(x, [0,0,1]) / (4*np.pi*r**3)
