"""
A word has been split into a left part and a right part. Re-form the word by adding both halves together, changing the first character to an uppercase letter.

Examples:

get_word("seas", "onal") ➞ "Seasonal"

get_word("comp", "lete") ➞ "Complete"

get_word("lang", "uage") ➞ "Language"
"""

def get_word(left, right):
	return (left+right).capitalize()