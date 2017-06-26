def tacofy(word):
	# Display arguments provided
	print('word = [{}]'.format(word))

	# Create the empty taco first, with default taco shells on both ends
	taco = ['shell', 'shell']

	# Process each letter in the word provided.
	for letter in word.lower():		# Normalize all letters to lowercase
		if (letter in 'aeiou'):
			ingredient = 'beef'
		elif (letter == 't'):
			ingredient = 'tomato'
		elif (letter == 'l'):
			ingredient = 'lettuce'
		elif (letter == 'c'):
			ingredient = 'cheese'
		elif (letter == 'g'):
			ingredient = 'guacamole'
		elif (letter == 's'):
			ingredient = 'salsa'
		else:			# If the letter doesn't match the ingredient list
			continue	# Then don't add any ingredients, and go to next letter

		# Add the ingredient into the taco, at the end, just before the last element (taco shell)
		taco.insert(-1, ingredient)
		
	# Display our scrumptious taco
	print('taco = {}'.format(taco))

	return taco