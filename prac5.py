# Accept the number of Fibonacci terms from the user
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Initializing the first two Fibonacci numbers
a, b = 0, 1

# Print Fibonacci series
print("Fibonacci series:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Update a and b for the next term
