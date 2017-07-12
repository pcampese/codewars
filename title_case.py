# https://www.codewars.com/kata/title-case/train/python

def title_case(title, minor_words=''):
	import string

	# Print arguments
	print('title = {}'.format(title))
	print('minor_words = {}'.format(minor_words))
	print

	# Verify if a non-empty title was passed
	if (not title):
		result = ''
	else:
		# The title is NOT empty
		# Convert the provided arguments into lowercase lists
		title = title.lower().split()
		minor_words = minor_words.lower().split()

		# Store the new title with correct case
		new_title = []

		# Always uppercase the first letter of the first word
		new_title.append(string.capitalize(title[0]))

		# For all other words, capitalize first letter of word, unless the word
		# is in the 'minor_words' list (then leave it in all lowercase)
		for word in title[1:]:
			if (word not in minor_words):
				word = word.capitalize()
			new_title.append(word)

		# Store the final result
		result = ' '.join(new_title)

	# Display the final value
	print('result = {}'.format(result))

	return result