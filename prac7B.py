# Left Pattern
n = 5
for i in range(1, n+1):
    print("*" * i)

# Middle Pattern
n = 5  # Number of rows
for i in range(1, n + 1):
    print(" " * (n - i) + (str(i) * (2 * i - 1)))

# Right Pattern
n = 5  # Number of rows
for i in range(1, n + 1):
    left = "".join(str(j) for j in range(i, 0, -1))  # Decreasing part
    right = "".join(str(j) for j in range(2, i + 1))  # Increasing part
    print(" " * (n - i) + left + right)
