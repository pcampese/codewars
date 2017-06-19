# https://www.codewars.com/kata/the-observed-pin/python

def get_pins2(observed):
    # Display the observed bin
    print('observed: [{}]'.format(observed))
	
	# Mapping list for which numbers are nearby for each digit
    digit_mapping = [
        ['0','8'],				# 0
        ['1','2','4'],			# 1
        ['1','2','3','5'],		# 2
        ['2','3','6'],			# 3
        ['1','4','5','7'],		# 4
        ['2','4','5','6','8'],	# 5
        ['3','5','6','9'],		# 6
        ['4','7','8'],			# 7
        ['0','5','7','8','9'],	# 8
        ['6','8','9'],			# 9
    ]
	
    list_of_lists = []	# List of lists to contain a list of numbers near each pin digit
	
    # Go through each digit digit in the observed pin and save the possible surrounding
	# digits around the observed digit (above, below, to the left, and to the right, and itself)
    for digit in observed:
        # Save the nearby_numbers to the list of lists, so that we can work on the next digit
        list_of_lists.append(digit_mapping[int(digit)])

    while (len(list_of_lists) >=2):		# While we still have nearby number lists to merge together
        # Get the individual lists that need to be merged
        list_a = list_of_lists.pop(0)	# Get the 1st list - nearby numbers from the next left-most digit
        list_b = list_of_lists.pop(0)	# Get the 2nd list - nearby numbers from the next left-most digit
        
        # Merge the 2 lists together, generating a string of 'ab', where a is from list_a, and b is from list_b
        big_list = [str(a) + str(b) for a in list_a for b in list_b]

        # Convert it to type <set>, which instantly removes duplicates.  Then back to a list.  And sorted.
        big_list = sorted(list(set(big_list)))
		
		# Insert the resulting 'big list' back into the beginning of the list of lists
		# so that it can be merged with any remaining numbers in the list of lists
        list_of_lists.insert(0,big_list)
    else:
		# Flatten the list and save each item in the list as type string
        flat_list = [item for inner_list in list_of_lists for item in inner_list]
    
    # Display the final return value
    print('return value = {}'.format(flat_list))
    
    return flat_list

def get_pins(observed):
    # Display the observed bin
    print('observed: [{}]'.format(observed))
	    
	# Convert the pin into a list if ints (from a string)
    observed_int_list = [int(d) for d in observed]
	
    list_of_lists = []	# List of lists to contain a list of numbers near each pin digit

    # Go through each digit digit in the observed pin and save the possible surrounding
	# digits around the observed digit (above, below, to the left, and to the right, and itself)
    for digit in observed_int_list:
        nearby_numbers= []    # List of numbers that are nearby
		
        # Special case for '0'
        if (digit == 0):
            nearby_numbers = [0, 8]
        else:
            # Itself
            nearby_numbers.append(digit)
        
            # Check number above
			# Do x - 3 because, example, 1 is above 4, so 4 - 3 = 1
            above = digit - 3		
            if (above >= 1):					# If it's valid on the keypad
                nearby_numbers.append(above)	# Append the above number to the nearby numbers list
        
            # Check number below
			# Do x + 3 because, example, 9 is below 6, so 6 + 3 = 9
            below = digit + 3
            if (4 <= below <= 9):				# If it's valid on the keypad
                nearby_numbers.append(below)	# Append the below number to the nearby numbers list
            elif (below == 11):					# Special case if digit == 8, since 0 is below 8
                nearby_numbers.append(0)		# Append the number 0 to the nearby numbers list
        
            # Left & Right
			# Do x + 3 so that doing modulo 3 on a row on the keypad will result in 0, 1, 2
			# We want to do modulo 3 to easily know where it's located on the keypad
            left_right = (digit - 1) % 3
            if (1 <= left_right <= 2):   	 		# There's a number to the left
                nearby_numbers.append(digit - 1)	# Append the number to the nearby numbers list
            if (0 <= left_right <= 1):				# There's a number to the right
                nearby_numbers.append(digit + 1)	# Append the number to the nearby numbers list
        
        # Save the nearby_numbers to the list of lists, so that we can work on the next digit
        list_of_lists.append(nearby_numbers)
                
    # Go through the list of lists (i.e. the list of nearby numbers for each digit) until all
	# the sub-lists (the nearby number lists) have been merged together
    while (len(list_of_lists) >=2):		# While we still have nearby number lists to merge together
        # Get the individual lists that need to be merged
        list_a = list_of_lists.pop(0)	# Get the 1st list - nearby numbers from the next left-most digit
        list_b = list_of_lists.pop(0)	# Get the 2nd list - nearby numbers from the next left-most digit
        
        # Merge the 2 lists together, generating a string of 'ab', where a is from list_a, and b is from list_b
        big_list = [str(a) + str(b) for a in list_a for b in list_b]

        # Convert it to type <set>, which instantly removes duplicates.  Then back to a list.  And sorted.
        big_list = sorted(list(set(big_list)))
		
		# Insert the resulting 'big list' back into the beginning of the list of lists
		# so that it can be merged with any remaining numbers in the list of lists
        list_of_lists.insert(0,big_list)
    else:
		# Flatten the list and save each item in the list as type string
        flat_list = [str(item) for inner_list in list_of_lists for item in inner_list]
    
    # Display the final return value
    print('return value = {}'.format(flat_list))
    
    return flat_list