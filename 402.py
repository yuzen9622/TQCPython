n=[]
while True:
    a=int(input())
    if a==9999:
        break
    n.append(a)
print(min(n))