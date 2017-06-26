def getCount(inputStr):
	# Display argument values
	print('inputStr'.format(inputStr))

	# Count all the vowels
	vowel_count = 0					# Start counting with 0 vowels
	for letter in inputStr:			# For each letter from the input string
		if (letter in 'aeiou'):		# If the letter is a vowel, then
			vowel_count += 1		# Increment the vowel count by 1

	return vowel_count