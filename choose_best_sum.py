# https://www.codewars.com/kata/best-travel/python

def choose_best_sum(max_distance, count, distance_list):
	# Use the 'combinations' itertool: https://docs.python.org/2/library/itertools.html#itertools.combinations
	from itertools import combinations
    
	# Create a list of all combinations from the 'distance_list' that are a combination of 3 elements
	combo_list = list(combinations(distance_list, count))

	# Store the best set so far.  Default is type 'None'
	best = None		

	# Loop through all the tuples in the combo_list, and pick the best one
	for combo in combo_list:					# For each combination tuple
		combo_sum = sum(combo)					# Sum the values in that tuple
		if (best < combo_sum <= max_distance):	# If the sum is better than the best one so far, but less than the max_distance
			best = combo_sum					# Then, take that one to be the best

	return best