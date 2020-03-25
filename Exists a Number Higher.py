"""
Write a function that returns True if there exists at least one number that is larger than or equal to n.

Examples:

exists_higher([5, 3, 15, 22, 4], 10) ➞ True

exists_higher([1, 2, 3, 4, 5], 8) ➞ False

exists_higher([4, 3, 3, 3, 2, 2, 2], 4) ➞ True

exists_higher([], 5) ➞ False
"""

def exists_higher(lst, n):
	return max(lst) >= n if len(lst)>0 else False