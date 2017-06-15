# https://www.codewars.com/kata/548ef5b7f33a646ea50000b2

def char_freq(message):
    freq_of_char = {}    # Create empty dictionary
    for c in message:                 # For each character in 'message'
        if(c not in freq_of_char):    # If the character is not in the dictionary
            freq_of_char[c] = 1       # then set it to 1
        else:                         # If the character is in the dictionary
            freq_of_char[c] += 1      # then increment the count by 1
        
    return freq_of_char