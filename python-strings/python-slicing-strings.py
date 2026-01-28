# This program demonstrates the use of python string slicing. 
# sequence[start:end:step]

# This is called python slicing where we can extract a portion of a string.
characterName = "RaiTech"
print(characterName[0:3])

# If we omit the start index, python assumes it to be 0.
characterName = "RaiTech"
print(characterName[:5])

# If we omit the end index, python assumes it to be the length of the string.
characterName = "RaiTech"
print(characterName[2:])

# We can also use negative indexing to slice strings.
characterName = "RaiTech"
print(characterName[-4:-1])

# We can also use step values in slicing.
characterName = "RaiTech"
print(characterName[0:7:2]) 