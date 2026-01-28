[PYTHON-STRINGS] - Strings in python are surrounded by either single quotation marks, or double quotation marks.

>>>'hello is same as "heloo"

You can display a string with the print() function: 

(1) Example

>>>print("Hello")
>>>print('Hello')

[QUOTATION-INSIDE-QOUTES] - You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

(2) Example

>>>print("It's alright")
>>>print("He is called 'Johnny'")
>>>print('He is called "Johnny"')

[ASSIGN-A-STRING-TO-A-VARIABLE] - Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

(3) Example

>>>a = "Hello"
>>>print(a)

[MULTILINE-STRINGS]

- You can assign a multiline string to a variable by using three quotes:

(4) Example 

You can use three double quotes:

>>> a = """Lorem ipsum dolor sit amet,
>>>consectetur adipiscing elit,
>>>sed do eiusmod tempor incididunt
>>>ut labore et dolore magna aliqua."""
>>>print(a)

Or three single quotes:

(5) Example

>>>a = '''Lorem ipsum dolor sit amet,
>>>consectetur adipiscing elit,
>>>sed do eiusmod tempor incididunt
>>>ut labore et dolore magna aliqua.'''
>>>print(a)