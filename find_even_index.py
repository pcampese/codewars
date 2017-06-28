# https://www.codewars.com/kata/equal-sides-of-an-array/train/python

def find_even_index(arr):
	# Print arguments
	print('arr = {}'.format(arr))

	# Iterate through the index, and sum both sides of the array
	for index in xrange(len(arr)):		# For each index of the array length
		left = sum(arr[:index])			# Sum all elements to the left of the current index
		right = sum(arr[index + 1:])	# Sum all elements to the right of the current index

		if (left == right):		# If the two sums are equal
			result = index		# Then the current index is the answer
			break				# Break out of the for loop - no need to check more
		else:					# Otherwise
			result = -1			# There is no valid answer, return -1

	print('result = {}'.format(result))

	return result