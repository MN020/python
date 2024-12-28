# Method 1: Mathematical Approach
# Function to reverse the digits of a number
def reverse_digits(number):
    reverse_num = 0
    while number > 0:
        last_digit = number % 10
        reverse_num = reverse_num * 10 + last_digit
        number //= 10
    return reverse_num

# Input from user
# Accept input from the user
n = input("Enter a number: ")

# Reverse the digits and print them
reversed_n = n[::-1]
print(f"Digits in reverse order: {reversed_n}")
