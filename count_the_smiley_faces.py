# https://www.codewars.com/kata/583203e6eb35d7980400002a

def count_smileys(arr):
    valid_smiley_list = [':)', ':D', ';)', ';D', ':-)', ':-D', ':~)', ':~D', ';-)', ';-D', ';~:', ';~D']
    smile_counter = 0
    
    for smile in arr:    # Look at each smile in the provided array
        if(smile in valid_smiley_list):    # If this smile is in the valid list
            smile_counter += 1    # Increment the counter by 1
    
    return smile_counter