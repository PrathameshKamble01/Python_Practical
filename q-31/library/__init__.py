"""

Title: Python Library Functions

Prerequisites: Basic knowledge of Python programming.

Objectives: Implement commonly used library functions in Python.

Algorithm:

1. Create a Python package named "library".
2. Inside the package, implement functions such as:
    a. Function to find the maximum value in a list.
    b. Function to find the minimum value in a list.
    c. Function to calculate the factorial of a number.
    d. Function to check if a number is prime.
    e. Function to calculate the square root of a number.
    f. Function to reverse a string.
3. Test each function to ensure its correctness.

"""

def find_max(arr):
    return max(arr)

def find_min(arr):
    return min(arr)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:

        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def square_root(n):
    return n ** 0.5

def reverse_string(s):
    return s[::-1]