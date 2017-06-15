# Link: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

def zeros(n):
    zeros = 0
    exponent = 0
    
    # Keep looping until the result is less than while
    while(True):                             # Keep looping
        exponent += 1                        # increment exponent by 1
        math_result = int(n / (5**exponent)) # calculate trailing zeros, so far
        if(math_result < 1):                 # if the result is less than 1
            break                            # Done.  Exit
        else:                                # Otherwise
            zeros += math_result             # Add the result to the running total
            
    return zeros