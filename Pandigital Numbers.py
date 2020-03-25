"""
A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, returning True if the integer is pandigital, and False otherwise.

Examples:

is_pandigital(98140723568910) ➞ True

is_pandigital(90864523148909) ➞ False
# 7 is missing.

is_pandigital(112233445566778899) ➞ False
"""

def is_pandigital(n):
    flag = 0
    strn=[]
    nums = ["1","2","3","4","5","6","7","8","9","0"]  
    for i in str(n):
        strn.append(i)
    for j in nums:
        if j not in strn:
            flag=1
    if flag == 1:
        return False
    else:
        return True