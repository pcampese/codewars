# https://www.codewars.com/kata/stop-gninnips-my-sdrow/train/python

def spin_words(sentence):
	# Display arguments
	print('sentence = {}'.format(sentence))
	print

	# Conditional expression to split sentence into words, reverse the long ones, and join them back
	result = ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])

	# Break it down...exploded:
	# word_list = []						# List to contain words from sentence
	# for word in sentence.split():			# For each word in the sentence (split by spaces)
		# if (len(word) >= 5):					# If the word is 5 or more characters
			# # word = ''.join(reversed(word))	# Option 1: Reverse the word (returned as list).  Join it.
			# word = word[::-1]					# Option 2: Reverse using extended slice with negative step [begin:end:step].
		# word_list.append(word)			# Add the word to the list

	# # Merge all the words back together
	# result = ' '.join(word_list)

	# Print the final result
	print('result = {}'.format(result))

	return result