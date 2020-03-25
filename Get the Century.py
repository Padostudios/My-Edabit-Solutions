"""
Create a function that takes in a year and returns the correct century.

Examples:

century(1756) ➞ "18th century"

century(1555) ➞ "16th century"

century(1000) ➞ "10th century"

century(1001) ➞ "11th century"

century(2005) ➞ "21st century"
"""

def century(year):
	yy = str((year+99)//100)
	return "21st century" if yy=="21" else yy + "th century"