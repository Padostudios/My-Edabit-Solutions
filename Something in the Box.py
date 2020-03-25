"""
Create a function that returns True if an asterisk * is inside a box.

Examples
in_box([
  "###",
  "#*#",
  "###"
]) ➞ True

in_box([
  "####",
  "#* #",
  "#  #",
  "####"
]) ➞ True

in_box([
  "*####",
  "# #",
  "#  #*",
  "####"
]) ➞ false

in_box([
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]) ➞ False
"""

def in_box(lst):
	for i in lst:
		if "*" in i:
			return True
	else:
		return False