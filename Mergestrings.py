word1="abcd"
word2="pqrs"

m=len(word1)
n=len(word2)
result=[]

i=0
j=0 

while i<m or j<n:
    if i<m:
        result+=word1[i]
        i+=1
    if j<n:
        result+=word2[j]
        j+=1

    print(result)       