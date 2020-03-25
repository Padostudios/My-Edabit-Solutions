"""
Write a function that takes a positive integer and return its factorial.

Examples:

factorial(4) ➞ 24

factorial(0) ➞ 1

factorial(9) ➞ 362880
"""

def factorial(Z):
	carp = 1
	for i in range(1,Z+1):
		carp = carp * i
	return carp