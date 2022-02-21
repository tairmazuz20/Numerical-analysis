import math
import sympy as sp
from sympy.utilities.lambdify import lambdify

x = sp.symbols('x')
my_f = (sp.sin((2 * x ** 3) + (5 * x ** 2) - 6)) / (2 * sp.exp((-2) * x))


def printFinalResult(result):
    """
    Function for printing final results according to the requested format
    :param result: The final results (list or number)
    :return: print the result
    """
    from datetime import datetime
    local_dt = datetime.now()
    d = str(local_dt.day)
    h = str(local_dt.hour)
    m = str(local_dt.minute)
    if isinstance(result, list):
        for i in range(len(result)):
            print(str(result[i]) + "00000" + d + h + m)
        return
    return str(result) + "00000" + d + h + m


def SimpsonRule(func, n, a, b):
    if n % 2 != 0:
        return 0, False
    h = (b - a) / n
    print("h = ", h)
    str_even = ""
    str_odd = ""
    k2 = b
    # print("Error evaluation En = ", round(SimpsonError(my_f, b, a, h), 6))
    integral = func(a) + func(b)
    # Calculation of a polynomial lagranz for the sections
    for i in range(n):
        k = a + i * h  # new a
        if i != n - 1:  # new b
            k2 = a + (i + 1) * h
        if i % 2 == 0:  # even places
            integral += 2 * func(k)
            str_even = "2 * " + str(func(k))
        else:  # odd places
            integral += 4 * func(k)
            str_odd = "4 * " + str(func(k))
        print("h/3 ( ", str(func(k)), " + ", str_odd, " + ", str_even, " + ", str(func(k2)), " )")
    integral *= (h / 3)
    return integral, True


epsilon = 0.00001
n = 18


def func(val):
    return lambdify(x, my_f)(val)


print("\n***  Simpson’s  ***")
res = SimpsonRule(func, n, 0, 1)
if res[1]:
    print("I = ", printFinalResult(round(res[0], 6)))
else:
    print("n must be even !")