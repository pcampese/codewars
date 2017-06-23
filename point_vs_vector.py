# https://www.codewars.com/kata/geometry-a-1-locate-point-to-the-right-to-the-left-or-on-the-vector/train/python

def point_vs_vector(point, vector):
	print('vector = {}'.format(vector))
	print('point = {}'.format(point))

	v_start = vector[0]
	v_end = vector[1]

	# Equation of line: y = mx + b
	#	m = slope
	#	b = y intercept

	# Calculate slope:  m = rise / run = (end(y) - start(y)) / (end(x) - start(x))
	rise = float(v_end[1] - v_start[1])
	run = float(v_end[0] - v_start[0])
	m = rise / run

	# Calculate y-intercept: b = y - mx
	b = v_start[1] - (m * v_start[0])

	# For the point provided, calculate value of 'y' using the point's value of 'x'
	y = int(round(m * point[0] + b))

	# Assume the vector goes from left to right
	if (point[1] > y):		# If the point's y-value is higher, then it's on the left
		result = -1			# -1 means on the left
	elif (point[1] < y):	# If the point's y-value is lower, then it's on the right
		result = 1			# 1 means on the right
	else:					# Otherwise, the point is the same line as vector
		result = 0			# 0 means on the line

	# Reverse the result if the vector actually goes from right to left (opposite of assumption)
	if (v_end[0] < v_start[0]):
		result *= -1

	print('result = {}'.format(result))
	return result