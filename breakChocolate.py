# https://www.codewars.com/kata/breaking-chocolate-problem/train/python

def breakChocolate(n, m):
	breaks = (n * m) - 1	# Calculate the number of breaks needed

	if (breaks < 0):	# If the number of breaks is -1, then one side has size = 0 (i.e. no chocolate!)
		result = 0		# Then, no breaks are needed
	else:				# Otherwise, there is some chocolate there
		result = breaks	# The answer is 'breaks' calculated earlier

	return result