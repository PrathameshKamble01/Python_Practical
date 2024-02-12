'''
Title:
    Program to Find the GCD of Two Positive Numbers

Prerequisites:

    Basic understanding of variables and arithmetic operations in Python.
    Familiarity with loops and conditionals.
    Knowledge of functions in Python.
Objectives:

    Understand the concept of the greatest common divisor (GCD) of two numbers.
    Implement an algorithm to find the GCD of two positive numbers.
    Write a Python program to execute the GCD calculation.
Algorithm:

    Define a function named gcd that takes two parameters a and b.
    Initialize a variable gcd_result to store the GCD.
    Use a while loop with the condition b != 0.
    Inside the loop, set temp to the value of b.
    Update b with the remainder of a divided by b.
    Update a with the value of temp.
    After the loop, set gcd_result to the absolute value of a.
    Return gcd_result.
    Input two positive numbers num1 and num2 from the user.
    Call the gcd function with num1 and num2 as arguments and store the result in a variable result.
    Print the result as the GCD of num1 and num2.

'''

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return abs(a)

# Input two positive numbers from the user
num1 = int(input("Enter the first positive number: "))
num2 = int(input("Enter the second positive number: "))

# Calculate and print the GCD
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", result)
