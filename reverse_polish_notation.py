# https://www.codewars.com/kata/reverse-polish-notation-calculator/train/python

def calc(expr):
	import re		# For regex
	import operator	# For doing operations

	# Print the arguments
	print('expr = <{}>'.format(expr))

	# Define the operations
	operation_of = {
		'+': operator.add,	# Addition
		'-': operator.sub,	# Subtraction
		'*': operator.mul,	# Multiplication
		'/': operator.div	# Division
	}

	# Put the expression into a list
	expr_list = [e if (e in operation_of.keys()) else float(e) for e in expr.split()]
		# expr.split(): Convert the reverse polish notation to a list, split on spaces
		# For each element in the expression, if it's operator, return back that same operator
		# Otherwise, it's a number, so return a float version of that number

	# Define the regex string for the operators
	pattern = '|'.join([re.escape(op) for op in operation_of.keys()])

	# Get the list of operators in the expression
	operator_list = [op.group() for op in re.finditer(pattern, expr)]
		# finditer returns an iterator of MatchObject; 1 MatchObject element for each operator found
		# For each MatchObject element (i.e. operator) found, use group() to get the search result (i.e. the operator we did find)
		# Save it in a list of objects

	# Evaluate the expression appropriately
	if (not expr_list):					# If it's an empty expression
		result = 0.0					# Answer = 0 (use 0.0 so it'll work with the float/int check at the end)
	elif (not operator_list):			# If there's no valid operator found
		result = expr_list[-1]			# Answer = last number in the expression
	elif (len(expr_list) >= 3):			# Valid expression if it has 3 or more elements
		# It's valid - lets do math
		for op in operator_list:				# For each operation that exists in the expression
			index = expr_list.index(op) - 2		# Get the index of that operator.  Use -2, since all valid operations are in 3's. Elements shift left as they pop from left.
			num1 = expr_list.pop(index)			# Get the 1st number
			num2 = expr_list.pop(index)			# Get the 2nt number (same index since 1st number is popped)
			expr_list.pop(index)				# Pop the expression, don't save - since we already have it (same index since 2nd number is popped)

			# Do the math
			operation = operation_of[op]		# Select which operation we need to do, from the dictionary
			op_result = operation(num1, num2)	# Perform the operation

			# Insert the result back into the expression list
			expr_list.insert(index, op_result)

		result = expr_list[0]					# Answer is the final number that remains

	# Convert final number to int, if appropriate
	if result.is_integer():
		result = int(result)

	# Print final result
	print('result = {}'.format(result))

	return result