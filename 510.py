def compute(x):
    if x>1:
        return compute(x-1)+compute(x-2)
    return x
n=int(input())
for i in range(n):
    print(compute(i),end=' ')

   
