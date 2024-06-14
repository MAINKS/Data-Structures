#Basic Recursion format using python functions
#Recursion is used if we can break problem into smaller sub problems
#Recursion is preferred more as compared to iterative solution.

# def recursionmethod(parameters):
#     if exit from condition satisfied:
#         return some Value
#     else:
#         recursionmethod(modified parameters)    

# def first():
#     second()
#     print("I am first")

# def second():
#     print("i am second") 

# n=int(input("enter your number"))


# def recursivemethod(n):
#     if n>1:
#         print("n is less than 1")
#     else: 
#         recursivemethod(n-1)
#         print(n)



def poweroftwo(n):
    if n==0:
        return 1
    else:
        return 2*poweroftwo(n-1)
print(poweroftwo(5))