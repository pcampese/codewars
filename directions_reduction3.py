# https://www.codewars.com/kata/directions-reduction/train/python

def dirReduc(arr):
	print('-- dirReduc: Start --')

	# Print the arguments
	print('arr = {}'.format(arr))
	print

	# Direction with reduced instructions
	reduced_directions = []

	# Track if changes have been made
	changes_made = False

	# Loop through each index in the directions list
	print('-- Loop through each index in the directions list: Start --')
	for index in xrange(len(arr)-1):
		dir1 = arr[index]
		dir2 = arr[index+1]
		# print('dir1 = {}'.format(dir1))
		# print('dir2 = {}'.format(dir2))
		print('{} of {}'.format(index, len(arr)-1))
		print("['{}', '{}']".format(dir1, dir2))
		print

		# Skip if changes were recently made
		if (changes_made):
			changes_made = False
			continue

		# Compare the directions
		directions = compare(dir1, dir2)

		# If we got directions back, add them to the new directions set
		if (directions):
			reduced_directions.append(directions)
		else:
			# We removed the "bad" directions
			changes_made = True

		print('===> reduced_directions = {}'.format(reduced_directions))
		print
	print('-- Loop through each index in the directions list: End --')

	# Call recursion
	if (changes_made):
		print('-- Recursion: Start --')
		reduced_directions = dirReduc(reduced_directions)
		print('-- Recursion: End --')

	print('reduced_directions = {}'.format(reduced_directions))

	print('-- dirReduc: End --')

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