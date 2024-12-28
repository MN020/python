import re

def count_pattern_occurrences(text, pattern):
    return len(re.findall(pattern, text))

# Example usage
text = "Hello world! Hello everyone!"
pattern = "Hello"
print(count_pattern_occurrences(text, pattern))  # Output: 2
