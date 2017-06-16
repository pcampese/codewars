# https://www.codewars.com/kata/where-is-my-parent-cry/python

def find_children(input_string):
    print('original = [{}]'.format(input_string))
    
    ###########
    # Method 1: 1st Attempt
    ###########
    
    string_sorted = ''.join(sorted(input_string))
    
    # Separate the string by case
    upper = [c for c in string_sorted if c.isupper()]
    lower = [c for c in string_sorted if c.islower()]
    
    # For each of the uppercase letters, get the number of lowercase letters, and append them all together, in that order
    upper_then_lower = ''                              # Stores the final result
    for u in upper:                                    # For each uppercase letter
        count = lower.count(u.lower())                 # Count the number of times it appears in the lowercase list
        upper_then_lower += u + (u.lower() * count)    # Append that to the final result
        

    ###########
    # Method 3: Single line (abysmal to read) (made from combining Method 1...)
    ###########
    
    upper_then_lower2 = ''.join([u + (u.lower() * [c for c in ''.join(sorted(input_string)) if c.islower()].count(u.lower())) for u in [c for c in ''.join(sorted(input_string)) if c.isupper()]])

    ###########
    # Method 3: Refactor Method 1
    ###########
    
    upper_then_lower3 = ''                                                 # Store the final result
    for char in sorted(input_string):                                      # For each character in the sorted input string
        if char.isupper():                                                 # If the character is uppercase
            lower_char = char.lower()                                      # Save a lowercase version of it
            lower_char_count = input_string.count(lower_char)              # Count the number of lowercase characters in the original string
            upper_then_lower3 += char + (lower_char * lower_char_count)    # In the final result, append the upper case character with the repeated count of lowercase characters
    
    ###########
    # Method 4: Single line (horible to read still) (made from combining Method 3...)
    ###########
    
    upper_then_lower4 = ''.join([char + (char.lower() * input_string.count(char.lower())) for char in sorted(input_string) if char.isupper()])

    return upper_then_lower3