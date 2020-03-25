"""
A number added with its additive inverse equals zero. Create a function that returns a list of additive inverses.

Examples
additive_inverse([5, -7, 8, 3]) ➞ [-5, 7, -8, -3]

additive_inverse([1, 1, 1, 1, 1]) ➞ [-1, -1, -1, -1, -1]

additive_inverse([-5, -25, 35]) ➞ [5, 25, -35]
"""

def additive_inverse(lst):
	return [-x for x in lst]