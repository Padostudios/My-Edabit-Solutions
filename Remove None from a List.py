"""
Create a function to remove all None values from a list.

Examples:

remove_none(["a", None, "b", None]) ➞ ["a", "b"]

remove_none([None, None, None, None, None]) ➞ []

remove_none([7, 8, None, 9]) ➞ [7, 8, 9]
"""

def remove_none(lst):
	return [i for i in lst if i is not None]