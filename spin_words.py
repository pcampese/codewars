# https://www.codewars.com/kata/human-readable-duration-format/train/python

def format_duration(seconds):
	import math

	# Display passed arguments
	print('seconds = [{}]'.format(seconds))

	# Define fixed time units (based on seconds)
	f_seconds = 1				# 1 second = 1 second
	f_minutes = 60				# 1 minute = 60 seconds
	f_hours = 60 * f_minutes	# 1 hour = 60 minutes
	f_days = 24 * f_hours		# 1 day = 24 hours
	f_years = 365 * f_days		# 1 year = 365 days

	# Calculate the time sets.  Start largest to smallest
	fixed_unit_values = [f_years, f_days, f_hours, f_minutes, f_seconds]	# A list containing the fixed time units

	# Loop through the time units to calculate the time value of the input provided: [years, days, hours, minutes, seconds]
	time_values = []											# Create empty list to store the result
	for unit in fixed_unit_values:								# For each time unit
		(fractional, number) = math.modf(float(seconds) / unit)	# Divide the 'seconds' by the time unit, split
		seconds = fractional * unit
		time_values.append(int(number))

	# Fix the last time value (i.e. seconds).  Add the number & fractional and round up
	# Due to math.modf() returning floats, we may end up with 17.999999 or 18.0000001 seconds.  We'd want 18 seconds.
	time_values[-1] = int(round(number + fractional))

	# Merge the formatted list with the time values.  The result will be list of lists: [[unit, value], ...]
	time_formatted = [['year'], ['day'], ['hour'], ['minute'], ['second']]
	for index, value in enumerate(time_values):
		time_formatted[index].append(value)

	# Remove units that have a zero value (written as: keep only if value is non-zero)
	time_formatted = [time_value for time_value in time_formatted if time_value[1]]

	# Adjust pluralization
		# List comprehension: iterate through all the (unit, value) pairs in time_formatted
		# If the value is greater than 1, then it needs to be pluralized, return the same (unit, value) pair, as a list, 
		# but with an 's' appended to the unit.  Otherwise, just return the same [unit, value] pair that came in
	time_formatted = [[unit + 's', value] if (value >= 2) else [unit, value] for (unit, value) in time_formatted]

	# Print the output
	# Iterate through the list in reverse to build (as needed), example:
		#                              "2 seconds"
		#                 "1 minute and 2 seconds"
		#         "4 days, 1 minute and 2 seconds"
		# "1 year, 4 days, 1 minute and 2 seconds"
	# Use list(enumerate(reversed(time_formatted))) to return index value with list element
	result = 'now'				# Set default result value to 'now' for case when zero-value input is provided
	for index, (unit, value) in list(enumerate(reversed(time_formatted))):
		if (index == 0):		# If it's the right-most item
			result = '{} {}'.format(value, unit)
		elif (index == 1):		# If it's the 2nd item from the right
			result = '{} {} and {}'.format(value, unit, result)
		else:					# If it's the 3rd (or more) item from the right
			result = '{} {}, {}'.format(value, unit, result)

	# See what final result is
	print('result = {}'.format(result))

	return result