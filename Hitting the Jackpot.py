"""
Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise. The list will contain 4 elements.

Examples:

test_jackpot(["@", "@", "@", "@"]) ➞ True

test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True

test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True

test_jackpot(["&&", "&", "&&&", "&&&&"]) ➞ False

test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False
"""

def test_jackpot(result):
	return True if len(set(result))==1 else False