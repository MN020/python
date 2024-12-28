import math

# Accept input from the user
n = int(input("Enter a number: "))

# a) Square root
print(f"Square root: {math.sqrt(n)}")

# b) Square
print(f"Square: {n**2}")

# c) Cube
print(f"Cube: {n**3}")

# d) Check for prime
print(f"Prime: {'Yes' if all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)) and n > 1 else 'No'}")

# e) Factorial
print(f"Factorial: {math.factorial(n)}")

# f) Prime factors
factors = []
for i in range(2, n+1):
    while n % i == 0:
        factors.append(i)
        n //= i
print(f"Prime factors: {factors}")