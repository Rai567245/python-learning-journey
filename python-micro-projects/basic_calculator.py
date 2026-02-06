# This program demonstrates a simple calculator that performs basic arithmetic operations.print
# It uses functions to organize the code and allows the user to perform multiple calculations until they choose to exit. 

# Function to perform arithmetic operations
def addition(x, y):
    return x + y

def substraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def divition(x, y):
    return x / y

# Main function to show calculator menu and perform calculations
def calculator():
    while True:
        print("| Simple Calculator |")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("\nChoose an operation(1-5): ")

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))

            if choice == '1':
                print(f"{num1} + {num2} = {addition(num1, num2)}\n")
            elif choice == '2':
                print(f"{num1} - {num2} = {substraction(num1, num2)}\n")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiplication(num1, num2)}\n")
            elif choice == '4':
                print(f"{num1} / {num2} = {divition(num1, num2)}\n")
            elif chocie == '5':
                print("Thank you for using the calculator!")
                break
            else:
                print("Invalid input. Please try again!\n")

calculator()

