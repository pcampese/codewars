# https://www.codewars.com/kata/roman-numerals-encoder/train/python

def solution(n):
	# Print the arguments
	print('n = {}'.format(n))
	print

	format_structure = []		# List of lists to store format stracture: [['X', <count>], ['V', <count>], ...]

	# Calculate for roman numerals
	for n in xrange(1000, 5000+1):		# This for loop is just for testing all the numbers.  Remove this from the for loop later
		result = []		# Store the final roman numeral result
		print('n = {}'.format(n))		# Show the current number

		# Calculate the I's -- 1
		numI = n % 5					# Do modulo 5, since we want to look at the I's

		if (numI == 4):		# If the modul result is 4, then we just want 1 roman numeral, before the  previous digit
			numI = -1		# Set it to '-1' to track the position, and we can use abs() to get the value/count
		print('numI = {}'.format(numI))	# Show the result of the modulo

		# Calculate the V's -- 5
		numV = n % 10					# Do modulo 10, since we want to look at the V's
		if (4 <= numV <= 8):
			numV = 1
		else:
			numV = 0
		print('numV = {}'.format(numV))	# Show the result of the modulo

		# Calculate the X's -- 10
		numX = n % 50					# Do modulo 10, since we want to look at the X's
		if (numX <= 8):
			numX = 0
		elif (9 <= numX <= 18):		# (0 * 10) + 0 <= (numX - 9) <= (0 * 10) + 9
			numX = 1
		elif (19 <= numX <= 28):	# (1 * 10) + 0 <= (numX - 9) <= (1 * 10) + 9
			numX = 2
		elif (29 <= numX <= 38):	# (2 * 10) + 0 <= (numX - 9) <= (2 * 10) + 9
			numX = 3
		elif (numX == 39):			# (numX - 9) == (3 * 10) + 0
			numX = 4
		elif (40 <= numX <= 48):	# (3 * 10) + 1 <= (numX - 9) <= (3 * 10) + 9
			numX = -1
		else:						# (numX - 9) == (4 * 10) + 0
			numX = -2
		print('numX = {}'.format(numX))	# Show the result of the modulo

		# Calculate the L's -- 50
		numL = n % 100					# Do modulo 100, since we want to look at the L's
		if (40 <= numL <= 89):
			numL = 1
		else:
			numL = 0
		print('numL = {}'.format(numL))	# Show the result of the modulo

		# Calculate the C's -- 100
		numC = n % 500					# Do modulo 10, since we want to look at the C's
		if (numC <= 89):
			numC = 0
		elif (90 <= numC <= 189):	# (0 * 100) + 0 <= (numC - 90) <= (0 * 100) + 99
			numC = 1
		elif (190 <= numC <= 289):	# (1 * 100) + 0 <= (numC - 90) <= (1 * 100) + 99
			numC = 2
		elif (290 <= numC <= 389):	# (2 * 100) + 0 <= (numC - 90) <= (2 * 100) + 99
			numC = 3
		elif (390 <= numC <= 399):	# (3 * 100) + 0 <= (numC - 90) <= (3 * 100) + 9
			numC = 4
		elif (400 <= numC <= 489):	# (3 * 100) + 10 <= (numC - 90) <= (3 * 100) + 99
			numC = -1
		else:						# (4 * 100) + 0 <= (numC - 90) <= (4 * 100) + 9
			numC = -2
		print('numC = {}'.format(numC))	# Show the result of the modulo

		# Calculate the D's -- 500
		numD = n % 1000					# Do modulo 1000, since we want to look at the D's
		if (400 <= numD <= 899):
			numD = 1
		else:
			numD = 0
		print('numD = {}'.format(numD))	# Show the result of the modulo

		# Calculate the M's -- 1000
		numM = n % 5000					# Do modulo 10, since we want to look at the M's
		if (numM <= 899):
			numM = 0
		elif (900 <= numM <= 1899):	# (0 * 1000) + 0 <= (numM - 900) <= (0 * 1000) + 999
			numM = 1
		elif (1900 <= numM <= 2899):	# (1 * 1000) + 0 <= (numM - 900) <= (1 * 1000) + 999
			numM = 2
		elif (2900 <= numM <= 3899):	# (2 * 1000) + 0 <= (numM - 900) <= (2 * 1000) + 999
			numM = 3
		elif (3900 <= numM <= 4899):	# (3 * 1000) + 0 <= (numM - 900) <= (3 * 1000) + 99
			numM = 4
		# elif (4900 <= numM <= 4899):	# (3 * 1000) + 10 <= (numM - 900) <= (3 * 1000) + 999
			# numM = -1
		# else:						# (4 * 1000) + 0 <= (numM - 900) <= (4 * 1000) + 99
			# numM = -2
		else:
			numM = 5
		print('numM = {}'.format(numM))	# Show the result of the modulo

		# Format the output
		# Format from largest to smallest

		# Format the M's
		# Insert all the negative numerals first
		if (numM < 0):	# We have an M to be used for subtraction
			result.insert(-1, 'M')
			numM = abs(numM + 1)	# Increment number of positive M's to add, take the ABS value
		if (numM >= 0):		# If we have M's
			result.extend(['M'] * numM)
		print('M: formatting result = {}'.format(''.join(result)))

		# Format the D's
		# Insert all the negative numerals first
		if (numD < 0):	# We have an D to be used for subtraction
			result.insert(-1, 'D')
			numD = abs(numD + 1)	# Increment number of positive D's to add, take the ABS value
		if (numD >= 0):		# If we have D's
			result.extend(['D'] * numD)
		print('D: formatting result = {}'.format(''.join(result)))

		# Format the C's
		# Insert all the negative numerals first
		if (numC < 0):	# We have an C to be used for subtraction
			result.insert(-1, 'C')
			numC = abs(numC + 1)	# Increment number of positive C's to add, take the ABS value
		if (numC >= 0):		# If we have C's
			result.extend(['C'] * numC)
		print('C: formatting result = {}'.format(''.join(result)))

		# Format the L's
		# Insert all the negative numerals first
		if (numL < 0):	# We have an L to be used for subtraction
			result.insert(-1, 'L')
			numL = abs(numL + 1)	# Increment number of positive L's to add, take the ABS value
		if (numL >= 0):		# If we have L's
			result.extend(['L'] * numL)
		print('L: formatting result = {}'.format(''.join(result)))

		# Format the X's
		# Insert all the negative numerals first
		if (numX < 0):	# We have an X to be used for subtraction
			result.insert(-1, 'X')
			numX = abs(numX + 1)	# Increment number of positive X's to add, take the ABS value
		if (numX >= 0):		# If we have X's
			result.extend(['X'] * numX)
		print('X: formatting result = {}'.format(''.join(result)))

		# Format the V's
		# Insert all the negative numerals first
		if (numV < 0):	# We have an V to be used for subtraction
			result.insert(-1, 'V')
			numV = abs(numV + 1)	# Increment number of positive V's to add, take the ABS value
		if (numV >= 0):		# If we have V's
			result.extend(['V'] * numV)
		print('V: formatting result = {}'.format(''.join(result)))


		# Format the I's
		# Insert all the negative numerals first
		if (numI < 0):	# We have an I to be used for subtraction
			result.insert(-1, 'I')
			numI = abs(numI + 1)	# Increment number of positive I's to add, take the ABS value
		if (numI >= 0):		# If we have I's
			result.extend(['I'] * numI)
		print('I: formatting result = {}'.format(''.join(result)))

		print

	# Join the final result
	result = ''.join(result)
	# Show the final result
	print('result = {}'.format(result))

	return result