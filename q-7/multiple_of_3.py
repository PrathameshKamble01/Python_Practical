'''
Title:
    Print First 10 Multiples of 3

Prerequisites:
    Basic understanding of Python programming syntax, loops, and arithmetic operations.

Objectives:

    Generate the first 10 multiples of 3.
    Print each multiple.

Algorithm:

    Initialize a variable count to 1 to keep track of the number of multiples printed.
    Use a loop (e.g., a for loop) to iterate from 1 to 10 (inclusive).
    Within the loop, calculate the multiple of 3 using the current iteration variable.
    Print each multiple.
    Increment the count variable after printing each multiple.

'''

count = 1

for i in range(1, 11):
    multiple = 3 * i
    print("Multiple", count, ":", multiple)
    count += 1
