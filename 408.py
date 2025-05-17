a=0
b=0

for i in range(10):
    n=int(input())
    if n%2==0:
        a+=1
    else:
        b+=1
print("Even numbers: %d"%a)
print("Odd numbers: %d"%b)