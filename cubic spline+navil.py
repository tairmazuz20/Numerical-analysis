from typing import Tuple, List
import bisect
import math


def compute_changes(x: List[float]) -> List[float]:
    return [x[i + 1] - x[i] for i in range(len(x) - 1)]


def create_tridiagonalmatrix(n: int, h: List[float]) -> Tuple[List[float], List[float], List[float]]:
    A = [h[i] / (h[i] + h[i + 1]) for i in range(n - 2)] + [0]
    B = [2] * n
    C = [0] + [h[i + 1] / (h[i] + h[i + 1]) for i in range(n - 2)]
    return A, B, C


def create_target(n: int, h: List[float], y: List[float]):
    return [0] + [6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1]) / (h[i] + h[i - 1]) for i in
                  range(1, n - 1)] + [0]


def solve_tridiagonalsystem(A: List[float], B: List[float], C: List[float], D: List[float]):
    c_p = C + [0]
    d_p = [0] * len(B)
    X = [0] * len(B)

    c_p[0] = C[0] / B[0]
    d_p[0] = D[0] / B[0]
    for i in range(1, len(B)):
        c_p[i] = c_p[i] / (B[i] - c_p[i - 1] * A[i - 1])
        d_p[i] = (D[i] - d_p[i - 1] * A[i - 1]) / (B[i] - c_p[i - 1] * A[i - 1])

    X[-1] = d_p[-1]
    for i in range(len(B) - 2, -1, -1):
        X[i] = d_p[i] - c_p[i] * X[i + 1]

    return X


def compute_spline(x: List[float], y: List[float], value):
    n = len(x)
    if n < 3:
        raise ValueError('Too short an array')
    if n != len(y):
        raise ValueError('Array lengths are different')

    h = compute_changes(x)
    if any(v < 0 for v in h):
        raise ValueError('X must be strictly increasing')

    A, B, C = create_tridiagonalmatrix(n, h)
    D = create_target(n, h, y)

    M = solve_tridiagonalsystem(A, B, C, D)
    xx = value
    for i in range(len(x)):
        if x[i] > xx:
            i = i - 1
            break
    coefficients = (pow(x[i + 1] - xx, 3) * M[i] + pow(xx - x[i], 3) * M[i + 1]) / (6 * h[i])
    coefficients += ((x[i + 1] - xx) * y[i] + (xx - x[i]) * y[i + 1]) / h[i]
    coefficients -= (((x[i + 1] - xx) * M[i] + (xx - x[i]) * M[i + 1]) * h[i]) / 6
    return coefficients


def neville(datax, datay, x):
    n = len(datax)
    p = n * [0]
    for k in range(n):
        for i in range(n - k):
            if k == 0:
                p[i] = datay[i]
            else:
                p[i] = ((x - datax[i + k]) * p[i] + \
                        (datax[i] - x) * p[i + 1]) / \
                       (datax[i] - datax[i + k])
    return p[0]

def main():
    datax = [1, 1.2, 1.3, 1.4]
    datay = [0, 0.112463, 0.167996, 0.222709]
    x = 1.28
    choice = int(input('Which method would you like to solve: \n1) neville\n2) CubicSpline\n'))
    if choice == 1:
        print(neville(datax, datay, x))
    elif choice == 2:
        solve = compute_spline(datax, datay, x)
        print(solve)

main()