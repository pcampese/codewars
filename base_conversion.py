# https://www.codewars.com/kata/base-conversion/train/python

# Fix the Sample Tests
# bin = Alphabet['BINARY']; oct = Alphabet['OCTAL']; dec = Alphabet['DECIMAL']; hex = Alphabet['HEXA_DECIMAL'];
# allow = Alphabet['ALPHA_LOWER']; alup = Alphabet['ALPHA_UPPER']; alpha = Alphabet['ALPHA']; alnum = Alphabet['ALPHA_NUMERIC'];

def convert(input, source, target):
	# Print the arguments
	print('--- Arguments ---')
	print('input = {}'.format(input))
	print('source = {}'.format(source))
	print('target = {}'.format(target))

	floor = True
	result = []
	sum = 0

	while (floor):
	# for i in xrange(3):
		divisor = len(target)
		if (len(target) < len(source)):
			input = int(input)
			floor = input // divisor
			modulo = input % divisor
			print('floor = {} // {} = {}'.format(input, divisor, floor))
			print('modulo = {} % {} = {}'.format(input, divisor, modulo))

			result.insert(0, modulo)
			input = floor
			print('result = {}'.format(result))
		else:
			input_string = list(input)
			print('input_string = {}'.format(input_string))

			# Walk through each digit from the input, and apply the value
			for digit in xrange(len(input_string)):
				input_digit = int(input_string[digit])
				print('input_digit = int(input_string[digit]) = int(input_string[{}]) = {}'.format(digit, input_digit))

				base_position_value = len(source) ** digit
				print('base_position_value = len(source) ** digit = len({}) ** {} = {}'.format(source, digit, base_position_value))

				sum += input_digit * base_position_value
				print('sum = input_digit * base_position_value = {} * {} = {}'.format(input_digit, base_position_value, sum))
			floor = False

		print

	result = ''.join([str(n) for n in result])
	print('result = {}'.format(result))

	return result