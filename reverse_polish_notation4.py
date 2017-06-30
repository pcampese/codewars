# https://www.codewars.com/kata/reverse-polish-notation-calculator/train/python

def calc(expr):
	import re		# For regex
	import operator	# For doing operations

	# Print the arguments
	print('expr = <{}>'.format(expr))

	# Put the expression into a list
	expr_list = expr.split()

	# Define the operations
	operation_of = {
		'+': operator.add,	# Addition
		'-': operator.sub,	# Subtraction
		'*': operator.mul,	# Multiplication
		'/': operator.div	# Division
	}

	# Define the regex string for the operators
	pattern = '|'.join([re.escape(op) for op in operation_of.keys()])

	# Get the list of operators in the expression
	operator_list = [op.group() for op in re.finditer(pattern, expr)]
	print('operator_list = <{}>'.format(operator_list))
		# 

	# Evaluate the expression appropriately
	if (not expr_list):					# If it's an empty expression
		result = 0.0					# Answer = 0
	elif (len(operator_list) == 0):			# If there's no valid operator found
		result = float(expr_list[-1])	# Answer = last number in the expression
	elif (len(expr_list) >= 3):		# Valid expression if it has 3 or more elements
		# It's valid - lets do math
		print('expr_list = <{}>'.format(expr_list))
		print('Starting calculation...')
		for op in operator_list:				# For each operation that exists in the expression
			index = expr_list.index(op) - 2		# Get the index of that operator.  Use -2, since all valid operations are in 3's. Elements shift left as they pop from left.
			num1 = float(expr_list.pop(index))	# Get the 1st number
			num2 = float(expr_list.pop(index))	# Get the 2nt number (same index since 1st number is popped)
			expr_list.pop(index)				# Pop the expression, don't save - since we already have it (same index since 2nd number is popped)

			# Do the math
			operation = operation_of[op]
			op_result = operation(num1, num2)

			# Insert the result back into the expression list
			expr_list.insert(index, op_result)
			print('Calculation complete')
			print('expr_list = <{}>'.format(expr_list))
			print
		result = expr_list[0]

	# Convert final number to int, if appropriate
	if result.is_integer():
		result = int(result)

	# Print final result
	print('result = {}'.format(result))

	return result