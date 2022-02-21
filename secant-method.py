import math
from datetime import datetime
import sympy as sp
from sympy.utilities.lambdify import lambdify
x = sp.symbols('x')
my_f = (sp.sin((2 * x ** 3) + (5 * x ** 2) - 6)) / (2 * sp.exp((-2) * x))
def SecantMethodInRangeIterations(f, check_range, epsilon=0.0000001):
    roots = []
    iterCounter = 0
    for i in check_range:
        startPoint = round(i, 2)
        endPoint = round(i + 0.1, 2)
        print("Checked range:", startPoint, "-", endPoint)
        # Send to the Secant Method with 2 guesses
        local_root = SecantMethod(f, startPoint, endPoint, epsilon, iterCounter)
        # If the root has been found in previous iterations
        if round(local_root, 6) in roots:
            print("Already found that root.")
        # If the root is out of range tested
        elif not (startPoint <= local_root <= endPoint):
            print("root out of range.")
        elif local_root is not None:
            roots += [round(local_root, 6)]
    return roots
def SecantMethod(func, firstGuess, secondGuess, epsilon, iterCounter):
    if iterCounter > 100:
        return

    if abs(secondGuess - firstGuess) < epsilon:  # Stop condition
        print("after ", iterCounter, "iterations The root found is: ", round(secondGuess, 6) , "00000" + d + h + m)
        return round(secondGuess, 6)  # Returns the root found

    next_guess = (firstGuess * func(secondGuess) - secondGuess * func(firstGuess)) / (
                func(secondGuess) - func(firstGuess))
    print("iteration no.", iterCounter, "\tXi = ", firstGuess, " \tXi+1 = ", secondGuess,
          "\tf(Xi) = ", func(firstGuess))
    # Recursive call with the following guess
    return SecantMethod(func, secondGuess, next_guess, epsilon, iterCounter + 1)
local_dt = datetime.now()
d = str(local_dt.day)
h = str(local_dt.hour)
m = str(local_dt.minute)
def frange(start, end=None, inc=None):
    "Function for a range with incomplete numbers"
    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)

    return L
checkRange = frange(-1, 1.6, 0.1)
def func(val):
    return lambdify(x, my_f)(val)



epsilon = 0.00001
# Function sin((2 * x ** 3) + (5 * x ** 2) - 6)) / (2 * sp.exp((-2) * x))
checkRange = frange(-1, 1.6, 0.1)
print("\n*** Secant Method***")
SecantMethodInRangeIterations(func, checkRange, 0.0000001)