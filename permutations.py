# https://www.codewars.com/kata/permutations/train/python

def permutations(text):
	import itertools

	# Get all permutations, saved as a list
	perms = list(itertools.permutations(text))

	# Remove duplicates
	perms = set(perms)

	# Merge elements in each permutation to a string
	perm_list = [''.join(p) for p in perms]

	return perm_list