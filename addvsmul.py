array1 = [2,5,6,7,9]
array2 = [9,8,7,6,5]


for a in array1:
    print(a)

for b in array2:
    print(b)

# O(A+B) is bigO for this program


#Multiplying elements of the array one by one using loop 
for a in array1:
    for b in array2:
        print(a*b)

#O(A*B) is the Big O for this program