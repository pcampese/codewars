# https://www.codewars.com/kata/pyramid-slide-down/train/python

def longest_slide_down(pyramid):
	import pprint

	# Print arguments
	pprint.pprint(pyramid)
	print_pyramid(pyramid)

	return 0

def print_pyramid(pyramid):
	spacing = ''

	for row in reversed(pyramid):
		print('{}{}'.format(spacing, row))
		spacing += ' '