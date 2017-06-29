# https://www.codewars.com/kata/snail

def snail(array):
	# Print the arguments
	print('array = {}'.format(array))

	result = []			# The final snaked resulted

	while True:			# Keep going
		if (array):		# If the array is not empty
			print('array[0] = {}'.format(array[0]))
			top_row = array.pop(0)
			print('top_row = {}'.format(top_row))
			for i in top_row:
				print('i = {}'.format(i))
				result.append(i)
			if (array):		# If the array is still not empty
#					array = list(reversed(zip(*array)))		# Rotate the array
				array = list(reversed([list(a) for a in zip(*array)]))		# Rotate the array
				print('rotated = {}'.format(array))
				if (not array):			# The array is empty
					break				# Then stop now
			print
		else:					# Otherwise, we're done!
			break				# Break out

	# Print the result
	print('result = {}'.format(result))

	return result