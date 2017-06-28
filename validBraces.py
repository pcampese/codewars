# https://www.codewars.com/kata/valid-braces/train/python

def validBraces(braces):
	# Print the arguments
	print('braces = -->{}<--'.format(braces))

	# Create dictionary to map closing brace to opening brace
	closing_brace_of = {
		'{' : '}',			# { }
		'[' : ']',			# [ ]
		'(' : ')',			# ( )
	}

	# Create a list to contain the closing braces for the opening braces we've seen so far
	closing = []

	# Go through each character.  If you see an opening brace, add the corresponding closing brace to the 'closing' list
	for c in braces:							# Look at all the braces in the string
		if c in closing_brace_of:				# If it's an opening brace: {, [, or (
			closing.append(closing_brace_of[c])	# Append its' closing brace to the 'closing' list
		else:									# Otherwise, we're looking at a closing brace
			if (closing and (c == closing.pop())):	# If there's a brace in the 'closing' list and the the most recent one matches
				result = True						# Then, we're good, so far (we still need to check until the end)
			else:									# Otherwise, either, no closing braces to check against, or they don't match
				result = False						# So, we have a problem
				break								# Stop here, no need to keep on checking

	# Make sure all the closing brackets have been used, for the case where only opening braces were provided
	if (closing):		# If the closing list is NOT empty (i.e. they haven't all been used)
		result = False	# Then it's a problem

	print('result = {}'.format(result))

	return result