[VARIABLES] - Variables are containers for storing data values.

[CREATING-VARIABLES] - Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

(1) Example

>>>x = 5
>>>y = "John"
>>>print(x)
>>>print(y)

- Variables do not need to be declared with any particular type, and can even change type after they have been set.

(2) Example

>>>x = 4       # x is of type int
>>>x = "Sally" # x is now of type str
>>>print(x)

[CASTING] - If you want to specify the data type of a variable, this can be done with casting.

(3) Example

>>>x = str(3)    # x will be '3'
>>>y = int(3)    # y will be 3
>>>z = float(3)  # z will be 3.0