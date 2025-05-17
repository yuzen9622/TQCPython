n={}
for i in range(10):
    n[i]=int(input())

for i in range(10):
    for j in range(1,10):
        if n[j]>n[j-1]:
            tmp=n[j]
            n[j]=n[j-1]
            n[j-1]=tmp
print(f'{n[0]} {n[1]} {n[2]}')