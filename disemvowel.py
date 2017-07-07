# https://www.codewars.com/kata/disemvowel-trolls/train/python

def disemvowel(string):
	# Print the arguments
	print('string = {}'.format(string))

	# If the lowercase version of the letter is NOT a vowel, then keep it
	# Return that consonant, put it into a list
	# Join the list without any spaces.  This is the final answer
	result = ''.join([letter for letter in string if letter.lower() not in 'aeiou'])

	print('result = {}'.format(result))

	return result