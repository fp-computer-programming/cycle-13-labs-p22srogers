# Author: SMR (AMDG) 03/17/22
def r_max(nested_list):
    lower = 0
    
    for x in nested_list:
        if type(x) == list:
            lower = r_max(x)
        elif lower < x:
            lower = x
    return lower

list = [2, 4, 6, [63, 89], 8]

print(r_max(list))