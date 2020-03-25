"""
Write a function to check if a list contains a particular number.

Examples:

check([1, 2, 3, 4, 5], 3) ➞ True

check([1, 1, 2, 1, 1], 3) ➞ False

check([5, 5, 5, 6], 5) ➞ True

check([], 5) ➞ False
"""

def check(lst, el):
	if el in list(lst):
		return True
	else:
		return False