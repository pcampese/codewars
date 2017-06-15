# https://www.codewars.com/kata/57faf7275c991027af000679

def remove(s, n):
    print('Input: Message = [{}] , Number = [{}]'.format(s, n))
    new_string = ''
    c_counter = 0
    
    for c in s:
        # print('Looking at character: [{}] -- c_counter = {}'.format(c, c_counter))
        if( (c == '!') and (c_counter < n) ):    # Found the '!' and still need to remove more
            # Skip the character
            c_counter += 1
        else:            # Exception (i.e. it's a '!' character)
            new_string += c
            
    print('Result: [{}]'.format(new_string))
    
    return new_string