"""
You're given a string of words. You need to find the word "Nemo", and return a string like this: "I found Nemo at [the order of the word you find nemo]!".

If you can't find Nemo, return "I can't find Nemo :(".

Examples:

find_nemo("I am finding Nemo !") ➞ "I found Nemo at 4!"

find_nemo("Nemo is me") ➞ "I found Nemo at 1!"

find_nemo("I Nemo am") ➞ "I found Nemo at 2!"
"""

def find_nemo(sentence):
    a = sentence.split()
    if "Nemo" in a:
        return "I found Nemo at {}!".format((a.index("Nemo"))+1)
    else:
        return "I can't find Nemo :("