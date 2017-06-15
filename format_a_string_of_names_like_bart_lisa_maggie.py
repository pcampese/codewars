# https://www.codewars.com/kata/53368a47e38700bd8300030d

def namelist(names):
    total_names = len(names)    # Total number of names in the list
    print("There are are a total of [%s] names." % total_names)
    return_value = ""    # Create empty string as the return value
    
    # Print all the names
    for n in names:
        print ("%s, " % n['name'], end="")
    
    print("\n-----")
        
    for name_dictionary in names:    # For each key:value pair in the names list
        current_index = names.index(name_dictionary);    # Current name index
        remaining_names = total_names - current_index    # Remaining names to process
        if (remaining_names >= 3):    # If there's 3 or more names remaining, separate them with a comma
            return_value += name_dictionary['name'] + ", "
            print("Return Value: [%s]" % return_value)
        if (remaining_names == 2):    # If there's exactly 2 names left, use the ampersand
            return_value += name_dictionary['name'] + " & "
            print("Return Value: [%s]" % return_value)
        if (remaining_names == 1):    # If there's exactly 1 name left, use the name only
            return_value += name_dictionary['name']
            print("Return Value: [%s]" % return_value)
    
    return return_value