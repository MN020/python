# Accept list of N integers from the user
N = int(input("Enter the number of elements: "))
numbers = []

# Accept N integers and append to the list
for _ in range(N):
    number = int(input("Enter a number: "))
    numbers.append(number)

# Partition list into even and odd sub-lists
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Output the sub-lists
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
