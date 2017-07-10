# https://www.codewars.com/kata/unique-in-order/train/python

def unique_in_order(iterable):
	# Print arguments
	print('iterable = <{}>'.format(iterable))

	# Do the work, if we have a non-empty iterable
	if (iterable):
		# Keep the first element, no matter what
		result = [iterable[0]]

		# Loop through (excluding first [saved above]) comparing the current
		# item in 'iterable' against the most recent unique item in 'result'
		for item in iterable[1:]:
			if (item != result[-1]):
				result.append(item)
	else:
		result = []

	print('result = {}'.format(result))

	return result