# https://www.codewars.com/kata/sudoku-solution-validator/train/python

def validSolution(board):
	# Print arguments (formatted)
	print('-- Initial board --')
	print_board(board)
	print

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
	print('Split Board:')
	print_board(split_board)
	print

	# Rotate the board
	rotated_board = list(reversed(zip(*split_board)))		# Rotate the board
	print('Rotated Board...')
	print_board(rotated_board)

	# Split the board again
	print('-- 2. Break up the 9 x 9 board into 3 x 3 boards --')
	for row in rotated_board:
		row = list(row)
		for s_index in xrange(0, len(row), 3):
			inner_board = row[s_index:s_index+3]
			single_row = [[digit for row in inner_board for digit in row]]
				# for row in inner_board:
				#	for digit in row:
				#		single_row[0].append(digit)
			print('+++ single_row = {}'.format(single_row))
			check_rows(single_row)

	return result

def check_rows(board):
	print_board(board)

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