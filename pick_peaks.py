# https://www.codewars.com/kata/pick-peaks/train/python

def pick_peaks(arr):
	# Print arguments
	print('arr = {}'.format(arr))

	# Store the list of valid peaks and indexes
	peaks = {
		'pos'  : [],
		'peaks': []
	}

	# At least 3 elements are required for a peak to exist
	if (len(arr) >= 3):
		# The first possible peak is the 2nd element of the array
		possible_peak_index = 1
		possible_peak_value = arr[possible_peak_index]

		# Plateu data
		plateu_index = None
		plateu_value = None

		# Loop through the array, searching for a peak
		#	Start at 1, to ignore the 1st element (which cannot be a peak)
		#	End at len()-1 to ignore the last element (which cannot be a peak)
		for possible_peak_index in xrange(1,len(arr)-1):

			# Get the possible peak value
			possible_peak_value = arr[possible_peak_index]

			# Look around to see what's before and after the potential peak
			lookback = arr[possible_peak_index-1]
			lookahead = arr[possible_peak_index+1]

			# Test if it's a peak value
			if (possible_peak_value > lookback and
				possible_peak_value > lookahead):
				# It's larger than the numbers surrounding it
				peaks['pos'].append(possible_peak_index)
				peaks['peaks'].append(possible_peak_value)

			# Test for possible plateau
			if (possible_peak_value > lookback and
				  possible_peak_value == lookahead):
				# We have a small number followed by 2 of the same number, so
				# this could be the start of a plateu
				plateu_index = possible_peak_index
				plateu_value = possible_peak_value
			elif (possible_peak_value == plateu_value and
				  possible_peak_value > lookahead):
				# The plateu is valid, and it is completed - lets save it.
				peaks['pos'].append(plateu_index)
				peaks['peaks'].append(plateu_value)

				# Reset the plateu values.
				plateu_index = None
				plateu_value = None

			elif (possible_peak_value > plateu_value):
				# There is no plateu.  Reset the values
				plateu_index = None
				plateu_value = None

	# Print the final results
	print(peaks)

	return peaks