"""
Create a function that changes all the elements in a list as follows:

Add 1 to all even integers, nothing to odd integers.
Concatenates "!" to all strings and capitalises them.
Changes all boolean values to its opposite.

Examples:
change_types(["a", 12, True]) ➞ ["A!", 13, False]

change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]

change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]
"""

def change_types(lst):
    nlst = []
    for i in lst:
        if type(i) == int:
            nlst.append(i+1 if i % 2==0 else i)
        elif type(i) == str:
            nlst.append(i.capitalize()+"!")
        else:
            nlst.append(not i)
    return nlst