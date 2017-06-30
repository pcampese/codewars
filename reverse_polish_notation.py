# https://www.codewars.com/kata/reverse-polish-notation-calculator/train/python

def calc(expr):
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
		pattern = ''
		# Find the first valid operator
#		operation = min([expr_list.index(op) for op in operation_list])
		for op inoperation_list:
			
		print('operation = <{}>'.format(operation))

	# Convert final number to int, if appropriate
	if result.is_integer():
		result = int(result)

	# Print final result
	print('result = {}'.format(result))

	return result