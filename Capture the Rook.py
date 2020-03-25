"""
Write a function that returns True if two rooks can attack each other, and False otherwise.

Examples:

can_capture(["A8", "E8"]) ➞ True

can_capture(["A1", "B2"]) ➞ False

can_capture(["H4", "H3"]) ➞ True

can_capture(["F5", "C8"]) ➞ False
"""

def can_capture(rooks):
	return True if rooks[0][0]==rooks[1][0] or rooks[0][1]==rooks[1][1] else False