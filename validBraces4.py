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
			if (not closing or (c != closing.pop())):	# If we're looking at a letter, but the closing list is empty or doesn't match what we expect
				print('closing is empty')
				result = False
				break
			else:
				print('all seems OK')
				result = True
		print
	print

	# Make sure all the closing brackets have been used
	if (closing):
		result = False

	print('result = {}'.format(result))

	return result