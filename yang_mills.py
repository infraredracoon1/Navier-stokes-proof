def curvature(A, g):
    F = g * (A @ A.T - A.T @ A)
    return F
