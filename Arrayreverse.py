# array = [1,2,3,4,5,6,7,8,9]
# array2=[]
# def reverse(array):
#         for j in range(len(array),0,-1):
#             array[j] = array2[j]
#             print(array2)
# reverse(array)
# print(reverse(array))



#Time complexity is O(N) 
array = [1,2,3,4,5,6,7,8,9]
def reverse(array):
    for i in range(0,int(len(array)/2)):     #O(N/2) = O(N)
        other = len(array)-i-1               #O(1)
        temp = array[i]                      #O(1)
        array[i] = array[other]              #O(1)
        array[other] = temp                  #O(1)
    print(array)
print(reverse(array))