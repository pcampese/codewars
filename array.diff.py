# Link: https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(numbers, to_remove):
    # "Expanded" List comprehension
    # new_list = []
    # for num in numbers:
    # if (num not in to_remove):
    # new_list.append(num)
            
    # List comprehension
    #   This is the same as above, but compressed...
    new_list = [num for num in numbers if num not in to_remove]
            
    return new_list