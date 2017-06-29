# https://www.codewars.com/kata/snail

def snail(array):
	# Print the arguments
	print('array = {}'.format(array))

	result = []			# The final snaked resulted

	while True:			# Keep going
		if (array):		# If the array is not empty
			print('array[0] = {}'.format(array[0]))
			for i in array[0]:
				print('i = {}'.format(i))
				t = array.pop(0)
				print('t = {}'.format(t))
				result.append(t)	# Take first element from array, append to result array
				if (array):		# If the array is still not empty
					array = list(reversed(zip(*array)))		# Rotate the array
					print('rotated = {}'.format(array))
					if (not array):			# The array is empty
						break				# Then stop now
				print
		else:					# Should never be here...
			print('??? ERROR!!!')
			break

	# Print the result
	print('result = {}'.format(result))

	return result