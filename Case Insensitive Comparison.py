"""
Write a function that validates whether two strings are identical. Make it case insensitive.

Examples:

match("hello", "hELLo") ➞ True

match("motive", "emotive") ➞ False

match("venom", "VENOM") ➞ True

match("mask", "mAskinG") ➞ False
"""

def match(s1, s2):
	if s1.lower()==s2.lower():
		return True
	else:
		return False