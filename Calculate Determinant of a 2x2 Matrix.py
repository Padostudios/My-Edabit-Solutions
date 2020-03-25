"""
Create a function to calculate the determinant of a 2 x 2 matrix. The determinant of the following matrix is: ad - bc:

[[a, b], [c, d]]

Examples:

calc_determinant([
  [1, 2],
  [3, 4]
]) ➞ -2

calc_determinant([
  [5, 3],
  [3, 1]
]) ➞ -4

calc_determinant([
  [1, 1],
  [1, 1]
]) ➞ 0
"""

import numpy as np
def calc_determinant(matrix):
	return round(np.linalg.det(matrix))