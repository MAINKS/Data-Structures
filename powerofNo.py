#Step 1 Find recursive case (x^n = x * x^(n-1)) and goes like this recursively
#step2 Base case (0,1 as exp)
#step 3 Unintentional cases (-ve nos) 

def power(base,exp): 
    assert exp >= 0 and int(exp)==exp,'Exp must be +ve'
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base*power(base,exp-1)

print(power(3,4))