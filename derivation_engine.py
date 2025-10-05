# uam/engines/derivation_engine.py
import sympy as sp

def derive_bkm_closure():
    y, t, A, C2 = sp.symbols('y t A C2', positive=True)
    ode = sp.Eq(sp.Derivative(y, t), A*y**2 - C2*y**3)
    sol = sp.dsolve(ode, ics={y.subs(t, 0): sp.Symbol('y0')})
    return sp.simplify(sol)
