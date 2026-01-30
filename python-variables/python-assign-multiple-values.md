[MANY-VALUES-TO-MULTIPLE-VARIABLES] - Python allows you to assign values to multiple variables in one line:

(1) Example

>>>x, y, z = "Orange", "Banana", "Cherry"
>>>print(x)
>>>print(y)
>>>print(z)

Note: Make sure the number of variables matches the number of values, or else you will get an error.

[ONE-VALUE-TO-MULTIPLE-VARIABLES] - And you can assign the same value to multiple variables in one line:

(2) Example

>>>x = y = z = "Orange"
>>>print(x)
>>>print(y)
>>>print(z)

[UNPACK-A-COLLECTION] - If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

(3) Example

Unpack a list: 

>>>fruits = ["apple", "banana", "cherry"]
>>>x, y, z = fruits
>>>print(x)
>>>print(y)
>>>print(z)