# https://www.codewars.com/kata/reverse-polish-notation-calculator/train/python

def calc(expr):
	import re		# For regex
	import operator	# For doing operations

	# Print the arguments
	print('expr = <{}>'.format(expr))

	# Put the expression into a list
	expr_list = expr.split()
	print('expr_list = <{}>'.format(expr_list))

	# Define a list of valid operators
	operation_list = ['+', '-', '*', '/']

	# Count the number of operators in the expression
	operator_count = sum([expr_list.count(op) for op in operation_list])
	print('operator_count = <{}>'.format(operator_count))

	# Check for an empty expression
	if (not expr_list):				# If it's an empty expression
		result = 0.0					# Answer = 0
	elif (operator_count == 0):		# If there's no valid operator found
		result = float(expr_list[-1])		# Answer = last number
	elif (len(expr_list) >= 3):		# Valid expression if it has 3 or more elements
		# It's valid - lets do math
		# Define the regex string for the operators
		pattern = '|'.join([re.escape(op) for op in operation_list])
		print('pattern = <{}>'.format(pattern))
		print

		# Find the first valid operator
#		operation = min([expr_list.index(op) for op in operation_list])

		# Find the first operator using regex
		search_result = re.search(pattern, expr)
		operation = search_result.group()

		# Convert the string into a list, split on spaces
			# I'd like to find a way to a void this, if possible...
		expr = expr.split()

		# Get the index of the operator
		operation_index = expr.index()

		# Get the numbers and operator and then remove them from the expression
		num1 = float(expr.pop(operation_index - 2))	# Get 1st number
		num2 = float(expr.pop(operation_index - 2))	# Get 2nd number (it's in the same position as num1, since it was popped)
		expr.pop(operation_index - 2)			# Pop operation (it's in the same position as num1, since it was popped).  No need to keep, already have it.

		print('operation = <{}>'.format(operation))
		print('operation_index = <{}>'.format(operation_index))

	# Convert final number to int, if appropriate
	if result.is_integer():
		result = int(result)

	# Print final result
	print('result = {}'.format(result))

	return result