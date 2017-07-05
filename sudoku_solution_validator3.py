# https://www.codewars.com/kata/sudoku-solution-validator/train/python

def validSolution(board):
	# Print arguments (formatted)
	print('board = ')
	for b in board:
		print('{},'.format(b))
	print

	# Default result
	result = True

	# Validate all rows
	if (not check_rows(board)):		# If the row check fails
		result = False				# Then then it fails

	# Validate all columns
	rotated_board = list(reversed(zip(*board)))		# Rotate the board counterclockwise
	if (not check_rows(rotated_board)):				# If the row check fails
		result = False								# Then it fails

	# Validate all the inner 3x3 boards
	# Step 1: Split the rows into 3 columns
	# 	Break up the 9x9 board into 3 9x3 boards (i.e. split up all the rows into 3 parts)
	split_board = []							# Contains original board with all rows split into 3 parts
	for row in board:							# Go through each row in the board
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
			if (not check_rows(single_row)):	# If the row validation fails
				result = False					# then it all fails
				break							# stop, get out

	print('result = {}'.format(result))

	return result

# Method to verify all rows in a column
def check_rows(board):
	# Define the list of required numbers
	required_numbers = range(1,9+1)

	# Default result
	result = True

	# Validate all rows
	for row in board:
		numbers_to_check = required_numbers[:]
		for number in row:
			if number in numbers_to_check:		# If the number we're checking hasn't been seen yet
				numbers_to_check.remove(number)	# Them remove it from the remaining numbers to check
			else:								# Otherwise, we're seeing a number we do not expect
				result = False					# Answer = False
				break
		if numbers_to_check:	# If, somehow, there's still numbers we never saw
			result = False		# Answer = False
			break				# Stop, get out

	return result