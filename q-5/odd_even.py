'''
Title:
Check Even or Odd Number

Prerequisites:
Basic understanding of programming concepts, such as variables, conditionals, and user input.

Objectives:

Prompt the user to input a number.
Determine whether the input number is even or odd.
Display the result to the user.
'''

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
