# https://www.codewars.com/kata/sudoku-solver/train/python

def sudoku(puzzle):
	import collections

	print('=== in sudoku ===')

	# Print arguments
	print_board(puzzle)

	# Count the numbers that are currently populated on the sudoku board
	number_count = collections.Counter(number for row in puzzle for number in row)
	number_count = dict(number_count)
	print_dict(number_count)

	if 0 in number_count:
		zero_count = number_count[0]
	else:
		zero_count = 0
	print('zero_count = {}'.format(zero_count))

	if (zero_count > 0):


		# Get the missing numbers for all the rows
		rows_missing_numbers = check_rows(puzzle)
		print('-- rows_missing_numbers --')
		# print_board(rows_missing_numbers)

		# Rotate the board to check the columns
		rotated_board = list(reversed(zip(*puzzle)))
		# print('-- Rotated Board --')
		# print_board(rotated_board)

		# Get the missing numbers for all the columns
		columns_missing_numbers = list(reversed(check_rows(rotated_board)))
		print('-- columns_missing_numbers --')
		# print_board(columns_missing_numbers)

		# Validate all the inner 3x3 boards

		grid_missing_numbers = []

		# Step 1: Split the rows into 3 columns
		# 	Break up the 9x9 board into 3 9x3 boards (i.e. split up all the rows into 3 parts)
		split_board = []							# Contains original board with all rows split into 3 parts
		for row in puzzle:							# Go through each row in the board
			single_row = [row[s_index:s_index+3] for s_index in xrange(0, len(row), 3)]
			# Break it down:
				# single_row = []							# 
				# for s_index in xrange(0, len(row), 3):	# s_index to define where to split the row (every 3 numbers)
					# split_row = row[s_index:s_index+3]	# Get the sub-row (of length 3) from the original row
					# single_row.append(split_row)			# Append that sub-row list to a new list containing the all 3 sub-rows
			split_board.append(single_row)			# Append "row that is split into 3 lists/rows" as a single row into the split board matrix

		# Rotate the board
		# Step 2: Split the columns into 3 rows
		# Converts the 9x3 boards into 3x9 boards (i.e. split up all the columns into 3 parts)
		# Technically, we're putting the 9 rows from the 9x3 board into a single row with 9 1x3 rows
		rotated_board = list(zip(*split_board))		# Rotate the board, so we can work on the columns as if they were rows

		# Split the board again
		# Break up the 3 3x9 boards into 9 3x3 boards
		for row in rotated_board:														# For each row in the rotated board
			for s_index in range(0, len(row), 3):										# Define the an index to split the columns on (step by 3)
				inner_board = row[s_index:s_index+3]									# Every 3 1x3 sub-rows in this row define the inner 3x3 matrix
				single_row = [[digit for row_3x3 in inner_board for digit in row_3x3]]	# Convert the 3x3 matrix into a single nested list [[1, ..., 9]], so we can check it
				# Break it down:
					# for row_3x3 in inner_board:			# 
					#	for digit in row_3x3:				# 
					#		single_row[0].append(digit)		# 
				grid_missing_numbers.append(*check_rows(single_row))
		print('-- grid_missing_numbers --')
		# print_board(grid_missing_numbers)

		# Loop through the puzzle board, until we find a '0'

		# Count of zeros

		print('-- Looking for a 0 --')
	
		board = replace_zero(puzzle, rows_missing_numbers, columns_missing_numbers, grid_missing_numbers)
		print('-- (replaced) board --')
		print_board(board)
		sudoku(board)
	else:
		return puzzle


	print_board(puzzle)


	return puzzle

def replace_zero(puzzle, rows_missing_numbers, columns_missing_numbers, grid_missing_numbers):

	print('-- in replace_zero --')

	grid_mapping = {
		'00': 0, 
		'01': 3, 
		'02': 6, 
		'10': 1, 
		'11': 4, 
		'12': 7, 
		'20': 2, 
		'21': 5, 
		'22': 8, 
		}

	for row in xrange(9):
		for column in xrange(9):
			# print('zero_count = {}'.format(zero_count))
			if (puzzle[row][column] == 0):
				# print('row = {}'.format(row))
				# print('column = {}'.format(column))

				# Determine which grid the 0 is in
				# Determine the row
				if (0 <= row <= 2):
					grid_row = 0
				elif (3 <= row <= 5):
					grid_row = 1
				elif (6 <= row <= 8):
					grid_row = 2

				# Determine the column
				if (0 <= column <= 2):
					grid_column = 0
				elif (3 <= column <= 5):
					grid_column = 1
				elif (6 <= column <= 8):
					grid_column = 2
					
				grid_key = '{}{}'.format(grid_row, grid_column)
				grid = grid_mapping[grid_key]

				# print('grid row, column = ({}, {} --> {})'.format(grid_row, grid_column, grid_key))
				# print('rows_missing_numbers[{}]: {}'.format(row, rows_missing_numbers[row]))
				# print('columns_missing_numbers[{}]: {}'.format(column, columns_missing_numbers[column]))
				# print('grid_missing_numbers[{}]: {}'.format(grid, grid_missing_numbers[grid]))
				# print

				# Intersect the 3 lists to get the common numbers from all lists
				missing_numbers = list(set.intersection(set(rows_missing_numbers[row]), set(columns_missing_numbers[column]), set(grid_missing_numbers[grid])))
				# print('missing_numbers = {}'.format(missing_numbers))

				# If there's only 1 missing number, put it into the original
				# puzzle, and re-run the loop
				if (len(missing_numbers) == 1):
					print('++ Replacing these numbers ++')
					print('missing_numbers = {}'.format(missing_numbers))
					print('row = {}'.format(row))
					print('column = {}'.format(column))

					puzzle[row][column] = missing_numbers[0]
					# zero_count -= 1
					# print_board(puzzle)
				# print

	return puzzle

def check_rows(board):
	# Define the list of required numbers
	required_numbers = range(1,9+1)

	# List of missing numbers for all rows in the board
	missing_numbers = []

	# Default result
	result = True

	# Validate all rows
	for row in board:
		# print('Row: <{}>'.format(row))
		numbers_to_check = required_numbers[:]
		for number in row:
			if number == 0:
				continue
			elif number in numbers_to_check:		# If the number we're checking hasn't been seen yet
				numbers_to_check.remove(number)	# Them remove it from the remaining numbers to check
			else:								# Otherwise, we're seeing a number we do not expect
				print('???')
		missing_numbers.append(numbers_to_check)
		# print('--> numbers_to_check = <{}>'.format(numbers_to_check))
		# print

	return missing_numbers

def print_board(board):
	print('-- print_board --')
	for row in board:
		print row

def print_dict(my_dict):
	for key in sorted(my_dict):
		print('{}: {}'.format(key, my_dict[key]))