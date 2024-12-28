# Create a list of integers from 1 to 10
numbers = list(range(1, 11))
print("Initial List:", numbers)

# i. Add the number 15 at the end of the list
numbers.append(15)
print("After adding 15:", numbers)

# ii. Insert the number 5 at the 2nd index
numbers.insert(2, 5)
print("After inserting 5 at index 2:", numbers)

# iii. Remove the number 8 from the list
numbers.remove(8)
print("After removing 8:", numbers)

# iv. Sort the list in descending order
numbers.sort(reverse=True)
print("After sorting in descending order:", numbers)

# v. Find the length of the list
length = len(numbers)
print("Length of the list:", length)

# vi. Retrieve the first and last elements of the list
first_element = numbers[0]
last_element = numbers[-1]
print("First element:", first_element)
print("Last element:", last_element)
