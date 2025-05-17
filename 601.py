n={}
sum=0
for i in range(12):
    a=int(input())
    n[i]=a
    if i%2==0:
        sum+=a
c=0
for i in range(12):
    print(' {:>2}'.format(n[i]),end="")
    c+=1
    if c==3:
        print()
        c=0
print(sum)