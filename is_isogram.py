# https://www.codewars.com/kata/next-bigger-number-with-the-same-digits/train/python

def next_bigger(n):
	# Print the arguments
	print('n = {}'.format(n))

	# Define default result as -1
	result = -1

	# Convert the number to a list of digits
	numbers = list(str(n))

	# Determine what the largest possible number is
	largest_possible_number = list_to_int(sorted(numbers, reverse=True))

	# Loop through each digit, from right to left, continuously making the number larger, until we find the next largest one
	if (n != largest_possible_number):									# If the number is NOT already the largest possible number
		for i in xrange(len(numbers)-2, -1, -1):						# Iterate in reverse over indexes for the length of number
			# Break it down:
			#	Start = len(numbers) - 2: Want at least 2 numbers to work with(i.e. swap). If statement guarantee's we have 2 numbers
			#	Stop = -1: Want to stop at the first element of the list.  So, 0 - 1, since the stop is not inclusive
			#	Step = -1: Want to go in reverse
			digit, remaining_digits = next_largest(numbers[i:])			# Get the next largest digit in position i, and remaining numbers
			test_number = list_to_int(numbers[:i] + digit + remaining_digits)		# Glue the numbers together, make it an int
			# Break it down:
				# numbers[:i] = The numbers we haven't touched
				# digit = the next largest number that's larger than numbers[i], from searching through numbers[i:]
				# remaining_digits = all the numbers from numbers[i:], with 'digit' removed

			if (test_number > n):		# If the new number we want to test is larger than the original number
				result = test_number	# Then this is our answer
				break					# Break out of the loop

	print
	print('result = {}'.format(result))

	return result

#############
# Functions #
#############

# For a list of digits, searches within itself for the next largest digit from the number in list[0].
# Returns: (a) The next largest digit and (b) a list of all other digits
def next_largest(array):
	current_number = array[0]			# The number to check against - find the next largest from the first element in the list
	next_largest = max(array)	# Assume the next largest number is the max number remaining in the array - pop it out

	for n in array:									# For each number in the array
		if (current_number < n < next_largest):		# If number is larger than current_number, but less than next_largest
			next_largest = n						# Then make it the next_largest number

	del array[array.index(next_largest)]	# Remove the next largest number from the array
	array.sort()							# Sort the array
	next_largest = list(next_largest)		# Make the next_largest number a list

	return (next_largest, array)

# Convert a list of numbers to an int
def list_to_int(list_of_numbers):
	return int(''.join([str(d) for d in list_of_numbers]))