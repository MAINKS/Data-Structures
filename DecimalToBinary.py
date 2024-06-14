#Step 1 divide decimal number by 2
#Step 2 Again divide quotient by 2 & and save the remainder
#Step 3 Repeat until we reached Quotient as 0
#Step 4 Obtained reversed remainder is the binary needed
#step 5 for saving remainder , mul with 10 and add next remainder to obtain the integer format of binary. 
# Base condition : n = 0 then binary = 0
#Unintentional case : negative numbers
# f(n) = n mod2 + 10  * f(n/2)

def decimaltobinary(n):
    assert n>0 and n==int(n), 'parameter must be integer'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimaltobinary(int(n/2))


print(decimaltobinary(-14))  