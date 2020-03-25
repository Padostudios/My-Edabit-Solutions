"""
Something which is not true is false, but something which is not not true is true!
Create a function where given n number of "not", evaluate whether it's True or False.

"""

def notNotNot(n, b):
	return True if b is True and  n%2==0 else True if b is False and n%2==1 else False