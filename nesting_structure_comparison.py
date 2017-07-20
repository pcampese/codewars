# https://www.codewars.com/kata/nesting-structure-comparison/train/python

def same_structure_as(original,other):
	print('-=: same_structure_as: Start :=-')

	# Print the arguments
	print('original = {}'.format(original))
	print('other = {}'.format(other))
	print

	print('type(original) = {}'.format(type(original)))
	print('type(other) = {}'.format(type(other)))
	print

	# Store the final result
	result = True

	# Loop through each element in the original
	print('-- Loop through each element in the original: Start -- ')
	for element in original:
		print('element = {}, type = {}'.format(element, type(element)))
	print('-- Loop through each element in the original: End -- ')
	print

	# Verify the length of the lists are the same
	print('-- Verify the length of the lists are the same: Start --')
	print('len(original) = {}'.format(len(original)))
	print('len(other) = {}'.format(len(other)))
	if (len(original) != len(other)):
		result = False
		print('-- Verify the length of the lists are the same: End --')
		print
	else:

		# Loop through using isinstance
		print('-- Loop through using isinstance: Start --')
		# for element in original:
		for index in xrange(len(original)):
			element_original = original[index]
			print('element_original = original[index] = original[{}] == {}'.format(index, element_original))

			element_other = other[index]
			print('element_other = other[index] = other[{}] == {}'.format(index, element_other))
			if (isinstance(element_original, list) and 
				isinstance(element_other, list)):
				print('List')
				result = True
				# Call Recursion
				print('-- Call Recursion: Start --')
				same_structure_as(element_original, element_other)
				print('-- Call Recursion: End --')
			elif (isinstance(element_original, list) or
				  isinstance(element_other, list)):
				print('NOT List')
				result = False
		print('-- Loop through using isinstance: End --')
		print

	print('-=: same_structure_as: Start :=-')

	return result