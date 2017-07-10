# https://www.codewars.com/kata/regex-password-validation/train/python
# Reference: http://www.rexegg.com/regex-lookarounds.html#password

# regex = '\A(?=[a-zA-Z0-9]{6,}\Z)(?=.*[a-z])(?=.*[A-Z])(?=.*\d).*'

regex = (""
		"(?=.*[a-z])"		# Look ahead for any char followed by a lowercase
		"(?=.*[A-Z])"		# Look ahead for any char followed by a uppercase
		"(?=.*\d)"			# Look ahead for any char followed by a digit
		"^[a-zA-Z0-9]{6,}$"	# Match at least 6 alphanumeric characters
		"")