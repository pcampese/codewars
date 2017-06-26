# https://www.codewars.com/kata/jaden-casing-strings/train/python

def toJadenCase(text):
	import string

	return string.capwords(text) # Capitalizes the first letter of each word