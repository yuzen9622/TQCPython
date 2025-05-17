arr1=[[0 for j in range(2)]for i in range(2)]
arr2=[[0 for j in range(2)]for i in range(2)]
print(f"Enter matrix 1:")
for j in range(2):
    for k in range(2):
        print(f"[{j+1}, {k+1}]: ",end="")
        arr1[j][k]+=int(input())
print(f"Enter matrix 2:")
for j in range(2):
    for k in range(2):
        print(f"[{j+1}, {k+1}]: ",end="")
        arr2[j][k]+=int(input())
print("Matrix 1:")
for i in range(2):
    for j in range(2):
        print(arr1[i][j],end=" ")
    print()
print("Matrix 2:")
for i in range(2):
    for j in range(2):
        print(arr2[i][j],end=" ")
    print()
print("Sum of 2 matrices:")
for i in range(2):
    for j in range(2):
        print(arr2[i][j]+arr1[i][j],end=" ")
    print()    

