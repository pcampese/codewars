# https://www.codewars.com/kata/570a6a46455d08ff8d001002

def no_boring_zeros(n):
    print("Number: %d" % n)
    
    # Convert number to string, and reverse it
    n_string = str(n)    # Convert to string
    n_string_reversed = n_string[::-1]    # Reverse it
        
    index_reverse = 0 # Set default index to 0
    
    # Get index of first non-zero number
    for digit in n_string_reversed:    # Iterate through reversed number
        if(digit != '0'):    # When we hit the first non-zero number
            index_reverse = n_string_reversed.index(digit)    # Get the index of it
            break    # and exit
                
    # Convert index of reversed string to index of original string
    index_n_string = len(n_string) - index_reverse
    
    # Extract substring without zeros
    no_zeros = int(n_string[:index_n_string])
            
    return no_zeros