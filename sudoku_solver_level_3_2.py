# https://www.codewars.com/kata/sudoku-solver/train/python

def sudoku(puzzle):
	import collections

	# Print arguments
	print_board(puzzle)

	# Flatten the puzzle, from list of lists to a single list of numbers
	flat_board = [number for row in puzzle for number in row]

	# Count all the numbers that are currently populated on the sudoku board
	number_count = collections.Counter(flat_board)

	# Convert that count of all numbers on the board, into a dictionary
	number_count = dict(number_count)

	# Count of the number of zeros in the sudoku board
	if 0 in number_count:
		# If the number 0 appears in the sudoku board, then get the count
		zero_count = number_count[0]
	else:
		# If the number 0 is not in the sudoku board, then set the count to zero
		zero_count = 0

	# Do the main work if there are zero's.  Otherwise, stop and return itself.
	if (zero_count > 0):
		# Get the missing numbers for all the rows
		rows_missing_numbers = check_rows(puzzle)

		# Rotate the board 90 degrees, so that the columns turn into rows.  This
		# allows us to check the columns using the same function
		rotated_board = list(reversed(zip(*puzzle)))

		# Get the missing numbers for all the columns
		columns_missing_numbers = list(reversed(check_rows(rotated_board)))

		# Validate all the inner 3x3 boards

		grid_missing_numbers = []

		# Step 1: Split the rows into 3 columns
		# 	Break up the 9x9 board into 3 9x3 boards
		# 	(i.e. split up all the rows into 3 parts)
		split_board = []							# Contains original board with all rows split into 3 parts
		for row in puzzle:							# Go through each row in the board
			split_row = [row[s_index:s_index+3] for s_index in xrange(0, len(row), 3)]
			# Break it down:
				# split_row = []							# 
				# for s_index in xrange(0, len(row), 3):	# s_index to define where to split the row (every 3 numbers)
					# row_section = row[s_index:s_index+3]	# Get the sub-row (of length 3) from the original row
					# split_row.append(row_section)			# Append that sub-row list to a new list containing the all 3 sub-rows
			split_board.append(split_row)			# Append "row that is split into 3 lists/rows" as a single row into the split board matrix

		# Step 2: Split the columns into 3 rows
		# 	Converts the 9x3 boards into 3x9 boards (i.e. split up all the columns into 3 parts)
		# 	Technically, we're putting the 9 rows from the 9x3 board into a single row with 9 1x3 rows
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

		# Replace all zero's on the board with their solution
		board = replace_zero(puzzle, rows_missing_numbers, columns_missing_numbers, grid_missing_numbers)

		# Call itself recursively to continue solving any unsolved squares.
		sudoku(board)

	return puzzle

# Loops through puzzle board replacing 0's with a solution, as long as it has a
# single, valid solution.  If a 0 has multiple possible solutions, then it
# leaves the 0 untouched
def replace_zero(puzzle, rows_missing_numbers, columns_missing_numbers, grid_missing_numbers):

	# Define how to map 
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

	# Loop through the entire board
	for row in xrange(9):
		for column in xrange(9):
			if (puzzle[row][column] == 0):
				# Determine which row the 0 is in
				if (0 <= row <= 2):
					grid_row = 0
				elif (3 <= row <= 5):
					grid_row = 1
				elif (6 <= row <= 8):
					grid_row = 2

				# Determine which column the 0 is in
				if (0 <= column <= 2):
					grid_column = 0
				elif (3 <= column <= 5):
					grid_column = 1
				elif (6 <= column <= 8):
					grid_column = 2

				# Concatenate the row and column positions to for a unique key
				grid_key = '{}{}'.format(grid_row, grid_column)

				# Determine which 3x3 board the grid key maps to
				grid = grid_mapping[grid_key]

				# Intersect the 3 lists (converted into sets) to get the common
				# numbers from all lists (ie. numbers that exist in all 3 lists)
				missing_numbers = list(
					set.intersection(
						set(rows_missing_numbers[row]),
						set(columns_missing_numbers[column]),
						set(grid_missing_numbers[grid])))

				# If there's only 1 missing number, replace that 0 with the
				# missing number
				if (len(missing_numbers) == 1):
					puzzle[row][column] = missing_numbers[0]

	return puzzle

# Returns which numbers (of the range 1-9) are missing from the provided row
def check_rows(board):
	# Define the list of required numbers
	required_numbers = range(1,9+1)

	# List of missing numbers for all rows in the board
	missing_numbers = []

	# Default result
	result = True

	# Validate all rows
	for row in board:
		# Make a new copy of the 'required numbers to check' for each row
		numbers_to_check = required_numbers[:]

		for number in row:
			if (number in numbers_to_check):
				# This number hasn't been seen yet.  Now that we see it, remove
				# it from the list
				numbers_to_check.remove(number)

		# Append this rows missing numbers into the missing numbers list
		missing_numbers.append(numbers_to_check)

	return missing_numbers

# Print the board, pretty
def print_board(board):
	import pprint

	print('-- print_board --')
	pprint.pprint(board)