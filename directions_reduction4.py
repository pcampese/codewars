# https://www.codewars.com/kata/directions-reduction/train/python
# Meh - my loop is stuck!

def dirReduc(arr):
	print('-- dirReduc: Start --')

	# Print the arguments
	print('arr = {}'.format(arr))
	print

	# Direction with reduced instructions
	reduced_directions = []

	# Track if changes have been made
	changes_made = True

	# Loop through each index in the directions list
	print('-- Loop through each index in the directions list: Start --')
	# while (changes_made):
	for x in xrange(99):
		print('x = {}'.format(x))
		for index in xrange(len(arr)-1):
			dir1 = arr[index]
			dir2 = arr[index+1]
			# print('dir1 = {}'.format(dir1))
			# print('dir2 = {}'.format(dir2))
			print('{} of {}'.format(index, len(arr)-1))
			print("['{}', '{}']".format(dir1, dir2))
			print

			# Compare the directions
			directions = compare(dir1, dir2)

			# If we got directions back, add them to the new directions set
			if (not directions):
				print('No directions.  Remove the 2 elements')
				arr.pop(index)
				arr.pop(index)
				changes_made = True
				break
			else:
				changes_made = False

			print('===> arr = {}'.format(arr))
			print
	print('-- Loop through each index in the directions list: End --')
	print('arr = {}'.format(arr))

	print('-- dirReduc: End --')

	return arr

def compare(a, b):
	result = None

	if ((a == 'NORTH' and b == 'SOUTH') or
		(a == 'SOUTH' and b == 'NORTH')):
		print('> if_1 - Add nothing')
		# Return nothing
	elif ((a == 'EAST' and b == 'WEST') or
		  (a == 'WEST' and b == 'EAST')):
		print('> if_2 - Add nothing')
		# Return Nothing
	else:
		result = a

	return result