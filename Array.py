#Stores homogeneous data with each element next to each other.
#Cannot store strings in an array
#Each element have unique address with indexing from 0 to nth element.
#Size of array cann't be modified or changed. (Biggest limitation)
#Used to store large no of integral values.


#1d array : single row and n columns
array=[1,2,3,4,5]
print(array)

#2d array : multiple row & columns especially cubic form
# a[i][j] to access elements 
arr = [1,2,3,4],[1,2,3,4]
print(arr)
print(arr[1][1])

#3d array : elements in all 3 axis like a Rubik's cube
# a[i][j][k] to access elements 

#create an array
# 1 assign the variable
# 2 Define types of elemnt to store
# 3 Define it's size (depends on prog language)

from array import*
# array1 = array('typecode',[initialisers])

from array import*
arr2 = array('i',[1,2,3,4,5])    #i for int data , d for decimal & so on
print(arr)

# #Inserting values into an array 
# # arr2.insert(index,value)
arr2.insert(6,7) # time complexity is O(1) when inserting value at the end of array
arr2.insert(0,0) #time complexity be equal to o(n) , as elements are shifting form 1 o nth position when inserting at oth index
arr2.insert(2,29) 

print(arr2)

#Arraytraverse :accessing elements of array

arr =[1,2,3,4,5,6,7]
def traversearray(array):
    for i in array:         #O(N) time complexity
        print(i)

traversearray(arr)

print(arr[2])

def aaccesselement(array,index):
    if index >= len(arr):
        print('Out of range')
    else:
        print("Element accessed is :" ,array[index])
aaccesselement(arr,5)   #O(1) time complexity



#Deleting element from last index , O(1) Time complexity
# Deleting element from First index , O(N) , as rest n elements'll keep shifting to left 

arr2 =[1,2,3,4,5,6,7,8]

arr2.remove(2)    #.remove(element)
arr2.pop(0)       #.pop(index)
arr2.append(100)  #.append(element)  , to add an element at end of an array
arr2.insert(0,199) #.insert(index,value) , to insert element at specified index
arr4 =[90,80,70,60]
arr2.extend(arr4)  #.extend , to add another array values to predefined array 

# list1 = [20,30,40]
# arr2.fromlist(list1)  # .fromlist(listname) , to add list elements to array

print("Index of value 5 is at : " , arr2.index(5))

print(arr2)

arr2.reverse()  # Reverse an array
print("Reversed array is : " , arr2)

print(arr2.count(199))   #Counts element repitition in an array

print(arr2[1:4])   # Slicing array elements b/w given indexes & printing

arrayyay=[1,2,34,5]   #updating values
arrayyay[2] = 35
print(arrayyay)

