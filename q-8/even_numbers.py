'''
Title:
    Print Even Numbers up to User's Input

Prerequisites:
    Basic understanding of programming concepts such as loops, conditionals, and user input in Python.

Objectives:

    Prompt the user to enter a number.
    Print all even numbers from 0 up to the entered number.

Algorithm:

    Begin by prompting the user to enter a number.
    Read the input number from the user.
    Initialize a loop variable, starting from 0 and going up to the entered number.
    Inside the loop, check if the current number is even using the modulo operator (%).
    If the current number is even, print it.
    Continue the loop until the loop variable reaches the entered number.
    End.

'''


number = int(input("Enter a number: "))

print("Even numbers from 0 to", number, "are:")
for i in range(number + 1):
    if i % 2 == 0:
        print(i)
