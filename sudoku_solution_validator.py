# https://www.codewars.com/kata/sudoku-solution-validator/train/python

def validSolution(board):
	# Print arguments (formatted)
	print_board(board)

	# Default result
	result = True

	# Validate all rows
	print('-- Validate all rows --')
	if (not check_rows(board)):
		print('Row Validation Failed')
		result = False
	print

	# Validate all columns
	print('-- Validate all columns --')
	rotated_board = list(reversed(zip(*board)))		# Rotate the board
	if (not check_rows(rotated_board)):
		print('Column Validation Failed')
		result = False
	print

	print('-- 1. Break up the 9 x 9 board into 3 x 3 boards --')
	# Break up the 9 x 9 board into 3 x 3 boards
	# ...need to figure this one out
	split_board = []
	for row in board:
		row_1 = row[:3]
		row_2 = row[3:6]
		row_3 = row[6:]
		# print('Each new split row')
		# print('row_1 = <{}>'.format(row_1))
		# print('row_2 = <{}>'.format(row_2))
		# print('row_3 = <{}>'.format(row_3))
		split_board.append([row_1, row_2, row_3])
	print_board(split_board)
	print

	# Rotate the board
	rotated_board = list(reversed(zip(*split_board)))		# Rotate the board

	# Split the board again
	print('-- 2. Break up the 9 x 9 board into 3 x 3 boards --')
	split_board2 = []
	for row in rotated_board:
		row_1 = row[:3]
		row_2 = row[3:6]
		row_3 = row[6:]
		print('Each new split row')
		print('row_1 = <{}>'.format(row_1))
		print('row_2 = <{}>'.format(row_2))
		print('row_3 = <{}>'.format(row_3))
		split_board2.append([row_1, row_2, row_3])
	print_board(split_board2)

	# !!!!!!!!!!!!!!!!!!!!!!!!!!!!! Continue here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	# The solution is in the tuple
	first_3x3 = split_board2[0][0]
	print('1st 3x3 = split_board2[0] = {}'.format(first_3x3))
	sum = 0
	single_row = []
	for row in first_3x3:
		for digit in row:
			print ('digit = {}'.format(digit))
			single_row.append(digit)
	print
	check_rows(single_row)

	return result

def check_rows(board):
	# print_board(board)

	# Define the list of required numbers
	required_numbers = range(1,9+1)
	# print('required_numbers = <{}>'.format(required_numbers))

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

	return result

def print_board(board):
	print('board = ')
	for b in board:
		print(b)