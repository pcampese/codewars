# https://www.codewars.com/kata/simple-pig-latin/train/python

def pig_it(text):
	# Print arguments
	print('text = {}'.format(text))

	# Split the text into words
	words = text.split()
	print('words = {}'.format(words))

	# Save the final list of pig latin words
	pig_words = []

	# Loop through the word list and make then into pig latin words
	for word in words:
		if (word.isalpha()):
			# Only convert the word to pig latin if it's letters only
			word = word[1:] + word[0] + 'ay'
		pig_words.append(word)

	# Put it back into text
	pig_text = ' '.join(pig_words)

	# Set the final result
	result = pig_text

	# Display the final value
	print('result = {}'.format(result))

	return result