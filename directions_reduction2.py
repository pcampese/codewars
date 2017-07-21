# https://www.codewars.com/kata/directions-reduction/train/python

def dirReduc(arr):
	print('-- dirReduc: Start --')

	# Print the arguments
	print('arr = {}'.format(arr))
	print

	# Direction with reduced instructions
	reduced_direction = []

	# Track if changes have been made
	changes_made = False

	# Loop through each index in the direction list
	print('-- Loop through each index in the direction list: Start --')
	for index in xrange(len(arr)-1):
		dir1 = arr[index]
		dir2 = arr[index+1]
		# print('dir1 = {}'.format(dir1))
		# print('dir2 = {}'.format(dir2))
		print('{} of {}'.format(index, len(arr)-1))
		print("['{}', '{}']".format(dir1, dir2))
		print

		if (changes_made):
			print('...skip to next index...')
			changes_made = False
			continue

		if ((dir1 == 'NORTH' and dir2 == 'SOUTH') or
			(dir1 == 'SOUTH' and dir2 == 'NORTH')):
			print('> if_1 - Add nothing')
			# Need to skeep the next element
			changes_made = True
		elif ((dir1 == 'EAST' and dir2 == 'WEST') or
			  (dir1 == 'WEST' and dir2 == 'EAST')):
			print('> if_2 - Add nothing')
			# Need to skeep the next element
			changes_made = True
		else:
			print('> else - Add 1st element')
			changes_made = False
			# print('arr[index:index+2] = arr[{}:{}] = {}'.format(index, index+2, arr[index:index+2]))
			# reduced_direction.extend(arr[index:index+2])
			print('arr[index] = arr[{}] = {}'.format(index, arr[index]))
			reduced_direction.append(arr[index])
		print('===> reduced_direction = {}'.format(reduced_direction))
		print
	print('-- Loop through each index in the direction list: End --')

	# Call recursion
	if (changes_made):
		print('-- Recursion: Start --')
		reduced_direction = dirReduc(reduced_direction)
		print('-- Recursion: End --')

	print('reduced_direction = {}'.format(reduced_direction))

	print('-- dirReduc: End --')