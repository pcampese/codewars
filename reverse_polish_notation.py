# https://www.codewars.com/kata/roman-numerals-encoder/train/python

# I'm not proud of what I've done here...

def solution(n):
	# Print the arguments
	print('n = {}'.format(n))

	roman_blueprint = []		# List of lists to store format structure: [[<letter>, <count>], ...]
	result = []		# Store the final roman numeral result

	# Calculate for roman numerals
	# Calculate the I's -- 1
	numI = n % 5					# Do modulo 5, since we want to look at the I's
	if (numI == 4):		# If the modul result is 4, then we just want 1 roman numeral, before the  previous digit
		numI = -1		# Set it to '-1' to track the position, and we can use abs() to get the value/count
	roman_blueprint.append(['I', numI])

	# Calculate the V's -- 5
	numV = n % 10					# Do modulo 10, since we want to look at the V's
	if (4 <= numV <= 8):
		numV = 1
	else:
		numV = 0
	roman_blueprint.append(['V', numV])

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
	roman_blueprint.append(['X', numX])

	# Calculate the L's -- 50
	numL = n % 100					# Do modulo 100, since we want to look at the L's
	if (40 <= numL <= 89):
		numL = 1
	else:
		numL = 0
	roman_blueprint.append(['L', numL])

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
	roman_blueprint.append(['C', numC])

	# Calculate the D's -- 500
	numD = n % 1000					# Do modulo 1000, since we want to look at the D's
	if (400 <= numD <= 899):
		numD = 1
	else:
		numD = 0
	roman_blueprint.append(['D', numD])

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
	else:
		numM = 5
	roman_blueprint.append(['M', numM])

	# Format the output
	# Format from largest to smallest

	for numeral, count in roman_blueprint[::-1]:
		if (count < 0):	# We have an M to be used for subtraction
			result.insert(-1, numeral)
			count = abs(count + 1)	# Increment number of positive M's to add, take the ABS value
		if (count >= 0):		# If we have M's
			result.extend([numeral] * count)

	# Join the final result
	result = ''.join(result)

	# Show the final result
	print('result = {}'.format(result))

	return result