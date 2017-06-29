# https://www.codewars.com/kata/snail

def snail(array):
	# Print the arguments
	print('array = {}'.format(array))

	result = []			# The final snaked resulted

	while (array):									# While the array is not empty
		for i in array.pop(0):						# Remove the top row of the array, and iterate through it
			result.append(i)						# Append each element from the top row into the 'result' array
		if (array):									# If the array is still not empty (after removing that top row)
			array = list(reversed(zip(*array)))		# Rotate the array
				# Break it down...
				# *array = 'unpacks' the list.  Converts list of lists into individual lists, separated by commas (i.e. removes outer list)
				# zip = 'stacks' the lists and turns columns into rows (i.e. column 0 becomes row 0, etc) (matrix is now mirrored on main diagonal)
				# reversed = reverse the order of the zipped rows (matrix is now rotated +90 degrees), returnx an iterator object
				# list = convert the iterator object into a normal list

	# Print the result
	print('result = {}'.format(result))

	return result