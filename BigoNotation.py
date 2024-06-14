# Time complexity : time taken by a program , depends on number of input , O(N),O(Nˆ2), O(2ˆN) 
# Space complexity : size required by the program  
# Best case : Time complexity is O(N) , n elements are there , n no of passes required , minimum time required.
# Average case : O(N LogN) ,  
# Worst case  : Time complexity is O(Nˆ2) , n elements are there , nˆ2 no of passes required, maximum time required for a program.

#O(1) , O(N) , 0(Nˆ2) , O(LOGN) , 0(2ˆN) , O(N!) , O(N LogN)
#O(1),O(NlOGN) are the excellent time complexities
#As input (n) increases , time complexity becomes horrible as in O(2ˆN) & O(Nˆ2 )

array = [1,2,3,4,5]

#example of O(1) Big o time complexity : accessing specific index of array
print(array[0])

#Example of O(N) BigO time complexity : going through each element once
#larger the input (ie :array) the greater it time takes to loop through it.
for i in array:
    print(i)

#Example of O(LogN) big o time complexity : going through only selected elements (like 0 then 3 then 6) , using range function
#Binary search is example for LogN time complexity in which we search for an elemnt in a sorted array 
for index in range (0,len(array),3):
    print(array[index]) 

#Example of O(Nˆ2) BIGO time complexity : going through each element of array twice :Quadratic
for x in array: #1,2,3,4,5
    for y in array: #1,2,3,4,5
        if x==y:     #1,1 & 2,2 till 5,5
            print(x,y)

#Example for O(2ˆN) Big O Time complexity : double fibonacci recursion : Exponential
def fibonacci(n): #greater the n is , greater the time complexity will be 
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2) #it's 

print(fibonacci(1))

#When dealing with multiple statements then , just add them up O(A+B)


#Space complexity is the measure of space required by the program 
# if array of n elemnts is created , it requires n bytes & similarly n cross n matrix requires nˆ2 no of bytes. 

def pairsumsequence(n):
    sum=0
    for i in range (0,n+1):
        sum=sum+pairsum(i,i+1)
    return sum

def pairsum(a,b):
    return a+b
print(pairsumsequence(4))

#Space complexity of above program is O(1)

def f(n):
    if n<=1:
        return n
    return f(n-1)+f(n-1)  #BigO for this program is o(2^n) as it's recursively calling twice 2^0 + 2^1 +...2^n = O(2^n)
print(f(4))  