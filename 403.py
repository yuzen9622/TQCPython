a=int(input())
b=int(input())

c=0
sum=0
for i in range(a,b+1):
    if i%4==0 or i%9==0:
        c+=1
        print('{:<4d}'.format(i),end="")
        sum+=i
        if c%10==0:
            print()
print()
print(c)
print(sum)

    