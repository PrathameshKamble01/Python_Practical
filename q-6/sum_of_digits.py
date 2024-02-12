'''
Title:
    Sum of Digits in a Number

Prerequisites:
    Basic understanding of programming concepts, such as variables, loops, and arithmetic operations in Python.

Objectives:

    Prompt the user to input a number.
    Calculate the sum of the digits of the input number.
    Display the sum to the user.

Algorithm:

    Begin by prompting the user to enter a number.
    Read the input number from the user.
    Initialize a variable to store the sum of digits (sum_digits) and set it to 0.
    Iterate through each digit of the number using a loop.
    For each digit, add it to sum_digits.
    Continue this process until all digits are processed.
    Display the sum of digits (sum_digits) to the user.

'''

number = input("Enter a number: ")

sum_digits = 0

for digit in number:
    sum_digits += int(digit)

print("The sum of digits in the number is:", sum_digits)
