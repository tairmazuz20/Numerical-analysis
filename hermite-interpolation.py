# calculate and print a value using hermite polynomial using divided difference
# the function takes a value to calculate, x array, fx array and fx derivative array
def hermitePolynomial(value, x, fx, fxDerivative):
    n = len(x)
    z = [0 for i in range(2 * n + 1)]
    q = [[0 for j in range(2 * n)] for i in range(2 * n)]

    for i in range(n):
        z[2 * i] = z[2 * i + 1] = x[i]
        q[2 * i][0] = q[2 * i + 1][0] = fx[i]
        q[2 * i + 1][1] = fxDerivative[i]

        if i != 0:
            q[2 * i][1] = (q[2 * i][0] - q[2 * i - 1][0]) / (z[2 * i] - z[2 * i - 1])

    for i in range(2, 2 * n):
        for j in range(2, i + 1):
            q[i][j] = (q[i][j - 1] - q[i - 1][j - 1]) / (z[i] - z[i - j])

    # calculate the product for the hermite sum formula
    def calcProduct(i, value, z):
        product = 1
        for j in range(i):
            product = product * (value - z[j])
        return product

    # calculate the interpolation of value using hermite interpolation
    def hermiteCalc(value, z, q, n):
        sum = q[0][0]

        for i in range(1, n):
            sum = sum + (calcProduct(i, value, z) * q[i][i])

        return sum

    result = hermiteCalc(value, z, q, n)
    print('The value of', value, 'is:', result)


x = [0, 1, 2]

fx = [3, 8, 7]

fxDer = [7, 1, 7]

hermitePolynomial(0.2, x, fx, fxDer)
print('part 1: question 4')
hermitePolynomial(0.2, x, fx, fxDer)
print('part 2: question 14')
hermitePolynomial(0.3, x, fx, fxDer)
print('part 3: question 24')
hermitePolynomial(0.1, x, fx, fxDer)
print('part 4: question 33')