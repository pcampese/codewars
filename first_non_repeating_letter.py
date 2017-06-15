# https://www.codewars.com/kata/first-non-repeating-letter/python

def first_non_repeating_letter(string):
    print('Original String: [{}]'.format(string))
    
    # Variable to store the final result
    result = ''    # Default is empty string, increase all words are repeated
    
    # Save a lowercase version of the original string
    lowercase_string = string.lower()
        
    # Loop through the string length, as an index.  Check against the lowercase version, but return from the original version
    for index in range(len(string)):
        char = lowercase_string[index]        # The character to check, in lowercase
        count = lowercase_string.count(char)  # The number of times that character exists in the lowercase string
                
        if (count == 1):            # If the character only appears once in the string
            result = string[index]  # We want the original case version of that character - get it from original string
            break                   # We're done.  Get out.
    
    return result