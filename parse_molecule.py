# https://www.codewars.com/kata/molecule-to-atoms/train/python

def parse_molecule (formula):
	import re			# Regex
	import collections	# To count stuff

	# Print arguments
	print('formula = {}'.format(formula))

	# PHASE 1 - Process the brackets
	# First, we need to process all the brackets.  We need to expand them out,
	# applying any number that exists to the right of the bracket to all
	# elements inside the bracket.  Essentially, convert (H2O)2 to H4O2.
	
	# While braces exist
	while (re.search('[\(\)\[\]\{\}]', formula) != None):
		# Match molcules in brackets, and everything before and after the match
		pattern = """
			# Match for round brackets
			(.*)	# Everything before the opening bracket
			\(		# The opening bracket
			(.+?)	# Everything inside the brackets, save in a group
			\)		# The closing bracket
			(\d*)	# Any numbers defined after the closing bracket
			(.*)	# Everything after the closing bracket
			|(.*)\[(.+?)\](\d*)(.*)		# Same as above, but for square brackets
			|(.*)\{(.+?)\}(\d*)(.*)		# Same as above, but for curly brackets
			"""

		# Match all the formula elements with brackets to work with
		match = re.search(pattern, formula, re.VERBOSE)

		# Capture/Break out the results of the search
		before = remove_none(match.group(1,5,9))
		formula_in_brackets = remove_none(match.group(2, 6, 10))
		count = remove_none(match.group(3, 7, 11))
		after = remove_none(match.group(4, 8, 12))

		# If no number is set to count, that that implies 1.  So, set it to 1
		if not count:
			count = 1

		# Expand out the formula that was in the brackets
		expanded_inner_formula = formula_in_brackets * int(count)

		# Merge the formula back together, replacing bracketed formula with
		# its' newly expanded version
		formula = before + expanded_inner_formula + after

	# PHASE 2 - Repeat all the individual elements
	# Next, we want to repeat all the elements based on the number that is
	# associated with them.  Basicaly, convert H4O2 to HHHHOO (4 H's and 2 O's)

	# This will store the expanded formula (i.e. H2O == HHO)
	expanded_formula = ""

	# Match a list of all the elements, and numbers that follow them
	element_list = re.finditer('([A-Z][a-z]?)(\d*)', formula)

	# For each match, repeat the element by the number of times in its number
	for element_set in element_list:
		element = element_set.group(1)
		count = element_set.group(2)

		# If there's no number, then it's implied to be 1, so set it to 1.
		if not count:
			count = 1

		# Expand out the elements by the number in 'count'
		expanded_formula += element * int(count)

	# Get a list of all the elements, from the expanded formula
	element_list = re.findall('[A-Z][a-z]?', expanded_formula)

	# Gather all the elements, and their count
	element_count = collections.Counter(list(element_list))

	# Set the final result
	result = element_count
	print('result = {}'.format(result))

	return result

# Function to extract the first element that is not 'None', from a list
def remove_none(array):
	for element in array:
		if element !=  None:
			return element