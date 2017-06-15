# https://www.codewars.com/kata/5467e4d82edf8bbf40000155

def Descending_Order(num):
    number_list = []    # Create an empty list
    for digit in str(num):    # Convert the number to a list of numbers
        number_list.append(digit)
    number_list.sort(reverse=True)    # Sort the list in descending order
    return_value = int(''.join(number_list))    # Merge the list into a single number (joing) and convert it to type int
    print(return_value)

    return return_value