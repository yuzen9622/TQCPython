arr=[[0 for j in range(5)] for i in range(3)]
tmp=["1st","2nd","3rd"]
st=["Student 1","Student 2","Student 3"]

for i in range(3):
    print(f"The {tmp[i]} student:")
    for j in range(5):
        n=int(input())
        arr[i][j]=n

for i in range(3):
    print(st[i])
    sum=0
    for j in range(5):
        sum+=arr[i][j]
    print("#Sum %d"%(sum))
    print('#Average %.2f'%(sum/5))


