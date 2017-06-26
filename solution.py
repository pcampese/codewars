def solution(string,markers):
	import re # For using re.split
	
	# Display passed variables
	print('string = [{}]'.format(repr(string)))		# Use repr() to represent newline as '\n'
	print('markers = [{}]'.format(markers))
	print

	# Create the 'splitting pattern' to use in re.split().  Use re.escape() to auto-escape characters, as needed
	pattern = '|'.join([re.escape(m) for m in markers])

	# Parse the list with the provided markers, and return them in a list
	processed = [re.split(pattern, line)[0].rstrip() for line in string.split('\n')]
		# Below: without list comprehension (and exploded in general)
		#
		# line_list = string.split('\n')			Split 'string' on newline
		# processed = []							List to contain results from processing the string with markers
		# for line in line_list:					For each element in that split string (i.e. each newline)
		#	 split_line = re.split(pattern, line)	Split the newline on the markers
		#	 split_line = split_line[0]				Keep only whatever is before the marker
		#	 split_line = split_line.rstrip()		Remove any whitespace at the end
		#	 processed.append(split_line)			Add the result to the processed list

	# Prepare the final result.  Join each separate newline with the newline character '\n'
	result = '\n'.join(processed)
	print('result = [{}]'.format(repr(result)))		# Use repr() to represent newline as '\n'

	return result