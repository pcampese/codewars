# Link: https://www.codewars.com/kata/57814d79a56c88e3e0000786

def decrypt(encrypted_text, n):
    # Get half of the encrypted_text length
    try:
        half_length = len(encrypted_text) // 2
    except:
        return
    
    # Break the encrypted text in half
    first_half = encrypted_text[:half_length]
    second_half = encrypted_text[half_length:]
    
    # Determine which half is longer
    max_length = max(len(first_half), len(second_half))
    
    # Generate the unencrypted string by iterating across both string halves
    decrypted_string = ''
    
    if (n <= 0):                             # If no decryption is requested
        decrypted_string = encrypted_text    # return the same as the original
    else:                                                      # Otherwise, decription is requested
        for char_index in range(max_length):                   # loop through the character index of the largest string half
            if (char_index < len(second_half)):                # If the index is within the half of the second half string
                decrypted_string += second_half[char_index]    # append the character to the decrypted_string
            if (char_index < len(first_half)):                 # If the index is within the half of the second half string
                decrypted_string += first_half[char_index]     # append the character to the decrypted_string
        decrypted_string = decrypt(decrypted_string, n - 1)    # decrypt the string again, recursively
        
    return decrypted_string

def encrypt(text, n):
    # Break the word down into a list of characters
    try:
        character_list = list(text)
    except:
        return
    
    encrypted_string = ''
    remaining_string = ''
    
    # Return original text if no encryption is requested.
    # Otherwise, encrypt recursively with number of encryptions requested
    if (n <= 0):                   # If no encryption is requested
        encrypted_string = text    # Encrypted string is the same as provided
    else:                                                              # Otherwise, encryption is requested 
        for character_index in range(len(character_list)):             # for each character in the text
            if (character_index % 2):                                  # if the character is in an odd index
                encrypted_string += character_list[character_index]    # append it to the encrypted string
            else:                                                      # otherwise
                remaining_string += character_list[character_index]    # append it to the remaining string
                
        encrypted_string += remaining_string    # append the remaining string to the encrypted one
        encrypted_string = encrypt(encrypted_string, n - 1)    # recursively encrypt, reduce encryption iteration by 1
        
    #print('Final Encryption: [{}]'.format(encrypted_string))
    return encrypted_string