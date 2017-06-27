def dig_pow(n, p):
	# Print arguments
	print('n = number = {}'.format(n))
	print('p = power = {}'.format(p))

	# Calculate the digits to their powers
	sum = 0
	for base_power, digit in enumerate(str(n)):
		exponent = base_power + p
		print('{} ** {}'.format(digit, exponent))
		sum = (int(digit) ** exponent) + sum
		
	# Display the sum
	print('sum = {}'.format(sum))

	return -1