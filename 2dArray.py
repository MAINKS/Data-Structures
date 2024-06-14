# #we'll use numpy library for 2d arrays
# #can we say a matrix as 2d array

# #Creating
# import numpy as np

# twoDarray = np.array([[10,20,30,40],[200,300,400,500],[300,400,500,600]])
# print(twoDarray)


#inserting values
#Adding columns  , O(mn) is time complexity , m are rows & n columns
# newarray = np.insert(prev array name , colum index to insert , values to add , axis = 1 to add as column , 0 to add as row)

# new2darray = np.insert(twoDarray ,0, [[1,2,3]], axis=1)
# print(new2darray)

#Inserting using append
# newarray = np.append(twoDarray,[[2,3,4]],axis=0)
# print(newarray)

# Deleting a row/column from 2darray
# new array to store = np.delete(Primary array , row/column index , axis = 0 for row wise removal & 1 for column wise)
# newarray = np.delete(twoDarray , 1 , axis = 1)
#removing row/column from 2d array have O(mn) time complexity , as corresponding n/m row/colum will shift n/m times.


array = ([[1,2,3],[4,5,6],[7,8,9]])
print(array)
print(array[0][2])
print("len of 2d array is : " , len(array)) #returns no of rows

def accesselements(array,rowindex,colindex):
    if rowindex >= len(array) and colindex >= len(array[0]):  #O(1) time complexity
        print("index out of range")
    else :
        print(array[rowindex][colindex])
print(accesselements(array,2,2))


def traverse2darray(array):              #O(mn) time complexity
    for i in range(len(array)):          #O(M)
        for j in range(len(array[0])):   #O(N)
            print(array[i][j])           #0(1)
print(traverse2darray(array))


def search2darray(array,value):         #O(mn) time complexity
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located at index  : ' +str(i)+ "," +str(j)
    return "Value not found"
print(search2darray(array,9))