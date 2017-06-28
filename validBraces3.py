# https://www.codewars.com/kata/valid-braces/train/python

def validBraces(braces):
	# Print the arguments
	print('braces = -->{}<--'.format(braces))

	# Create dictionary to map closing brace to opening brace
	closing_brace_of = {
		'{' : '}',
		'[' : ']',
		'(' : ')',
	}

	# Create lists to contain the closing braces
	closing = []

	# Go through each character.  If you see an opening brace, add the corresponding closing brace to the list
	result = None
	for c in braces:
		print('Looking at c = [{}]'.format(c))
		if c in closing_brace_of:
			print('[{}] is in an opening bracket'.format(c))
			closing.append(closing_brace_of[c])
			print('closing = {}'.format(closing))
		else:
			print('[{}] is in a closing bracket'.format(c))
			if (closing):		# If the list of closing braces is not empty
				print('The closing list is NOT empty: {}'.format(closing))
				popped = closing.pop()	# Get the most recently added closing brace
				print('popped = {}'.format(popped))
				if (c == popped):		# If the one we're verifying matches
					print('==> TRUE')
					result = True		# Then we're still good
				else:					# If the one we're verifying does NOT match
					result = False		# Then we have a problem
					break
			else:						# We want to verify a letter, but our closing braces list is empty
				print('==> FALSE')
				result = False			# Then we have a problem
				break
			### Method 2
			# print('[{}] is in a closing bracket'.format(c))
			# print('closing = {}'.format(closing))
			# print('not closing = {}'.format(not closing))
			# if (closing):
				# popped = closing.pop()
			# else:
				# popped = None
			# print('popped = {}'.format(popped))
			# if (c == popped):
				# print('Set result = TRUE')
				# result = True
			# else:
				# print('Set result = FALSE')
				# result = False
				# break
			### Method 1
			# if (closing):
				# print('[{}] is NOT in {}'.format(c, closing_brace_of))
				# popped = closing.pop()
				# print('popped = {}'.format(popped))
				# if (c != popped):
					# print('[{}] does NOT equal {} ==> FALSE'.format(c, popped))
					# result = False
					# break
				# else:
					# print('[{}] does equal {} ==> TRUE'.format(c, popped))
					# result = True
			# else:
					# result = False
		print
	print

	# Make sure all the closing brackets were used, if not - then it's False
	print('Check if braces is empty: closing = {}'.format(closing))
	if (closing):
		result = False

	print('result = {}'.format(result))

	return result