# https://www.codewars.com/kata/title-case/train/python

def title_case(title, minor_words=None):
	import string

	# Print arguments
	print('title = {}'.format(title))
	print('minor_words = {}'.format(minor_words))
	print

	# Verify if a non-empty title was passed
	if (not title):
		print('Empty title: <{}>'.format(title))
		result = ''
	else:
		# The title is NOT empty
		# Convert the provided arguments into lists
		title = title.split()
		if (minor_words != None):
			minor_words = minor_words.split()
		print('title = {}'.format(title))
		print('minor_words = {}'.format(minor_words))
		print

		# Store the new title with correct case
		new_title = []

		# Always uppercase the first letter of the first word
		new_title.append(string.capitalize(title[0]))

		# For all other words, capitalize first letter of word, unless the word
		# is in the 'minor_words' list
		for word in title[1:]:
			if (word.lower in )
			if word not in minor_words:
				word = word.capitalize()
			new_title.append(word)

		# Store the final result
		result = ' '.join(new_title)

	# Display the final value
	print('result = {}'.format(result))

	return result