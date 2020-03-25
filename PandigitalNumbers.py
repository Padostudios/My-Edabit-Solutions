"""
Pandigital Numbers

A pandigital number contains all digits (0-9) at least once.
Write a function that takes an integer, returning True if the integer is pandigital, and False otherwise.

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






print(is_pandidigital(10282343456789))