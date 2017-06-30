# https://www.codewars.com/kata/sudoku-solution-validator/train/python

def validSolution(board):
	# Print arguments (formatted)
	print('board = ')
	for b in board:
		print(b)
	print

	# Default result
	result = True

	# Validate all rows
	if (not check_rows(board)):
		print('Row Validation Failed')
		result = False

	# Validate all columns
	rotated_board = list(reversed(zip(*board)))
	if (not check_rows(rotated_board)):
		print('Column Validation Failed')
		result = False

	# Break up the 9 x 9 board into 3 x 3 boards
	# ...need to figure this one out
	

	return result

def check_rows(board):
	# Print arguments (formatted)
	print('board = ')
	for b in board:
		print(b)
	print

	# Define the list of required numbers
	required_numbers = range(1,9+1)
	print('required_numbers = <{}>'.format(required_numbers))

	# Default result
	result = True

	# Validate all rows
	for row in board:
		numbers_to_check = required_numbers[:]
		for number in row:
			# print('number = {}'.format(number))
			if number in numbers_to_check:		# If the number we're checking hasn't been seen yet
				numbers_to_check.remove(number)	# Them remove it from the remaining numbers to check
			else:								# Otherwise, we're seeing a number we do not expect
				print('FAIL: number:{} is not in numbers_to_check:{}'.format(number, numbers_to_check))
				result = False					# Answer = False
				break
		if numbers_to_check:				# If, somehow, there's still numbers we never saw
			print('FAIL: numbers_to_check should be empty: {}'.format(numbers_to_check))
			result = False						# Answer = False
			break
		print

	return result