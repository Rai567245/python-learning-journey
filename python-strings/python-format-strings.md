[PYTHON-FORMAT-STRINGS] - As we learned in the Python Variable chapter, we cannot combine strings and number like this:

(1) Example

>>>age = 36
>>>#This will produce an error:
>>>txt = "My name is John, I am " + age
>>>print(txt)
 
But we can combine strings and numbers by using f-string or the format() method!

[F-STRINGS] - F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

(2) Example

Create an f-string:

>>>age = 36
>>>txt = f"My name is John, I am {age}"
>>>print(txt)

[PLACEHOLDERS-AND-MODIFIERS] - A placeholder can contain variables, operations, functions, and modifiers to format the value.

(3) Example 

Add a placeholder for the price variable:

>>>price = 59
>>>txt = f"The price is {price} dollars"
>>>print(txt)

A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

(4) Example

Display the price with 2 decimals:

>>>price = 59
>>>txt = f"The price is {price:.2f} dollars"
>>>print(txt)

A placeholder can contain Python code, like math operations:

(5) Example

Perform a math operation in the placeholder, and return the result:

>>>txt = f"The price is {20 * 59} dollars"
>>>print(txt)