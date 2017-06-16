# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

def get_pins(observed):
    # Display the observed bin
    print('observed: [{}]'.format(observed))
    
    observed_int_list = [int(d) for d in observed]
    list_of_lists = []
    nearby_numbers= []    # List of numbers that are nearyby

    # Go through each observed pin
    for digit in observed_int_list:
        print('digit = [{}]'.format(digit))
        
        # Save the possible surrounding digits around the observed digit (above, below, to the left, and to the right, and itself)
        # Itself
        nearby_numbers.append(digit)
        print('1. nearby_numbers = {}'.format(nearby_numbers))
        
        # Check number above
        above = digit - 3
        if (above >= 1):
            nearby_numbers.append(above)
        print('2. nearby_numbers = {}'.format(nearby_numbers))
        
        # Below
        below = digit + 3
        if (below <= 9):
            nearby_numbers.append(below)
        elif (below == 11):
            nearby_numbers.append(0)
        print('3. nearby_numbers = {}'.format(nearby_numbers))
        
        # Left & Right
        left_right = (digit - 1) % 3
        if (left_right >= 1):    # There's a number to the left
            nearby_numbers.append(digit - 1)
        if (left_right <= 1):    # There's a number to the right
            nearby_numbers.append(digit + 1)
        print('4. nearby_numbers = {}'.format(nearby_numbers))
        
        # Save the nearby_numbers to a list of lists
        list_of_lists.append(nearby_numbers)
        print('list_of_lists = {}'.format(list_of_lists))
        
    # !!!!!!!!!!!!!!!!!!!!!!!!!!
    # Need to fix this
    # Once all the lists in lists are used, in goes from being a list of lists to a list of elements
    # So the length starts counting the number of total elements, instead of the counting the number of lists in the list
    # Might want to convert this to a dictionary of lists
    # Unless I can find a way to detect if it's a list of lists...
    while (len(list_of_lists) >=2):
        # Get the individual lists that need to be merged
        list_a = list_of_lists.pop(0)
        list_b = list_of_lists.pop(0)
        
        # Merge the 2 lists together, generating a string of 'ab', where a is from list1, and b is from list2
        big_list = [str(a) + str(b) for a in list_a for b in list_b]

        # Convert it to type <set>, to remove duplicates.  Then back to a list.  And sorted
        big_list = sorted(list(set(big_list)))
        
        print('big_list = {}'.format(big_list))
        nearby_numbers_str_list = big_list
        
        list_of_lists = big_list[:]
        print('len(list_of_lists) = {}'.format(len(list_of_lists)))
    else:
        # Convert from list of int() to sorted list of str()        
        nearby_numbers_str_list = [str(d) for d in sorted(nearby_numbers)]
        print('f. nearby_numbers_str_list = {}'.format(nearby_numbers_str_list))

    print('nearby_numbers = {}'.format(nearby_numbers_str_list))
    
    # Join the list of strings into a single string, for the final return value
    
    print('return value = [{}]'.format(nearby_numbers_str_list))
    
    return nearby_numbers_str_list