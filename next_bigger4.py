# https://www.codewars.com/kata/next-bigger-number-with-the-same-digits/train/python

def next_bigger(n):
	import itertools

	# Print the arguments
	print('n = {}'.format(n))

	# Define default result as -1
	result = -1

	# Convert the number to a list of digits
	numbers = list(str(n))
	print('numbers = {}'.format(numbers))

	# Save a permanent copy of the original numbers list
	numbers_vault = numbers[:]

	# Create next largest number
	# Start from right to left
	# Goal is to keep as many as the left most digits as possible, as they are and
	# for the right-most digits, sort as few as possible (sorted from low to high)
	# Current number sorted
	numbers_sorted = sorted(numbers)
	print('numbers_sorted = {}'.format(numbers_sorted))

	# Get the number length
	number_length = len(numbers)

	# Start from the right
	# If the right 2 digits can be sorted, do it - then that should be the answer
	# If the right 2 digits are already sorted,
	#	Then find the smallest of the right 2 digits that is larger than the 3rd digit
	#		Put that (minimally larger) digit into 3rd place.  Sort the remaining 2 digits from smallest to largest
	#	If the right 2 digits don't have anything that's slightly larger than the 3rd digit (i.e. the right 3 digits are sorted largest to smallest)
	#	Then repeat the process for the 4th digit...
	#		Then find the smallest of the right 3 digits that is larger than the 4th digit
	#			Put that (minimally larger) digit into 4th place.  Sort the remaining 3 digits from smallest to largest
	#		If the right 3 digits don't have anything that's slightly larger than the 4th digit (i.e. the right 4 digits are sorted largest to smallest)
	#		Then repeat the process for the 5th digit, etc...

	if (number_length >= 2):
		# Sort 2 digits on the right
		test_number = list_to_int(numbers[:-2] + sorted(numbers[-2:], reverse=True))
		print('test_number2 = {}'.format(test_number))

		if (test_number > n):
			result = test_number

		# If the right 2 digits are already sorted,
	if (number_length >= 3 and result == -1):
		# 	Then find the smallest of the right 2 digits that is larger than the 3rd digit
		digit, remaining_digits = next_largest(numbers[-3:])
		test_number = list_to_int(list(digit) + remaining_digits)
		print('test_number3 = {}'.format(test_number))

		if (test_number > n):
			result = test_number


	print('result = {}'.format(result))

	return result

def next_largest(array):
	number = array[0]			# The number to check against - find the next largest from the first element in the list
	next_largest = max(array)	# Assume the next largest number is the max number remaining in the array - pop it out

	for n in array:
		if (number < n < next_largest):
			next_largest = n

	del array[array.index(next_largest)]	# Remove the next largest array
	array.sort()							# Sort the array

	# Return the next largest number, and the remaining array, with that next largest removed
	return (n, array)

def swap(array, item1, item2):
	index_1 = array.index(item1)
	index_2 = array.index(item2)
	array[index_1], array[index_2] = array[index_2], array[index_1]

	return array

def shift_left(arr, index):
	print('Array = {}'.format(arr))
	print('Index = {}'.format(index))

	# element = arr.pop(index)
	# arr.insert(index - 1, element)
	arr.insert(arr[index-1], [arr[index]])
	del arr[index]

def list_to_int(numbers):
	return int(''.join([str(d) for d in numbers]))