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
	print

	result = []
	sum = 0
	divisor = len(target)

	# Determine which conversion method needs to be used.
	# 1. Target base is higher than source base
	# 2. Target base is lower than source base
	if (len(target) < len(source)):
		# Method 1: Target base is lower than source base
		# Steps:
		# 1. input % "target base" = "left most" digit
		# 2. input = input // "target base"
		# 3. Repeat
		floor = True

		while (floor):
			input = int(input)
			floor = input // divisor
			modulo = input % divisor
			print('floor = {} // {} = {}'.format(input, divisor, floor))
			print('modulo = {} % {} = {}'.format(input, divisor, modulo))

			result.insert(0, modulo)
			input = floor
			print('result = {}'.format(result))

		result = ''.join([str(n) for n in result])
	else:
		# Method 2: Target base is higher than source base
		input = up_to_base10(input, source)
		print('input = {}'.format(input))

		# Convert the base10 number to the target base
		input = list(str(input))
		while (True):
			if (sum > divisor):
				next_digit = target[sum // divisor]
			else:
				next_digit = target[sum]
			result.append(next_digit)
			modulo = input % divisor
			sum = modulo
			# if ()
			break

		result = str(sum)

	print('result = {}'.format(result))

	return result

def up_to_base10(number, source):
	number = list(number)
	# print('number = {}'.format(number))

	sum = 0

	for digit in xrange(len(number)-1, -1, -1):
		input_digit = int(number[digit])
		# print('input_digit = int(number[digit]) = int(number[{}]) = {}'.format(digit, input_digit))

		base_position_value = len(source) ** ((len(number) - 1) - digit)
		# print('base_position_value = len(source) ** ((len(number) - 1) - digit) = len({}) ** ((len({}) - 1) - {}) = {}'.format(source, number, digit, base_position_value))

		sum += input_digit * base_position_value
		# print('sum = input_digit * base_position_value = {} * {} = {}'.format(input_digit, base_position_value, sum))
		# print
	return sum