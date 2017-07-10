# https://www.codewars.com/kata/find-the-parity-outlier/train/python

def find_outlier(integers):
	import operator
	# Print arguments
	print('integers = {}'.format(integers))

	# First, determine the "trend" - is it mostly odd?  Or mostly even?
	even_tracker = 0	# positive = even; negative = odd

	# We only need to look at the first 3 integers, to determine a set's trend
	for i in integers[:3]:
		if (i % 2 == 0):
			# It's even
			even_tracker += 1
		else:
			# It's odd
			even_tracker -= 1

	# Define which comparison we want to perform, for checking remaining numbers
	if (even_tracker > 0):
		# It's even, so to find the outlier: (number % 2) NOT equal to (0)
		ops = operator.ne
	else:
		# It's odd, so to find the outlier: (number % 2) IS equal to (0)
		ops = operator.eq

	# Find the element that doesn't match the set, and break out ASAP
	for i in integers:
		if (ops(i%2,0)):
			result = i
			break

	# Display the final value
	print('result = {}'.format(i))

	return result