"""
Create a function that counts the number of syllables a word has. Each syllable is separated with a dash -.

Examples:

number_syllables("buf-fet") ➞ 2

number_syllables("beau-ti-ful") ➞ 3

number_syllables("mon-u-men-tal") ➞ 4

number_syllables("on-o-mat-o-poe-ia") ➞ 6
"""

def number_syllables(word):
	return ((word.count("-"))+1)