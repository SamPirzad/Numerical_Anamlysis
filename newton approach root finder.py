import math

def f(x):
    return x + math.cos(x)

def f_prime(x):
    return 1 - math.sin(x)

def find_root():
    x = int(input("Enter the starting \"x\" value : "))
    max_iter = int(input("Enter the maximum iterations : "))
    tol = 1e-6 #the tolerance of  each x with the next 
    for i in range(max_iter):
        x_new = x - f(x) / f_prime(x)
        print(f"Found root after {i+1} iterations: {x_new}")
        if abs(x_new - x) < tol:
            break
        x = x_new
    
find_root()
