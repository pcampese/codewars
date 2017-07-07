# https://www.codewars.com/kata/get-the-middle-character/train/python

def get_middle(s):
	# Print the arguments
	print('s = {}'.format(s))

	# Determine the middle index
	middle = len(s) / 2

	# If the string length is not odd (i.e. even), then there is no single
	# middle character
	if (not len(s) % 2):
		result = s[middle-1:middle+1]
	# Otherwise, take the single middle character
	else:
		result = s[middle]

	# Show final answer
	print('result = {}'.format(result))

	return result