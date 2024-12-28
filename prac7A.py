# Initialize the sum of positive numbers to 0
total_sum = 0

# Start a loop to ask for positive numbers
while True:
    # Ask the user for input
    number = float(input("Enter a positive number (or a negative number to stop): "))
    
    # Check if the number is negative, then break the loop
    if number < 0:
        break
    
    # Add the positive number to the total sum
    total_sum += number

# Display the sum of positive numbers
print("The sum of all positive numbers entered is:", total_sum)
