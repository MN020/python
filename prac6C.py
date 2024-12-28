# List of dictionaries where each dictionary represents a student
students = [
    {"name": "Alice", "age": 20, "gpa": 3.5},
    {"name": "Bob", "age": 22, "gpa": 3.8},
    {"name": "Charlie", "age": 21, "gpa": 3.9},
    {"name": "David", "age": 23, "gpa": 3.2}
]

# Compute the average GPA
total_gpa = 0
num_students = len(students)

# Summing the GPAs of all students
for student in students:
    total_gpa += student["gpa"]

# Calculating the average GPA
average_gpa = total_gpa / num_students if num_students > 0 else 0

# Print the average GPA
print("Average GPA of students:", average_gpa)
