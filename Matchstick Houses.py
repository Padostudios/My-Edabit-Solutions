"""
This challenge will help you interpret mathematical relationships both algebraically and geometrically

Create a function that takes a number (step) as an argument and returns the amount of matchsticks in that step. See step 1, 2 and 3 in the image above.

Examples:

match_houses(1) ➞ 6

match_houses(4) ➞ 21

match_houses(87) ➞ 436
"""

def match_houses(step):
	return ((5*step)+1) if step>0 else 0