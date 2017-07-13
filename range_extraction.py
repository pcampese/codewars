# https://www.codewars.com/kata/range-extraction/train/python

def solution(arr):
	# Print arguments
	print('arr ='.format(arr))
	print

	# Get the length of the list
	length = len(arr)

	# First deal with it appropriately, depending on the length of the list
	if (length <= 2):
		# If the list is too short, there's nothing to do, so just return itself
		result = arr
	else:
		# The list is long enough to do some analysis
		# List to save the original list converted with the ranged numbers
		range_list = []
		result = ""

		# Walk through the list, excluding the last 2 numbers (since we want to
		# guarantee three digits)
		for index in xrange(0, length-2):
			number = arr[index]
			lookahead1 = arr[index+1]
			lookahead2 = arr[index+2]
			print('[number] lookahead1 and 2: [{}] {} {}'.format(number,
																 lookahead1,
																 lookahead2))

			# Check if the number with 2 lookaheads form a range
			triple_range = [False for (a, b) in zip(xrange(number,number+3), arr[index:index+3]) if (a != b)]
			if (False in triple_range):
				# It is not a triple range
				print('No.')
				result += '{},'.format(number)
				next()
			else:
				# It is a triple range
				print('Yes.')
				result += '{}-'.format(number)

			print('  |--> result = {}'.format(result))
			print

	# Print the final results
	print('result = {}'.format(result))

	return result