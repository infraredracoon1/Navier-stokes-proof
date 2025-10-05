import sympy as sp

def derive_bkm_closure():
    y, t, A, C2, y0 = sp.symbols('y t A C2 y0', positive=True)
    ode = sp.Eq(sp.Derivative(y, t), A*y**2 - C2*y**3)
    sol = sp.dsolve(ode, ics={y.subs(t, 0): y0})
    return sp.simplify(sol)

def check_finiteness(sol_expr):
    y = sol_expr.rhs
    lim_inf = sp.limit(y, t, sp.oo)
    return lim_inf.is_finite
