# https://www.codewars.com/kata/where-my-anagrams-at/train/python

#############
# Attempt 1 #
#############
def anagrams(word, word_list):
	# Define an empty anagram_list to contain the valid anagram words
	anagram_list = []

	# Go through each word in the word_list (the ones we want to check) - call it 'test_word'
	for test_word in word_list:
		# Make a copy of the word we want to make an anagram FROM, so it resets for each new word we test
		buffer = list(word)	# Make that buffer a list, so it's iterable
		is_anagram = True	# Set the default value to being an anagram

		for letter in test_word:			# For each letter in the word we are checking
			# If the buffer still has letters remaining AND
			# If the letter exists in the buffer, it still has potential for being an anagram
			if (buffer and letter in buffer):		
					buffer.remove(letter)	# Remove the letter from the buffer, since each letter can only be used once
			else:							
				# Not an anagram, since the letter we're checking doesn't exist in the buffer
				# Either because the buffer is empty or because it's an "invalid" letter
				is_anagram = False			# Set anagram to False
		if (is_anagram and not buffer):		# If it's an anagram AND all letters in the buffer have been used
			anagram_list.append(test_word)	# It's a valid anagram, append it to the anagram_list
	
	return anagram_list
	
##########################################
# Attempt 2 - After seeing the solutions #
##########################################
def anagrams2(word, word_list):
	anagram_list = []
	for test_word in word_list:
		if sorted(word) == sorted(test_word):
			anagram_list.append(test_word)
	return anagram_list