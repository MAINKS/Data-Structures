array = [10,90,67,45,32,43,99,68,34,12] 
print(max(array))

biggestno = array[0]

for a in range(0,len(array)):
    if array[a] > biggestno :
        biggestno = array[a]
print(biggestno)


#Using recursion
# def maxno(array,n): #n is size of array
#     if n==1:
#         return array[0]
#     return max(array[n-1], maxno(array,n-1))
# print(maxno(array,9))


# def findbiggestno(array):
#     biggestno = array[0]
#     for i in array(0,len(array)):
#         if array[i] > biggestno :
#             biggestno = array[i]
#     print(biggestno)

