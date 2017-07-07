# https://www.codewars.com/kata/youre-a-square/train/python

def is_square(n):
	import math

	# Print the arguments
	print('n = {}'.format(n))

	# Define default return value
	result = False

	# If it's a positive number
	if (n >= 0):
		# Get the square root of the number
		square_root = math.sqrt(n)
		# If the square root is an integer, then the answer is 'True'
		if (square_root.is_integer()):
			result = True

	print('result = {}'.format(result))

	return result