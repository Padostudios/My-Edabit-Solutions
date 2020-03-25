"""
Create a function that takes a dictionary argument sizes (contains width, length, height keys) and returns the volume of the box.

Examples:

volume_of_box({ "width": 2, "length": 5, "height": 1 }) ➞ 10

volume_of_box({ "width": 4, "length": 2, "height": 2 }) ➞ 16

volume_of_box({ "width": 2, "length": 3, "height": 5 }) ➞ 30
"""

def volume_of_box(sizes):
	s=list(sizes.values())
	return s[0]*s[1]*s[2]