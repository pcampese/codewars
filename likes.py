# https://www.codewars.com/kata/who-likes-it/train/python

def likes(names):
	# Display the arguments
	print('names = {}'.format(names))

	# Generate using lots of if statements...
	length = len(names)
	if (not names):		# If no names are provided
		display_name = 'no one'
	elif (length == 1):	# There's 1 name
		display_name = names[0]
	elif (length == 2):	# There are 2 names
		display_name = '{} and {}'.format(names[0], names[1])
	elif (length == 3):	# There are 3 names
		display_name = '{}, {} and {}'.format(names[0], names[1], names[2])
	else:				# There are 4 or more names
		display_name = '{}, {} and {} others'.format(names[0], names[1], len(names[2:]))

	# Final formatting
	if (length <= 1):									# If there's 0 or 1 names
		result = '{} likes this'.format(display_name)	# Use the plural 'likes'
	else:												# Otherwise
		result = '{} like this'.format(display_name)	# Use the singular 'like'

	print('result = {}'.format(result))

	return result