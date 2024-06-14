#Ques 1 Sum of digits of +ve integer (Ex :112 , so add 1+1+2)
#step 1 Find the recursive case
#step 2 If we divide 2 digit no with 10 , we're gonaa get those 2 digits separately (54/10 = 5 with 4 as remainder)
#step 3 for 3 and 4 digit no ,(112/10 = 11 and 2 remainder then 11/10=1 and 1 remainder)
# step 4 Unintentional case  

def sumofdigits(n):
    assert n>=0 and int(n)==n , 'no is negative and must be positive integer'
    if n ==0:
        return 0
    else:
        return int(n%10) + sumofdigits(int(n/10))

print(sumofdigits(1234))