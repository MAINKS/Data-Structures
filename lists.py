# # A data structure that holds an ordered colelction of items
# # list of integers = [10,20,30,40]
# # list of strings = ['s','t','r','i','n','g']
# # list of string , integer ,float = ['spam',1,2.05]

# # Diff b/w array and list is , array contains homogeneous data while list can have variable data as string , int, float etc.
# #Also we can create list inside another list = nested list

# #nested list = ['spam',1,2,3.05,[10,20]]   , nested list would be taken account as one element.

# integer_list = [1,2,3,4]
# print(integer_list)

# stringlist = ['hello','bye','why']
# print(stringlist)
# print(stringlist[-1])
# # print(stringlist[-4])  list index out of range
# print('why' in stringlist)
# print('who' in stringlist)

# mixedlist = ['spam',1,2.05]
# print(mixedlist)

# nestedlist = ['spam',1,2,3.05,[10,20]]
# print(nestedlist)

# #Accessing / Traversing list   , indexing & accessing is same as array
# list = ['milk','cheese','butter']
# print(list[2])
# print(list[-2])  # negative index starts from last element

# #in operator  , true if in list else false
# print('milk' in list)
# print('bread' in list)

# for i in list:
#     print(i)

# #Doing modifications to elements using loop
# for i in range(len(list)):
#     list[i] = list[i]+'+'
#     print(list[i])


# #Update/insert data into a list  , lists are mutable ie we can update the values
# list[2] = 8999   #O(1)
# print(list)

# # insert,append,extend functions - 
# list.insert(0,111)   # .insert(index,value) , at 0 index O(N) Time complexity as n elements shifts.

# list.append(654)   # .append(value) , inserts value at the end of list  , O(1) Time complexity

# newlist =[34,45,56,23,12,4,5,67,8,99,34]  #.extend(list to add) , adds new list values to existing list 
# list.extend(newlist)  #0(n)  , n = no of elements in new list  

# print(list)


# #SLICING from the list
# print(newlist[2:4])
# newlist[0:2]= ['x','y']   #updating values
# print(newlist)


# #Delete from a list : pop,delete,remove synatx

# print(newlist.pop(2))  #takes index as parameter , default last index

# del newlist[0:1]
# print(newlist)   #also takes index as parameter , but can delete multiple values using slicing

# newlist.remove(34)   # takes value as parameter , not index
# print(newlist)


# #Searching for an element in a list - builtin in operator and linear search
# newlist1 = [10,20,30,40,50,60,70,80,90]

# if 2000 in newlist1:
#     print(newlist1.index(2000))
# else:
#     print("Value doesn't exists")


# #Using linear search
# value = int(input("ënter value to be searched"))

# def search(listname,value):
#     for i in newlist1:
#         if i == value:
#             return newlist1.index(value)
#     return 'value do not exists'

# print(search(newlist1,value))

# #Concatination of list using + operator
# list1 = [1,2,3,4,5]
# list2 = [2,3,4,5,6]
# list3 = list1+list2
# print(list3)
# print(list1*4)   # using * operator - extends list 4 times

# print(max(list1))
# print(min(list1))
# print(len(list1))
# print(sum(list1))  # gives sum of all elements of a list

# mylist = []
# while(True):
#     inp = input('énter a number')
#     if inp == 'done': break
#     value = float(inp)
#     mylist.append(value)
#     avg = sum(mylist)/len(mylist)

# print("Äverage : ", avg)

# #String to list conversion

string = 'value num int any'
converted = list(string)     #convert string to list by splitting each character
print(converted)

cbv = string.split()        #convert string to list by splitting each word using delimiter(separation unit) as a space
print(cbv)
