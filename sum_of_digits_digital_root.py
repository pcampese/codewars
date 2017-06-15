# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):    
    result = 0    # The final result
        
    if(len(str(n)) >= 2):    # If we still have more than 2 digits in the number
        # Convert number to list of numbers
        list_of_digits = [str(digit) for digit in str(n)]
        
        sum = 0    # The sum of the digits
        
        # Loop to sum all the digits together
        for digit in str(n):
            sum += int(digit)
        result = digital_root(sum)    # Recursive call on the new number
    else:    # If there's only 1 digit in the number
        return n    # Then return that number
    
    return result