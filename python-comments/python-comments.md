[PYTHON-COMMENTS] 

1. Comments can be used to explain Python code.
2. Comments can be used to make the code more readable.
3. Comments can be used to prevent execution when testing code.

[CREATING-A-COMMENT] - Comments starts with a #, and Python will ignore them.

(1) Example
#This is a comment
>>>print("Hello, World!")

- Comments can be placed at the end of a line, and Python will ignore the rest of the line.

(2) Example
>>>print("Hello, World!) # This is a comment

- A comment does not have to be text that explains the code, it can also be used to prevent Python from executing code:

>>>#print("Hello, World!")
>>>print("Cheers, Mate!")

[MULTILINE-COMMENTS] 

1. Python does not really have a syntax for multiline comments.
2. To add a multiline comment you could insert a # for each line:

(3) Example

>>>#This is a comment
>>>#written in
>>>#more than just one line
>>>print("Hello, World!")

- Or, not quite as intended, you can use a multiline string.

- Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

(4) Example

>>>"""
>>>This is a comment
>>>written in
>>>more than just one line
>>>"""
>>>print("Hello, World!")

- As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.