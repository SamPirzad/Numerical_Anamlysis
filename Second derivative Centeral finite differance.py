import math

def f(x):
    return math.sin(3*x)

def ddf(x):
    return -9*math.sin(3*x)

# Calculate exact value of f''(x) at x=2
exact_value = ddf(2)
print("Exact value of f''(2) = ", exact_value)

# Initialize table with column headers
table = [["h", "Central Difference", "Approximate Error", "Error Ratio"]]

# Loop over different h values and calculate finite difference and error
x = 2
for h in [1, 0.5, 0.25, 0.125, 0.0625 , 0.03125]:
    center_diff = (f(x+h) - 2*f(x) + f(x-h)) / (h**2)
    approx_error = abs(ddf(x) - center_diff)
    error_ratio = "-"
    if len(table) > 1:
        prev_error = table[-1][2]
        if prev_error != 0:
            error_ratio = prev_error / approx_error
    table.append([h, center_diff, approx_error, error_ratio])

# Print table
for row in table:
    print("{:<10} {:<20} {:<20} {:<20}".format(*row))
