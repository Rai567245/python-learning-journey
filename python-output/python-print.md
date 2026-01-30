[PRINT-TEXT] - You have already learned that you can use the print() function to display text or output values:

(1) Example
>>>print("Hello World!")

- You can use the print() function as many times as you want. Each call prints text on a new line by default:

>>>print("Hello World")
>>>print("I am learning Python.")
>>>print("It is awesome!")

[DOUBLE-QOUTES] - Text in Python must be inside quotes. You can use either " double quotes or ' single quotes:

(2) Example
>>>print("This will work!")
>>>print('This will also work!')

- If you forget to put the text inside quotes, Python will give an error:

>>>print(This will cause an error)

[PRINT-WITHOUT-A-NEW-LINE] - By default, the print() function ends with a new line.

If you want to print multiple words on the same line, you can use the end parameter:

>>>print("Hello World!", end=" ")
>>>print("I will print on the same line.")

- Note that we add a space after end=" " for better readability.