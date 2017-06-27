# https://www.codewars.com/kata/find-the-odd-int/train/python

def find_it(seq):
	import collections
	# Print arguments
	print('seq = {}'.format(seq))

	# User Counter to create a dictionary of all the items, and their frequency (i.e. count)
	count_of = collections.Counter(seq)

	# Determine which entries in the dictionary have an odd count
	for (number, count) in count_of.viewitems():	# For each number:count pair
		if (count % 2):								# If it's odd, this returns non-zero
			result = number	

	return result