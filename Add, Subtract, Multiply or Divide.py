"""
Write a function that takes two numbers and returns if they should be added, subtracted, multiplied or divided to get 24. If none of the operations can give 24, return None.

Examples:

operation(15, 9) ➞ "added"

operation(26, 2) ➞ "subtracted"

operation(11, 11) ➞ None
"""

def operation(num1, num2):
	if num1+num2==24:
		return "added"
	elif num1-num2==24:
		return "subtracted"
	elif num1*num2==24:
		return "multiplied"
	elif num1/num2 ==24:
		return "divided"
	else:
		return None