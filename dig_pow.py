# https://www.codewars.com/kata/playing-with-digits/train/python

def dig_pow(n, p):
	# Print arguments
	print('n = number = {}'.format(n))
	print('p = power = {}'.format(p))

	# Calculate the digits to their powers
	sum = 0											# Variable to hold the rolling sum
	for base_power, digit in enumerate(str(n)):		# Convert the number to a string.  Enumerate iterates and returns index too.
		exponent = base_power + p					# Exponent we want is the digit's index + argument 'p'
		sum = (int(digit) ** exponent) + sum		# Add digit ** exponent to the rolling sum

	# Find a divisor for this sum
	if (sum % n == 0):		# If the sum is divisible by the argument 'n', that was passed
		result = sum / n	# Then the answer is the sum divided by the argument 'n'
	else:					# Otherwise
		result = -1			# Then return '-1'

	print('result = {}'.format(result))

	return result