"""
Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.

Examples:

factorial(3) ➞ 6

factorial(5) ➞ 120

factorial(13) ➞ 6227020800
"""

def factorial(num):
    carp = 1
    for i in range(1,num+1):
        carp = carp * i
    return carp