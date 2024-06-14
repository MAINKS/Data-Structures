#GCD or HCF are same (greatest common divisor or factor) is a no which divides the given set of number without leaving remainder
# gcd(8,12) = 4
# Using Euclideian algorithm that is :
#Step 1 gcd(48,18)  48/18 = 2 & 12 remainder
#step 2  18/12 = 1 and 6 remainder
#step 3  12/6 = 2 and remainder 0 (so , 6 is gcd)

#Base case , b==0 then gcd = a
#Unintentional case , -ve no to +ve

def gcd(a,b):
    assert int(a)==a and int(b)==b, 'The nos must be integer'
    if a<0:
        a=-1*a
    if b<0:
        b=-1*b
    if b==0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(48,-18))