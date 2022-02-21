import sympy as sp
from sympy.utilities.lambdify import lambdify
from datetime import datetime


# Defining Function
def f(x):
    return (sp.sin((2 * x ** 3) + (5 * x ** 2) - 6)) / (2 * sp.exp((-2) * x))


# Defining derivative of function
def g(z):
    x = sp.symbols('x')
    f = (sp.sin((2 * x ** 3) + (5 * x ** 2) - 6)) / (2 * sp.exp((-2) * x))
    f_prime = f.diff(x)  # Derivation of  f by x
    f_prime = lambdify(x, f_prime)
    return f_prime(z)


# Implementing Newton Raphson Method
def newtonRaphson(x0, e):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break

        x1 = x0 - f(x0) / g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1))+"00000"+d+h+m)
        x0 = x1
        step = step + 1

        condition = abs(f(x1)) > e

    print('\nRequired root is: %0.8f' % x1+"00000"+d+h+m)

local_dt = datetime.now()
d = str(local_dt.day)
h = str(local_dt.hour)
m = str(local_dt.minute)
# Input Section
# Function sin((2 * x ** 3) + (5 * x ** 2) - 6)) / (2 * sp.exp((-2) * x))
x1 = float(input('Enter start Range: '))
x2 = float(input('Enter end Range: '))
x0 = 0.05
# Converting x0
x0 = float(x0)
e = float(0.00001)
# Starting Newton Raphson Method
newtonRaphson(x0, e)