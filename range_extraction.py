# https://www.codewars.com/kata/range-extraction/train/python

def solution(arr):
	import pprint
	
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
		list_of_sequences = [[]]
		result = []

		# Walk through the list, comparing the current number against a range
		# buffer
		for number in arr:
			# Check if it's the first number
			if (not list_of_sequences[-1]):
				list_of_sequences[-1].append(number)
				continue

			# See if the number is exactly 1 + "most recent number"
			if (number == list_of_sequences[-1][-1] + 1):
				# Yes.  It's sequential
				list_of_sequences[-1].append(number)
			else:
				# No.  It's not sequential.  Generate a new list
				list_of_sequences.append([number])

		# Generate the final list using the list_of_lists
		for sequence in list_of_sequences:
			if (len(sequence) <= 2):
				# There aren't enough numbers to generate a sequence, so just
				# append those numbers to the final result
				result.extend([str(n) for n in sequence])
			else:
				# There are enough numbers for a sequence, so use the 1st and
				# last numbers to define the sequence
				result.append('{}-{}'.format(sequence[0], sequence[-1]))

		# Join the final list
		result = ','.join(result)

	# Print the final results
	print('result = {}'.format(result))

	return result