# https://www.codewars.com/kata/replace-with-alphabet-position/train/python

def alphabet_position(text):
	import string

	# Print arguments
	print('text = {}'.format(text))

	# Get the list of all lowercase letters
	lowercase_string = string.ascii_lowercase

	index_list = []

	# Loop through each letter in 'text'
	for letter in text:
		if (letter.isalpha()):
			letter = letter.lower()
			index = lowercase_string.find(letter)

			# Adjust index, so that counting starts at 1, and convert it to a
			# string.
			index = str(index+1)

			# Append it to the final list of indexes
			index_list.append(index)

	# Join the index list, with spaces
	index_string = ' '.join(index_list)

	# Store the final result
	result = index_string

	# Display the final value
	print('result = {}'.format(result))

	return result