"""
Create a function that returns the sum of missing numbers.
"""

def sum_missing_numbers(lst):
	nlst = []
	for i in range(min(lst),max(lst)):
		if i not in lst:
			nlst.append(i)
	return sum(nlst)