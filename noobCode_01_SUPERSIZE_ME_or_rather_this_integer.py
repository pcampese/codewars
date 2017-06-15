# https://www.codewars.com/kata/5709bdd2f088096786000008

def super_size(n):
    n_str = str(n)
    print("n_str: %s" % type(n_str))
    
    n_str_sorted = sorted(n_str, reverse=True)
    print("n_str_sorted: %s" % type(n_str_sorted))

    n_str_sorted_join = ''.join(n_str_sorted)
    print("n_str_sorted_join: %s" % type(n_str_sorted_join))

    n_str_sorted_join_int = int(n_str_sorted_join)
    print("n_str_sorted_join_int: %s" % type(n_str_sorted_join_int))
    
    #return int(''.join(sorted(str(n), reverse=True)))    

    return int(n_str_sorted_join_int)