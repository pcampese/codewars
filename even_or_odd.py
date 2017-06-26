def even_or_odd(number):

	result = "Even"		# Assume the number is 'Even' by default
	if (number % 2):	# If the number is NOT divisible by 2, then
		result = "Odd"	# the number is odd
		
	return result