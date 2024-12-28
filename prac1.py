# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert number to string to calculate the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of powers equals the original number
    return sum_of_powers == number

# Input from the user
num = int(input("Enter a number: "))

# Output result
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
