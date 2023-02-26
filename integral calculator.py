import numpy as np
import math

def f1(x):
    return np.sin(x)

def f2(x):
    return math.exp(-x**2)

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        sum += f(a + i * h)
    return h * sum

a = 1 # lower bound
b = 2 # upper bound
n = int(input("Enter the count of intervals : ")) # number of intervals

result1 = trapezoidal_rule(f1, a, b, n)
result2 = trapezoidal_rule(f2, a-1, b-1, n)
print("Area under the graph of sin(x) from", a, "to", b, ":", result1)
print("Area under the graph of exp(-x^2) from", a-1, "to", b-1, ":", result2)
