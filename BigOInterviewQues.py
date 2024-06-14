# #1  Find the time complexity / runtime of this code
# # Combining all time complexities , we get O(N) Time complexity.
def sp(array):
    sum = 0          #O(1)
    product = 1      #O(1)

    for i in array:  #O(N)
        sum += i     #O(1)

    for j in array:   #O(N)
        product *= i   #O(1)

    print ("sum is " +str(sum)+ " , Product is " +str(product))  #O(1)
sp([1,2,3,4,5,6,7,8])


# # 2  Time complexity = O(N^2) as going through each element of array twice / Nested loop
array = [2,3,5,4,6,7,8,7]
def printpair(array):
    for i in array:          #O(N^2)
        for j in array:      #O(N)
            print(str(i)+","+str(j))    #O(1)
printpair(array) 

# # 3 Time complexity = O(N^2 )

array=[1,2,3,4,5,6,7,8] 
def printunorderedpair(array):
    for i in range(0,len(array)):        #O(N^2)
        for j in range(i+1,len(array)):  #O(N-1)+...O(N)
            print(array[i],array[j])     #0(1)
print(printunorderedpair(array))

#4 Time complexity (Most imp)
#The common mistake that students do is after viewing two loops they considers it as O(N^2) time complexity
# But , there are two arrays , loops are running differently on them
#Let len(array1) = m  and len(array2) be n 
#So the time complexity be O(m*n)  not O(n^2)

array1 = [1,2,3,4,5,6,7]
array2 = [2,3,4,5,6,7,8]

def printunoreredpairs(array1, array2):
    for i in range(len(array1)):           #O(m)
        for j in range(len(array2)):       #O(n)
            if array1[i]<array2[j]:        #O(1)
                print(array1[i],array2[j])
printunoreredpairs(array1,array2)



# #5 Time complexity be O(mn)
array1 = [1,2,3,4,5,6,7]
array2 = [2,3,4,5,6,7,8]
def printunorderedpairs(array1, array2):
    for i in range(len(array1)):         #O(M)
        for j in range(len(array2)):     #O(N)
            for k in range(0,100000):   #O(100000) - drop constant
                print(array1[i],array2[j])
printunorderedpairs(array1,array2)
