"""
Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples:

count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4
"""

def count_vowels(txt):
	flag = 0
	wovels=["a","e","o","u","i"]
	for i in txt:
		if i in wovels:
			flag=flag+1
	return flag