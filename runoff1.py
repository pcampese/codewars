# http://www.codewars.com/kata/instant-runoff-voting/train/python

def runoff(voters):
	import collections
	import pprint

	# Print arguments
	# print('voters = {}'.format(voters))
	print('voters =')
	pprint.pprint(voters)
	print

	# Keep on looping until we have a majority
	while True:
		print('++ LOOP ++')

		# Create a copy of the voters argument
		voters_copy = []

		# Flip the array on the diagonal to get a list sorted by voting order
		voting_order = [list(tuple) for tuple in zip(*voters)]
		print('voting_order =')
		pprint.pprint(voting_order)
		print

		# Verify we have a non-empty set of voting priorities
		if (not voting_order):
			print('Voter list is empty!')
			result = None
			break

		# Count all the first place votes
		first_place_results = collections.Counter(voting_order[0])
		print('first_place_results = {}'.format(first_place_results))
		print

		# Merge the candidate list and the first place voting list
		candidate_results = {}
		for candidate in voters[0]:
			if candidate in first_place_results:
				candidate_results[candidate] = first_place_results[candidate]
			else:
				candidate_results[candidate] = 0
		first_place_results = collections.Counter(candidate_results)

		# Get the count of the most common first place choice
		first_max_count = max(first_place_results.values())
		print('first_max_count = {}'.format(first_max_count))
		print

		total_candidates = len(voting_order[0])
		if (first_max_count > (total_candidates / 2)):
			# We have a majority
			result = first_place_results.most_common()[0][0]
			print('We have a majority'.format(result))
			break
		else:
			# We do not have a majority
			print('We DO NOT have a majority')
		print

		# Get the count of the least common first place choice
		lowest_max_count = min(first_place_results.values())
		print('lowest_max_count = {}'.format(lowest_max_count))
		print

		# Find all choices that have the lowest max count
		lowest_choices = []
		for (choice, vote_count) in first_place_results.iteritems():
			if (vote_count == lowest_max_count):
				lowest_choices.append(choice)
		print('lowest_choices = {}'.format(lowest_choices))
		print

		# Remove all the lowest choices from the original votes
		for voter in voters:
			# print('voter = {}'.format(voter))
			filtered_voting_list = [vote for vote in voter if vote not in lowest_choices]
			# print('filtered_voting_list = {}'.format(filtered_voting_list))
			voters_copy.append(filtered_voting_list)

		print('voters_copy =')
		pprint.pprint(voters_copy)
		print

		voters = voters_copy

	# Print the final results
	print('result = {}'.format(result))

	return result