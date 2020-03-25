"""
Create a function that adds a string ending to each member in a list.

Examples:

add_ending(["clever", "meek", "hurried", "nice"], "ly")
➞ ["cleverly", "meekly", "hurriedly", "nicely"]

add_ending(["new", "pander", "scoop"], "er")
➞ ["newer", "panderer", "scooper"]

add_ending(["bend", "sharpen", "mean"], "ing")
➞ ["bending", "sharpening", "meaning"]
"""

def add_ending(lst, ending):
	return [x+ending for x in lst]