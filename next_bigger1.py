# https://www.codewars.com/kata/next-bigger-number-with-the-same-digits/train/python

def next_bigger(n):
	import itertools

	# Print the arguments
	print('n = {}'.format(n))

	# Define default result as -1
	result = -1

	# Convert the number to a list of digits
	numbers = [int(d) for d in str(n)]
	print('numbers = {}'.format(numbers))

	# Create a list of permutations
	perms = [int(''.join([str(d) for d in p])) for p in itertools.permutations(sorted(numbers))]
	# print('perms = {}'.format(perms))

	# Compare original number against all permutations
	for p_number in perms:
		if p_number > n:
			result = p_number
			break

	print('result = {}'.format(result))

	return result