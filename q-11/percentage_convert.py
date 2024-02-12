'''Write a Program to Read marks from user and Find the percentage of marks of student

Title:
    Calculate Percentage of Marks

Prerequisites:
    Basic understanding of programming concepts, such as variables, input/output operations, and arithmetic operations in Python.

Objectives:

    Prompt the user to input marks obtained by a student.
    Calculate the total marks.
    Calculate the percentage of marks obtained by the student.
    Display the percentage of marks to the user.

Algorithm:

    Begin by prompting the user to input marks obtained in each subject.
    Read the input marks from the user.
    Sum up all the marks to calculate the total marks.
    Calculate the percentage using the formula: (total marks obtained / total marks) * 100.
    Display the percentage of marks to the user.

'''

subject1 = float(input("Enter marks obtained in subject 1: "))
subject2 = float(input("Enter marks obtained in subject 2: "))
subject3 = float(input("Enter marks obtained in subject 3: "))

total_marks = subject1 + subject2 + subject3

percentage = (total_marks / 300) * 100

print("Percentage of marks:", percentage)
