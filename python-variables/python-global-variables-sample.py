# The use of Python Global Variables
# This program demonstrates the use of global variables in Python.
# A global variable is a variable that is defined outside of any function and can be accessed from any function within the same module.

# Defining a global variable
global_var = "I am a global variable"
def display_global_variable():
    # Accessing the global variable inside a function
    print(global_var)
# Calling the function to display the global variable
display_global_variable()
# Modifying a global variable inside a function
def modify_global_variable():
    global global_var  # Declare that we are using the global variable
    global_var = "I have been modified"
# Calling the function to modify the global variable
modify_global_variable()
# Displaying the modified global variable
display_global_variable()
# Demonstrating that the global variable has been modified
print("Outside the function:", global_var)

