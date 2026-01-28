# This program demonstrate the modification of strings in Python.

# The use of upper() method to convert a string to uppercase the text inside the quotation marks.
original_string = "Hello, World!"
uppercase_string = original_string.upper()

print("Original String:", original_string)
print("Uppercase String:", uppercase_string)

# The use of lower() method to convert a string to lowercase the text inside the quotation marks.
lowercase_string = original_string.lower()
print("Lowercase String:", lowercase_string)

#The use of strip() method to remove any leading and trailing whitespace characters from the string.
stripped_string = original_string.strip()
print("Stripped String:", stripped_string)

# The use of replace() method to replace a substring with another substring.
modified_string = original_string.replace("World", "Python")
print("Modified String:", modified_string)