# https://www.codewars.com/kata/isograms/train/python

def is_isogram(word):
	# Print arguments
	print('word = {}'.format(word))

	# Store the final result, default is False
	result = False

	# Make it all lowercase and sorted
	word = sorted(list(word.lower()))

	# Make it a set, to make all elements unique, and sorted
	word_set = sorted(set(word))

	if (word == word_set):
		result = True

	print('result = {}'.format(result))
	return result