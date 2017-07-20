# https://www.codewars.com/kata/nesting-structure-comparison/train/python

def same_structure_as(original,other):
	print('-=: same_structure_as: Start :=-')
	print

	# Print the arguments
	print('original = {}'.format(original))
	print('other = {}'.format(other))
	print

	# Store the final result
	result = True

	# Verify that they are both lists
	if (isinstance(original, list) and 
		isinstance(other, list)):
		# Yes, they are both lists
		# Verify the lists have the same length
		if (len(original) == len(other)):
			# Yes, both lists have the same length
			for index in xrange(len(original)):
				element_original = original[index]
				element_other = other[index]
				result = same_structure_as(element_original, element_other)
				if (result == False):
					break
		else:
			result = False
	elif (isinstance(original, list) or
		  isinstance(other, list)):
		result = False

	print('Final: result = {}'.format(result))

	return result