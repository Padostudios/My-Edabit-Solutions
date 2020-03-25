"""
Write a function that takes the last number of a consecutive list of numbers and returns the total of all numbers up to and including it.

Examples: 

add_up_to(3) ➞ 6
# 1 + 2 + 3 = 6

add_up_to(10) ➞ 55
# 1 + 2 + 3 + ... + 10 = 55

add_up_to(7) ➞ 28
# 1 + 2 + 3 + ... + 7 = 28
"""

def addUpTo(n):
	summ = 0
	while n>=0:
		summ = summ + n
		n=n-1
	return summ