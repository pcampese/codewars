# https://www.codewars.com/kata/nesting-structure-comparison/train/python

def same_structure_as(original,other):
	# Print the arguments
	print('original = {}'.format(original))
	print('other = {}'.format(other))
	print

	# Store the final result
	result = True

	# Verify that they are both lists and they have the same length
	if (isinstance(original, list) and 
		isinstance(other, list)    and
		len(original) == len(other)):
		# Yes, they are both lists with the same length
		# Now, check each element within the list
		for index in xrange(len(original)):
			element_original = original[index]
			element_other = other[index]

			# Recursively check the elements
			result = same_structure_as(element_original, element_other)
			if (result == False):
				break
	elif (isinstance(original, list) or
		  isinstance(other, list)):
		# One is a list, but the other is not a list
		result = False

	print('Final: result = {}'.format(result))

	return result