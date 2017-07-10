# https://www.codewars.com/kata/build-a-pile-of-cubes/train/python

def find_nb(m):
	# Print arguments
	print('m = {}'.format(m))

	# Define the maximum number to try up to
	max_loop = int(m * 0.23)
	print('max_loop = {}'.format(max_loop))

	# Store the final result
	result = 0

	# Keep on counting cubes until we reach the right number
	counter = 0
	for i in xrange(1,max_loop):
		result += i**3
		counter += 1
		# print('result = {}'.format(result))
		if (result == m):
			break

	# Set the final result
	result = counter

	# Display the final value
	print('result = {}'.format(result))

	return result