# https://www.codewars.com/kata/pyramid-slide-down/train/python

def longest_slide_down(pyramid):
	# Print arguments
	# print('pyramid (ugly) = {}'.format(pyramid))
	# print_pyramid(pyramid)
	# print

	# Assume it's the smallest pyramid possible
	# [[1], [2, 3]] == [ [1],  ==   1
	#                  [2, 3]]    2   3
	if (len(pyramid) == 2):
		# There are exactly 2 rows in the pyramid
		# print('...There are exactly 2 rows in the pyramid...')
		largest = max(pyramid[1])
		# print('largest = {}'.format(largest))
		result = pyramid[0][0] + largest
		# print('result = pyramid[0][0] + largest = {} + {} = {}'.format(pyramid[0][0], largest, result))
	else:
		# The pyramid is too big, lets break it down
		# print('...The pyramid is too big, lets break it down...')
		# Get the left side of the smaller pyramid
		# Remove the top row
		# Remove the last element from each row
		# print('...Generate the "left" sub-pyramid...')
		pyramid_left = []
		for row in pyramid[1:]:
			pyramid_left.append(row[:-1])
		# print_pyramid(pyramid_left)
		# print
		# print('-- Call longest_slide_down for pyramid_left: Start --')
		result_left = longest_slide_down(pyramid_left)
		# print('-- Call longest_slide_down for pyramid_left: End --')
		# print('result_left = {}'.format(result_left))
		# print

		# Get the right side of the smaller pyramid
		# Remove the top row
		# Remove the last element from each row
		# print('...Generate the "right" sub-pyramid...')
		pyramid_right = []
		for row in pyramid[1:]:
			pyramid_right.append(row[1:])
		# print_pyramid(pyramid_right)
		# print
		# print('-- Call longest_slide_down for pyramid_right: Start --')
		result_right = longest_slide_down(pyramid_right)
		# print('result_right = {}'.format(result_right))
		# print('-- Call longest_slide_down for pyramid_right: End --')
		# print

		# Put the "left" result into the bottom left corner
		# print('...Put the "left" result into the bottom left corner...')
		# pyramid[-2][0] = result_left
		pyramid[1][0] = result_left

		# Put the "right" result into the bottom right corner
		# print('...Put the "right" result into the bottom right corner...')
		# pyramid[-2][-1] = result_right
		pyramid[1][1] = result_right

		# Remove the bottom row of the pyramid
		# print('...Remove the bottom row of the pyramid...')
		# print('...before...')
		# print_pyramid(pyramid)
		pyramid = pyramid[:2]
		# print('...after...')
		# print_pyramid(pyramid)

		# print('-- Call longest_slide_down for combined: Start --')
		result = longest_slide_down(pyramid)
		# print('-- Call longest_slide_down for combined: End --')
		# result = max(result_left, result_right)
		# print('result = max(result_left, result_right) = max({}, {}) = {}'.format(result_left, result_right, result))

	# print('result = {}'.format(result))
	return result

def print_pyramid(pyramid):
	# Determine the width for center spacing
	# width = "# of digits" + "# of spaces"
	#						  "# of spaces" = "# of digits" - 1
	width = (len(pyramid[-1]) * 2) -1

	# Loop through each row, printing the row, center justified
	for row in pyramid:
		row_string = ' '.join([str(element) for element in row])
		print(row_string.center(width, ' '))