#first two nos are 0 and 1 and each number is sum of previous two nos
# f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    assert n>=0 and int(n)==n , 'fibonacci no cannot be negative'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)    #O(2ˆN)    Branchˆdepth , fxn is calling itself twice. 

print(fibonacci(3)) 