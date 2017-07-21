# https://www.codewars.com/kata/directions-reduction/train/python

def dirReduc(arr):
	print('-- dirReduc: Start --')

	# Print the arguments
	print('arr = {}'.format(arr))
	print

	# Direction with reduced instructions
	reduced_direction = []

	# Loop through each index in the direction list
	print('-- Loop through each index in the direction list: Start --')
	for index in xrange(len(arr)-1):
		print('reduced_direction = {}'.format(reduced_direction))
		dir1 = arr[index]
		dir2 = arr[index+1]
		print('dir1 = {}'.format(dir1))
		print('dir2 = {}'.format(dir2))
		print

		if (dir1 == 'NORTH' or dir2 == 'SOUTH'):
			reduced_direction.extend(arr[index:index+2])
		elif (dir1 == 'EAST' or dir2 == 'WEST'):
			reduced_direction.extend(arr[index:index+2])
		else:
			changes_made = True
	print('-- Loop through each index in the direction list: End --')

	if (changes_made):
		reduced_direction = dirReduc(reduced_direction)

	print('reduced_direction = {}'.format(reduced_direction))

	print('-- dirReduc: End --')