# http://www.codewars.com/kata/instant-runoff-voting/train/python

def runoff(voters):
	import collections
	import pprint

	# Print arguments
	print('voters =')
	pprint.pprint(voters)
	print

	# Get the total number of voters
	total_voters = len(voters)

	# Keep on looping until we have a majority
	while True:
		# Create a copy of the voters argument
		voters_copy = []

		# Flip the array on the diagonal to get a list sorted by voting order
		voting_order = [list(tuple) for tuple in zip(*voters)]

		# Verify we have a non-empty set of voting priorities
		if (not voting_order):
			result = None
			break

		# Count all the first place votes
		first_place_results = collections.Counter(voting_order[0])

		# Merge the candidate list and the first place voting list
		# If a candidate wasn't the first choice for any voter, then remove that
		# add that candidate into the tally, with count 0
		for candidate in voters[0]:
			if candidate not in first_place_results:
				first_place_results[candidate] = 0

		# Get the vote count of the candidate with the most votes
		most_votes_count = max(first_place_results.values())

		# Determine whether or not we have a majority voting result
		if (most_votes_count > (total_voters / 2)):
			# We have a majority
			result = first_place_results.most_common()[0][0]
			break

		# Get the count of the least common first place choice
		lowest_max_count = min(first_place_results.values())

		# Find all choices that have the lowest max count
		lowest_choices = []
		for (choice, vote_count) in first_place_results.iteritems():
			if (vote_count == lowest_max_count):
				lowest_choices.append(choice)

		# Remove all the lowest choices from the original votes
		for voter in voters:
			filtered_voting_list = [vote for vote in voter if vote not in lowest_choices]
			voters_copy.append(filtered_voting_list)

		voters = voters_copy

	# Print the final results
	print('result = {}'.format(result))

	return result