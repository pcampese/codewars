# https://www.codewars.com/kata/next-bigger-number-with-the-same-digits/train/python

def next_bigger(n):
	import itertools
	import random

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
	print('number_length = len(numbers) = {}'.format(number_length))
	print

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
		# test_number = list_to_int(numbers[:-2] + sorted(numbers[-2:], reverse=True))
		digit, remaining_digits = next_largest(numbers[-2:])
		test_number = list_to_int(numbers[:-2] + list(digit) + remaining_digits)
		print('test_number2 = {}'.format(test_number))

		if (test_number > n):
			print(''.format())
			result = test_number
		print

		# If the right 2 digits are already sorted,
	if (number_length >= 3 and result == -1):
		# 	Then find the smallest of the right 2 digits that is larger than the 3rd digit
		# digit, remaining_digits = next_largest(numbers[-3:])
		# test_number = list_to_int(list(digit) + remaining_digits)
		digit, remaining_digits = next_largest(numbers[-3:])
		test_number = list_to_int(numbers[:-3] + list(digit) + remaining_digits)
		print('test_number3 = {}'.format(test_number))

		if (test_number > n):
			result = test_number
		print

	if (number_length >= 4 and result == -1):
		# 	Then find the smallest of the right 2 digits that is larger than the 3rd digit
		# digit, remaining_digits = next_largest(numbers[-3:])
		# test_number = list_to_int(list(digit) + remaining_digits)
		digit, remaining_digits = next_largest(numbers[-4:])
		test_number = list_to_int(numbers[:-4] + list(digit) + remaining_digits)
		print('test_number4 = {}'.format(test_number))

		if (test_number > n):
			result = test_number
		print

	# Create 2 lists
	#	Outer list: goes right to left (reverse) (i.e. list[-1] to list[0])
	#	Inner list: goes left to right (forward) (i.e. list[index_of_outer_list] to list[len(list)])
	stop = 0	# Variable to define if we need to break out of the loop (1 = break out)

	# Determine if it's not the largest possible number already
	largest_possible_number = list_to_int(sorted(numbers, reverse=True))
	print('largest_possible_number = {}'.format(largest_possible_number))
	print

	if (n != largest_possible_number):
		for outer in xrange(len(numbers)-2, -1, -1):
			print('Right to left: outer = {} (== {})'.format(outer, numbers[outer]))

			search_in = numbers[outer:]
			print('search_in = {}'.format(search_in))

			digit, remaining_digits = next_largest(numbers[outer:])
			print('digit = {}'.format(digit))
			print('remaining_digits = {}'.format(remaining_digits))
			test_number = list_to_int(numbers[:outer] + list(digit) + remaining_digits)
			print('test_number_x = {}'.format(test_number))
			if (test_number > n):
				print('Answer is probably = {}'.format(test_number))
				result = test_number
				break
			print

			print

			# test_number = list_to_int(numbers[:-4] + list(digit) + remaining_digits)
			# for inner in xrange(outer+1, len(numbers)):
				# print('+ Left to right: inner = {} (== {})'.format(inner, numbers[inner]))
				
				# # If we found the correct answer, then we need to break all the way out
				# stop = random.choice([0,1])
				# print('stop = {}'.format(stop))
				# if (stop == 1):
					# print('......inner: time to break!')
					# break
			# # Check if we need to break the outer break
			if (stop == 1):
				print('...outer: time to break!')
				break

	print
	print('result = {}'.format(result))

	return result

#############
# Functions #
#############

def next_largest(array):
	# print('DDD --- start: next_largest --- DDD')
	# print('array = {}'.format(array))
	number = array[0]			# The number to check against - find the next largest from the first element in the list
	# print('number = {}'.format(number))
	next_largest = max(array)	# Assume the next largest number is the max number remaining in the array - pop it out
	# print('next_largest = {}'.format(next_largest))

	for n in array:
		# print('n = {}'.format(n))
		if (number < n < next_largest):
			# print('{} < {} < {}'.format(number, n, next_largest))
			next_largest = n
			# print('new next_largest = {}'.format(next_largest))

	del array[array.index(next_largest)]	# Remove the next largest array
	# print('array = {}'.format(array))
	array.sort()							# Sort the array
	# print('Final: array = {}'.format(array))
	# print('Final: next_largest = {}'.format(next_largest))

	# Return the next largest number, and the remaining array, with that next largest removed
	# print('DDD --- end: next_largest --- DDD')
	return (next_largest, array)

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