"""
List A is contained inside list B if each element in A also exists in B.

The number of times a number is present doesn't matter. In other words, if we transformed both lists into sets, A would be a subset of B.

Create a function that determines if the first list is a subset of the second.

Examples:

subset([1, 3], [1, 3, 3, 5]) ➞ True

subset([4, 8, 7], [7, 4, 4, 4, 9, 8]) ➞ True

subset([1, 3], [1, 33]) ➞ False

subset([1, 3, 10], [10, 8, 8, 8]) ➞ False
"""

def subset(lst1, lst2):
	return True if set(lst1).issubset(set(lst2)) else False