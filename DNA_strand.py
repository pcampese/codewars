# https://www.codewars.com/kata/complementary-dna/train/python

def DNA_strand(dna):
	# Print arguments
	print('dna = {}'.format(dna))

	# Dictionary containing replacement characters
	base_pair = {
		'A': 'T',
		'T': 'A',
		'G': 'C',
		'C': 'G'}

	# # Loop through the privided dna strand and create the complementary side
	complementary_side = ''.join([base_pair[s] for s in dna])

	# Show final complementary side
	print('complementary_side = {}'.format(complementary_side))

	return complementary_side