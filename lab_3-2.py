# Author: SMR (AMDG) 03/17/22
count = 1

def factorial(x):
    global count
    if x <= 0:
        return 1
    elif x >= 1:
        count = count * x
        factorial(x - 1)
    return count

print(factorial(8))