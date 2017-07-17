# https://www.codewars.com/kata/recover-a-secret-string-from-random-triplets/train/python

def recoverSecret(triplets):
	import pprint

	# Print arguments
	print('triplets = ')
	pprint.pprint(triplets)
	print

	# Store the final phrase
	phrase = []

	# Rotate the triplets
	rotated = list(zip(*triplets))

	# Create a list of sets, used to find the first and last letters of the
	# secret word
	set_list = [set(row) for row in rotated]

	# Get the first letter, and put it in as the first letter in the phrase
	first = set_list[0] - set_list[1] - set_list[2]
	first = list(first)[0]
	phrase.append([first])

	# Get the last letter
	last = set_list[2] - set_list[0] - set_list[1]
	last = list(last)[0]

	# Continue to loop and decode the secret word, until we break from inside
	while True:
		# Find all letters that might come after the latest set of possible
		# letters.  We want to keep our "next options" stored in a set, since
		# we want to ensure no duplicates are added.
		next_options = set()
		for letter in phrase[-1]:
			for triplet in triplets:
				if (triplet[0] == letter):
					next_options.add(triplet[1])
				elif (triplet[1] == letter):
					next_options.add(triplet[2])

		# Convert the next possible options to a list, and append to the phrase.
		next_options = list(next_options)
		phrase.append(next_options)

		# Remove stuff from the current phrase if it exists in the
		# "next options" list.  Since we know it comes "next", that means it
		# cannot stay in the current phrase, so get rid of it.
		filtered_phrase = []
		for letter_list in phrase[:-1]:
			new_letter_list = [letter for letter in letter_list if letter not in phrase[-1]]
			filtered_phrase.append(new_letter_list)
		filtered_phrase.append(phrase[-1])
		phrase = filtered_phrase

		# Once the last letter in the phrase matches what we know should be the
		# last letter, get out.  We're done.
		if (phrase[-1] == [last]):
			break

	# Convert the final result into a string
	phrase = [letter_list[0] for letter_list in phrase]
	phrase = ''.join(phrase)

	# Show the phrase
	print('phrase = {}'.format(phrase))

	return phrase