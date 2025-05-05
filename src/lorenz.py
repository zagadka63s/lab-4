import numpy as np
from scipy.integrate import solve_ivp

def lorenz(t, state, sigma=10.0, rho=28.0, beta=8.0/3.0):
    """
    рівняння Лоренца
    """
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

def integrate_lorenz(initial_state, t_span, t_eval, sigma=10.0, rho=28.0, beta=8.0/3.0):
    """
    чисельний розв'язок системи Лоренца
    """
    sol = solve_ivp(
        lorenz,
        t_span,
        initial_state,
        t_eval=t_eval,
        args=(sigma, rho, beta),
        method='RK45'
    )
    return sol
