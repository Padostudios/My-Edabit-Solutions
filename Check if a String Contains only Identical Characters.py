"""
Write a function that returns True if all characters in a string are identical and False otherwise.

Examples:

is_identical("aaaaaa") ➞ True

is_identical("aabaaa") ➞ False

is_identical("ccccca") ➞ False

is_identical("kk") ➞ True
"""

def is_identical(s):
	return True if len(s)==s.count(s[0]) else False