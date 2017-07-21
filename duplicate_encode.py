# https://www.codewars.com/kata/duplicate-encoder/train/python

def duplicate_encode(word):
	import collections

	# Print arguments
	print('word = {}'.format(word))

	# Final result
	result = ''

	# Normalize the case to lowercase
	word = word.lower()

	# Get a count of all the letters in the word
	letter_count = dict(collections.Counter(word))

	for letter in word:
		if (letter_count[letter] == 1):
			result += '('
		else:
			result += ')'

	# Print final result
	print('result = {}'.format(result))

	return result