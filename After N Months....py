"""
Create a function that takes in year and month as input, then return what year it would be after n-months has elapsed.
"""

def afterNMonths(year,month):
	if year == None:
		return "year missing"
	elif month == None:
		return "month missing"
	else:
		return year+(int(month/12))