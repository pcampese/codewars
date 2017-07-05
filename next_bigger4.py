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

	# For length of 2
	if (number_length == 2):
		sorted_number = int(''.join([str(d) for d in sorted(numbers)]))
		if (sorted_number > n):
			result = sorted_number
		else:
			element = numbers.pop(1)
			print(element)
			numbers.insert(0, element)
			print(numbers)
			result = list_to_int(numbers)
			print(result)

	# For length of 3
	elif (number_length >= 3):
		numbers_on_right = next_bigger(list_to_int(numbers[1:]))
		if numbers_on_right >= 0:
			result = list(str(numbers_on_right))
			result.insert(0,numbers[0])
			result = list_to_int(result)

	print('result = {}'.format(result))

	return result

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