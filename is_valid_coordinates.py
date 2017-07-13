# https://www.codewars.com/kata/coordinates-validator/train/python

def is_valid_coordinates(coordinates):
	import re

	# Print arguments
	print('coordinates = {}'.format(coordinates))
	print

	pattern = ('\A'							# Anchor at beginning of string
			   '-?'							# Negative number is possible
			   '(\d|[0-8]\d|90)'			# 0 (and 00) to 90
			   '(\.\d*)?'					# Optional decimal with number
			   ', '							# Next coordinate
			   '-?'							# Negative number is possible
			   '(\d|\d\d|1[0-7]\d|180)'		# 0 - 180
			   '(\.\d*)?'					# Optional decimal with number
			   '\Z')						# Anchor at end of string

	# Check the coordinate against the pattern
	if (re.search(pattern, coordinates)):
		result = True
	else:
		result = False

	# Print the final results
	print('result = {}'.format(result))

	return result