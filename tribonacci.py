# https://www.codewars.com/kata/tribonacci-sequence/train/python

def tribonacci(signature, n):
	# Print arguments
	print('signature = {}'.format(signature))
	print('n = {}'.format(n))

	# The final tribonacci sequence.  Start with the provided signature.
	# If n is less than 3, then [:n] will shorten it
	tribonacci = signature[:n]

	# Create the tribonacci sequence, as long as n >= 4
	for i in xrange(3, n):
		next = tribonacci[i-3] + tribonacci[i-2] + tribonacci[i-1]
		tribonacci.append(next)

	# Display the final value
	print('tribonacci = {}'.format(tribonacci))

	return tribonacci