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

	print('source base = {}'.format(len(source)))
	print('target base = {}'.format(len(target)))
	print

	# # Convert input to source alphabet numbers
	# new_number = []
	# input_list = list(input)
	# for unit in input_list:
		# i = source.index(unit)
		# print('{} => {}'.format(unit, i))
		# new_number.append(source.index(unit))
		# print('new_number = {}'.format(new_number))
	# print('new_number = {}'.format(new_number))
	# input = ''.join([str(n) for n in new_number])
	# print('input = {}'.format(input))


	# If the source alphabet has letters, then convert it to pythons "standard"
	# type, where alphabet starts with 0-9, and then continues with the
	# alphabet
	if (not source.isdigit()):
		source_converted = source[:]
		# If the source alphabet has at least one alphabet character
		#	Literally: if the source is NOT all digits [0-9]
		print('{} has at least 1 alphabet character'.format(source))
		# Then do the conversion process
		for d in xrange(9, -1, -1):
			# Replace old letter with new digit, by shifting right and inserting
			source_converted = source_converted[:-1]		# Remove old digit at the end
			source_converted = str(d) + source_converted	# Append new digit to beginning
			print('source_converted = {}'.format(source_converted))

		# Convert input to new (converted) alphabet
		print('-- Convert input to new (converted) alphabet: Start --')
		new_input = ''
		for digit in input:
			print('digit = {}'.format(digit))
			source_index = source.index(digit)
			print('source_index = {}'.format(source_index))
			converted_digit = source_converted[source_index]
			print('converted_digit = {}'.format(converted_digit))
			new_input += converted_digit
			print('new_input = {}'.format(new_input))
		print('new_input = {}'.format(new_input))
		input = new_input
		print('-- Convert input to new (converted) alphabet: End --')

	# Convert to base 10 first
	source_base = len(source)
	print('source_base = {}'.format(source_base))

	current_number = int(input, source_base)
	print('current_number = {}'.format(current_number))
	print

	input = str(current_number)

	result = []
	sum = 0
	divisor = len(target)


	# Determine which conversion method needs to be used.
	# 1. Target base is higher than source base
	# 2. Target base is lower than source base
	# if (len(target) < 10):
	if (len(target) != 10):
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

			result.insert(0, target[modulo])
			input = floor
			print('result = {}'.format(result))
			print

		result = ''.join([str(n) for n in result])
	# elif (len(target) > 10):
		# # Method 2: Target base is higher than source base
		# input = up_to_base10(input, source)
		# print('input = {}'.format(input))

		# # Convert the base10 number to the target base
		# input = list(str(input))
		# while (True):
			# if (sum > divisor):
				# next_digit = target[sum // divisor]
			# else:
				# next_digit = target[sum]
			# result.append(next_digit)
			# modulo = input % divisor
			# sum = modulo
			# # if ()
			# break

		# result = str(sum)
	else:
		result = input

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