n=int(input())
tmp=0
while n:
    n1=n%10
    n//=10
    tmp=tmp*10+n1
print(tmp)