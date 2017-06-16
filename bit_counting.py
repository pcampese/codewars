# http://www.codewars.com/kata/bit-counting/python

def countBits(n):

    # Convert to binary
    binary = bin(n)
        
    # Count 1's
    count = binary.count('1')
    
    # 1-line
    # return bin(n).count('1')

    return count