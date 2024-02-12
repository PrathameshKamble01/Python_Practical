'''
Title:
    Leap Year Checker

Prerequisites:
    Basic understanding of programming concepts, such as variables, conditionals, and user input.

Objectives:

    Prompt the user to input a year.
    Determine whether the input year is a leap year or not.
    Display the result to the user.

Algorithm:

    Begin by prompting the user to enter a year.
    Read the input year from the user.
    Use a conditional statement to check if the year is divisible by 4.
    If the year is divisible by 4, check if it is also divisible by 100.
    If the year is divisible by 100, check if it is also divisible by 400.
    If the year is divisible by 400, it is a leap year. Otherwise, it is not.
    If the year is not divisible by 100, but divisible by 4, it is a leap year.
    If the above conditions are met, print "Leap year", otherwise, print "Not a leap year".

'''

year = int(input("Enter a year: "))

# Checking if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
