arr=[]

for i in range(9):
    arr.append(int(input()))

m=max(arr)
mi=arr.index(m)
print("Index of the largest number  {} is: ({}, {})".format(m,mi//3,mi%3))
s=min(arr)
si=arr.index(s)
print("Index of the smallest number  {} is: ({}, {})".format(s,si//3,si%3))