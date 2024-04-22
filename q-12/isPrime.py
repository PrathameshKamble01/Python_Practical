"""
Title: 

Printing Prime Numbers

Prerequisites: 

Basic understanding of loops, conditionals, and functions in Python.

Objectives: 

To create a Python function that prints the first n prime numbers.

Algorithm:

1. Define a function print_n_primes(n) that takes the number of prime numbers to print, n, as input.
2. Initialize a variable num to 2 (the first prime number).
3. Initialize a variable count to 0 to keep track of the number of prime numbers printed.
4. Start a while loop until count reaches n:
    a. Check if num is prime.
    b. If it is prime, print num and increment count.
    c. Increment num.
5. Return from the function.
"""

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num)
            count += 1
        num += 1

# Example usage:
n = 10
print("First", n, "prime numbers:")
print_n_primes(n)
