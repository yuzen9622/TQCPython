def compute(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
a=int(input())

if compute(a):
    print("Prime")
else:
    print("Not Prime")