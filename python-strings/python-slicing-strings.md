[PYTHON-SLICING-STRINGS] - You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

(1) Example 

Get the characters from position 2 to position 5 (not included):

>>>b = "Hello, World!"
>>>print(b[2:5])

Note: The first character always starts with 0 as its index.

[SLICE-FROM-THE-START] - By leaving out the start index, the range will start at the first character:

(2) Example

Get the characters from the start to position 5 (not included):

>>>b = "Hello, World!"
>>>print(b[:5])

[SLICE-TO-THE-END] - By leaving out the end index, the range will go to the end:

(3) Example

Get the characters from position 2, and all the way to the end:

>>>b = "Hello, World!"
>>>print(b[2:])

[NEGATIVE-INDEXING] - Use negative indexes to start the slice from the end of the string:

(4) Example

Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

>>>b = "Hello, World!"
>>>print(b[-5:-2])