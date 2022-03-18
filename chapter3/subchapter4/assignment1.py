import scipy.optimize as opt
import numpy as np

def func(x):
    #return ((x-1)*(x+1))
    return (x-2)*(x-1)*(x+3)

def num_bisect(fun, tup, tol = 1e-5, n_max = 10000):
    a, b = tup
    # error
    n = 0
    while n < n_max: #error > tol:
        mid = (a+b)/2
        
        if fun(mid) == 0 or np.abs((b-a)/2) < tol:
            return mid
    
        if np.sign(fun(mid)) == np.sign(fun(a)):
            a = mid
        else:
            b = mid
        n += 1
    


#x1 = -2.0
#x2 = 0.0

#x1 = -4.0
#x2 = -2.0
x1 = 1.5
x2 = 2.7

sci_root = opt.bisect(func, x1, x2, xtol = 1e-5)
app_root = num_bisect(func, (x1, x2), 1e-3)

print(f'Root given by SciPy: {sci_root:.6f}.')
print(f'Root given by approximation: {app_root:.6f}.')