import numpy as np
import scipy.integrate as intg
import math

def integrate_with_trapeziod(func, boundaries, n_dx):
    a,b = boundaries
    x_val = np.linspace(a,b, n_dx - 1)
    y_val = []

    for x in x_val:
        y_val.append(func(x))

    integral = intg.trapezoid(y_val)
    print(f'Integralen blir {integral}.')


func = lambda x: math.sin(x)
bound = (0, math.pi)
steps = 10
integrate_with_trapeziod(func, bound, steps)
