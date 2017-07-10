# https://www.codewars.com/kata/title-case/train/python

def title_case(title, minor_words=None):
	# Print arguments
	print('title = {}'.format(title))
	print('minor_words = {}'.format(minor_words))
	print

	# Convert the provided arguments into lists
	title = title.split()
	if (minor_words != None):
		minor_words = minor_words.split()
	print('title = {}'.format(title))
	print('minor_words = {}'.format(minor_words))
	print

	# Store the final result
	result = 0

	# Display the final value
	print('result = {}'.format(result))

	return result