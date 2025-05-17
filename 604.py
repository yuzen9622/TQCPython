n=[0]*100

for i in range(10):
    a=int(input())
    n[a]+=1
print(n.index(max(n)))
print(max(n))
