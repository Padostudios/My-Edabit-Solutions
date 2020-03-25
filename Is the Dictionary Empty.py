"""
Write a function that returns True if a dictionary is empty, and False otherwise.

Examples:

is_empty({}) ➞ True

is_empty({ "a": 1 }) ➞ False
"""

def is_empty(dictionary):
	if len(dictionary)==0:
		return True
	else:
		return False