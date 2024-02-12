'''
Title:
    Grade Classification Program

Prerequisites:
    Basic understanding of programming concepts, such as variables, conditionals, and user input.

Objectives:

    Prompt the user to input their percentage.
    Determine the corresponding grade based on the provided percentage.
    Display the grade to the user.

Algorithm:

    Begin by prompting the user to input their percentage.
    Read the input percentage from the user.
    Use nested conditional statements to check the percentage range and assign the corresponding grade.
    Print the grade based on the determined range.

'''

percentage = float(input("Enter your percentage: "))

if percentage >= 80:
    grade = 'O'
elif percentage >= 75:
    grade = 'A+'
elif percentage >= 70:
    grade = 'A'
elif percentage >= 65:
    grade = 'B+'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 55:
    grade = 'Pass'
else:
    grade = 'Fail'

print("Your grade is:", grade)
