def solution(number):
	# Display the arguments provided
	print('number = [{}]'.format(number))

	# Extract all the numbers that are multiples of 3 or 5
	result = 0										# Define variable to hold an initial empty value
	for number in xrange(1, number):				# Iterate over the number range: 1 to (number - 1)
		if (number % 3 == 0 or number % 5 == 0):	# If number is divisible by 3 or 5, then
			result += number						# Add that number to the rolling total

	print('result = [{}]'.format(result))

	return result