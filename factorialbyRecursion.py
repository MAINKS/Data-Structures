#step1 - Find out the recursive case - the flow
# n! = n*(n-1)*(n-2) and so on till n

#step2 Base case that is n = o or 1
#step3 Unintentional case (-ve integers)


def factorial(n):
    # assert n>=0 and int(n)==n   #n should be +ve and an integer
    if n in [0,1]:               #if n is 0,1 n then n! = 1 only
        return 1
    elif n<0:
        return n*factorial(n+1)
    else:
        return n*factorial(n-1)  # provides multiplication repeatedly

print(factorial(3))


# def factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Example usage:
# result = factorial(5)
# print("Factorial of 5:", result)



#Time complexity be O(N )
def factorial(n):    #O(N)
    if n in [0,1]:   #O(1)
        return 1
    else:
        return n*factorial(n-1)  #O(N-1)
print(factorial(5))