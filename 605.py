sum=0
a=0
min=100
max=0
for i in range(10):
    n=int(input())
    sum+=n
    if n<min :
        min=n
    elif n>max:
        max=n
sum-=(min+max)
a=sum/8
print(sum)
print("%.2f"%a)