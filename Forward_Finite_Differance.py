import math

def f(x):
    return math.sin(3*x)

def df(x):
    return 3 * math.cos(3*x)

# Calculate exact value of f'(x) at x=2
exact_value = df(2)
print("Exact value of f'(2) = ", exact_value)

# Initialize table with column headers
table = [["h", "Forward Difference", "Approximate Error", "Error Ratio"]]

# Loop over different h values and calculate finite difference and error
x = 2
for h in [1, 0.5, 0.25, 0.125, 0.0625 , 0.03125]:
    forward_diff = (f(x+h) - f(x)) / h
    approx_error = abs(df(x) - forward_diff)
    error_ratio = "-"
    if len(table) > 1:
        prev_error = table[-1][2]
        if prev_error != 0:
            error_ratio = prev_error / approx_error
    table.append([h, forward_diff, approx_error, error_ratio])

# Print table
for row in table:
    print("{:<10} {:<20} {:<20} {:<20}".format(*row))
