# https://www.codewars.com/kata/range-extraction/train/python

def solution(arr):
	import pprint
	
	# Print arguments
	print('arr ='.format(arr))
	print

	# Get the length of the list
	length = len(arr)

	# First deal with it appropriately, depending on the length of the list
	if (length <= 2):
		# If the list is too short, there's nothing to do, so just return itself
		result = arr
	else:
		# The list is long enough to do some analysis
		# List to save the original list converted with the ranged numbers
		list_of_sequences = [[]]
		result = []

		# Walk through the list, comparing the current number against a range
		# buffer
		for number in arr:
			print('number = {}'.format(number))

			# Show the current list_of_sequences
			print('Starting point.  list_of_sequences =')
			pprint.pprint(list_of_sequences)

			# Check if it's the first number
			if (not list_of_sequences[-1]):
				print('  |--> Add it to a new list to work with')
				list_of_sequences[-1].append(number)
				print('list_of_sequences'.format(list_of_sequences))
				print
				continue
			else:
				# There's already something to work with
				print('list_of_sequences =')
				pprint.pprint(list_of_sequences)
				print


			# See if the number is exactly 1 + "most recent number"
			if (number == list_of_sequences[-1][-1] + 1):
				# Yes.  It's sequential
				print('YES.  Sequential')
				list_of_sequences[-1].append(number)
			else:
				# No.  It's not sequential.  Generate a new list
				print('NO.  Not sequential.')
				list_of_sequences.append([])
			print

			print('list_of_sequences = ')
			pprint.pprint(list_of_sequences)
			# number = arr[index]
			# lookahead1 = arr[index+1]
			# lookahead2 = arr[index+2]
			# print('[number] lookahead1 and 2: [{}] {} {}'.format(number,
																 # lookahead1,
																 # lookahead2))

			# # Check if the number with 2 lookaheads form a range
			# triple_range = [False for (a, b) in zip(xrange(number,number+3), arr[index:index+3]) if (a != b)]
			# if (False in triple_range):
				# # It is not a triple range
				# print('No.')
				# result += '{},'.format(number)
				# next()
			# else:
				# # It is a triple range
				# print('Yes.')
				# result += '{}-'.format(number)

			# print('  |--> result = {}'.format(result))
			# print

	result = 0

	# Print the final results
	print('result = {}'.format(result))

	return result