#Find the index of elemnent you want to search for in an array

arr =[10,20,30,40,50,60,70,80,90]
def searchinarray(array,value):
    for i in array:           #O(n)
        if i == value:        #O(1)
            return array.index(value)
    return "Value doesn't exists"
print(searchinarray(arr,620))


#Best case : element at beginning
#worst case : element at the last index

#space complexity : no need to save any other data, O(1) space complexity