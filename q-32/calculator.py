"""
Title:
Simple Calculator Module

Prerequisites:
Basic understanding of Python programming language.

Objectives:
- Implement a module in Python for performing simple calculator operations such as addition, subtraction, multiplication, and division.
- Ensure the module is easy to use and integrate into other Python programs.

Algorithm:
1. Define functions for addition, subtraction, multiplication, and division.
2. Accept input from the user for two numbers and the desired operation.
3. Perform the corresponding operation based on the user input.
4. Return the result of the operation.
"""

def add(num1, num2):
    """Function to add two numbers"""
    return num1 + num2

def subtract(num1, num2):
    """Function to subtract two numbers"""
    return num1 - num2

def multiply(num1, num2):
    """Function to multiply two numbers"""
    return num1 * num2

def divide(num1, num2):
    """Function to divide two numbers"""
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    else:
        return num1 / num2

# Test the module
if __name__ == "__main__":
    while True:
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid input! Please select a valid operation.")
