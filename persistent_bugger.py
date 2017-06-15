# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    #print('Input = [{}]'.format(n))
    
    counter = 0
    
    n_string = str(n)    # Convert Number to string
    n_length = len(n_string)    # Get the length of the string
    
    #print('Number length = [{}]'.format(n_length))
    #print('counter = [{}]'.format(counter))
    
    # Loop until there's only 1 digit left
    while(n_length >= 2):
        #print('Loop: [{}]'.format(counter))
        multiplied = 1    # Store the result of multiplying all digits here, reset for each iteration
        for digit in n_string:    # Look at each digit in the string of numbers
            multiplied *= int(digit)    # Multiply each digit to the total so far
        counter += 1    # Increase total iterations performed so far
        n_length = len(str(multiplied))    # Update the length of the multiplication result
        n_string = str(multiplied)    # Convert the multiplication result to a string

    #print('Result: [{}]'.format(counter))
  
    return counter    # Return the number of iterations performed in the while loop